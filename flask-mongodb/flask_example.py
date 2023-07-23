from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/',methods=[ 'GET'])
def hello_world():
    return 'GET METHOD'

@app.route('/data',methods=['POST'])
def data():
    params = request.args.get('params')
    param2 = request.args.get('param_2')
    return f'Hello {params} param2: {param2}'


if __name__ == '__main__':
    app.run(host='0.0.0.0')