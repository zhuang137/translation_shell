import os
ffs=os.listdir('..')
xls=[xl for xl in ffs if os.path.isdir(xl) and xl.startswith('values')]
suffixs=[os.path.splitext(suffix)[0] for suffix in xls]
#os.mkdir('lzz')
#os.chdir('lzz')
for suffix in suffixs:
    with open('suffixs.xml','a+') as ff:
        ff.write(suffix+",")
