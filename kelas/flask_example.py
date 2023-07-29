from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/',methods=[ 'GET'])
def hello_world():
    return 'GET METHOD'

@app.route('/data',methods=['POST'])
def data():
    input = request.args.get('sensor')
    input2 = request.args.get('sensor2')
    input3 = request.args.get('sensor3')
    return f'sensor1= {input}, sensor2= {input2}, sensor3= {input3}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')