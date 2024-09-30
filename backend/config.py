from pymongo import MongoClient

client = MongoClient("mongodb+srv://aishwaryamensinkai:sOGs4TlFH7uh0apD@cluster0.7pzey.mongodb.net/livestream_app_db?retryWrites=true&w=majority")
db = client['livestream_app_db']
overlays_collection = db['overlays']


# mongodb+srv://aishwaryamensinkai:sOGs4TlFH7uh0apD@cluster0.7pzey.mongodb.net/

# "mongodb+srv://aishwaryamensinkai:sOGs4TlFH7uh0apD@cluster0.mongodb.net/?retryWrites=true&w=majority")
