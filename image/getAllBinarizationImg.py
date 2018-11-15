import os
import sys
import math
import util
import random
import functools
import numpy as np
from PIL import Image, ImageEnhance


img_path = sys.argv[1]

i = 0
while  i < 256:
    util.convertTo1(img_path, i)
    i += 1
