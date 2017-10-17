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



def select_all_students():
     '''
     Look up each students grades
     Printss a list of tuples with grades
     '''
     f="acids.db"
     db = sqlite3.connect(f) #open if f exists, otherwise create
     c = db.cursor()    #facilitate db ops             
     
    
     q = "SELECT id, name FROM peeps"
     foo = c.execute(q)
     students=[]
     for bar in foo:
          students+=[bar]
     db.close()
     return students


def compute_avgs(students):
     f="acids.db"
     db = sqlite3.connect(f) #open if f exists, otherwise create
     c = db.cursor()
     
     avgDict={}
     for student in students:
          p = "SELECT mark FROM courses WHERE id = '"+ student[0]+"'"
          marks=c.execute(p)
          i=0
          total=0
          for grade in marks:
             i+=1
             total+=int(grade[0])
             avgDict[student[1]]=int(total*10/i)/10.0 
             
     print(avgDict)
     #print(foo)
     #print foo.fetchall()
     db.close()
    
compute_avgs(select_all_students())
