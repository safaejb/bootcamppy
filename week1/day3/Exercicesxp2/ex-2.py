class Dog :
  def __init__(self,name , height ):
    self.name=name
    self.height=height

  def bark (self):
    print(f"{self.name} goes Woof!")
  def jump (self) :
    jump_height= self.height * 2
    print(f"{self.name} jumps {jump_height} cm heigh!")

davids_dog= Dog("Rex", 50)
print(davids_dog.name,davids_dog.height)
davids_dog.bark()
davids_dog.jump()
sarahs_dog= Dog("Teacup",20)
print(sarahs_dog.name,sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

if sarahs_dog.height > davids_dog.height:
  print("the bigger one is ", sarahs_dog.name)
else:
  print("the bigger one is ", davids_dog.name)