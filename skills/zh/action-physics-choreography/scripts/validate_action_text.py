#!/usr/bin/env python3
"""Check how action beats are written: setup -> contact -> result, force direction,
stacked intensifiers, clip length. Chinese and English blocks are both recognized.

检查动作写法：起手-接触-结果、受力方向、结果词堆砌、片段时长。中英文块都认。

Usage / 用法
  validate_action_text.py FILE [--prose] [--model 2.5|2.0]

Blocks (content inside ``` fences is skipped) / 识别的块（代码块内跳过）
  【动作】名称｜片段10秒｜第1/2拍        [Action] name | clip 10s | beat 1/2
  起手：… 接触：… 结果：…              Setup: … Contact: … Result: …
  碰撞：轻/重/大招  受力方向：…  镜头配合：…   Impact: light/heavy/finisher  Force direction: …  Camera: …

  【动作段】 / [Action passage]: a prose process chain; the following non-empty lines form one passage.
  过程链正文段，标记后的连续非空行是一段。

  --prose: untagged paragraphs are checked as passages too (headings, tables and dialogue
  lines are skipped). 没有标记的段落也按动作段检查（跳过标题、表格和对白行）。

Only checks the writing, not whether the physics is right. Exit code 1 when there are errors.
只检查写法，不判断物理是否合理。有 ERROR 时退出码为 1。
"""
import argparse
import re
import sys
from pathlib import Path

VOCAB = {
    "zh": {
        "intensifiers": ("狠狠地", "狠狠", "猛地", "猛然", "重重地", "狠命", "疯狂地", "剧烈地", "用力地",
                         "拼尽全力", "巨大的冲击", "巨大冲击", "一记重击", "瞬间爆发", "惊天动地", "毁天灭地", "震撼"),
        "contact": ("抓", "扣", "按", "踩", "蹬", "撞", "砸", "劈", "砍", "刺", "踢", "抽", "击中", "打在", "格", "挡",
                    "托", "抱", "咬", "压", "握", "撑", "推", "拽", "拉", "扑", "勾", "绊", "扫", "落在", "碰到", "磕",
                    "抡", "摔", "顶", "夹", "缠"),
        "body": ("手", "脚", "拳", "掌", "肘", "膝", "肩", "腰", "胯", "背", "胸", "肋", "头", "脸", "腿", "爪", "角",
                 "尾", "翼", "颈", "刀", "剑", "枪", "刃", "棍", "鞭", "盾"),
        "result": ("倒", "落地", "着地", "停", "跪", "滑出", "飞出", "翻", "摔", "撞上", "退", "晃", "稳住", "躺",
                   "趴", "离地", "脱出", "松开", "裂", "碎", "塌"),
        "fields": {"setup": "起手", "contact": "接触", "result": "结果", "direction": "受力方向",
                   "camera": "镜头配合", "impact": "碰撞"},
        "levels": ("轻", "重", "大招"),
    },
    "en": {
        "intensifiers": ("violently", "brutally", "fiercely", "ferociously", "powerfully", "with all his might",
                         "with all her might", "with all their might", "tremendous force", "massive impact",
                         "devastating", "earth-shattering", "explosively", "epic"),
        "contact": ("grab", "grip", "clamp", "press", "step", "stomp", "kick", "punch", "strik", "hit", "slash",
                    "cut", "stab", "thrust", "block", "parr", "push", "pull", "hold", "catch", "lands on", "knock",
                    "smash", "sweep", "hook", "trip", "throw", "pin", "bite", "tackle", "shove", "slam", "lunge",
                    "hurl", "swing", "drive", "elbow", "knee", "touch"),
        "body": ("hand", "fist", "palm", "elbow", "knee", "shoulder", "waist", "hip", "back", "chest", "rib",
                 "head", "face", "leg", "foot", "feet", "heel", "claw", "horn", "tail", "wing", "neck", "blade",
                 "sword", "spear", "staff", "shield", "axe", "arm", "jaw"),
        "result": ("fall", "land", "stop", "kneel", "slide", "fly", "flies", "flip", "roll", "stagger", "steadies",
                   "steady", "lies", "lying", "off the ground", "drop", "lets go", "crack", "shatter", "collapse",
                   "skid", "crash", "topple", "tumble", "sprawl", "comes to rest"),
        "fields": {"setup": "Setup", "contact": "Contact", "result": "Result", "direction": "Force direction",
                   "camera": "Camera", "impact": "Impact"},
        "levels": ("light", "heavy", "finisher"),
    },
}
DIRECTION = {
    "zh": re.compile(r"(画面[左右上下中])|((向|往|朝|从|到)[^，。；、]{0,6}(左|右|前|后|上|下|里|外|中心|两边|两侧))"
                     r"|朝镜头|迎面|自[^，。；、]{0,6}至|→|斜向|沿着|顺着"),
    "en": re.compile(r"\b(frame|screen) (left|right|top|bottom)\b|\b(to|toward|towards|from|into) the "
                     r"(left|right|front|back|rear|center|sides?)\b|\b(left|right)ward\b|\bbackwards?\b|\bforwards?\b"
                     r"|\bupwards?\b|\bdownwards?\b|\btoward(s)? (the )?camera\b|\baway from (the )?camera\b|→"
                     r"|\bleft to right\b|\bright to left\b|\bdiagonally\b", re.I),
}
SENTENCE_SPLIT = {"zh": re.compile(r"[。！？；!?;\n]"), "en": re.compile(r"(?<=[.!?;])\s+|\n")}
ZH_HEADER = re.compile(r"^【动作】(?P<name>[^｜|]*)[｜|]?(?P<rest>.*)$")
EN_HEADER = re.compile(r"^\[Action\]\s*(?P<name>[^|]*)\|?(?P<rest>.*)$", re.I)
ZH_INLINE = re.compile(r"^【动作】(?P<name>[^｜|：:\n]{0,24})[：:]\s*(?P<body>\S.*)$")
CLIP_SEC = re.compile(r"(?:片段|节点)\s*(\d+(?:\.\d+)?)\s*秒|\bclip\s*(\d+(?:\.\d+)?)\s*s(?:ec(?:onds?)?)?\b", re.I)
DIALOGUE = re.compile(r"[：:]\s*[“\"「]")
CJK = re.compile(r"[一-鿿]")


