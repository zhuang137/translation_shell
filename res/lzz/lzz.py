import os
ffs=os.listdir('.')
print ffs
xls=[xl for xl in ffs if os.path.isdir(xl) and xl.startswith('values')]
#suffixs=[os.path.splitext(suffix)[0] for suffix in xls]
print xls
#os.mkdir('xlss')
os.chdir('xlss')
for suffix in xls:
    with open(suffix+'.xls','w+') as ff:
        pass

