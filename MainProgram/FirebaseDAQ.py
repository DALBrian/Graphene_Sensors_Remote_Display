import pyrebase
locat =  'D:\\BudProgram\\ntust-dal-firebase.json'
class Firebase():
    def __init__(self, DBfolder = 'Folder2'):
        self.DBfolder = DBfolder
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
        self.db = pyrebase.initialize_app(db_config).database()
    def ReadData(self,i):
        return self.db.child('Force').child(i).get().val()
    def upload(self,data):
        self.db.child(self.DBfolder).put(data)