class Block:
    def __init__(self, kind, lang, line, title):
        self.kind, self.lang, self.line, self.title, self.lines = kind, lang, line, title, []


def strip_fences(text):
    out, fenced = [], False
    for no, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            out.append((no, line))
    return out


def parse_blocks(text, prose_mode):
    blocks, cur = [], None
    for no, raw in strip_fences(text):
        line = raw.strip()
        inline = ZH_INLINE.match(line) if prose_mode else None
        if inline and not CLIP_SEC.search(inline.group("name")):
            cur = Block("prose", "zh", no, f"【动作】{inline.group('name').strip()}")
            cur.lines.append(inline.group("body"))
            blocks.append(cur)
            continue
        if line.startswith("【动作段】") or line.lower().startswith("[action passage]"):
            lang = "zh" if line.startswith("【") else "en"
            cur = Block("prose", lang, no, line.split("】")[0] + "】" if lang == "zh" else "[Action passage]")
            blocks.append(cur)
            rest = line[len("【动作段】"):] if lang == "zh" else line[len("[Action passage]"):]
            if rest.strip():
                cur.lines.append(rest.strip())
            continue
        if line.startswith("【动作】") or line.lower().startswith("[action]"):
            cur = Block("struct", "zh" if line.startswith("【") else "en", no, line)
            blocks.append(cur)
            continue
        if not line:
            if cur is not None and cur.lines:
                cur = None
            continue
        if line.startswith(("#", "|")):
            cur = None
            continue
        if DIALOGUE.search(line) and (cur is None or cur.kind == "prose"):
            if cur is not None and cur.title.startswith("@"):
                cur = None
            continue
        if cur is not None:
            cur.lines.append(line)
        elif prose_mode:
            cur = Block("prose", "zh" if CJK.search(line) else "en", no, f"@{no}")
            cur.lines.append(line)
            blocks.append(cur)
    return blocks


def sentences(text, lang):
    return [s.strip() for s in SENTENCE_SPLIT[lang].split(text) if s.strip()]


def has_any(text, words, lang):
    if lang == "en":
        low = text.lower()
        return any(re.search(r"\b" + re.escape(w), low) for w in words)
    return any(w in text for w in words)


def check_intensifiers(where, text, lang, errors, warnings):
    v, count = VOCAB[lang], 0
    for s in sentences(text, lang):
        hits = [w for w in v["intensifiers"] if (w in s.lower() if lang == "en" else w in s)]
        if not hits:
            continue
        count += 1
        if not (has_any(s, v["contact"], lang) and (has_any(s, v["body"], lang) or DIRECTION[lang].search(s))):
            errors.append(f"{where}: 结果词“{hits[0]}”没有过程（缺接触部位或方向）/ intensifier without process "
                          f"(no contact point or direction): {s}")
    if count > 2:
        warnings.append(f"{where}: 强调词出现 {count} 处，换成部位、方向、位移、落点 / {count} intensifiers; "
                        f"replace them with body part, direction, displacement, landing")


def field_value(line, name):
    line = re.sub(r"^[-*•]\s*", "", line)
    m = re.match(rf"^{re.escape(name)}\s*[:：]\s*(.*)$", line, re.I)
    return m.group(1).strip() if m else None


