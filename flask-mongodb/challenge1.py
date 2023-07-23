import pymongo # meng-import library pymongo yang sudah kita install
from flask import Flask
from flask import request
app = Flask(__name__)

password = 'ebNcWXOU9EiNrSJq'
uri = f"mongodb+srv://ahmaddidiks:{password}@sic.mig4sp7.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(uri)
db = client['challenge1'] # ganti sesuai dengan nama database kalian
my_collections = db['sensor'] # ganti sesuai dengan nama collections kalian

def kirim_data(temperature, kelembapan):
    sensor = {'kelembapan':kelembapan, 'temperature':temperature}
    results = my_collections.insert_many([sensor])
    print(results.inserted_ids) # akan menghasilkan ID dari data yang kita masukkan

@app.route('/',methods=[ 'GET'])
def hello_world():
    return 'GET METHOD'

@app.route('/sensor1',methods=['POST'])
def data():
    temperature = request.args.get('temperature')
    kelembapan = request.args.get('kelembapan')

    if temperature is not None:
        temperature = float(temperature)
    if kelembapan is not None:
        kelembapan = float(kelembapan)

    #mengirim data sensor ke db
    kirim_data(temperature=temperature, kelembapan=kelembapan)

    return f'temperature: {temperature}, kelembapan: {kelembapan}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')