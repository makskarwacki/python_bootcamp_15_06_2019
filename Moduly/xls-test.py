
from excel import OpenExcel
f = OpenExcel('Zeszyt1.xls')
f.read() # read all
x = f.read('A') # read 'A' row
print(x)
f.read(1) # f.read('1'), read '1' column
f.read('A5') # read 'A5' position
