Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Brief description: This project is used to calculate the travel expense. 
... #Date- 2/27/23
... #CTI - 110 P2HW1 - Travel Expenses
... #Name - Lucas Garcia
... 
... 
... 
... print("This program calculates and displays travel expenses")
... amount = int(input("Enter budget: "))
... dest = input("Enter your travel destination: ")
... gas = int(input("How much do you think you will spend on gas? "))
... hotel = int(input("Approximately, how much will you need for accommodation/hotel? "))
... food = int(input("Last, how much do you need for food? "))
... 
... 
... print("---------------Travel Expense---------------")
... print(f"{'Location:' : <20}", f"{ dest : <20}")
... print(f"{'Initial budget:' : <20}", f"{ '$'+str(float(amount)) : <20}")
... print(f"{'Fuel:' : <20}", f"{'$'+str(float(gas)) : <20}")
... print(f"{'Accommodation:' : <20}", f" {'$'+str(float(hotel)) : <20}")
... print(f"{'Food:' : <20}", f"{'$'+str(float(food)) : <20}")
... 
... 
... remaining = amount - (gas+hotel+food)
... print("--------------------------------------------")
... print(f"{'Remaining balance:' : <20}", f"{'$'+str(float(remaining)) : <20}")
