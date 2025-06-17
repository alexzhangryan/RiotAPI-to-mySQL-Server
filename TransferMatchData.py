import requests
import sys
import pandas as pd
import mysql.connector
import sqlalchemy
from sqlalchemy import create_engine
from api import *
class TransferMatchData:
    def readTable(self):
        con_string = "mysql+mysqlconnector://root:test_password@localhost/lol_data"
        engine = create_engine(con_string)
        query = "SELECT * FROM matches"
        df_read_sql = pd.read_sql(query, engine)
        print(df_read_sql)
    def insertMatch(self, match):
        try:
            connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="test_password",
            database="lol_data",
            )
            cursor = connection.cursor()

            query = "INSERT INTO matches VALUES (%s)"

            cursor.execute(query, (match,))

            connection.commit()
            cursor.close()
            connection.close()
        except:
            print("match_id already exists in the database")
    def __init__(self):
        self.readTable()
        puuid = 'mjP3GtqTPOeE2-jg8bqSOt2QsI5ml5VYA4O5jbKjLA7dVUIsVj44LuPN6kwD3NKV9AZOpVAJPS1htw'
        matches = api.get_matches(api, puuid)
        for match in matches:
            self.insertMatch(match)
        self.readTable()


if __name__ == "__main__":
    TransferMatchData()