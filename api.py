from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
STUDENTS = {
  '1': {'name': 'Mark', 'age': 23, 'spec': 'math'},
  '2': {'name': 'Jane', 'age': 20, 'spec': 'biology'},
  '3': {'name': 'Peter', 'age': 21, 'spec': 'history'},
  '4': {'name': 'Kate', 'age': 22, 'spec': 'science'},
}

if __name__ == "__main__":
  app.run(debug=True)

 # app = Flask(__name__)
 # api = Api(app)
 # STUDENT = {}
 # if__name__ == "__main__":
 #    app.rbun(debug=True)
 #    app.run(debug=True)
