class Human:
    species = "Homo sapiens"
    
    def __init__(self, age):
        self.age = age

    def get_age(self):
        print('Retrieving age.')
        print(self.age)
        return self.age
    
    def set_age(self, age):
        if (type(age) in (int, float)) and (0 <= age <= 150):
            print(f'Setting age to {age}')
            self.age = age
        else:
            print("Age must be a number between 0 and 150")
        
    age = property(get_age, set_age)

BooBoo = Human(age = 3)

BooBoo.get_age()
BooBoo.age = False