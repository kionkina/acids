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

     #print(person)
     if type(person) is int:
          person = str(person)
          q = "SELECT code, mark FROM courses WHERE courses.id="+ person

     else:
          person = str(person)
          the_id = c.execute("SELECT id FROM peeps WHERE peeps.name=" + "'" + person + "'")
          #print "THE_ID IS"
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


#takes list of all students and calculates their averages with find_grades()
#returns dict in form{name:[id,average]}
def compute_avgs():

     students=select_all_students()#takes list of all students
     avg_dict={}#creates dictionary of student averages

     for student in students:
          marks=find_grades(student[1])
          i=0
          total=0
          for grade in marks:
             i+=1
             total+=int(grade[1])
             avg_dict[student[1]]=[int(student[0]),int(total*10/i)/10.0]

     #print(avg_dict)
     return avg_dict
     #print(foo)
     #print foo.fetchall()

#takes dictoionary of {students:avgs} and creates table in db
def tablify():
     avgs=compute_avgs()

     f="acids.db"
     db = sqlite3.connect(f) #open if f exists, otherwise create
     c = db.cursor()    #facilitate db ops

     drop = "DROP TABLE peeps_avg"
     try:
		 c.execute(drop)
     except:
		'the fact that life is meaningless'

     create="CREATE TABLE peeps_avg (id INTEGER, average REAL)"
     c.execute(create)

     for student in avgs:
          add="INSERT INTO peeps_avg VALUES ('"+str(avgs[student][0])+"', '"+str(avgs[student][1])+"')"
          c.execute(add)
     c.execute("SELECT * FROM peeps_avg")
     rows=c.fetchall()
     '''
     for row in rows:
          print(row)
     '''
     db.commit()
     db.close()

def update_average(student, new_avg):
	f = "acids.db"
	db = sqlite3.connect(f)
	c = db.cursor()
	avgs = compute_avgs()
	cmd = 'this is a placeholder so i decide what goes here'
	if type(student) is int:
		cmd = "UPDATE peeps_avg SET average=" + str(new_avg) + " WHERE peeps_avg.id=\'" + str(student) + "\'"
	else:
		cmd = "UPDATE peeps_avg SET average=" + str(new_avg) + " WHERE peeps_avg.id=\'" + str(avgs[student][0]) + "\'"
	print cmd;
	c.execute(cmd)
	db.commit()
	db.close()
	#print avgs[student]

#update_average(4, 60)
#display_table('peeps_avg')
#update_average('digweed')
