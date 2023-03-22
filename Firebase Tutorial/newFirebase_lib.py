# new firebase test
# pip install pyrebase4 
import pyrebase
JSONlocation = "D:\\Download\\firebase.json"
db_config = {
  "apiKey": "AIzaSyCJ7NBM2vTv71EM2AQMtfW3cXNnWiXvGBQ",
  "authDomain": "ntust-dal.firebaseapp.com",
  "databaseURL": "https://ntust-dal-default-rtdb.firebaseio.com/",
  "serviceAccount": JSONlocation,
  "projectId": "ntust-dal",
  "storageBucket": "ntust-dal.appspot.com",
  "messagingSenderId": "839926714277",
  "appId": "1:839926714277:web:f949cc304a2dd7948b224c",
  "measurementId": "G-0N1ZF71Q81"
}
#firebase storage儲存照片空間的宣告
stor_config = {
   "apiKey": "AIzaSyCJ7NBM2vTv71EM2AQMtfW3cXNnWiXvGBQ",
   "authDomain": "ntust-dal.firebaseapp.com",
   "databaseURL": "gs://ntust-dal.appspot.com/",
   "serviceAccount": "D:\\Download\\firebase.json",
   "projectId": "ntust-dal",
   "storageBucket": "ntust-dal.appspot.com",
   "messagingSenderId": "839926714277",
   "appId": "1:839926714277:web:f949cc304a2dd7948b224c",
   "measurementId": "G-0N1ZF71Q81"
}
stor = pyrebase.initialize_app(stor_config)
storage = stor.storage()

class Firebase():
    def database_init(self, JSONlocation):
        db_config = {
          "apiKey": "AIzaSyCJ7NBM2vTv71EM2AQMtfW3cXNnWiXvGBQ",
          "authDomain": "ntust-dal.firebaseapp.com",
          "databaseURL": "https://ntust-dal-default-rtdb.firebaseio.com/",
          "serviceAccount": JSONlocation,
          "projectId": "ntust-dal",
          "storageBucket": "ntust-dal.appspot.com",
          "messagingSenderId": "839926714277",
          "appId": "1:839926714277:web:f949cc304a2dd7948b224c",
          "measurementId": "G-0N1ZF71Q81"
        }
        return db_config
    def storage_init(self, JSONlocation):
        stor_config = {
           "apiKey": "AIzaSyCJ7NBM2vTv71EM2AQMtfW3cXNnWiXvGBQ",
           "authDomain": "ntust-dal.firebaseapp.com",
           "databaseURL": "https://ntust-dal.appspot.com/",
           "serviceAccount": JSONlocation,
           "projectId": "ntust-dal",
           "storageBucket": "ntust-dal.appspot.com",
           "messagingSenderId": "839926714277",
           "appId": "1:839926714277:web:f949cc304a2dd7948b224c",
           "measurementId": "G-0N1ZF71Q81"
        }
        return stor_config
#initialization
locat =  'D:\\Download\\firebase.json'
db = pyrebase.initialize_app(Firebase().database_init(locat)).database()
storage = pyrebase.initialize_app(Firebase().storage_init(locat)).storage()

#download file
dbfilepath = '0218test'
localfilepath = 'D:\Download'
storage.child(dbfilepath).put(localfilepath+'\\test.jpg')

storage.child().download('D://Download','A.jpg')
storage.child('0218test.jpg').download('D://Download','B.jpg')
storage.child().download('0218test.jpg','D://Download//C.jpg')

storage.child().download('A.jpg','D://Download')
storage.child().download('D://Download//C.jpg','0218test.jpg')

