from flask import Flask, request, abort
import json
import sqlite3

app = Flask(__name__)
i = 10

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/post', methods=['POST'])

def create_blogpost():
    if not request.data or not 'title' in request.data:
        abort(400)
    conn = sqlite3.connect('/python-scripts/create_api/blog.db')
    with conn:
      c = conn.cursor()
      query = "insert into posts values("+str(i)+",'"+json.loads(request.data)['title']+"','"+json.loads(request.data)['body']+"');"
      print query
      print c.execute(query)
    global i
    i +=1
    return request.data, 201

@app.route('/get', methods=['GET'])

def get_blogpost():
    conn1 = sqlite3.connect('/python-scripts/create_api/blog.db')
    with conn1:
      g = conn1.cursor()
      g.execute('select * from posts')
      res_dict=dict()
      j=0
      for row in g:
        res_dict[j]={'id':row[1], 'title': row[1], 'post': row[2]}
        j += 1
      print type(json.dumps(res_dict))
    return json.dumps(res_dict), 200

if __name__ == '__main__':
    app.run(debug=True)
