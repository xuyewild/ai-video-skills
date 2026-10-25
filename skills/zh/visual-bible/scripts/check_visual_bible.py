#!/usr/bin/env python3
"""Visual bible format check (Chinese or English template).

视觉圣经格式检查（中文或英文模板都认）。

Usage / 用法
  check_visual_bible.py BIBLE.md [--registry ASSETS.md] [--prompts PROMPTS.md ...]

Checks / 检查
  - style name and one-line style present / 风格短名、风格一句话存在且非空
  - fixed effects: "none"/"无" or "name = color; ..." / 固定特效写“无”或“名字＝颜色；……”
  - required sections present and non-empty / 必需段落齐全且非空
  - video style block: no hex color codes, no @ references / 视频风格段不写色值、不引用素材
  - asset image style block: no -- parameters, no hex, no time of day / weather / scene light
    资产图风格段不写参数、色值、时段天气和环境光
  - optional Midjourney block: English, no -- parameters, no time / weather, has a
    style-reference line / 可选的 Midjourney 段：英文、不带参数、不写时段天气、有“风格参考”行
  - scale baseline: every "- name: ..." line has a number with cm / m
    尺度基线每个“- 名字：”行写了带单位的数字
  - optional asset-sheet section: style baseline (before brackets) equals the style name
    可选的“与资产表对应”段：风格基线括号前与风格短名一致
  - --registry: the asset sheet's style baseline and gray background match
    资产表的风格基线、灰底与本文件一致
  - --prompts: colors written next to a fixed effect name must come from the bible
    (heuristic, warnings only) / 提示词里固定特效附近的颜色要照抄视觉圣经（启发式，只提醒）

Only checks format, not whether the style is good. Exit codes: 0 = pass, 1 = errors.
只查格式，不评判风格好坏。返回 0 通过，1 有错误。
"""
import argparse
import re
import sys
from pathlib import Path

LANG = {
    "zh": {
        "short": "风格短名", "oneline": "风格一句话", "fixed": "固定特效",
        "sections": ["色彩", "光线", "材质", "镜头质感", "时段与天气变体", "禁止项",
                     "资产图风格段", "视频风格段", "尺度基线"],
        "asset": "资产图风格段", "video": "视频风格段", "scale": "尺度基线",
        "registry": "与资产表对应", "base": "风格基线", "grey": "灰底",
        "mj": "Midjourney 风格段", "ref": "风格参考", "sentence": "比例句",
    },
    "en": {
        "short": "Style name", "oneline": "One-line style", "fixed": "Fixed effects",
        "sections": ["Color", "Light", "Materials", "Camera texture", "Time and weather variants",
                     "Don'ts", "Asset image style", "Video style", "Scale baseline"],
        "asset": "Asset image style", "video": "Video style", "scale": "Scale baseline",
        "registry": "Asset sheet link", "base": "Style baseline", "grey": "Gray background",
        "mj": "Midjourney style", "ref": "Style reference", "sentence": "Scale sentence",
    },
}
# Older Chinese headings still accepted / 旧标题也认
ALIASES = {"Seedance 风格段": "视频风格段", "与资产登记表对应": "与资产表对应",
           "Midjourney 风格段（备用）": "Midjourney 风格段", "Midjourney 风格段(备用)": "Midjourney 风格段"}
NONE_WORDS = ("无", "none", "None", "-", "—")

SIZE_NUM = re.compile(r"\d+(?:\.\d+)?\s*(?:厘米|公分|米|cm|m)(?![a-z])", re.I)
HEX = re.compile(r"#[0-9A-Fa-f]{6}\b")
CJK = re.compile(r"[一-鿿]")
FIXED_ITEM = re.compile(r"^\s*([^＝=：:（(]+?)\s*[＝=]\s*([^（(；;]+)")
TIME_WEATHER_ZH = re.compile(
    r"夜晚|夜景|夜色|黄昏|傍晚|日落|日出|清晨|晨光|夕阳|月光|阳光|天光|烛光|火光|逆光|"
    r"下雨|雨天|雨夜|雨景|下雪|雪天|雪景|雾气|薄雾|浓雾")
TIME_WEATHER_EN = re.compile(
    r"\b(night|nighttime|sunset|sunrise|dawn|dusk|twilight|moonlight|moonlit|sunlight|sunlit|"
    r"candlelight|firelight|backlight|backlit|golden hour|rain|rainy|snow|snowy|fog|foggy|mist)\b", re.I)
# Chinese color phrase: color characters followed by 色/光/芒 (金色, 银白光) / 中文颜色词组
ZH_COLOR_CHAR = re.compile(r"[金银红橙黄绿青蓝紫白黑粉灰褐棕赤]")
ZH_COLOR_PHRASE = re.compile(r"([金银红橙黄绿青蓝紫白黑粉灰褐棕赤]+)(?=色|光|芒)")
EN_COLORS = ("gold", "golden", "silver", "red", "crimson", "scarlet", "orange", "amber", "yellow",
             "green", "emerald", "teal", "cyan", "blue", "azure", "purple", "violet", "white",
             "black", "pink", "gray", "grey", "brown")
