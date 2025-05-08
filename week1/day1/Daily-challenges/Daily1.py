#Challenge1
#number = input("Enter the number:")
#length = input("Enter the length:")

#number=int(number)
#length=int(length)

#array=[]
#for i in range(1,length +1):
 # array.append(number*i)
#print(f"number: {number} - length {length} ➞ {array} ")

#Challenge2

word = input("Enter your word : ")
new_word=""
for i in range(len(word)) :
  if i == 0 or word[i] != word[i - 1] :
    new_word += word[i]
print("new word without duplicate consecutive letters:", new_word)

