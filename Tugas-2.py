name = [ ' ' ]
notlp= [ ' ' ]

#Contact list code
def contactlist( ) :
	print("Contact List : \n")
	for n in range (len(name)):
		print ("Name  : " + name[n])
		print ("Phone No :  " + notlp[n])
		print ("")
		
#nambah kontak code
def addcontact():	
	name.append(input("Name : "))
	notlp.append(input("Phone No. : "))
	print("Data Successfully Added")
	
#menucode
print(' Welcome !')
while True:
	print("####Menu####")
	print("1. Contact List")
	print("2. Add Contact")
	print("3. Exit")
	menu = int(input("Choose Menu : "))
	
	if menu == 1:
		contactlist()
	elif menu == 2:
		addcontact()
	elif menu == 3:
		print(" Programe Done, See You !")
		break
	else :
		print ("Menu Not Available\n")
