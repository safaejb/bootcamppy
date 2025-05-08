class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
first_Cat= Cat("Leo", 3)
second_Cat= Cat("Minouche", 12)
third_Cat= Cat("Cesar", 4)
print(first_Cat.name,first_Cat.age)
print(second_Cat.name,second_Cat.age)
print(third_Cat.name,third_Cat.age)


def find_oldest_cat(cats):
    oldest = cats[0]
    for cat in cats[1:]:
        if cat.age > oldest.age:
            oldest = cat
    return oldest
cat_list = [first_Cat, second_Cat, third_Cat]
oldest_cat = find_oldest_cat(cat_list)
print(f"The oldest cat is {oldest_cat.name}, who is {oldest_cat.age} years old.")