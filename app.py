import mysql.connector
import datetime
from datetime import date
from dbconnect import mydb
from createcsv import create_csv
from tkinterShow import showcsv

mydb

class CustomError (Exception) :
  pass


class ArrivalAfterDeparture(CustomError):
    """Raised when the arrival is after the departure"""
    pass



today = date.today()

while True:
  cursor = mydb.cursor()
  print("Select Action:\n1)Add a new Customer\n2)Add a new Position\n3)Add a new Booking\n4)Check In\n"
        "5)Show Current Customers On Camping\n6)Show Future Arrivals\n7)Show All Customers\n8)Show All Bookings\n"
        "9)Show  Available Positions\n10)Exit")

  a = input()

  ##Exit
  if(a=='10'):
    break
  ## Add a new Customer
  elif(a=='1'):
    try:

      id1=int(input("Give customer's Id\n"))
      name1=input("Give customer's full name\n")
      print("Does the customer has another customers who is responsible?If yes please press Yes!")
      ans=input()
      if ans in ["YES","Yes","yes"]:
        print("Please choose the main customer from below:\n")
        query11 = "SELECT Id, `Full name` FROM Customers"
        cursor.execute(query11)
        result11 = cursor.fetchall()
        print("Choose a customers Id from the following\n")
        for x in result11:
          print("Customer's Id: {}, Customer's Full Name: {}\n".format(x[0], x[1]))
        resId1 = int(input("Please Choose:\n"))
      else:
        resId1=None

      phone1 =(input("Give customer's phone\n"))
      year1 = int(input('Enter year of birth\n'))
      month1 = int(input('Enter month of birt\n'))
      day1 = int(input('Enter day of birth\n'))
      date1 = datetime.date(year1, month1, day1)
      formatted_date1 = date1.strftime('%Y-%m-%d')

      while date1>today:
        print("The date of birth must be before current date. Please give again the customer's day of birth")
        year1 = int(input('Enter year of birth\n'))
        month1 = int(input('Enter month of birt\n'))
        day1 = int(input('Enter day of birth\n'))
        date1 = datetime.date(year1, month1, day1)
        formatted_date1 = date1.strftime('%Y-%m-%d')

      adt1=input("Give ADT\n")
      cpd1=float(input("Give cost per day\n"))
      tc1=0
      val1=(id1,name1,resId1,phone1,formatted_date1,adt1,cpd1,tc1)

      print(val1)

      query1 = "INSERT INTO  Customers(Id,`Full name`,ResId,`Phone number`,Birthdate,ADT,`Cost per day`,`Total cost`)" \
              "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
      cursor.execute(query1, val1)
      mydb.commit()
    except mysql.connector.Error as error:
      print("Something went wrong: {} \n".format(error))
      if error.errno == 1062:
        print("The Customer's id you choose is already in the system")
      elif error.errno == 1452:
        print("The Id you give for main customer is not in the database. Please select an id that's correct")
      else:
        print("There was an unexpected error")

  ## Add a new Position
  elif (a == '2'):
    try:
      id2 = int(input("Give position's Id\n"))
      type2 = input("Give position's type\n")
      usagecost2 = (input("Give position's usage cost\n"))
      electricity2 = input("Give position's status for electricity\n")
      wifi2 = input("Give position's status for wifi\n")
      annual2 = input("Give position's status for annual rent\n")
      maxnum2 = int(input("Give position's max number\n"))
      val2 = (id, type, usagecost, electricity, wifi, annual, maxnum)
      print(val2)
      query2 ="INSERT INTO Position (Id,Type,`Usage Cost`,Electricity,Wifi,`Available for annual book`,`Max number`)"\
              "VALUES (%s,%s,%s,%s,%s,%s,%s);"
      cursor.execute(query2,val2)
      mydb.commit()
    except mysql.connector.Error as error:
      print("Something went wrong: {} \n".format(error))
      if error.errno == 1062:
        print("The Position's id you choose is already in the system")
      else:
        print("There was an unexpected error")

  ## Add a new Booking
  elif (a == '3'):
    try:
      id3 = int(input("Give Booking's Id:\n"))

### Customer's Id
      query31 = "SELECT Id FROM Customers"
      cursor.execute(query31)
      result31 = cursor.fetchall()
      print("Choose a customers Id from the following\n")
      for x in result31:
        print("Customer's Id: {}\n".format(x[0]))
      custId3 = int(input("Give customers's Id:\n"))

### Positions Id
      query32 = "SELECT Id FROM Position"
      cursor.execute(query32)
      result32 = cursor.fetchall()
      print("Choose a position's Id from the following\n")
      for x in result32:
        print("Position's Id: {}\n".format(x[0]))
      posId3 = int(input("Give position's Id:\n"))
