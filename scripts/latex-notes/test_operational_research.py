"""Focused regressions for corrected claims; no added exposition in the note."""
import json
from pathlib import Path
import unittest
from corrections import apply_corrections

SOURCE = Path(__file__).resolve().parents[2] / 'sources/deterministic-operational-research'

class RevisionTests(unittest.TestCase):
    def test_ledger_reconstructs_exact_revision(self):
        self.assertEqual(apply_corrections((SOURCE/'original.md').read_text(), json.loads((SOURCE/'corrections.json').read_text())), (SOURCE/'revised.md').read_text())

    def test_projection_midpoint_algebra(self):
        # Equal-distance points: the cross term need not be negative.
        y, x1, x2 = (0, 3), (-1, 0), (1, 0)
        dot = lambda a,b: sum(x*z for x,z in zip(a,b))
        sub = lambda a,b: tuple(x-z for x,z in zip(a,b))
        u,v = sub(y,x1),sub(y,x2)
        distance2=dot(u,u)
        cross=dot(u,v)
        self.assertGreater(cross,0)
        self.assertEqual(cross,distance2-.5*dot(sub(x1,x2),sub(x1,x2)))
        midpoint_distance=.25*dot(u,u)+.25*dot(v,v)+.5*cross
        self.assertEqual(midpoint_distance,9)
        self.assertLess(midpoint_distance,distance2)

    def test_nearest_pair_is_not_unique(self):
        pairs=[((t,0),(t,1)) for t in (0,.5,1)]
        self.assertEqual(len({(b[0]-a[0],b[1]-a[1]) for a,b in pairs}),1)
        self.assertEqual(len(set(pairs)),3)

    def test_farkas_rhs_is_essential(self):
        # A=-1, b=1: x=1 satisfies Ax<=0, x>=0, bx>0.
        # The old certificate A'y>=0 has y=0; the corrected A'y>=b has none.
        x,A,b=1,-1,1
        self.assertTrue(A*x<=0 and x>=0 and b*x>0)
        self.assertTrue(A*0>=0)
        self.assertTrue(all(A*y<b for y in (0,.1,1,100)))

    def test_positive_slack_step(self):
        slack,ad=2,-3
        bound=slack/(2*abs(ad))
        self.assertGreater(bound,0)
        self.assertTrue(all(slack+t*ad>0 for t in (-bound*.9,bound*.9)))

if __name__=='__main__': unittest.main()
