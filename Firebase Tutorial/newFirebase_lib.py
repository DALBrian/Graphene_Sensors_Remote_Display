# new firebase test
# pip install pyrebase4 
import pyrebase
JSONlocation = "D:\\Download\\firebase.json"
db_config = {
  "apiKey": "XXX",
   "authDomain": "g-service-at-asia.firebaseapp.com",
   "databaseURL": "https://XXX.app",
   "serviceAccount": "C:/Users/dal/Desktop/5gdemo/newAccount.json",
   "projectId": "g-service-at-asia",
   "storageBucket": "g-service-at-asia.appspot.com",
   "messagingSenderId": "XXX",
   "appId": "1:XXX:web:XXX",
   "measurementId": "G-XXX"
}
#firebase storage儲存照片空間的宣告
stor_config = {
   "apiKey": "XXX",
   "authDomain": "g-service-at-asia.firebaseapp.com",
   "databaseURL": "https://XXX.app",
   "serviceAccount": "C:/Users/dal/Desktop/5gdemo/newAccount.json",
   "projectId": "g-service-at-asia",
   "storageBucket": "g-service-at-asia.appspot.com",
   "messagingSenderId": "XXX",
   "appId": "1:XXX:web:XXX",
   "measurementId": "G-XXX"
}
stor = pyrebase.initialize_app(stor_config)
storage = stor.storage()

class Firebase():
    def database_init(self, JSONlocation):
        db_config = {
          "apiKey": "XXX",
          "authDomain": "g-service-at-asia.firebaseapp.com",
          "databaseURL": "https://XXX.app",
          "serviceAccount": "C:/Users/dal/Desktop/5gdemo/newAccount.json",
          "projectId": "g-service-at-asia",
          "storageBucket": "g-service-at-asia.appspot.com",
          "messagingSenderId": "XXX",
          "appId": "1:XXX:web:XXX",
          "measurementId": "G-XXX"
        }
        return db_config
    def storage_init(self, JSONlocation):
        stor_config = {
           "apiKey": "XXX",
            "authDomain": "g-service-at-asia.firebaseapp.com",
            "databaseURL": "https://XXX.app",
            "serviceAccount": "C:/Users/dal/Desktop/5gdemo/newAccount.json",
            "projectId": "g-service-at-asia",
            "storageBucket": "g-service-at-asia.appspot.com",
            "messagingSenderId": "XXX",
            "appId": "1:XXX:web:XXX",
            "measurementId": "G-XXX"
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

