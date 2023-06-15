from math import pi as p

print(p)

#import fibonacci as fibo

#from fibonacci import ifib

#for i in range(5):
#  print(ifib(i))
  
#print(dir(fibo))
import fibonacci

from importlib import reload
reload(fibonacci)

import sys
print(sys.builtin_module_names)

import random
print(random.__file__)
 

