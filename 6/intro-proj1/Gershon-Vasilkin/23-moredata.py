def get_file(filename):
    l=[]
    for line in open(filename).readlines():
        l.append(line.strip().split(','))
    return l

##Print out Stuyvesant's SAT info, it's progress report grade and it's
##frl_percent data from 2011. To do this, you have to look for 02M475
##in the appropriate columne in each list. Note that the demographic info
##has multiple years - you should just print the frl_percent data from the
##most recent year (which I believe is 2011)

satdata=get_file('SATnewest.csv')
demodata=get_file('demographics.csv')
progressdata=get_file('progress_reports.csv')

def print_sat():
    '''
    Prints out the most recent SAT data from Stuyvesant for each category
    '''
    for list in satdata:
        if list[0]=='02M475':
            #data=list[2:]
            testtakers=int(list[2])
            verbal=int(list[3])
            math=int(list[4])
            writing=int(list[5])
    print "Stuy SAT data: Test takers:", testtakers, "Verbal:", verbal, "Math:", math, "Writing:", writing


        
def print_frl_percent():
    '''
    Prints out the most recent free/reduced lunch percentage for Stuyvesant
    '''
    for list in demodata:
        if list[0]=='02M475':
            if list[2]=='20102011':
                frl=float(list[4])
    print "Free/Reduced Lunch Percent for 2011 at Stuyvesant: ", frl

##def progress_report_grade():
##    '''
##    Prints out the progress report grade for Stuyvesant for 2010-2011
##    '''
##    for list in progressdata:
##        if list[0]=='02M475':
##            prg=list[7]
##    print "Progress report grade for Stuyvesant for 2010-2011: ", prg
#Stuyvesant is not in the progress report data file

print_sat()
print_frl_percent()

