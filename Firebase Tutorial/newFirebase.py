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

realtime = pyrebase.initialize_app(db_config)
db = realtime.database()
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

# Have a  test
#upload string
word = 'say hi hi'
db.child("folder1").set(word) 
#read string
string = db.child("folder1").get() 
string = str(string.val())
print(string)