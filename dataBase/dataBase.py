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
        return list(sum(self.cursor.fetchall(), ()))

    def getFullText(self, chapterName):
        print("getFulltext()")
        self.cursor.execute("SELECT description FROM VBScriptTutorial WHERE chapterName =  \"%s\";" % chapterName)
        return str(self.cursor.fetchone()[0])

    def deleteChapter(self, name):
        print("delete()")
        print("DELETE FROM VBScriptTutorial WHERE chapterName = \"%s\";" % name)
        self.cursor.execute("DELETE FROM VBScriptTutorial WHERE chapterName = \"%s\";" % name)
        self.connection.commit()
        print("After")
        self.getChapterName()
