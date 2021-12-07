#%%
import unittest

from mapsud.graph import trajet_optimal,trajet_optimal_min
#%%
#On test les cas particuliers
class TestTraj(unittest.TestCase):
    def test_traj1(self):
        result=trajet_optimal_min(41,42)
        self.assertEqual(result,-1)

    def test_traj1(self):
        result=trajet_optimal(41,42)
        self.assertEqual(result,-1)
        
    def test_taj3(self):
        result=trajet_optimal(1,3)
        self.assertEqual(result,[(0, [1, 3], 0), (0, [1, 3], 1)])

if __name__=='__main__':
    unittest.main()

# %%
