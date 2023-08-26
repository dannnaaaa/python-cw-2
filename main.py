my_name = input(" what is you name? ")
my_age = int(input("how old are you?") )

print(f"my name is {my_name} and i am {my_age} years old")



first_number = int(input("choose a number"))
second_number =int(input("choose a second number "))
operation =input("put in an arithmetic for the first number and the second number" )

if operation == '+':
    print(first_number+second_number)

elif operation == "-":
        print(first_number-second_number)

elif operation == "*":
      print(first_number*second_number)

elif operation == "/":
      print(first_number/second_number)

else:
      print("the operation is invalid")


bus_capacity = 100
people_inBus = int (input("how many people are on the bus?"))
people_GetIn = int (input("how many people want to get in?"))
empty_seats = bus_capacity - people_inBus

if empty_seats>= people_inBus :
      print("join us we have space")

else:
      print("sorry yall have to wait for the next bus")
