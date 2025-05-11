import random

class Game:
    
  def get_user_item(self):
    while True:
     user_item = input("please choose rock, paper or scissors: ").lower()
     if user_item in ['rock', 'paper', 'scissors']:
      return user_item
     else:
      print("Invalid choice. Please enter rock, paper or scissors.")
   
  def get_computer_item(self):
    computer_item = ['rock', 'paper', 'scissors']
    return random.choice(computer_item)
  

  def get_game_result(self, user_item, computer_item):

    if user_item == computer_item:
      return "draw"
    
    elif user_item == "rock" and computer_item == "scissors":
      return "win"
    elif user_item == "scissors" and computer_item == "paper":
      return "win"
    elif user_item == "paper" and computer_item == "rock":
      return "win"
    else :
      return "loss"
    
  def play(self):
    user_item = self.get_user_item()
    computer_item = self.get_computer_item()
    result = self.get_game_result(user_item, computer_item)
    print(f"\nYou chose: {user_item}")
    print(f"Computer chose: {computer_item} ")
    print(f"Result :{result}")
    return result

