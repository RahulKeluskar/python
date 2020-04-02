'''
Module to implement operator overloading using a superhero class
'''


class Superhero():
    '''Superhero class to initialise superhero using name power and age '''

    def __init__(self, name, power, age):
        """
        Using parameters name as string, power as a float and age as a integer
        """
        self.name = name
        self.power = power
        self.age = age

    def __add__(self, other):
        new_name = self.name + ' ' + other.name
        new_power = int(self.power) + int(other.power)
        new_age = (int(self.age) + int(other.age))/2
        return Superhero(name=new_name, power=new_power, age=new_age)

    def get_name(self):
        """
        Get the name of the superhero
        """
        return f'The name is {self.name}'

    def get_power(self):
        ''' Get the power level of the superhero '''
        return f'The power level is {self.power}'

    def get_age(self):
        ''' Get the age of the superhero '''
        return f'The age of the superhero is {self.age}'

    def __str__(self):
        return f'The name is {self.name}\n The power is {self.power} \n The age is {self.age}'


if __name__ == '__main__':
    NAME1, POWER1, AGE1 = input(
        'Enter the NAME POWER and AGE separted by spaces: ').split()
    NAME2, POWER2, AGE2 = input(
        'Enter the NAME POWER and AGE of his opponent separted by spaces: ').split()
    SUPERHERO_1 = Superhero(NAME1, POWER1, AGE1)
    SUPERHERO_2 = Superhero(NAME2, POWER2, AGE2)

    CHILD = SUPERHERO_1 + SUPERHERO_2
    print(CHILD)
