import pyrebase


filename = "dump.yaml"
with open("dump.yaml","rb") as f:
  file_data =f.read()




# Initialize Firebase app with configuration
config ={
  "apiKey": "AIzaSyAEGVt9PH7mXuCoYzQQTAyiHFIs9iyQfxw",
  "authDomain": "abhishek-kong.firebaseapp.com",
  "databaseURL" : "https://abhishek-kong-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "abhishek-kong",
  "storageBucket": "abhishek-kong.appspot.com",
  "messagingSenderId": "63263581613",
  "appId": "1:63263581613:web:ff2de0a479a06f5b13ad24",
  "measurementId": "G-F2DGX8NWZ5"
}


firebase = pyrebase.initialize_app(config)

storage = firebase.storage()
# storage.child("Specs/" + "filename.yaml").put(file_data)
storage.child("Specs/filename1.yaml").put(file_data)

