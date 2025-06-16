import requests
import sys
import pandas as py
import mysql.connector
from sqlalchemy import create_engine
class TransferMatchData:
    def __init__(self):
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Alex94563$",
        database="match_data",
        )
        cursor = connection.cursor()
        print("hwllo qol")

if __name__ == "__main__":
    TransferMatchData()