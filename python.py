#name = input ("Whats your name? ")
#Removes any extra spaces #argumments btwn (_) and capitalizes first letters
#name = name.strip().tile()
#name = name.capitalize() #Capitalizes first letter of one name
#print ("Hello " + name) #Greets and displays input
# end="" stops new line end="\n" adds new line sep="," adds comma between items
# \"text\" allows quotes within quotes
#print (f"hello {name}, welcome to python programming!")

#Slpits name into first and last
#name = input ("Whats your full name? ").strip().title()
#first, last = name.split(" ")
#print (f"Hello {first} {last}") 

#Grabs users numbers and adds them assuming user enters an integer
#x = int(input("Number"))
#y = int(input("Number"))
#print (x + y)

#Grabs users numbers and adds them assuming user enters a float
#x = float(input("Number: "))#Adds decimal point for decimal numbers
#y = float(input("Number: "))
#print (f"{round(x + y):,}") #or can make a z variable z = x + y then print (round(z))
# the f string formats the number with commas

#x = float(input("Number: "))#Adds decimal point for decimal numbers
#y = float(input("Number: "))
#z = round(x / y, 3)# Rounds to 3 decimal places(can change number)
#print(z) #can also do print (f"{z:.2f}") to format to 2 decimal places

def hello (to="world"):
    print ("hello, ", to)
hello ()
name = input ("Name please>").strip().title()
hello (name)
# resume vid at 1:45:15
just = input ("What do you want to say? ")