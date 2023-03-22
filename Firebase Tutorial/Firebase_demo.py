# new firebase test
# pip install pyrebase4 
#syntax needed modified when applying on Colab
import pyrebase
#required firebase-related JSON credential file 
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
db = pyrebase.initialize_app(Firebase().database_init(locat)).database() #store value/string
storage = pyrebase.initialize_app(Firebase().storage_init(locat)).storage() #store figure/video

#upload value
db.child("folder1").set('value') 
#download value
word = str(db.child("folder1").get().val())

#upload file
dbfilepath = '0218test' #the location where you wanna put your file on the cloud database
localfilepath = 'D:\Download'
storage.child('filename').put(localfilepath+'\\test.jpg') #filename will change to your assign name after upload
#download file
storage.child().download('filename.jpg','D://Download//filename.jpg') 
#delete file
storage.child().delete('','0218test.jpg')



