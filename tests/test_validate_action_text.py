import tempfile
import unittest
from pathlib import Path

from helpers import LANGS, SKILLS, run, script

GOOD = {
    "zh": """【动作】过肩摔｜片段10秒｜第1/2拍
起手：她右脚踩稳，双手抓住他的衣领。
接触：她转身把右胯顶进他的腹部。
结果：他从她肩上翻过去，后背着地，滑到木箱边停住。
碰撞：重｜环境：地上的灰被震起｜镜头：着地那一下画面向下一震
受力方向：从画面右向画面左。
镜头配合：中景，镜头沿弧线跟住。
""",
    "en": """[Action] Shoulder throw | clip 10s | beat 1/2
Setup: She plants her right foot and grabs his collar with both hands.
Contact: She turns and drives her right hip into his belly.
Result: He flips over her shoulder, lands on his back and slides to a stop against the crate.
Impact: heavy | Environment: dust jumps off the floor | Shake: one jolt downward
Force direction: from frame right to frame left.
Camera: medium shot, the camera follows the arc.
""",
}
PROSE = {
    "zh": "【动作段】\n他左脚踩实，右腿从右侧甩出，脚背抽在岩石侧面。岩石裂开，上半块向左滑出翻倒。\n",
    "en": "[Action passage]\nHe plants his left foot and whips his right leg in, striking the rock with his instep. "
          "The rock cracks and the top half slides to the left and topples.\n",
}
BAD_PROSE = {"zh": "【动作段】\n他狠狠地出手。\n", "en": "[Action passage]\nHe violently attacks.\n"}


class ValidateActionTest(unittest.TestCase):
    def check(self, lang, text, *args):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        p = Path(tmp.name) / "a.md"
        p.write_text(text, encoding="utf-8")
        return run(script(lang, "action-physics-choreography", "validate_action_text.py"), p, *args)

    def test_good_blocks(self):
        for lang in LANGS:
            for text in (GOOD, PROSE):
                with self.subTest(lang=lang):
                    code, out = self.check(lang, text[lang])
                    self.assertEqual(code, 0, out)

    def test_templates_pass(self):
        for lang in LANGS:
            with self.subTest(lang=lang):
                p = SKILLS / lang / "action-physics-choreography" / "references" / "action-templates.md"
                code, out = run(script(lang, "action-physics-choreography", "validate_action_text.py"), p)
                self.assertEqual(code, 0, out)

    def test_missing_field_and_order(self):
        for lang in LANGS:
            with self.subTest(lang=lang):
                lines = GOOD[lang].splitlines()
                code, out = self.check(lang, "\n".join(l for l in lines if not l.startswith(("受力方向", "Force"))))
                self.assertEqual(code, 1)
                self.assertIn("missing", out)
                swapped = "\n".join([lines[0], lines[3], lines[2], lines[1]] + lines[4:])
                code, out = self.check(lang, swapped)
                self.assertIn("order must be", out)

    def test_direction_and_impact_level(self):
        for lang in LANGS:
            with self.subTest(lang=lang):
                text = GOOD[lang]
                no_dir = text.replace("从画面右向画面左。", "很远。").replace("from frame right to frame left.", "far.")
                code, out = self.check(lang, no_dir)
                self.assertIn("no direction", out)
                bad_level = text.replace("碰撞：重", "碰撞：超重").replace("Impact: heavy", "Impact: mega")
                code, out = self.check(lang, bad_level)
                self.assertIn("impact must be one of", out)

    def test_clip_length(self):
        for lang in LANGS:
            with self.subTest(lang=lang):
                long = GOOD[lang].replace("片段10秒", "片段20秒").replace("clip 10s", "clip 20s")
                self.assertEqual(self.check(lang, long)[0], 0)
                code, out = self.check(lang, long, "--model", "2.0")
                self.assertIn("outside 4–15s", out)
                frac = GOOD[lang].replace("片段10秒", "片段7.5秒").replace("clip 10s", "clip 7.5s")
                self.assertIn("not a whole number", self.check(lang, frac)[1])

    def test_bad_prose_and_intensifier(self):
        for lang in LANGS:
            with self.subTest(lang=lang):
                code, out = self.check(lang, BAD_PROSE[lang])
                self.assertEqual(code, 1)
                for needle in ("no contact", "no force or movement direction", "intensifier without process"):
                    self.assertIn(needle, out)

    def test_prose_mode_and_empty_file(self):
        for lang in LANGS:
            with self.subTest(lang=lang):
                plain = PROSE[lang].split("\n", 1)[1]
                self.assertEqual(self.check(lang, plain)[0], 1)
                code, out = self.check(lang, plain, "--prose")
                self.assertEqual(code, 0, out)


if __name__ == "__main__":
    unittest.main()
