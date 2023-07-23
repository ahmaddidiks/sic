import pymongo # meng-import library pymongo yang sudah kita install

password = 'ebNcWXOU9EiNrSJq'
uri = f"mongodb+srv://ahmaddidiks:{password}@sic.mig4sp7.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(uri)
db = client['test_database'] # ganti sesuai dengan nama database kalian
my_collections = db['test_collection'] # ganti sesuai dengan nama collections kalian

for x in my_collections.find():
 print(x)