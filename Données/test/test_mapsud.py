#%%
import sys 
import os
import pytest
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import mapsud
from mapsud.graph import trajet_optimal_min, trajet_optimal

#%%
#On test les cas particuliers

def test_traj1():
    assert trajet_optimal_min(41,42) == -1 

   
def test_traj2():
    assert trajet_optimal(41,42) == -1

