from pymongo import MongoClient
#import setting
mongodb_uri ='mongodb+srv://raghugaikwad8641:Raghugaikwad8@userinfo.d4n8sns.mongodb.net/?retryWrites=true&w=majority'
port = 8000
conn = MongoClient(mongodb_uri,port)
Database = conn.get_database('userinfo')
print(Database)
print(conn)
db=conn['userinfo'] 
print(db)