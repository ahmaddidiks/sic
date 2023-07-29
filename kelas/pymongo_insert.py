import pymongo # meng-import library pymongo yang sudah kita install


password = "mn8LS7xnBTMLNc39"
uri = f"mongodb+srv://ahmaddidiks:{password}@sic.mig4sp7.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(uri)


db = client['182'] # ganti sesuai dengan nama database kalian
my_collections = db['sensor'] # ganti sesuai dengan nama collections kalian

# Data yang ingin dimasukkan
murid_1 = {'nama':'Didik','Jurusan':'IPA','Nilai':80}
murid_2 = {'nama':'Wilan', 'Jurusan':'TKJ','Nilai':90}

results = my_collections.insert_many([murid_1,murid_2])
print(results.inserted_ids) # akan menghasilkan ID dari data yang kita masukkan
