family0 = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

family = {}

while True :
  name= input("enter your name : ")
  if name.lower() == "quit":
    break
  age= input("enter your age : ")
  family[name]=age

print(family)

ticket = 0
result = 0

for member in family:
  if family[member] < 3 :
    ticket = 0
  elif family[member] > 3 and family[member] < 12 :
    ticket = 10
  else :
    ticket = 15 
  result +=ticket

print(result)
