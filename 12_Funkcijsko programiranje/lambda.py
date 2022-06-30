def obrni(s):
  return s[::-1]
  
print((lambda s: s[::-1])("test"))

print(obrni("test"))

forty_two_producer = lambda: 42
forty_two_producer()