EN_COLOR_RE = re.compile(r"\b(" + "|".join(EN_COLORS) + r")\b", re.I)


def detect_lang(text):
    if re.search(r"^Style name\s*:", text, re.M | re.I):
        return "en"
    return "zh"


def value(text, key):
    m = re.search(rf"^{re.escape(key)}\s*[:：]\s*(.*)$", text, re.M | re.I)
    return m.group(1).strip() if m else None


def strip_note(v):
    return re.split(r"[（(]", v.strip())[0].strip()


def split_sections(text):
    parts, current, buf = {}, None, []
    for line in text.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            if current is not None:
                parts[current] = "\n".join(buf).strip()
            raw = m.group(1).strip()
            # "配色体系（可选，……）" -> "配色体系"; "Palette (optional)" -> "Palette"
            name = ALIASES.get(raw) or strip_note(raw)
            current, buf = ALIASES.get(name, name), []
        elif current is not None:
            buf.append(line)
    if current is not None:
        parts[current] = "\n".join(buf).strip()
    return parts


def code_block(body):
    m = re.search(r"```[a-z]*\n(.*?)```", body, re.S)
    return (m.group(1) if m else body).strip()


def is_none(v):
    return v.strip().split("（")[0].split("(")[0].strip() in NONE_WORDS


def fixed_effects(text):
    """'shield light = cyan white; fox fire = orange gold' -> {name: color}."""
    lang = detect_lang(text)
    out = {}
    for part in re.split(r"[；;]", value(text, LANG[lang]["fixed"]) or ""):
        m = FIXED_ITEM.match(part)
        if m:
            out[m.group(1).strip()] = m.group(2).strip()
    return out


def check(text, registry_text=None):
    k = LANG[detect_lang(text)]
    errors = []
    short = value(text, k["short"])
    if not short:
        errors.append(f"缺“{k['short']}:”或为空 / missing or empty")
    if not value(text, k["oneline"]):
        errors.append(f"缺“{k['oneline']}:”或为空 / missing or empty")
    fixed = value(text, k["fixed"])
    if fixed is None:
        errors.append(f"缺“{k['fixed']}:”，没有写“无/none” / missing; write none if there are none")
    elif not is_none(fixed) and not fixed_effects(text):
        errors.append(f"“{k['fixed']}”每项写成“名字＝颜色”，用“；”隔开 / write 'name = color; ...': {fixed[:30]}")

    sections = split_sections(text)
    for name in k["sections"]:
        if name not in sections:
            errors.append(f"缺段落 / missing section: ## {name}")
        elif not sections[name]:
            errors.append(f"段落为空 / empty section: ## {name}")

    video = code_block(sections.get(k["video"], ""))
    if video:
        if HEX.search(video):
            errors.append("视频风格段含色值代码，改写成文字颜色 / video style block has a hex code; use color words")
        if "@" in video:
            errors.append("视频风格段不引用素材 / video style block must not reference assets with @")

    asset = code_block(sections.get(k["asset"], ""))
    if asset:
        if "--" in asset:
            errors.append("资产图风格段不写参数 / asset image style block must not carry -- parameters")
        if HEX.search(asset):
            errors.append("资产图风格段不写色值 / asset image style block must not carry hex codes")
        hit = TIME_WEATHER_ZH.search(asset) or TIME_WEATHER_EN.search(asset)
        if hit:
            errors.append(f"资产图风格段不写时段、天气、环境光 / no time of day, weather or scene light "
                          f"in the asset image style block: {hit.group(0)}")

    mj_body = sections.get(k["mj"])
    if mj_body is not None:
        mj = code_block(mj_body)
        if mj and CJK.search(mj):
            errors.append("Midjourney 段应为英文 / Midjourney block should be in English")
        if "--" in mj:
            errors.append("Midjourney 段不写参数，参数放风格参考行 / put parameters on the style reference line")
        hit = TIME_WEATHER_EN.search(mj)
        if hit:
            errors.append(f"Midjourney 段不写时段天气 / no time of day or weather in the Midjourney block: {hit.group(0)}")
        ref = value(mj_body, k["ref"])
        if ref is None:
            errors.append(f"Midjourney 段下缺“{k['ref']}:”行 / missing style reference line (write none)")
        elif not is_none(ref) and "--sref" not in ref:
            errors.append(f"“{k['ref']}”写“无/none”或“--sref <链接> --sw <数值>” / write none or --sref <url> --sw <n>")

    for line in sections.get(k["scale"], "").splitlines():
        m = re.match(r"^\s*[-*]\s*([^：:]+)[：:](.*)$", line)
        if m and m.group(1).strip().lower() != k["sentence"].lower() and not SIZE_NUM.search(m.group(2)):
            errors.append(f"尺度基线“{m.group(1).strip()}”没写带单位的数字 / scale line has no number with cm or m")

    reg_sec = sections.get(k["registry"], "")
    base, grey = value(reg_sec, k["base"]), value(reg_sec, k["grey"])
    if reg_sec:
        if base is None:
            errors.append(f"“{k['registry']}”缺“{k['base']}:”行 / missing line")
        elif short and strip_note(base) != short:
            errors.append(f"{k['base']}“{strip_note(base)}”与{k['short']}“{short}”不一致 / does not match")
        if grey is None:
            errors.append(f"“{k['registry']}”缺“{k['grey']}:”行 / missing line")

    if registry_text is not None:
        r_base = value(registry_text, LANG["zh"]["base"]) or value(registry_text, LANG["en"]["base"])
        r_grey = value(registry_text, LANG["zh"]["grey"]) or value(registry_text, LANG["en"]["grey"])
        if r_base is None:
            errors.append("资产表缺风格基线行 / asset sheet has no style baseline line")
        elif short and strip_note(r_base) != short:
            errors.append(f"资产表风格基线“{strip_note(r_base)}”与风格短名“{short}”不一致 / does not match the style name")
        if r_grey is None:
            errors.append("资产表缺灰底行 / asset sheet has no gray background line")
        elif grey and strip_note(r_grey) != strip_note(grey):
            errors.append(f"资产表灰底“{strip_note(r_grey)}”与视觉圣经“{strip_note(grey)}”不一致 / gray background differs")
    return errors


