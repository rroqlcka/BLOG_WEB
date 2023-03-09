# from flask import Flask, render_template
#
# app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.DBtest

db.users.insert_one({'name':'Yoon','age':21})
all_users = list(db.users.find({}))
print(all_users)

# @app.route('/')
# def home():
#     return render_template('start_page.html')
#
# @app.route('/main_page')
# def main_page():
#     return render_template('main_page.html')
#
#
# if __name__ == '__main__':
#     app.run('0.0.0.0',port=5000, debug= True)
