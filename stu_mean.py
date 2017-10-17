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

def find_grades(person):
     '''
     Look up each students grades
     Printss a list of tuples with grades
     '''
     f="acids.db"
     db = sqlite3.connect(f) #open if f exists, otherwise create
     c = db.cursor()    #facilitate db ops
     q = "so the merge didn't update this part and I spent so long being confused lol"
     db = sqlite3.connect(f) #open if f exists, otherwise create
     c = db.cursor()    #facilitate db ops

     print(person)
     if type(person) is int:
          person = str(person)
          q = "SELECT code, mark FROM courses WHERE courses.id="+ person

     else:
          person = str(person)
          the_id = c.execute("SELECT id FROM peeps WHERE peeps.name=" + "'" + person + "'")
#          print "THE_ID IS"
          the_id = the_id.fetchall()[0][0] #stores id
          q = "SELECT code, mark FROM courses WHERE courses.id = " + "'" + the_id + "'"

     foo = c.execute(q)
     print(foo.fetchall())
     for x in foo:
          print(x)
     db.close()


find_grades(1)
#find_grades(4)
find_grades('digweed')


def add_to_courses(code, mark, id): #Important takeaway: always use db.commit()
	f = "acids.db"
	db = sqlite3.connect(f)
	c = db.cursor()
	cmd = "INSERT INTO courses (code, mark, id) VALUES (\'" + str(code) + "\', " + str(mark) + ", " + str(id) + ");"
	c.execute(cmd)
	db.commit() #apparently you need this
	db.close()

def add_rows_to_courses(list_of_people):
	#Use this format for list_of_people:
	#abunchofcourses = [("forensics", 27, 1), ("gov", 28, 2)]
	f="acids.db"
	db = sqlite3.connect(f)
	c = db.cursor()
	cmd = "INSERT INTO courses VALUES (?, ?, ?)"
	c.executemany(cmd, list_of_people)
	db.commit()
	db.close()

def delete_row(row_name):
	#I added this one so no one can see my testing
	try:
		f="acids.db"
		db = sqlite3.connect(f)
		c = db.cursor()
		cmd = "DELETE FROM courses WHERE code=\'"+row_name + "\'"
		c.execute(cmd)
		db.commit()
		db.close()
	except:
		print "sqlite3 got mad at you? maybe fix your request"

def display_table(table):
	f = "acids.db"
	db = sqlite3.connect(f)
	c = db.cursor()
	cmd = "SELECT * FROM " + table;
	ret = c.execute(cmd);
	for thing in ret:
		print thing;
	db.close()

#display_table("courses")

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
