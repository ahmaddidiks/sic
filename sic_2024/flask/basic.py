#!/usr/bin/python
# coding: utf-8
from flask import Flask
from flask import request

app = Flask(__name__)

data = []

@app.route('/sic')
def sic():
    return 'Kelas SIC 2024'

@app.route('/sensor/data', methods=['POST'])
def post():
    temperature = request.args.get("temperature")
    kelembapan = request.args.get("kelembapan")
    subData = [temperature, kelembapan]
    
    data.append(subData)

    return  'berhasil disimpan ke server'

@app.route('/sensor/data', methods=['GET'])
def get():
    return data

if __name__ == '__main__':
    app.run(debug=True)
