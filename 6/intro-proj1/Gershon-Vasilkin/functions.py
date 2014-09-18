

def get_file(filename):
    l=[]
    for line in open(filename).readlines():
        l.append(line.strip().split(','))
    return l
    
inspectiondata = get_file('Results_Without_violations.csv')


def general_data(col1,data1,col2):
    '''
    col1 - column of first data type
    data1 - string of what you are looking for
    col2 - the other column you are comparing it to
    '''
    d = {}
    for list in inspectiondata:
        if list[col1]==data1:
            if d.has_key(list[col2]):
                d[list[col2]]+=1
            else:
                d[list[col2]]=1
    return d

def specific_data(col1,data1,col2,data2):
    i = 0
    for list in inspectiondata:
        if list[col1] == data1 and list[col2] == data2:
            i+=1
    return i

#print general_data(1,"QUEENS",3)
print "\n"
print general_data(1,"QUEENS",6)
print specific_data(1,"QUEENS",6,"A")
