print ("Please Enter Your Average For Each Class.")
print ("=========================================")
grade1 = input("Enter grade for class 1: ")
grade2 = input("Enter grade for class 2: ")
grade3 = input("Enter grade for class 3: ")
grade4 = input("Enter grade for class 4: ")

map= {"A": 4.0, "-A": 3.7, "+B": 3.3, "B": 3.0}
def convert ( cGPA ):
	if cGPA == "A":
		cGPA = 4.0;
	elif cGPA == "-A":
		cGPA = 3.7;
	elif cGPA == "+B":
		cGPA = 3.3;
	elif cGPA == "B":
		cGPA = 3.0;
	return cGPA

gavg1 = convert(grade1)
gavg2 = convert(grade2)
gavg3 = convert(grade3)
gavg4 = convert(grade4)

GPA = (gavg1*5 + gavg2*3 + gavg3*3 + gavg4*4) / 15

print ("----------------------------------------")
print ("Your Grade Point Average is: " + str(GPA))

overallGPA = (GPA + 3.90) / 2
print ("Your overall GPA is: " + str(overallGPA))