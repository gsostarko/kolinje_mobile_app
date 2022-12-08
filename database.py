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
        'datum_registracije': date_time_format
        }
        
        return db.korisnici.insert_one(user)