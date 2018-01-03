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
        print(self.staffAvail)
        
        
        print('Initialisation of new rota done!')


    def printAvailability(self):
        '''
        Loops through and prints:
         - Everyone in list 'people'
         - Their availability in list 'availability'
        '''        
        
        for x in range(self.numPeople): #Loop round and print every name and availability
            print('\n' + self.people[x], end="\t") #Names
            print(self.staffAvail[self.people[x]], end="\t") #Availability

        print("\n")
        
        
    def editAvailability(self):
        '''
        Allows the editing of each person availability.
        '''
        
        for i in range(self.numPeople):
            print("{}. {}".format(i+1, self.people[i]))

        person = input("Select person to edit")
        
        
        print(TIMESLOTS_AM)
        timeslot = int(input("timeslot to edit:"))
        
        value = input("new value:")
        
        self.staffAvail[person][timeslot] = value


TIMESLOTS_AM = ["0530","0600","0630","0700"]
            
rota1 = rota(["john", "lewis", "bob", "wayne"])
rota1.printAvailability()
rota1.editAvailability()
rota1.printAvailability()

