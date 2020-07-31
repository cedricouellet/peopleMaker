# description : makes text file of random people (first name, last name, job position, favorite color)
# author : Cédric-Antoine Ouellet
# github : www.github.com/cedricouellet
# website : cedricao.tk

import random
import os
from time import sleep


# putting OOP into practice
class Person():
    '''A template for a person with a first name, last name, job title and favorite color'''
    # collect list of data and read them
    FIRST_NAMES = open('first_names.txt', 'r').readlines()
    LAST_NAMES = open('last_names.txt', 'r').readlines()
    JOBS = open('jobs.txt', 'r').readlines()
    COLORS = open('colors.txt', 'r').readlines()

    def __init__(self, first_name, last_name, job_title, favorite_color):
        self.firstName = first_name
        self.lastName = last_name
        self.job = job_title
        self.color = favorite_color
        
    def make_person():

        ''' Summary : Used by method `generate_list` to make a list of people.
            \nAssigns a random `firstName`, `lastName`, `job` and `color`.
            \nParams: `none`.
            \nOutput: A `Person` with attributes.
        '''

        firstName = random.choice(Person.FIRST_NAMES)
        lastName = random.choice(Person.LAST_NAMES)
        job = random.choice(Person.JOBS)
        color = random.choice(Person.COLORS)
        return Person(firstName, lastName, job, color)

    def generate_list(amount, name):

        ''' 
            Summary: Generates a `.txt` file of people (first name, last name, job title, favorite color).
            Params: 
                (int) number : number of people to be created.
                (string) name : name of the file (without `.txt`).
            Output: `.txt` file.
        '''
        people = []
        for i in range(number_of_people):
            people.append(Person.make_person())

            if os.path.exists(filename + '.txt'):
                f = open(filename + '.txt', 'a') # append to existing file
            else:
                f = open(filename + '.txt', 'x') # make new file

            i = 0 # init counter
            for p in people:

                # remove `\n` from values (due to reading documents via `readlines()`)
                if p.firstName.endswith('\n'):
                    p.firstName = p.firstName[:-1]
                if p.lastName.endswith('\n'):
                    p.lastName = p.lastName[:-1]
                if p.job.endswith('\n'):
                    p.job = p.job[:-1]
                if p.color.endswith('\n'):
                    p.color = p.color[:-1]

            # write entries onto the `.txt` file
            f.write('{} {}, {}, {}'.format(p.firstName, p.lastName, p.job, p.color))
            f.write('\n')
            
            i = i + 1 # increment counter

def main():
    Person.generate_list(amount=5, name='myPeople')

if __name__ == "__main__":
    main()
