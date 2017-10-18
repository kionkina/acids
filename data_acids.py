####CREATES acids.db WITH peeps.csv and courses.csv

import csv
import sqlite3

f="acids.db"


def datify(name):

    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    #==========================================================
    #INSERT YOUR POPULATE CODE IN THIS ZONE
    table = csv.DictReader(open(name+".csv"))

    has_table=False
    for row in table:
        #first time through
        if not has_table:
            # Create table
            createStr="CREATE TABLE "+name+" ("
            for key in row:
                createStr+=key+" blob, "
                
            createStr=createStr[0:-2]+")"
            #print(createStr) #diag print
            c.execute(createStr)
            has_table=True
        
        # Insert a row of data
        insertStr="INSERT INTO "+name+" VALUES ("
        for key in row:
            insertStr+="'"+row[key]+"',"
            #print(key+", "+row[key]) #diag print
            
        insertStr=insertStr[0:-1]+")"
        #print(insertStr)#diag print
        c.execute(insertStr)
    #diagnostic that prints table out by row
    """
    c.execute("SELECT * FROM "+name)
    rows=c.fetchall()
    for row in rows:
        print(row)
    """
    #==========================================================
    db.commit() #save changes    
    db.close()  #close database

datify("peeps")
datify("courses")
'''
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

foo=c.execute("""SELECT name, peeps.id, mark, code
    FROM peeps, courses
    WHERE peeps.id=courses.id;""")
for bar in foo:
    print(bar)


db.commit() #save changes    
db.close()  #close database
'''
