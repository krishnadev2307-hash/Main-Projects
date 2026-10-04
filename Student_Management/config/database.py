"""Design of Database class, creates a Database object and gives
connection to db"""
import mysql.connector
import os

class Database:

    def __init__(self):
        self._connection = None
        '''Will be none firstly'''

    def connect(self):#Gives the connection to the database
        password = os.getenv("MYSQL_PASSWORD")
        try:
            self._connection = mysql.connector.connect(
            host = "localhost",
            port = 3306,
            password = password,
            database = "StudentManagement",
            user = "root",
            )
        except mysql.connector.Error as err:
            print(err)
        return self._connection

    def close(self): #Closes the connection
        if self._connection is not None:
            self._connection.close()
            self._connection = None
        else:
            print("There is no connection to the database")