import os
from flask import Flask, request
from flask_bcrypt import Bcrypt
from flaskext.mysql import MySQL

app = Flask(__name__, static_url_path="/")
mysql = MySQL(app)
bcrypt = Bcrypt(app)

app.config['MYSQL_DATABASE_HOST'] = "localhost"
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = ""
app.config['MYSQL_DATABASE_DB'] = "simera"


def sql_database(sql_query):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql_query)
        row = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return row
    except Exception as e:
        print(e)
        return {"status": "failure"}


@app.after_request
def after_request_func(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response




@app.route('/api/login', methods=["POST"])
def check_user():
    try:
        _emailValue = request.json["emailValue"]
        _passwordValue = request.json["passwordValue"]
        print(_emailValue)

        sql_query = f"SELECT pwd FROM simera.users WHERE email='{_emailValue}';"
        password = sql_database(sql_query)

        if password:
            # pwd = bcrypt.check_password_hash(password[0], _passwordValue)
            if _passwordValue == password[0]:

                sql_query = f"SELECT token FROM simera.users WHERE email='{_emailValue}';"
                token= sql_database(sql_query)

                return {"status": "success", "token": token}
            else:
                return {"status": "false"}
        else:
            return {"status": "false"}
    except Exception as e:
        print(e)
        return {"status": "failure", "reason": e}


app.debug = True