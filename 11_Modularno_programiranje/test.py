#import fibonacci

#print(dir(fibonacci))

#a = fibonacci.fib(6)
#print(a)

#b = fibonacci.ifib(7)
#print(b)

from fibonacci import fib as f

print(f(6))

import fibonacci

from importlib import reload
reload(fibonacci)




