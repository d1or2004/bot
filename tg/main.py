import psycopg2 as db


class Database:
    @staticmethod
    def connetc(query, type):
        database = db.connect(
            database="n37",
            user="postgres",
            host="localhost",
            password="2004"

        )
        cursor = database.cursor()
        cursor.execute(query)
        if type == " insert":
            database.commit()
            return " Inserted"

        if type == "select":
            return cursor.fetchall()
