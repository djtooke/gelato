from enum import Enum

AIM = {'fat': range(6, 12),
       'sugar': range(16, 22),
       'lm_s': range(8, 12),
       'oth_s': range(0, 100),
       'water': range(58, 68),
       'dry': range(32, 42)
     }

class Result(Enum):
    TOO_LOW = 0
    OKAY = 1
    TOO_HIGH = 2