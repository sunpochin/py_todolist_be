from flask import Flask, render_template
from dotenv import load_dotenv
import os
# import MySQLdb

load_dotenv()

RDS_HOSTNAME = os.getenv("RDS_HOSTNAME")
RDS_USERNAME = os.getenv("RDS_USERNAME")
RDS_PASSWORD = os.getenv("RDS_PASSWORD")
RDS_PORT = os.getenv("RDS_PORT")
RDS_DB_NAME = os.getenv("RDS_DB_NAME")


# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
# application.add_url_rule('/', 'index', (lambda: header_text +
#     say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

def getDances():
    dances = []
    # db = MySQLdb.connect(host=RDS_HOSTNAME,
    #     port=3306,
    #     user=RDS_USERNAME,
    #     passwd=RDS_PASSWORD,
    #     db=RDS_DB_NAME,
    #     autocommit=True,
    #     use_unicode=True
    #     )
    # cursor = db.cursor()
    # query = """SELECT * FROM dances;"""
    # cursor.execute(query)
    # dances = cursor.fetchall()

    # # Convert it into a list for readability
    # dances = [list(l) for l in dances]
    # print('get Dances from mysql DB: ', dances)
    return dances


@application.route('/', methods=["GET"])
def index():
    return render_template('index.html', dances=getDances()) 


getDances()

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()


