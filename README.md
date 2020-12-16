# Booking-App
Booking app for a camping using MySQL and Python

IMPORTANT
Create a dbconnect.py file with the necessary code for the database connection

For example if you want to connect to a MySQL  database with mysql.connector your code must be as bellow

import mysql.connector

mydb = mysql.connector.connect(
  host="NameOfHost",
  user="NameOfRoot",
  database="NameOfDatabase",
  password="YourPassword"
)


For now the static and templates folders are NOT in use. 
Future goals involve the use of the flask framework and the above folders are created with that in mind.

