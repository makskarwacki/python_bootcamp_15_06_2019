
module_name = "re"
m = __import__(module_name)

for s in dir(m):
    print(s)

del(m)
print(m)
