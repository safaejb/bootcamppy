#exercice1

#for i in range(4):
 #  print("hello word")


#exercie2
#a = 99
#b = a * a * a  
#result = b * 8
#print(result)


#exercice3
#name_entered = input("enter your name!")
#name = "Safae"
#if name_entered == name :
 # print("YESS! we have the same name")
#else :
 # print("we don't have the same name bro")

 #exercice4

#height = int(input("Enter your height : "))
#if height > 145:
 #   print("You are tall enough to ride! ")
#else:
#    print("you need to grow some more to ride. ")

#Exercice5
#my_fav_numbers = {1,2,3,4,5}
#my_fav_numbers.add(9)
#my_fav_numbers.add(10)
#print(my_fav_numbers)
#my_fav_numbers.remove(9)
#print(my_fav_numbers)
#friend_fav_numbers = {10,20,30}
#our_fav_numbers = my_fav_numbers | friend_fav_numbers
#print(our_fav_numbers)

#Exercice6
# we can't add more integers to the tuple but we can create a new one with a new values plus the old values like:
#for example 
#tuple=(1,2,3)
#new_tuple=tuple+(4,5,6)
#print(new_tuple)


#Exercice 7

#basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#print(basket)
#basket.remove("Banana")
#print(basket)
#basket.remove("Blueberries")
#print(basket)
#basket.append("kiwi")
#print(basket)
#basket.insert(0 ,"Apples")
#print(basket)
#print(basket.count("Apples"))
#basket.clear()
#print(basket)

#Exercice8
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
print("the deli has run out the orders")
while "Pastrami sandwich" in sandwich_orders :
  sandwich_orders.remove("Pastrami sandwich")
finished_sandwich = []
while len(sandwich_orders) > 0:
    sandwich = sandwich_orders.pop(0)
    print("I made your", sandwich)
    finished_sandwich.append(sandwich)


