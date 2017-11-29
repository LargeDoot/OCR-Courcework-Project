'''
Created on 21 Nov 2017

@author: Ethan
'''

if __name__ == '__main__':
    print("")
    
    

#    - - - - - - - - - -
#pe1 1 0 0 0 0 0 0 0 0 0 
#pe2 1 0 0 1 0 0 0 0 0 0
#pe3 1 0 0 0 0 0 0 0 0 0
#pe4 1 1 0 0 0 0 0 0 0 0


class rota:

    def __init__(self,people):

        self.people = people #Saves the list of people as a self var.
        self.numPeople = len(people) #Creates a var for number of people in list.
        
        self.staffAvail = {key: ([0] * 18) for key in self.people} #Creates a dict to store people and their availability.
        print(self.dict)
        
        
        print('Initialisation of new rota done!')


    def printAvailability(self):
        '''
        Loops through and prints:
         - Everyone in list 'people'
         - Their availability in list 'availability'
        ''' 
        
        for x in range(self.numPeople):
            print('\n' + self.people[x], end="\t")
            
            for y in range(self.numPeople):
                print(self.availability[x][y], end='\t')

        print("\n")
        
    def editAvailability(self):

        person = input("Select person to edit")
        
        for i in range(self.numPeople):
            print("{}. {}".format(i, self.people[i]))

        selection = input()
        

            
rota1 = rota(["john", "lewis", "bob", "wayne"])
rota1.printAvailability()
rota1.editAvailability()

