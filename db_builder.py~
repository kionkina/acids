"""
Karina Ionkina
SoftDev1 pd07
HW09 -- All About That Base
2017-10-15
"""
import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
from csv import DictReader


def populate(filename, table_name):
    '''
    CREATES AND POPULATES TABLE FROM CSV FILE
    '''
    f="discobandit.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        dicts = []
        for dict in reader:
            dicts.append(dict)
        command1 = "CREATE TABLE " + table_name + " ( "
        for key in dicts[0].keys():
            command1 += key + " BLOB, "
        command1 = command1[: len(command1)-2] + ")"
        print command1
        c.execute(command1)
        for dict in dicts:
            s = "INSERT INTO " + table_name + " VALUES (" 
            for key in dict.keys():
                s += "'" + dict[key] + "'" + ","
            s = s[: len(s) - 1] + ")"
            c.execute(s)
            db.commit() #save changes
    db.close()  #close database


#populate("peeps.csv", "Peepz")
#populate("courses.csv", "coursez")

f="discobandit.db"
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

q = "SELECT * FROM coursez"

foo = c.execute(q).fetchall()
print foo