def check_warnings(text):
    """Warn when the scale baseline has 2+ entries but no scale-sentence line.
    尺度基线有两个以上条目却没有“比例句”时提醒。"""
    k = LANG[detect_lang(text)]
    entries, has_sentence = 0, False
    for line in split_sections(text).get(k["scale"], "").splitlines():
        m = re.match(r"^\s*(?:[-*]\s*)?([^：:]+)[：:]", line)
        if not m:
            continue
        if m.group(1).strip().lower() == k["sentence"].lower():
            has_sentence = True
        elif re.match(r"^\s*[-*]\s", line):
            entries += 1
    if entries >= 2 and not has_sentence:
        return [f"尺度基线有 {entries} 个条目，但没有“{k['sentence']}:”一行，视频提示词要逐字照抄它 / "
                f"{entries} scale entries but no '{k['sentence']}:' line for prompts to copy"]
    return []


def colors_in(window):
    return set("".join(ZH_COLOR_PHRASE.findall(window))) | {c.lower() for c in EN_COLOR_RE.findall(window)}


def check_prompt_colors(text, prompts):
    """Colors written near a fixed-effect name must come from that effect's color in the bible.
    提示词里写到固定特效时，名字附近的颜色要在视觉圣经那一项的颜色里。只提醒。"""
    warnings = []
    for name, color in fixed_effects(text).items():
        allowed = set(ZH_COLOR_CHAR.findall(color)) | {c.lower() for c in EN_COLOR_RE.findall(color)}
        if not allowed:
            continue
        for lineno, line in enumerate(prompts.splitlines(), 1):
            for m in re.finditer(re.escape(name), line, re.I):
                left = max([line.rfind(c, 0, m.start()) for c in "，。；！？：、,.;!?:"] + [m.start() - 25]) + 1
                ends = [i for i in (line.find(c, m.end()) for c in "，。；！？：、,.;!?:") if i >= 0]
                right = min(ends + [m.end() + 25])
                window = line[left:m.start()] + " " + line[m.end():right]
                odd = sorted(colors_in(window) - allowed)
                if odd:
                    warnings.append(f"第{lineno}行 / line {lineno}: “{name}”旁边写了 {'、'.join(odd)}，"
                                    f"视觉圣经是“{color}”，逐字照抄 / bible says '{color}', copy it verbatim")
                    break
    return warnings


def main(argv=None):
    ap = argparse.ArgumentParser(description="Visual bible format check / 视觉圣经格式检查")
    ap.add_argument("file")
    ap.add_argument("--registry", help="asset sheet / 资产表")
    ap.add_argument("--prompts", nargs="*", default=[], help="prompt files to check fixed-effect colors / 提示词文件")
    args = ap.parse_args(argv)
    text = Path(args.file).read_text(encoding="utf-8")
    reg = Path(args.registry).read_text(encoding="utf-8") if args.registry else None
    errors = check(text, reg)
    warnings = check_warnings(text)
    for p in args.prompts:
        warnings += [f"{Path(p).name}: {w}" for w in check_prompt_colors(text, Path(p).read_text(encoding="utf-8"))]
    for e in errors:
        print("ERROR " + e)
    for w in warnings:
        print("WARN  " + w)
    print(("PASS" if not errors else f"FAIL: {len(errors)} error(s)") + (f", {len(warnings)} warning(s)" if warnings else ""))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
