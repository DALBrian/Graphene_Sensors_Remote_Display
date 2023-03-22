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

realtime = pyrebase.initialize_app(db_config)
db = realtime.database()
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

# Have a  test
#upload string
word = 'say hi hi'
db.child("folder1").set(word) 
#read string
string = db.child("folder1").get() 
string = str(string.val())
print(string)