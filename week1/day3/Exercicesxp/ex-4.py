class Zoo :
  def __init__(self,zoo_name) :
    self.zoo_name = zoo_name
    self.animals = []
  def add_animal(self,new_animal):
    if new_animal not in self.animals:
      self.animals.append(new_animal)
  def get_animal(self):
    for animal in self.animals:
     print(animal)
  def sell_animal(self, animal_sold):
    self.animal_sold=animal_sold
    if animal_sold in self.animals :
      self.animals.remove(animal_sold)
      print(f"the {animal_sold} has been sold. ")
    else:
      print(f"The {animal_sold} is not in the zoo.")
  def sort_animals(self):
    self.animals.sort()
    print("animals sorted alphabetically")

  def group_animals_by_first_letter(self):
        grouped = {}
        for animal in self.animals:
          first_letter = animal[0].upper()
          if first_letter not in grouped:
            grouped[first_letter]=[]
          grouped[first_letter].append(animal)
        for letter, animals in grouped.items():
            print(f"{letter}: {', '.join(animals)}")




