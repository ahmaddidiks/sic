import pymongo # meng-import library pymongo yang sudah kita install
client = pymongo.MongoClient("MASUKAN ID KALIAN")

password = "mn8LS7xnBTMLNc39"
uri = f"mongodb+srv://ahmaddidiks:{password}@sic.mig4sp7.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(uri)

db = client['gudang'] # ganti sesuai dengan nama database kalian
my_collections = db['rak'] # ganti sesuai dengan nama collections kalian

for x in my_collections.find():
  print(x["nama"], x["Nilai"])
