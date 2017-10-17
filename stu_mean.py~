"""
TEAM ACIDS: Holden Higgins, Karina Ionkina, Shaina Peters
SoftDev1 pd07
HW10 -- Average
2017-10-15
"""
import sqlite3   #enable control of an sqlite database


#populate("peeps.csv", "Peepz")
#populate("courses.csv", "coursez")

#f="acids.db"
#db = sqlite3.connect(f) #open if f exists, otherwise create
#c = db.cursor()    #facilitate db ops

#print foo #list of tuples containing course data
#---------------------------------------HW 10 CODE ------------------------------------------------

def find_grades(input):
     '''
     Look up each students grades
     Printss a list of tuples with grades
     '''
     f="acids.db"
     db = sqlite3.connect(f) #open if f exists, otherwise create                                   
     c = db.cursor()    #facilitate db ops             
     input = str(input)
     print(input)
     q = "SELECT code, mark FROM courses WHERE courses.id = " + "'" + input + "'" 
     foo = c.execute(q)
     #print(foo)
     #print(foo.fetchall())
     for x in foo:
          print(x)
     db.close()
     
 
find_grades(1)



def compute_avgs():
    '''
    Look up each students grades
    Printss a list of tuples with grades
    '''
    f="acids.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c1 = db.cursor()    #facilitate db ops             
    c2 = db.cursor()
    
    q = "SELECT id, name FROM peeps"
    foo = c1.execute(q)

    avgDict={}
    for bar in foo:
        #print(bar)
        p = "SELECT mark FROM courses WHERE id = '"+ bar[0]+"'"
        marks=c2.execute(p)
        i=0
        total=0
        for grade in marks:
            i+=1
            total+=int(grade[0])
        avgDict[bar[1]]=int(total*10/i)/10.0 

    print(avgDict)
    #print(foo)
    #print foo.fetchall()
    db.close()
    

compute_avgs()
