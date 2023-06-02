import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognization-84460-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Pankaj Raturi",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "234234":
        {
            "name": "Dr. Bhumika Gupta",
            "major": "Associate Professor",
            "starting_year": 2005,
            "total_attendance": 7,
            "standing": "S",
            "year": 18,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "123123":
        {
            "name": "Mrs. Meenakshi Kathayat",
            "major": "Assistant Professor",
            "starting_year": 2010,
            "total_attendance": 7,
            "standing": "N",
            "year": 18,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "321656":
        {
            "name": "Arjun Badola",
            "major": "CSE",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "F",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "321657":
        {
            "name": "Sohail Akhtar Ansari",
            "major": "IT",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "D",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "321658":
        {
            "name": "Sohail Akhtar Ansari",
            "major": "IT",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "D",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Shashank Pandey",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "111222":
        {
            "name": "Tanishq Negi",
            "major": "Geography",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Aditya Bhardwaj",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)