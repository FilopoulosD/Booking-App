import mysql.connector
import datetime
from datetime import date
from dbconnect import mydb
from createcsv import create_csv
from tkinterShow import showcsv

mydb


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
    id1=int(input("Give customer's Id\n"))
    name1=input("Give customer's full name\n")
    phone1 =(input("Give customer's phone\n"))
    year1 = int(input('Enter year of birth\n'))
    month1 = int(input('Enter month of birt\n'))
    day1 = int(input('Enter day of birth\n'))
    date1 = datetime.date(year, month, day)
    formatted_date1 = date1.strftime('%Y-%m-%d')
    adt1=input("Give ADT\n")
    cpd1=float(input("Give cost per day\n"))
    tc1=0
    val1=(id1,name1,phone1,formatted_date1,adt1,cpd1,tc1)

    print(val1)

    query1 = "INSERT INTO  Customers(Id,`Full name`,`Phone number`,Birthdate,ADT,`Cost per day`,`Total cost`)" \
            "VALUES (%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query1, val1)
    mydb.commit()
  ## Add a new Position
  elif (a == '2'):
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
### Arrival
      year31 = int(input('Enter arranged year of arrival\n'))
      month31 = int(input('Enter arranged month of arrival\n'))
      day31 = int(input('Enter arranged day of arrival\n'))
      date31 = datetime.date(year31, month31, day31)
### Departure
      year32 = int(input('Enter arranged year of departure\n'))
      month32 = int(input('Enter arranged month of departure\n'))
      day32 = int(input('Enter arranged day of departure\n'))

### Check if arrival is before departure
      date32 = datetime.date(year2, month2, day2)
      arrival = date31.strftime('%Y-%m-%d')
      departure = date32.strftime('%Y-%m-%d')
      if date31>date32:
        print("There is an error with the arrival and departure date: The arrival date can't be after the departure date\n")
        break
      advance3 = float(input("Enter advance (if there is not please enter 0)\n"))
      totalcost3 = float(input("Enter total cost of Booking\n"))
### Condition
      condition3 = 'Active'

      val3 = (id, custId3, posId3, arrival3, departure3, advance3, totalcost3, condition3)

      query33 = "INSERT INTO  Booking(Id,`Customer Id`, `Position Id`,`Due date of arrival` ,`Due date of departure`,Advance,`Total Cost`, `Condition`)" \
              "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
      cursor.execute(query33, val3)
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
        print("The Booking's id you choose is already in the system")
      else:
        print("There was an unexpected error")
  ## Check In
  elif (a == '4'):

### Booking's Id
    query41 = "SELECT Id FROM Booking"
    cursor.execute(query41)
    result4 = cursor.fetchall()
    print("Choose a booking's Id from the following\n")
    for x in result4:
      print("Booking's Id: {}\n".format(x[0]))
    custId4 = int(input("Give booking's Id:\n"))


### Check In date
    today4 = date.today()
    formatted_date41 = today4.strftime('%Y-%m-%d')


### Due Date of Departure
    year4 = int(input('Enter year of departure\n'))
    month4 = int(input('Enter month of departure\n'))
    day4 = int(input('Enter day of departure\n'))
    date4 = datetime.date(year4, month4, day4)
    formatted_date42 = date4.strftime('%Y-%m-%d')

    val4=(custId4,formatted_date41,formatted_date42)

    query42 = "INSERT INTO  CheckIn(`Booking Id`,`Arrival Date`, `Due date of departure`)" \
              "VALUES (%s,%s,%s)"
    cursor.execute(query42, val4)
    mydb.commit()


  ## Show Current Customers On Camping
  elif (a == '5'):
    print(a)
  ## Show Future Arrivals
  elif (a == '6'):
    query = "SELECT * FROM Customers"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    firstrow = [('Id', 'Full Name', 'ResId', 'Phone Number', 'Birthdate', 'ADT', 'Cost per Day', 'Total Cost')]
    create_csv(result, firstrow)
    showcsv("file.csv")
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

