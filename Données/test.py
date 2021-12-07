#%%
import pytest

from mapsud.graph import trajet_optimal,trajet_optimal_min
#%%
#On test les cas particuliers

def test_traj1():
    assert trajet_optimal_min(41,42) == -1
   
def test_traj1():
    assert trajet_optimal(41,42) ==-1

# %%
