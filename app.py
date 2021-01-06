import mysql.connector
import datetime
from datetime import date
from dbconnect import mydb
from createcsv import create_csv
from tkinterShow import showcsv
from DeleteFileCSV import delete



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
          "9)Show  Available Positions\n10)Cancel a Booking\n11)Search A Customer By Name\n12)Check Out\n20)Exit")

    a = input()

    ##Exit
    if(a=='20'):
        delete("file.csv")
        cursor.close()
        mydb.close()
        break
    ## Add a new Customer
    elif (a == '1'):
        try:

            id1=int(input("Give customer's Id\n"))
            name1=input("Give customer's full name\n")
            print("Does the customer has another customers who is responsible?If so please type Yes!")
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
            while month1>13 or month1<=0 or day1>=31 or day1<=0:
                print("There is an error with the dates.Please type again.")
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
            print("Are you sure you want to add to positions the following:\nCustomer's Id: "
                  , id1, "\nCustomer's Name: ", name1, "\nResponsible customer's Id: ", resId1, "\nPhone Number: "
                  , phone1, "\nDate of Birth: ", formatted_date1, "\nADT: "
                  , adt1, "\nCost Per Day: ", cpd1,"Total Cost: ",tc1,"\nIf so enter yes")
            add1=input()
            if add1 in ["YES","Yes","yes"]:


                query1 = "INSERT INTO  Customers(Id,`Full name`,ResId,`Phone number`,Birthdate,ADT,`Cost per day`,`Total cost`)" \
                         "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(query1, val1)
                mydb.commit()
                print("A new customer was added to the database")
            else:
                print("Operation Interupted ")
        except mysql.connector.Error as error:
            print("Something went wrong: {} \n".format(error))
            if error.errno == 1062:
                if 'Customers.SSN' in error.msg:
                    print("The customer's SSN is already in the database")
                else:
                    print("The Customer's id is already in the system")
            elif error.errno == 1452:
                print("The Id for main customer is not in the database. Please select an id that's correct")
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
            val2 = (id2, type2, usagecost2, electricity2, wifi2, annual2, maxnum2)
            print("Are you sure you want to add to positions the following:\nPosition's Id: "
                  ,id2, "\nPosition's Type:", type2, "\nUsage Cost: ", usagecost2,"\nElectricity: "
                  , electricity2,"\nWifi: ", wifi2,"\nAvailability for annual rental"
                  , annual2, "\nMax number:", maxnum2,"\nIf so enter yes" )
            add2 = input()
            if add2 in ["YES", "Yes", "yes"]:
                query2 = "INSERT INTO Position (Id,Type,`Usage Cost`,Electricity,Wifi,`Available for annual book`,`Max number`)" \
                         "VALUES (%s,%s,%s,%s,%s,%s,%s);"
                cursor.execute(query2, val2)
                mydb.commit()
                print("A new position was added to the database")

            else:
                print("Operation Interupted ")


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
            query31 = "SELECT Id FROM Customers "
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
                    while month31 > 13 or month31 < 1 or day31 > 31 or day31 < 0:
                        print("There is an error with the dates.Please type again.")
                        month31 = int(input('Enter month of birt\n'))
                        day31 = int(input('Enter day of birth\n'))
                    date31 = datetime.date(year31, month31, day31)
                    ### Departure
                    year32 = int(input('Enter arranged year of departure\n'))
                    month32 = int(input('Enter arranged month of departure\n'))
                    day32 = int(input('Enter arranged day of departure\n'))
                    while month32 > 13 or month32 < 1 or day32 > 31 or day32 < 0:
                        print("There is an error with the dates.Please type again.")
                        month32 = int(input('Enter month of birt\n'))
                        day32 = int(input('Enter day of birth\n'))
                    date32 = datetime.date(year32, month32, day32)

                    arrival3 = date31.strftime('%Y-%m-%d')
                    departure3 = date32.strftime('%Y-%m-%d')
                    if date31 > date32:
                        raise ArrivalAfterDeparture
                    else:
                        break
                except ArrivalAfterDeparture:
                    print("The Arrival date is after Departure. Please Give again the correct dates")
            ### Number of Adults
            print("Please give the number of adults")
            adults = int(input())
            ### Number of Children
            print("Please give the number of Children")
            children = int(input())
            ### Total Cost
            cursor.execute("select `Usage Cost`,`Electricity`,`Wifi`, `Max Number` from Position where `id`=%s;",
                           (posId3,))
            result33 = cursor.fetchall()
            totaldays = date32 - date31
            if result33[0][1] in ["YES", "Yes", "yes"]:
                electr = 2
            else:
                electr = 0

            if result33[0][2] in ["YES", "Yes", "yes"]:
                wifi = 3
            else:
                wifi = 0

            totalcost3 = totaldays.days * result33[0][0] + adults * totaldays.days * 5 + children * totaldays.days * 3 + totaldays.days * electr + totaldays.days * wifi

            print("Total Cost is: ", totalcost3)
            ### Advance
            advance3 = float(input("Enter advance (if there is not please enter 0)\n"))
            ### Condition
            condition3 = 'Active'
            ### Booking Date
            year33 = int(input('Enter year of booking\n'))
            month33 = int(input('Enter month of booking\n'))
            day33 = int(input('Enter day of booking\n'))
            while month33 > 13 or month33 < 1 or day33 > 31 or day33 < 0:
                print("There is an error with the dates.Please type again.")
                month33 = int(input('Enter month of birt\n'))
                day33 = int(input('Enter day of birth\n'))
            date33 = datetime.date(year33, month33, day33)
            BookingDate3 = date33.strftime('%Y-%m-%d')
            val3 = (id3, custId3, posId3, arrival3, departure3, advance3, totalcost3, condition3, BookingDate3, adults,
                    children)
            print("Are you sure you want to add to positions the following:\nBooking's Id: "
                  , id3, "\nCustomer's Id:", custId3, "\nPosition's Id: ", posId3, "\nArrival: "
                  , arrival3, "\nDeparture: ", departure3, "\nAdvance: "
                  , advance3, "\nTotal Cost:", totalcost3, "\nBooking Date: ", BookingDate3, "\nNumber of Adults: ",
                  adults, "\nNumber of Children: ", children, "\nIf so enter yes")
            add3 = input()
            if add3 in ["YES", "Yes", "yes"]:
                query33 = "INSERT INTO  Booking(Id,`Customer Id`, `Position Id`,`Due date of arrival` ," \
                          "`Due date of departure`,Advance,`Total Cost`, `Condition`,`Booking Date`,`Adults`,`Underage`)" \
                          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                cursor.execute(query33, val3)
                mydb.commit()
                print("A new booking was added to the database")
            else:
                print("Operation Interupted ")


        ### Handle errors
        except mysql.connector.Error as error:
            print("Something went wrong: {} \n".format(error))

            if error.errno == 1452:

                if 'REFERENCES `Customers` (`Id`)' in error.msg:
                    print(
                        "There was a problem with the customer's id. Please choose an id that exists on the database\n")
                elif 'REFERENCES `Position` (`Id`)' in error.msg:
                    print(
                        "There was a problem with thw position's id. Please choose an id that exists on the database\n")
            elif error.errno == 1062:
                print("The Booking's id you choose is already in the system")
            elif ArrivalAfterDeparture:
                print("The Arrival date can't be after the departure date")
            else:
                print("There was an unexpected error")
    ## Check In
    elif (a == '4'):
        try:
            query41 = "SELECT Id FROM Customers"
            cursor.execute(query41)
            result41 = cursor.fetchall()
            print("Choose a customers Id from the following\n")
            for x in result41:
                print("Customer's Id: {}\n".format(x[0]))
            custId4 = int(input("Give customers's Id:\n"))

            query42= "SELECT Id FROM Position"
            cursor.execute(query42)
            result42=cursor.fetchall()
            print("Choose a position's Id from the following\n")
            for i in result42:
                print("Position's Id: {}\n".format(i[0]))
            posId4= int(input("Give Position's Id: \n"))

            arrival4=today

            year4 = int(input('Enter year of arranged departure\n'))
            month4 = int(input('Enter month of arranged departure\n'))
            day4 = int(input('Enter day of arranged departure\n'))
            while month4 > 13 or month4 < 1 or day4 > 31 or day4 < 0:
                print("There is an error with the dates.Please type again.")
                month4 = int(input('Enter month of birt\n'))
                day4 = int(input('Enter day of birth\n'))
            date4 = datetime.date(year4, month4, day4)
            BookingDate4 = date4.strftime('%Y-%m-%d')

            val4=(posId4,custId4,arrival4,BookingDate4)
            print("Are you sure you want to add to Check Ins the following:\nPosition's Id: "
                  , posId4, "\nCustomer's Id:", custId4, "\nArrival: ", arrival4, "\nBooking Date: "
                  , BookingDate4,"\nIf so enter yes")
            add4 = input()
            if add4 in ["YES", "Yes", "yes"]:
                query43 = "INSERT INTO CheckIn(`Position Id`,`Customers Id`,`Arrival Date`,`Due date of departure`) VALUES (%s,%s,%s,%s)"
                cursor.execute(query43, val4)
                mydb.commit()
                print("A new check in was added to the database")
            else:
                print("Operation Interupted ")
        except mysql.connector.Error as error:
            print("Something went wrong: {} \n".format(error))
    ## Show Current Customers On Camping
    elif (a == '5'):
        query5="select `Position Id`, `Customers Id`,`Arrival Date`, `Due date of departure`, `Full name`,`Phone number`,`ADT` " \
               "from CheckIn join Customers " \
               "where `Due date of departure`>curdate() " \
               "and `Position Id` = Id"

        cursor.execute(query5)
        result5= cursor.fetchall()

        firstrow5=[("Position's Id", "Customer's Id", "Arrival Date"," Departure Date"," Full Name","Phone Number","Social Security Number")]
        create_csv(result5,firstrow5)
        showcsv("file.csv")
    ## Show Future Arrivals
    elif (a == '6'):
        query6="select  * from Booking " \
               "WHERE `Due date of arrival`>curdate();"
        cursor.execute(query6)
        result6 = cursor.fetchall()
        firstrow6 = [("Id", "Customer's Id", "Position's Id", " Date of Arranged Arrival", " Date of Departure", "Advance",
                      "Total Cost","Condition", "Type","Booking Date")]
        create_csv(result6, firstrow6)
        showcsv("file.csv")
    ## Show All Customers
    elif (a == '7'):
        query="SELECT * FROM Customers"
        cursor.execute(query)
        result = cursor.fetchall()

        firstrow = [('Id', 'Full Name', 'ResId', 'Phone Number', 'Birthdate', 'ADT', 'Cost per Day', 'Total Cost')]
        create_csv(result,firstrow)
        showcsv("file.csv")
    ## Show All Bookings
    elif (a == '8'):
        query = "SELECT * FROM Booking"
        cursor.execute(query)
        result = cursor.fetchall()
        firstrow = [('Id', "Customer's Id", "Position's Id", 'Due Date of Arrival', 'Due Date of Departure', 'Advance', 'Total Cost', 'Condition','Type','Booking Date')]
        create_csv(result, firstrow)
        showcsv("file.csv")
    ## Show All Available Positions
    elif (a == '9'):
        query = "SELECT  p.id, p.Type FROM Position p " \
                "WHERE p.id NOT IN (" \
                "SELECT Position.id FROM Position LEFT JOIN Booking b ON Position.`id`=b.`Position Id`LEFT JOIN CheckIn c ON p.`id`=c.`Position Id`" \
                "WHERE (current_date()<b.`Due date of departure` or current_date()>b.`Due date of arrival`) or  current_date()<c.`Due date of departure`)"
        cursor.execute(query)
        result = cursor.fetchall()
        firstrow = [('Position Id', 'Type')]
        create_csv(result, firstrow)
        showcsv("file.csv")
    ##Cancel a Booking
    elif ( a== '10'):
        print("Please choose the book you want to cancel:\n")
        query101 = "SELECT Id FROM Booking where `Condition`!= 'Canceled'"
        cursor.execute(query101)
        result101 = cursor.fetchall()
        for x in result101:
            print("Customer's Id: {}\n".format(x[0]))
        canceledId = int(input("Please Choose:\n"))
        cursor.execute("update Booking set `Condition`='Canceled' where id=%s;", (canceledId,))
        mydb.commit()
        if canceledId in result101:
            print("Booking has been canceled")
        else:
            print("The Id you choose is not correct")
    ##Customer Search By Name
    elif(a == '11'):
        print("Please enter the full name of the customer you want\n")
        name11=input()
        cursor.execute("select * from Customers where `Full name`=%s;", (name11,))
        result112 = cursor.fetchall()
        firstrow = [('Id', 'Full Name', 'ResId', 'Phone Number', 'Birthdate', 'ADT', 'Cost per Day', 'Total Cost')]
        create_csv(result112, firstrow)
        showcsv("file.csv")
    ### Check Out
    elif(a == '12'):
            ##Position's Id
            query121 = "SELECT `Position Id` FROM `CheckIn`"
            cursor.execute(query121)
            result121 = cursor.fetchall()
            print("Choose a position's Id from the following\n")
            for x in result121:
                print("Position's Id: {}\n".format(x[0]))
            posId12 = int(input("Give position's Id:\n"))
            ##Customer's Id
            query122 = "SELECT `Customers Id` FROM `CheckIn`"
            cursor.execute(query122)
            result122 = cursor.fetchall()
            print("Choose a position's Id from the following\n")
            for x in result122:
                print("Position's Id: {}\n".format(x[0]))
            cusId12 = int(input("Give position's Id:\n"))

            cursor.execute("DELETE FROM `CheckIn` WHERE `Position Id`=%s AND `Customers Id`=%s", (posId12,cusId12,))
            mydb.commit()
    ### Calculate the total cost of all the bookings of a specific customer
    elif(a == '13'):
        custId13=input("Please give the customer's Id: \n")
        cursor.execute("SELECT `Total Cost` FROM `Booking` WHERE `Customer Id`=%s",(custId13,))
        result13=cursor.fetchall()
        totalcost13=0
        for i in range(len(result13)):
            totalcost13=totalcost13 + result13[i][0]
        cursor.execute("UPDATE `Customers` SET `Total Cost`=%s WHERE Id=%s", (totalcost13, custId13,))
        print("The total cost is: ", totalcost13)
        mydb.commit()
    else:
        print("Please choose again\n")




