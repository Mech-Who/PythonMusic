from enum import Enum

class Beat(float, Enum):
    FULL = 1/4
    HALF = 1/8
    QUAR = 1/16
