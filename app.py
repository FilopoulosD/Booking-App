import mysql.connector
import datetime
from dbconnect import mydb

mydb



while True:
  cursor = mydb.cursor()
  print("Select Action:\n1)Add Customer\n2)Add Position\n3)Add a Reservation\n4)Check In\n5)Show Current Customers On Camping\n6)Show Future Arrivals\n7)Show All Customers\n8)Show All Bookings\n9)Show All Available Positions\n10)Exit")
  a = input()

  ##Exit
  if(a=='10'):
    break
  ## Add Customer
  elif(a=='1'):
    id=int(input("Give customer's Id\n"))
    name=input("Give customer's full name\n")
    phone =(input("Give customer's phone\n"))
    year = int(input('Enter year of birth\n'))
    month = int(input('Enter month of birt\n'))
    day = int(input('Enter day of birth\n'))
    date1 = datetime.date(year, month, day)
    formatted_date = date1.strftime('%Y-%m-%d')
    adt=input("Give ADT\n")
    cpd=float(input("Give cost per day\n"))
    tc=0
    val=(id,name,phone,formatted_date,adt,cpd,tc)
    print(val)
    query = "INSERT INTO  Customers(Id,`Full name`,`Phone number`,Birthdate,ADT,`Cost per day`,`Total cost`)" \
            "VALUES (%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query, val)
    mydb.commit()
  ## Add Position
  elif (a == '2'):
    id = int(input("Give position's Id\n"))
    type = input("Give position's type\n")
    usagecost = (input("Give position's usage cost\n"))
    electricity = input("Give position's status for electricity\n")
    wifi = input("Give position's status for wifi\n")
    annual = input("Give position's status for annual rent\n")
    maxnum = int(input("Give position's max number\n"))
    val = (id, type, usagecost, electricity, wifi, annual, maxnum)
    print(val)
    query ="INSERT INTO Position (Id,Type,`Usage Cost`,Electricity,Wifi,`Available for annual book`,`Max number`)"\
            "VALUES (%s,%s,%s,%s,%s,%s,%s);"
    cursor.execute(query,val)
    mydb.commit()
  ## Add Reservation
  elif (a == '3'):
    try:
      id = int(input("Give reservation's Id:\n"))

### Customer's Id
      query1 = "SELECT Id FROM Customers"
      cursor.execute(query1)
      result = cursor.fetchall()
      print("Choose a customers Id from the following\n")
      for x in result:
        print("Customer's Id: {}\n".format(x[0]))
      custId = int(input("Give customers's Id:\n"))

### Positions Id
      posId = (input("Give position's Id\n"))
      query1 = "SELECT Id FROM Position"
      cursor.execute(query1)
      result = cursor.fetchall()
      print("Choose a position's Id from the following\n")
      for x in result:
        print("Position's Id: {}\n".format(x[0]))
      custId = int(input("Give position's Id:\n"))
### Arrival
      year1 = int(input('Enter arranged year of arrival\n'))
      month1 = int(input('Enter arranged month of arrival\n'))
      day1 = int(input('Enter arranged day of arrival\n'))
      date1 = datetime.date(year1, month1, day1)
### Departure
      year2 = int(input('Enter arranged year of departure\n'))
      month2 = int(input('Enter arranged month of departure\n'))
      day2 = int(input('Enter arranged day of departure\n'))

### Check if arrival is before departure
      date2 = datetime.date(year2, month2, day2)
      arrival = date1.strftime('%Y-%m-%d')
      departure = date2.strftime('%Y-%m-%d')
      if date1>date2:
        print("There is an error with the arrival and departure date: The arrival date can't be after the departure date\n")
        break
      advance = float(input("Enter advance (if there is not please enter 0)\n"))
      totalcost = float(input("Enter total cost of reservation\n"))
### Condition
      condition = 'Active'

      val = (id, custId, posId, arrival, departure, advance, totalcost, condition)

      query = "INSERT INTO  Booking(Id,`Customer Id`, `Position Id`,`Due date of arrival` ,`Due date of departure`,Advance,`Total Cost`, `Condition`)" \
              "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
      cursor.execute(query, val)
      mydb.commit()
### Handle errors
    except mysql.connector.Error as error:
      print("Something went wrong: {} \n".format(error))

      if error.errno == 1452 :

        if 'REFERENCES `Customers` (`Id`)' in error.msg:
          print("There was a problem with thw customer's id. Please choose an id that exists on the database\n")
        elif 'REFERENCES `Position` (`Id`)' in error.msg:
          print("There was a problem with thw position's id. Please choose an id that exists on the database\n")
      elif error.errno == 1062:
        print("The Reservation's id you choose is already in the system")
      else:
        print("There was an unexpected error")
  ## Check In
  elif (a == '4'):

### Reservation's Id
      query1 = "SELECT Id FROM Booking"
      cursor.execute(query1)
      result = cursor.fetchall()
      print("Choose a reservation's Id from the following\n")
      for x in result:
        print("Reservation's Id: {}\n".format(x[0]))
      custId = int(input("Give reservation's Id:\n"))

### Customer's Id
      query1 = "SELECT Id FROM Customers"
      cursor.execute(query1)
      result = cursor.fetchall()
      print("Choose a customers Id from the following\n")
      for x in result:
        print("Customer's Id: {}\n".format(x[0]))
      custId = int(input("Give customers's Id:\n"))


### Check In date
      year = int(input('Enter year of check in\n'))
      month = int(input('Enter month of check in\n'))
      day = int(input('Enter day of check in\n'))
      date1 = datetime.date(year, month, day)
      formatted_date = date1.strftime('%Y-%m-%d')
  ## Show Current Customers On Camping
  elif (a == '5'):
    print(a)
  ## Show Future Arrivals
  elif (a == '6'):
    print(a)
  ## Show All Customers
  elif (a == '7'):
    print(a)
  ## Show All Bookings
  elif (a == '8'):
    print(a)
  ## Show All Available Positions
  elif (a == '9'):
    print(a)

  else:
    print("Please choose again\n")


cursor.close()
mydb.close()

