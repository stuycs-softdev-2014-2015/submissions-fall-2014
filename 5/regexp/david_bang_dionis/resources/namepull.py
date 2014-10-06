import re,sys
if __name__ =="__main__":
    var= raw_input("Enter input file name:\t")
    var2= raw_input("Enter output filname:\t")
    try:
        f1=open(var,"r")
        f2=open(var2,"w")
        f=f1.read()
        r=re.findall("[A-Z]+",f)
        for i in r:
            f2.write(i[0]+i[1:].lower()+"\n")
        f1.close()
        f2.close()
    except:
        print "Fatal Error!"
    
