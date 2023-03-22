# 引用必要套件
import firebase_admin
from firebase_admin import firestore
from firebase_admin import db
import time

# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = firebase_admin.credentials.Certificate('D:\\BudProgram\\ntust-dal-firebase.json')

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred, {
	'databaseURL':'https://ntust-dal-default-rtdb.firebaseio.com/'
	})

# 初始化firestore
#db = firestore.client()
ref = db.reference('/')
#%%



d1 = 1
d2 = 2
ref.child('folder').child('1').set(d1)
ref.child('folder').child('2').set(d2)
t1 = time.time()
for i in range(1,1000):
    ref.child('test').child(str(i)).set(i)
t2 = time.time()
print(t2-t1)

#%%
import pyrebase
class Firebase():
    def __init__(self,JSONlocation ,DBfolder = 'Folder2'):
        self.DBfolder = DBfolder
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
        self.db = pyrebase.initialize_app(db_config).database()
    
    def upload(self,i, data):
        self.db.child('Folder2').child(str(i)).set(data)


locat =  'D:\\BudProgram\\ntust-dal-firebase.json'
#FB = Firebase()
F = Firebase(locat,DBfolder = 'Folder2')
t1 = time.time()
for i in range(1,1000):
    F.upload(i, i)
t2 = time.time()
print(t2-t1)
