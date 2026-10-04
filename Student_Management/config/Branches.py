"""The branches table in the database contains
branch name and branch id."""
from Student_Management.config.database import Database
def create_branches():
    DATABASE = Database()
    connection = DATABASE.connect()
    cursor = connection.cursor()
    query = ("insert into branches values (1,'AIML'),"
             "(2,'CS'),"
             "(3,'DS'),"
             "(4,'CSE'),"
             "(5,'MECH'),"
             "(6,'CIVIL'),"
             "(7,'EEE'),"
             "(8,'ECE');")
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()