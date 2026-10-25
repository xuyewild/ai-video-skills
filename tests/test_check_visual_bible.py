import re
import tempfile
import unittest
from pathlib import Path

from helpers import LANGS, SKILLS, run, script

# Words that differ between the two templates / 两份模板里不同的字
K = {
    "zh": {"video": "## 视频风格段", "dont": "## 禁止项", "short": "风格短名：", "fixed": "固定特效：",
           "scale": "## 尺度基线", "sentence": "比例句", "base": "风格基线：", "grey": "灰底："},
    "en": {"video": "## Video style", "dont": "## Don'ts", "short": "Style name:", "fixed": "Fixed effects:",
           "scale": "## Scale baseline", "sentence": "Scale sentence", "base": "Style baseline:",
           "grey": "Gray background:"},
}


def blocks(lang):
    text = (SKILLS / lang / "visual-bible" / "references" / "template.md").read_text(encoding="utf-8")
    return re.findall(r"````markdown\n(.*?)````", text, re.S)


def bible(lang, midjourney=False):
    b = blocks(lang)
    return b[0].replace(K[lang]["video"], b[1].strip() + "\n\n" + K[lang]["video"]) if midjourney else b[0]


def line_of(text, prefix):
    return next(l for l in text.splitlines() if l.startswith(prefix))


class CheckVisualBibleTest(unittest.TestCase):
    def check(self, lang, text, *extra):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        p = Path(tmp.name) / "bible.md"
        p.write_text(text, encoding="utf-8")
        args = []
        for name, content in extra:
            q = Path(tmp.name) / name
            q.write_text(content, encoding="utf-8")
            args += ["--registry" if name.startswith("reg") else "--prompts", q]
        return run(script(lang, "visual-bible", "check_visual_bible.py"), p, *args)

    def test_template_passes(self):
        for lang in LANGS:
            for mj in (False, True):
                with self.subTest(lang=lang, midjourney=mj):
                    code, out = self.check(lang, bible(lang, mj))
                    self.assertEqual(code, 0, out)

    def test_missing_section_and_fields(self):
        for lang in LANGS:
            k = K[lang]
            base = bible(lang)
            with self.subTest(lang=lang):
                code, out = self.check(lang, base.replace(k["dont"], "## Other"))
                self.assertEqual(code, 1)
                self.assertIn("missing section", out)
                code, out = self.check(lang, base.replace(line_of(base, k["short"]) + "\n", ""))
                self.assertEqual(code, 1)
                code, out = self.check(lang, base.replace(line_of(base, k["fixed"]), k["fixed"] + " gold"))
                self.assertIn("name = color", out)

    def test_video_hex_rejected(self):
        for lang in LANGS:
            with self.subTest(lang=lang):
                text = bible(lang)
                video = text.split(K[lang]["video"], 1)
                video[1] = video[1].replace("```text\n", "```text\n#526B70 ", 1)
                code, out = self.check(lang, K[lang]["video"].join(video))
                self.assertEqual(code, 1)
                self.assertIn("hex", out)

    def test_asset_block_rejects_time_weather(self):
        for lang in LANGS:
            for word in ("月光", "moonlight"):
                with self.subTest(lang=lang, word=word):
                    text = bible(lang)
                    head, tail = re.split(r"(?=^## (?:资产图风格段|Asset image style)\s*$)", text, maxsplit=1, flags=re.M)
                    tail = tail.replace("```text\n", f"```text\n{word}, ", 1)
                    code, out = self.check(lang, head + tail)
                    self.assertEqual(code, 1)
                    self.assertIn(word, out)

    def test_midjourney_rules(self):
        for lang in LANGS:
            with self.subTest(lang=lang):
                text = bible(lang, midjourney=True)
                code, out = self.check(lang, text.replace("no film grain\n```", "no film grain --ar 16:9\n```"))
                self.assertEqual(code, 1)
                self.assertIn("parameters", out)
                ref = "风格参考：" if lang == "zh" else "Style reference:"
                code, out = self.check(lang, text.replace(line_of(text, ref) + "\n", ""))
                self.assertEqual(code, 1)

    def test_scale_needs_numbers_and_sentence(self):
        for lang in LANGS:
            with self.subTest(lang=lang):
                text = bible(lang)
                scale = text.split(K[lang]["scale"], 1)[1].split("\n## ", 1)[0]
                first = next(l for l in scale.splitlines() if l.startswith("- "))
                code, out = self.check(lang, text.replace(first, first.split(":")[0].split("：")[0] + "： tall"))
                self.assertEqual(code, 1)
                sentence = next(l for l in scale.splitlines() if K[lang]["sentence"] in l)
                code, out = self.check(lang, text.replace(sentence + "\n", ""))
                self.assertEqual(code, 0, out)
                self.assertIn("WARN", out)

    def test_registry_match_and_mismatch(self):
        for lang in LANGS:
            with self.subTest(lang=lang):
                text = bible(lang)
                good = line_of(text, K[lang]["base"]) + "\n" + line_of(text, K[lang]["grey"]) + "\n"
                self.assertEqual(self.check(lang, text, ("reg.md", good))[0], 0)
                bad = good.replace("#808080", "#7F7F7F")
                code, out = self.check(lang, text, ("reg.md", bad))
                self.assertEqual(code, 1)
                self.assertIn("gray background differs", out)

    def test_prompt_color_warning(self):
        cases = {"zh": ("固定特效：护身符光＝青白色", "林舟举起手，护身符光泛起金色，照亮四周。", "护身符光泛起青白色的光。"),
                 "en": ("Fixed effects: amulet light = cyan white", "The amulet light flares gold across the room.",
                        "The amulet light flares cyan white.")}
        for lang in LANGS:
            line, bad, good = cases[lang]
            with self.subTest(lang=lang):
                text = bible(lang).replace(line_of(bible(lang), K[lang]["fixed"]), line)
                code, out = self.check(lang, text, ("p.md", bad))
                self.assertEqual(code, 0, out)
                self.assertIn("WARN", out)
                code, out = self.check(lang, text, ("p.md", good))
                self.assertNotIn("WARN", out)


if __name__ == "__main__":
    unittest.main()
