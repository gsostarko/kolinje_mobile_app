from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.environ.get("MONGODB_URI"))

db = client.kolinje

now = datetime.now()
date_time_format = now.strftime("%d-%m-%Y %H:%M:%S")

class DatabaseManagement():
    def NewUserRegistration(username,email, password):
        """
        Saving new user to database

        Args:
        : username - new user username
        : email - new user email
        : password - new user password
        
        Returns:
        : Saving new user to database
        """
        user = {
        'username': username,
        'email': email,
        'password': password,
        'datum_registracije': date_time_format,
        'name': ''
        }
        
        return db.korisnici.insert_one(user)

class DatabaseQuery():
    def LoginQuery(username, password):
        db = client.get_database('kolinje')
        collection = db.get_collection('korisnici')
        filter = {'username': username}

        podaci = collection.find(filter)
        korisnici_temp = []
        for each_doc in podaci:
            korisnici_temp.append(each_doc)
        print(korisnici_temp)
        #print(korisnici_temp[0])
        
        try:
            loged_in_user = korisnici_temp[0]['username']
            loged_in_password = korisnici_temp[0]['password']
        
            if loged_in_user == username and loged_in_password == password:
        
                print(loged_in_user, loged_in_password)

                return True, loged_in_user
            else:
                return False, None
        except:
            return False, None