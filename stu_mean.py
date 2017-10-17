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

     ###print(input)
     if type(input) is int:
          input = str(input)
          q = "SELECT code, mark FROM courses WHERE courses.id = " + "'" + input + "'" 

     else: 
          input = str(input)
          the_id = c.execute("SELECT id FROM peeps WHERE peeps.name = " + "'" + input + "'")
#          print "THE_ID IS"
          the_id = the_id.fetchall()[0][0] #stores id
          q = "SELECT code, mark FROM courses WHERE courses.id = " + "'" + the_id + "'" 

     foo = c.execute(q)
     #print(foo.fetchall())
     grades=[]
     for x in foo:
          grades+=[x]
     db.close()
     #print(grades)
     return grades
 
#find_grades(1)
#find_grades(4)
#find_grades('digweed')

#returns list of all students and their ID numbers in the form [(<name>,<id>)...]
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
     #print(students)
     return students


def compute_avgs():
     
     students=select_all_students()#takes list of all students
     avgDict={}#creates dictionary of student averages

     for student in students:
          marks=find_grades(student[1])
          i=0
          total=0
          for grade in marks:
             i+=1
             total+=int(grade[1])
             avgDict[student[1]]=int(total*10/i)/10.0 
             
     print(avgDict)
     #print(foo)
     #print foo.fetchall()
     
    
compute_avgs()