### Check if arrival is before departure
      while True:
        try:
          ### Arrival
          year31 = int(input('Enter arranged year of arrival\n'))
          month31 = int(input('Enter arranged month of arrival\n'))
          day31 = int(input('Enter arranged day of arrival\n'))
          date31 = datetime.date(year31, month31, day31)
          ### Departure
          year32 = int(input('Enter arranged year of departure\n'))
          month32 = int(input('Enter arranged month of departure\n'))
          day32 = int(input('Enter arranged day of departure\n'))
          date32 = datetime.date(year32, month32, day32)

          arrival3 = date31.strftime('%Y-%m-%d')
          departure3 = date32.strftime('%Y-%m-%d')
          if date31 > date32:
            raise ArrivalAfterDeparture
          else:
            break
        except ArrivalAfterDeparture:
          print("The Arrival date is after Departure. Please Give again the correct dates")

      advance3 = float(input("Enter advance (if there is not please enter 0)\n"))
      totalcost3 = float(input("Enter total cost of Booking\n"))
### Condition
      condition3 = 'Active'


      Type3 = "Annual"

      year33 = int(input('Enter year of booking\n'))
      month33 = int(input('Enter month of booking\n'))
      day33 = int(input('Enter day of booking\n'))
      date33 = datetime.date(year33, month33, day33)
      BookingDate3 =date33.strftime('%Y-%m-%d')

      val3 = (id3, custId3, posId3, arrival3, departure3, advance3, totalcost3, condition3, Type3, BookingDate3)

      query33 = "INSERT INTO  Booking(Id,`Customer Id`, `Position Id`,`Due date of arrival` ,`Due date of departure`,Advance,`Total Cost`, `Condition`,`Type`,`Booking Date`)" \
              "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      print(val3)
      cursor.execute(query33, val3)
      mydb.commit()
### Handle errors
    except mysql.connector.Error as error:
      print("Something went wrong: {} \n".format(error))

      if error.errno == 1452 :

        if 'REFERENCES `Customers` (`Id`)' in error.msg:
          print("There was a problem with the customer's id. Please choose an id that exists on the database\n")
        elif 'REFERENCES `Position` (`Id`)' in error.msg:
          print("There was a problem with thw position's id. Please choose an id that exists on the database\n")
      elif error.errno == 1062:
        print("The Booking's id you choose is already in the system")
      elif ArrivalAfterDeparture:
        print("The Arrival date can't be after the departure date")
    except ArrivalAfterDeparture:
      print("The Arrival date can't be after the departure date")

  ## Check In
  elif (a == '4'):
    try:

      ### Booking's Id
      query41 = "SELECT Id FROM Booking"
      cursor.execute(query41)
      result4 = cursor.fetchall()
      print("Choose a booking's Id from the following\n")
      for x in result4:
        print("Booking's Id: {}\n".format(x[0]))
      custId4 = int(input("Give booking's Id:\n"))


      ### Check In date

      arrival4 = today.strftime('%Y-%m-%d')


      ### Due Date of Departure
      while True:
        try:
          ### Departure
          year42 = int(input('Enter arranged year of departure\n'))
          month42 = int(input('Enter arranged month of departure\n'))
          day42 = int(input('Enter arranged day of departure\n'))
          date42 = datetime.date(year42, month42, day42)
          departure4 = date42.strftime('%Y-%m-%d')
          if today > date42:
            raise ArrivalAfterDeparture
          else:
            break
        except ArrivalAfterDeparture:
          print("The Arrival date is after Departure. Please Give again the correct departure date")





      val4=(custId4,arrival4,departure4)

      query42 = "INSERT INTO  CheckIn(`Booking Id`,`Arrival Date`, `Due date of departure`)" \
                "VALUES (%s,%s,%s)"
      cursor.execute(query42, val4)
      mydb.commit()
    except mysql.connector.Error as error:
      print("Something went wrong: {} \n".format(error))

      if error.errno == 1452:
          print("There was a problem with the Booking's id. Please choose an id that exists on the database\n")
      else:
        print("There was an unexpected error")


  ## Show Current Customers On Camping
  elif (a == '5'):
    print(a)

  ## Show Future Arrivals
  elif (a == '6'):
    print(a)
  ## Show All Customers
  elif (a == '7'):
    query="SELECT * FROM Customers"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    firstrow = [('Id', 'Full Name', 'ResId', 'Phone Number', 'Birthdate', 'ADT', 'Cost per Day', 'Total Cost')]
    create_csv(result,firstrow)
    showcsv("file.csv")

  ## Show All Bookings
  elif (a == '8'):
    query = "SELECT * FROM Booking"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    firstrow = [('Id', "Customer's Id", "Position's Id", 'Due Date of Arrival', 'Due Date of Departure', 'Advance', 'Total Cost', 'Condition','Type','Booking Date')]
    create_csv(result, firstrow)
    showcsv("file.csv")

  ## Show All Available Positions
  elif (a == '9'):
    print(a)

  else:
    print("Please choose again\n")


cursor.close()
mydb.close()

