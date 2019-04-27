import mysql.connector
from mysql.connector import Error

class DataBase:
    def __init__(self):
        self.log = {}

        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                 user='root',
                                                 password='password',
                                                 database="aipos")

            print("Connected to MySQL database... ")
            self.cursor = self.connection.cursor()

        except Error as e:
            print("Error while connecting to MySQL", e)
        pass

    def getChapterName(self):
        print("getChapterName()")
        self.cursor.execute("select chapterName from VBScriptTutorial;")
        records = list(sum(self.cursor.fetchall(), ()))
        print(records)
        return records
