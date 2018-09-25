#!flask/bin/python
from flask import Flask,request,render_template,json
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
 
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'CyNeuro'
app.config['MYSQL_DATABASE_PASSWORD'] = 'CtDewpCU2qwWsYkhjX89aZSH'
app.config['MYSQL_DATABASE_DB'] = 'CyNeuro'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/createUserProfile')
def createUserProfile():
    return render_template('createUserProfile.html')
@app.route('/signUp',methods=['create'])
def signUp():
 
    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    _hashed_password = generate_password_hash(_password)
    cursor.callproc('sp_createUserProfile',(_name,_email,_hashed_password))
    data = cursor.fetchall();
	# validate the received values
    #if _name and _email and _password:
    #    return json.dumps({'html':'<span>All fields good !!</span>'})
    #else:
    #    return json.dumps({'html':'<span>Enter the required fields</span>'})
	
    #print(data);	 
    if len(data) is 0:
        conn.commit()
        return json.dumps({'message':'User created successfully !'})
    else:
        return json.dumps({'error':str(data[0])})
@app.route("/Authenticate")
def Authenticate():
    name = request.args.get('name')
    email = request.args.get('email')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from users where name='" + name + "' and email='" + email + "'")
    data = cursor.fetchone()
    if data is None:
     return "Username or Password is wrong"
    else:
     return "email exists"

if __name__ == '__main__':
    app.run(debug=True)
