from pymongo import MongoClient
from gridfs import GridFS
from django.conf import settings

def get_fs():
    client = MongoClient(settings.MONGO_CONFIG['HOST'], settings.MONGO_CONFIG['PORT'])
    db = client[settings.MONGO_CONFIG['NAME']]
    return GridFS(db)

def guardar_imagen(file_obj, filename):
    fs = get_fs()
    return fs.put(file_obj, filename=filename)

def obtener_imagen(file_id):
    fs = get_fs()
    return fs.get(file_id)
