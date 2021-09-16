import pymysql
pymysql.install_as_MySQLdb()

from dotenv import load_dotenv
import os

load_dotenv()

# DATABASE_URL = os.getenv("MYSQL_DATABASE_URL")
DATABASE_URL = os.getenv("AWS_MYSQL_URL")
DATABASE_USER = os.getenv("AWS_MYSQL_USER")
DATABASE_PASSWORD = os.getenv("AWS_MYSQL_PASSWORD")


from flask import Flask, render_template
import MySQLdb
application = Flask(__name__)
 
@application.route('/', methods=["GET"])
def index():
    db = MySQLdb.connect(host=DATABASE_URL,
        port=3306,
        user=DATABASE_USER,
        passwd=DATABASE_PASSWORD,
        db="flask_app",
        autocommit=True,
        use_unicode=True
        )
    cursor = db.cursor()
    query = """SELECT * FROM dances;"""
    cursor.execute(query)
    dances = cursor.fetchall()
    print('dances: ', dances)

    # Convert to a list for better readability
    dances = [list(l) for l in dances]
 
    return render_template('index.html', dances=dances)

