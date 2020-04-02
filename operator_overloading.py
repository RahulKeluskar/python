'''
Module to implement operator overloading using a superhero class
'''


class Superhero():
    '''Superhero class to initialise superhero using name power and age '''

    def __init__(self, name, power, age, moves):
        """
        Using parameters name as string, power as a float and age as a integer
        """
        self.name = name
        self.power = power
        self.age = age
        self.moves = moves

    def __add__(self, other):
        ''' Adding 2 superhero objects '''
        new_name = self.name + ' ' + other.name
        new_power = int(self.power) + int(other.power)
        new_age = (int(self.age) + int(other.age))/2
        new_moves = list(set(self.moves + other.moves))
        return Superhero(name=new_name, power=new_power, age=new_age, moves=new_moves)

    def __contains__(self, item):
        ''' Check for equality of name '''
        return item in self.moves

    def __eq__(self, other):
        ''' Find if the power and age of the 2 superheroes is the same '''
        return self.age == other.age and self.power == other.power

    def __ge__(self, other):
        ''' Find if power of superhero1 is greater than equal to power of superhero2 where superheroes 1 and 2 are the 2 parameters respectively '''
        return self.age >= other.age and self.power >= other.power

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
        return f'The name is {self.name}\n The power is {self.power} \n The age is {self.age}\n and his moves are {self.moves}'


if __name__ == '__main__':
    NAME1, POWER1, AGE1, *MOVES1 = input(
        'Enter the NAME, POWER ,AGE and MOVES separted by spaces: ').split()
    MOVES1 = list(MOVES1)
    NAME2, POWER2, AGE2, *MOVES2 = input(
        'Enter the NAME , POWER, AGE and MOVES of his opponent separted by spaces: ').split()
    MOVES2 = list(MOVES2)
    SUPERHERO_1 = Superhero(NAME1, POWER1, AGE1, MOVES1)
    SUPERHERO_2 = Superhero(NAME2, POWER2, AGE2, MOVES2)

    CHILD = SUPERHERO_1 + SUPERHERO_2
    print(CHILD)
