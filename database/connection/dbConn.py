from pymongo import MongoClient


# MongoDB Client 및 db 커넥션 생성
def getDatabaseConn(dbName: str, url: str = 'localhost', port: int = 27017) -> MongoClient:
    client = MongoClient(url, port)
    print('MongoDB Connected')
    database = client[dbName]
    return database
