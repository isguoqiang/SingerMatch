import numpy as np
from sklearn.model_selection import KFold
from sklearn.mixture import GaussianMixture
from routines import Routines
import configparser

config = configparser.ConfigParser()
config.read('../system.ini')
routines = Routines(config)