from flask import Flask

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
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()


# import pymysql
# pymysql.install_as_MySQLdb()

# from dotenv import load_dotenv
# import os

# load_dotenv()

# # DATABASE_URL = os.getenv("MYSQL_DATABASE_URL")
# DATABASE_URL = os.getenv("AWS_MYSQL_URL")
# DATABASE_USER = os.getenv("AWS_MYSQL_USER")
# DATABASE_PASSWORD = os.getenv("AWS_MYSQL_PASSWORD")


# from flask import Flask, render_template
# import MySQLdb
# application = Flask(__name__)
 
# @application.route('/', methods=["GET"])
# def index():
#     db = MySQLdb.connect(host=DATABASE_URL,
#         port=3306,
#         user=DATABASE_USER,
#         passwd=DATABASE_PASSWORD,
#         db="flask_app",
#         autocommit=True,
#         use_unicode=True
#         )
#     cursor = db.cursor()
#     query = """SELECT * FROM dances;"""
#     cursor.execute(query)
#     dances = cursor.fetchall()
#     print('dances: ', dances)

#     # Convert to a list for better readability
#     dances = [list(l) for l in dances]
 
#     return render_template('index.html', dances=dances)

