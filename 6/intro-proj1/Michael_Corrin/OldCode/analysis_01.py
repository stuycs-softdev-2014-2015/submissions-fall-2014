#!/usr/bin/python
print "Content-type:text/html\n"
print ""
 
def sumSAT(table):
    outStream=open(table,'r')
    x = outStream.readlines()
    outStream.close()
    y = 1
    num = 0
    num2 = 0
    num3 = 0
    num4 = 0
    v = 0
    m= ""
    while y < len(x):
        n = x[y].split(",")
        if n[3] == "s":
            y+= 1
        else:
            num += int(n[3]) + int(n[4]) + int(n[5])
            num2 += int(n[3])
            num3 += int(n[4])
            num4 += int(n[5])
            v += 1
            y+= 1
    m += "<tr> <td>" +str(num/v)+" </td> <td>" +str(num2/v)+ "</td> <td>"\
        +str(num3/v)+ "</td> <td>"+str(num4/v)+"</td></tr> </table>"
    return m
            
            
        
#print int(x[1].split(",")[5])+ int(x[1].split(",")[4])

sumSAT("2010SAT.csv")

def sumSAT2(table,num=0):
    outStream=open(table,'r')
    x = outStream.readlines()
    outStream.close()
    y = 1
    num = 0
    num2 = 0
    num3 = 0
    num4 = 0
    v = 0
    m= ""
    while y < len(x):
        n = x[y].split(",")
        if n[3] == "s":
            y+= 1
        else:
            
            num += int(n[3]) + int(n[4]) + int(n[5])
            if num >= 1800:
                m+="<td>"+ n[1]+"</td><td>" + n[2] +"</td><td>"+ str(num)+"</td></tr><tr>"
            num = 0
            y += 1
    return m

sumSAT2('2010SAT.csv')

def makeanalysis():
    y = "<!DOCTYPE html> <html><body> <h1><div align='center'> 2010 SAT NYC Scores</div></h1><body> <br>"+\
        "By Michael Huang and Nathan Fok <br><br> I chose this data because I feel personally connected to the SAT scores of others sinceI will be taking the test myself around next year. Looking at other people's scores give me a good idea of what I should aim for. A few questions that I have for the data is the average of all the schools, the average of each individual score. I can use the data to get a good idea of just how well NYC is doing SAT-wise.<br>"+\
        "The link to the original data table is <a href='http://bart.stuy.edu/~zhao.huang/Hw_26/data01.py'> Data_01 </a> <br><br>"+\
        "The link to the SAT CSV file is <a href='http://bart.stuy.edu/~zhao.huang/Hw_26/2010SAT.csv'>SAT </a><br><br>"+\
        "<table border='1'><tr> <th>Overall Mean</th><th>Critical Reading Mean</th><th>Mathematics Mean</th><th>Writing Mean</th></tr>"+ sumSAT("2010SAT.csv")+\
        "<tr> <br> <br> Since the test is out of 2400, an average of 1214 is pretty mediocre. We can see that the best subject for NYC is mathematics and the worse is writing, but not by far though. <br> Now lets take a look at schools with SAT scores over 1800 along with how many students took the test in that school. <br><br><table border='1'><tr>"+\
        "<br> <br> Since the test is out of 2400," +\
        "an average of 1214 is pretty mediocre. We can see that the best subject" +\
        "for NYC is mathematics and the worst is writing, but not by far though. <br>"+\
        "Now lets take a look at schools with SAT scores over 1800 along with how many students took the test in that school. <br><br>"+\
        "<table border='1'><tr> <th>School Name </th><th>Number of Test Takers</th><th>Score</th></tr> <tr>"+\
        sumSAT2("2010SAT.csv")+"</tr></table> <br><br>  Many of these top scoring schools are specialized high schools and have quite a bit of test-takers. Brooklyn Tech has the largest amount of test takers while Stuyvesant has the highest mean out of all the schools."+ \
        "Being a Stuyvesant student myself, I feel proud of our great school and will strive to do my best !</body> </html> " 
    print y

makeanalysis() 
