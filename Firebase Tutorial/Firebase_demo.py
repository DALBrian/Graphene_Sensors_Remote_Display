# new firebase test
# pip install pyrebase4 
#syntax needed modified when applying on Colab
import pyrebase
#required firebase-related JSON credential file 
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



