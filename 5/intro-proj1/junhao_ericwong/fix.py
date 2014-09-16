import sys
if len(sys.argv)>1:
    fileName=sys.argv[1]    
    f=open(fileName)
    s=f.read()
    f.close()
    f=open(fileName,'w')
    f.write(s.replace('\r\n','\n'))
    f.close()
else:
    print "Error, no arguments given\nProper usage: 'python fix.py fileToFix.py'"
