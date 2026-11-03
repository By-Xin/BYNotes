import hashlib
import json
import math
from pathlib import Path
import re
import unittest
from corrections import apply_corrections

LEDGER = json.loads(Path(__file__).with_name("decision-theory-corrections.json").read_text())
CHANGES = {entry["id"]: entry for entry in LEDGER["changes"]}


class CorrectionTests(unittest.TestCase):
    def test_stale_sources_and_ambiguous_context_fail(self):
        ledger = {"source_sha256": hashlib.sha256(b"one one").hexdigest(), "changes": [{"id":"x", "before":"one", "after":"two"}]}
        with self.assertRaises(ValueError):
            apply_corrections("new source", ledger)
        with self.assertRaises(ValueError):
            apply_corrections("one one", ledger)
        ledger["changes"][0]["count"] = 2
        self.assertEqual(apply_corrections("one one", ledger), "two two")

    def test_published_sqrt_expectations_match_given_lotteries(self):
        body = CHANGES["expected-utility-example"]["after"]
        p, q = map(float, re.findall(r"\\approx ([0-9.]+)", body))
        self.assertAlmostEqual(p, .25*math.sqrt(10)+.25*math.sqrt(20)+.5*math.sqrt(40), places=3)
        self.assertAlmostEqual(q, .5*math.sqrt(10)+.5*math.sqrt(20), places=3)
        self.assertGreater(p, q)

    def test_cara_sign_preserves_certain_outcome(self):
        formula = CHANGES["cara-sign-and-domain"]["after"]
        sign = -1 if re.search(r"=\s*-\\frac", formula) else 1
        a, z = .2, 3
        ce = sign * math.log(math.exp(-a*z))/a
        self.assertAlmostEqual(ce, z)

    def test_risk_aversion_implication_matches_certainty_equivalents(self):
        relation = CHANGES["risk-aversion-direction"]["after"]
        first, second = map(int, re.findall(r"\\succeq_([12])", relation))
        # 50% at 0 / 50% at 4: sqrt utility has CE=1; linear utility CE=2.
        ce = {1:1, 2:2}
        for z in (0, .5, 1, 1.5, 2, 3, 4):
            self.assertTrue(not z >= ce[first] or z >= ce[second])


if __name__ == "__main__":
    unittest.main()
