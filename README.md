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
