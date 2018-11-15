import os
import sys
import util
import math
import random
import functools
import numpy as np
from PIL import Image, ImageEnhance


dir = sys.argv[1]
size = sys.argv[2]

for img_path in util.imgList(dir):
    util.randomCrop(img_path, int(size))
