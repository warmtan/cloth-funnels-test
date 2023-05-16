
#%%

import torch
from torchmetrics import StatScores
import torchvision.transforms.functional as TF
import matplotlib.pyplot as plt
from real.utils import *
from argparse import ArgumentParser


import os
import sys
sys.path.append('/home/alper/folding-unfolding/src/PyFlex/bindings/build')
os.environ['PYFLEXROOT'] = '/home/alper/folding-unfolding/src/PyFlex'
os.environ['PYTHONPATH'] = '/home/alper/folding-unfolding/src/PyFlex/bindings/build'
os.environ['LD_LIBRARY_PATH'] = '/home/alper/folding-unfolding/src/PyFlex/external/SDL2-2.0.4/lib/x64'
os.chdir('/home/zhenjia/dev/folding-unfolding/src')
# from learning.nets import 
from utils import OrientationNet
from learning.nets import MaximumValuePolicy
from itertools import product

from real.setup import *
from learning.Memory import Memory

import time
import hashlib
import imageio
from tqdm import tqdm
from functools import partial
from cair_robot.envs.transformed_view_env import ImageStackTransformer
from real.realEnv import RealEnv

#%%
if __name__ == "__main__":
    print("cloth-funnels")
