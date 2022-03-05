from django.shortcuts import render
import pyrebase
# Create your views here.

firebaseConfig = {
    "apiKey": "AIzaSyCpPudkOMwKF74EK2ikFDcfjf6wmEXBhzs",
    "authDomain": "cz2006-72f87.firebaseapp.com",
    "databaseURL": "https://cz2006-72f87-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "cz2006-72f87",
    "storageBucket": "cz2006-72f87.appspot.com",
    "messagingSenderId": "680188247477",
    "appId": "1:680188247477:web:9a140e75af81b6056b2dfc",
    "measurementId": "G-XNTRKQYHBG"
}

firebase = pyrebase.initialize_app(firebaseConfig)
authe = firebase.auth()
database = firebase.database()


def index(request):
    # accessing our firebase data and storing it in a variable
    userID = database.child('Data').child('userID').get().val()
    email = database.child('Data').child('email').get().val()
    name = database.child('Data').child('name').get().val()
    password = database.child('Data').child('password').get().val()
    gender = database.child('Data').child('gender').get().val()
    age = database.child('Data').child('age').get().val()
    hasBicycle = database.child('Data').child('hasBicycle').get().val()
    currentLocation = database.child('Data').child(
        'currentLocation').get().val()
    profilePhoto = database.child('Data').child('profilePhoto').get().val(),
    socialAccount = database.child('Data').child('socialAccount').get().val()

    context = {
        'userID': userID,
        'email': email,
        'name': name,
        'password': password,
        'gender': gender,
        'age': age,
        'hasBicycle': hasBicycle,
        'currentLocation': currentLocation,
        'profilePhoto': profilePhoto,
        'socialAccount': socialAccount,
    }
    return render(request, 'index.html', context)
