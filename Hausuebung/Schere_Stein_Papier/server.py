import random
import sqlite3
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()


# with open("stats.json", "w") as outfile:
# json.dump(stats, outfile)
connection = sqlite3.connect(os.getenv("DB_URL"), check_same_thread=False)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS statistics (player INTEGER, computer INTEGER, draw INTEGER, "
                   "stein INTEGER, papier INTEGER, schere INTEGER, spock INTEGER, echse INTEGER)")

@app.route('/saveStats', methods=['POST'])
def saveStats():
    data = request.get_json()
    print(data)
    cursor.execute("SELECT * FROM statistics")

    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO statistics VALUES (:Player, :Computer, :Unentschieden, :Stein, :Papier, :Schere, :Spock, :Echse)",
                       data)
    else:
        cursor.execute("UPDATE statistics SET player = :Player, computer = :Computer, draw = :Unentschieden, stein = :Stein, "
                       "papier = :Papier,  schere = :Schere, spock = :Spock, echse = :Echse", data)
    connection.commit()
    return jsonify({"message": "Success"})

@app.route('/getStats')
def getStats():
    cursor.execute("SELECT * FROM statistics")
    data = cursor.fetchall()
    res = {"Player": data[0][0], "Computer": data[0][1], "Unentschieden": data[0][2], "Stein": data[0][3], "Papier": data[0][4], "Schere": data[0][5], "Spock": data[0][6], "Echse": data[0][7]}
    print(res)
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)

