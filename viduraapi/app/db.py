from flask import Flask,jsonify,abort, make_response
import MySQLdb

app = Flask(__name__)

db = MySQLdb.connect("localhost", "CyNeuro", "CtDewpCU2qwWsYkhjX89aZSH", "CyNeuro")

@app.route('/todo/api/v1.0/db', methods=['GET'])
def get_items():
    curs = db.cursor()
    try:
        curs.execute("SELECT * FROM monitor")
        

    except:
        print("Error: unable to fetch items")
    return jsonify({"desired: ",response})