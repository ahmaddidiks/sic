from flask import Flask
from flask import request
import pymongo # meng-import library pymongo yang sudah kita install


app = Flask(__name__)

password = "mn8LS7xnBTMLNc39"
uri = f"mongodb+srv://ahmaddidiks:{password}@sic.mig4sp7.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(uri)

db = client['231'] # ganti sesuai dengan nama database kalian
my_collections = db['sensor'] # ganti sesuai dengan nama collections kalian


def kirim_data(temperature, kelembapan, timestamp):
  # Data yang ingin dimasukkan
  sensor = {'temperature':temperature,'kelembapan': kelembapan, 'timestamp': timestamp}

  results = my_collections.insert_one(sensor)
  # print(results.inserted_ids) # akan menghasilkan ID dari data yang kita masukkan

@app.route('/',methods=[ 'GET'])
def hello_world():
    return 'GET METHOD'

@app.route('/sensor1',methods=['POST'])
def sensor1():
    temperature = request.args.get('temperature')
    kelembapan  = request.args.get('kelembapan')
    timestamp  = request.args.get('timestamp')
    
    kirim_data(temperature=temperature, kelembapan=kelembapan, timestamp=timestamp)

    return f'sensor1= {temperature}, sensor2= {kelembapan}, timestamp= {timestamp}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')