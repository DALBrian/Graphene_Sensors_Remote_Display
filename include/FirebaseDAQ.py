import pyrebase
locat =  'D:\\BudProgram\\ntust-dal-firebase.json'
class Firebase():
    def __init__(self, DBfolder = 'Folder2'):
        self.DBfolder = DBfolder
    def database_init(self, JSONlocation):
        db_config = {
          "apiKey": "XXX",
          "authDomain": "XXX.com",
          "databaseURL": "XXX/",
          "serviceAccount": JSONlocation,
          "projectId": "ntust-dal",
          "storageBucket": "ntust-dal.appspot.com",
          "messagingSenderId": "XXX",
          "appId": "1:XXX:web:XXX",
          "measurementId": "G-XXX"
        }
        self.db = pyrebase.initialize_app(db_config).database()
    def ReadData(self,i):
        return self.db.child('Force').child(i).get().val()
    def upload(self,data):
        self.db.child(self.DBfolder).put(data)
