import pymongo
import pandas as pd

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'house'
MONGODB_DOCNAME = 'hangzhou'
FILE_NAME = 'house.csv'

def read_from_db():
    pyclient = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
    mdb = pyclient[MONGODB_DBNAME]
    post = mdb[MONGODB_DOCNAME]
    return pd.DataFrame(list(post.find()))

def write_to_csv():
    df = read_from_db()
    df.to_csv(FILE_NAME, encoding='utf_8_sig')

if __name__ == "__main__":
    write_to_csv()