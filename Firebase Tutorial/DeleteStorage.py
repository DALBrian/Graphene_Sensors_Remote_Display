#刪除舊有照片資訊
import pyrebase #will receive error at the first time, just start this column
import os
import numpy as np
#上傳到firebase與storage的網址不同，需要分開宣告
#realtime database的初始宣告#firebase initialization
db_config = {
   "apiKey": "AIzaSyCzY5kCuzdTQP3QDwluIf9ciRQdZpS11uM",
   "authDomain": "g-service-at-asia.firebaseapp.com",
   "databaseURL": "https://g-service-at-asia-default-rtdb.asia-southeast1.firebasedatabase.app",
   "serviceAccount": "//Users//brian//Downloads//newAccount.json",
   "projectId": "g-service-at-asia",
   "storageBucket": "g-service-at-asia.appspot.com",
   "messagingSenderId": "833474823375",
   "appId": "1:833474823375:web:6e79322d52a3e1b36063ba",
   "measurementId": "G-28H2EGDHNP"

}
realtime = pyrebase.initialize_app(db_config)
db = realtime.database()
#firebase storage儲存照片空間的宣告
stor_config = {
   "apiKey": "AIzaSyCzY5kCuzdTQP3QDwluIf9ciRQdZpS11uM",
   "authDomain": "g-service-at-asia.firebaseapp.com",
   "databaseURL": "https://g-service-at-asia.appspot.com",
   "serviceAccount": "//Users//brian//Downloads//newAccount.json",
   "projectId": "g-service-at-asia",
   "storageBucket": "g-service-at-asia.appspot.com",
   "messagingSenderId": "833474823375",
   "appId": "1:833474823375:web:6e79322d52a3e1b36063ba",
   "measurementId": "G-28H2EGDHNP"
}
stor = pyrebase.initialize_app(stor_config)
storage = stor.storage()

M = 1
while (True): 
    num = str(np.int0(M)) #流水號。直接放在shape後面 eg. Tri1.jpg
    extension = ".jpeg"
    #存檔檔名（檔名及副檔名）
    filename = str(num) + extension
    #path_on_local = '/content/drive/MyDrive/Colab Notebooks/5g Robot Demo/download'
    path_on_db = ""
    #下載路徑顯示
    dbfilepath = os.path.join(path_on_db, filename)
    #print("download from storage path: {}" .format(dbfilepath))
    storage.child().delete(dbfilepath,filename)
    M = M + 1