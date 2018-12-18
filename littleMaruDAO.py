import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

def getToken (userID = "1"):
    cur = conn.cursor()
    cur.execute("SELECT line_bot_api, webhook_handler FROM line_data WHERE user_id = \'" + userID + "\';")
    token = cur.fetchall()
    if token[0] == None:
        return None
    return token[0]

