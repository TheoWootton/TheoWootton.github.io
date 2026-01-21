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

#def hello (to="world"):
    #print ("hello, ", to)
#hello ()
#name = input ("Name please>").strip().title()
#hello (name)
# resume vid at 1:45:15
#just = input ("What do you want to say? ")

#def main():#provides structure to program
    #name=input("Enter your name: ").strip().title()
    #hello(name)#calls hello function with name argument

#def hello(to="World"):#f with default argument
    #print("Hello,", to)
#main()#calls main function to start program after it is defined

def main():#provides structure to program
    x = int(input("What's x?"))#gets user input
    print("x squared is", square(x))#calls square function with x argument
def square(n):#function to square number
    return n * n#can also use return n ** 2 as well as pow(n, 2)
main()

#resume vid at 1:50:24