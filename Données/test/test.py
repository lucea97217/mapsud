#%%
import sys 
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from mapsud.graph import trajet_optimal_min, trajet_optimal

#%%
#On test les cas particuliers

def test_traj1():
    result = trajet_optimal_min(41,42) 
    if result == -1:
        print('test trajet_optimal_min OK')
    else:
        print('Test failed')

   
def test_traj2():
    result =trajet_optimal(41,42)
    if result == -1:
        print('test trajet_optimal_min OK')
    else:
        print('Test failed')

if __name__ == '__main__':
    test_traj1()
    test_traj2()
# %%
