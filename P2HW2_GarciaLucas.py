Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Brief description: This project is used to calculate grade average
... #Date- 2/27/23
... #CTI - 110 P2HW2 - Grade Average
... #Name - Lucas Garcia
... 
... m1=float(input(" Enter grade for module 1 : "))
... m2=float(input("Enter grade for module 2 :"))
... m3=float(input("Enter grade for module 3 :"))
... m4=float(input("Enter grade for module 4 :"))
... m5=float(input("Enter grade for module 5 :"))
... m6=float(input("Enter grade for module 6  :"))
... #grades empty list
... grades=[ ]
... #appending one by one grades into list with name grades
... grades.append(m1)
... grades.append(m2)
... grades.append(m3)
... grades.append(m4)
... grades.append(m5)
... grades.append(m6)
... print("Grades list is: \n",grades)
... 
... lg=min(grades)
... hg=max(grades)
... sg=sum(grades)
... avg=sg/6
... 
... print("-----------------------------Results---------------------------")
... print("Lowest grade  :   ",lg)
... print("Highest grade :   ",hg)
... print("Sum of grades :   ",sg)
... print("Average            : %.2f"%avg)
... 
... print("----------------------------------------------------------------")
... 
