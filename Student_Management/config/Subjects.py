"""The subjects table in the database contains
subject name and subject id."""
from Student_Management.config.database import Database
def create_subjects():
    DATABASE = Database()
    connection = DATABASE.connect()
    cursor = connection.cursor()
    query = ("insert into branches values (1,'OOPS'),"
             "(2,'ADS'),"
             "(3,'JAVA');")
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()