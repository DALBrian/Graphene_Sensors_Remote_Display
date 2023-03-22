# Read sensor data and upload to Firebase
import pyrebase
import random
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
db = pyrebase.initialize_app(Firebase().database_init(locat)).database() #t
storage = pyrebase.initialize_app(Firebase().storage_init(locat)).storage()
db_path = 'BudsProgram'

#read data simulate by random data
datasheet = []
index = 1
while True and index < 10: 
    data = random.randint(1,10)
    datasheet.append(data)
    db.child(db_path).set(datasheet[index-1])
    print('the data is {}, and the index is {}'.format(data, index))
    index +=1
    

    
    
    
    
    
    
    
    