def check_struct(b, model, errors, warnings):
    v, where = VOCAB[b.lang], f"line {b.line} {b.title}"
    f = v["fields"]
    header = (ZH_HEADER if b.lang == "zh" else EN_HEADER).match(b.title)
    sec = CLIP_SEC.search(header.group("rest") if header else "")
    if sec:
        raw = sec.group(1) or sec.group(2)
        n, hi = float(raw), (15 if model == "2.0" else 30)
        if not n.is_integer():
            errors.append(f"{where}: 片段时长 {raw} 秒不是整数 / clip length {raw}s is not a whole number")
        elif not 4 <= n <= hi:
            errors.append(f"{where}: 片段 {raw} 秒超出 Seedance {model} 的 4–{hi} 秒 / outside 4–{hi}s for Seedance {model}")
    found = {}
    for idx, line in enumerate(b.lines):
        for key, name in f.items():
            val = field_value(line, name)
            if val is not None and key not in found:
                found[key] = (idx, val)
    if "impact" in found:
        level = re.split(r"[｜|\s，。；,;]", found["impact"][1])[0]
        if level.lower() not in v["levels"]:
            errors.append(f"{where}: “{f['impact']}”只能写 {' / '.join(v['levels'])} / impact must be one of "
                          f"{' / '.join(v['levels'])}, got '{level or 'empty'}'")
    for key in ("setup", "contact", "result", "direction"):
        if key not in found or not found[key][1]:
            errors.append(f"{where}: 缺 / missing “{f[key]}”")
    order = [found[k][0] for k in ("setup", "contact", "result") if k in found]
    if order != sorted(order):
        errors.append(f"{where}: 顺序应为 起手 → 接触 → 结果 / order must be setup -> contact -> result")
    for key in ("setup", "contact", "result"):
        if key in found and len(sentences(found[key][1], b.lang)) > 1:
            warnings.append(f"{where}: “{f[key]}”写了多句，每项一句 / one sentence per field")
    if "contact" in found and found["contact"][1] and not has_any(found["contact"][1], v["contact"] + v["body"], b.lang):
        warnings.append(f"{where}: “{f['contact']}”没写出部位或接触动作 / contact names no body part or contact verb")
    if "direction" in found and found["direction"][1] and not DIRECTION[b.lang].search(found["direction"][1]):
        errors.append(f"{where}: “{f['direction']}”没有方向词 / force direction has no direction "
                      f"(frame left/right, backward, upward ...)")
    if "camera" not in found:
        warnings.append(f"{where}: 缺 / missing “{f['camera']}”")
    check_intensifiers(where, "\n".join(b.lines), b.lang, errors, warnings)


def check_prose(b, errors, warnings):
    v, where = VOCAB[b.lang], f"line {b.line} {b.title}"
    text = ("" if b.lang == "zh" else " ").join(b.lines)
    if not text.strip():
        errors.append(f"{where}: 动作段为空 / empty passage")
        return
    if not has_any(text, v["contact"], b.lang):
        errors.append(f"{where}: 没有接触（抓哪、踩哪、打在哪）/ no contact (what grabs, steps on or hits what)")
    if not DIRECTION[b.lang].search(text):
        errors.append(f"{where}: 没有受力或运动方向 / no force or movement direction")
    if not has_any(text, v["result"], b.lang):
        errors.append(f"{where}: 没有受力结果或停姿 / no result or end pose")
    if len(sentences(text, b.lang)) < 2:
        warnings.append(f"{where}: 只有一句，起手、接触、结果可能挤在一起 / only one sentence; setup, contact "
                        f"and result may be crammed together")
    check_intensifiers(where, text, b.lang, errors, warnings)


def validate_text(text, prose_mode=False, model="2.5"):
    errors, warnings = [], []
    blocks = parse_blocks(text, prose_mode)
    if not blocks:
        errors.append("没有找到【动作】或【动作段】块（查正文请加 --prose）/ no [Action] or [Action passage] "
                      "blocks found (use --prose for plain paragraphs)")
    for b in blocks:
        if b.kind == "struct":
            check_struct(b, model, errors, warnings)
        else:
            check_prose(b, errors, warnings)
    return errors, warnings


def main(argv=None):
    ap = argparse.ArgumentParser(description="Action beat writing check / 动作写法检查")
    ap.add_argument("file")
    ap.add_argument("--prose", action="store_true", help="check untagged paragraphs too / 无标记段落也查")
    ap.add_argument("--model", choices=("2.5", "2.0"), default="2.5", help="Seedance version for clip length")
    args = ap.parse_args(argv)
    errors, warnings = validate_text(Path(args.file).read_text(encoding="utf-8"), args.prose, args.model)
    for e in errors:
        print("ERROR " + e)
    for w in warnings:
        print("WARN  " + w)
    print(f"{'FAIL' if errors else 'PASS'}: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
