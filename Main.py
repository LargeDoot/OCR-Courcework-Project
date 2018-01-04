'''
Created on 21 Nov 2017

@author: Ethan
'''

if __name__ == '__main__':
    print("")


class rota:

    def __init__(self,people):

        self.people = people #Saves the list of people as a self var.
        self.numPeople = len(people) #Creates a var for number of people in list.
        
        self.staffAvail = {key: ([1] * 18) for key in self.people} #Creates a dict to store people and their availability.
        self.matrix = {key: ([1] * 18) for key in self.people} #Creates a dict to store people and their availability.

        print(self.staffAvail)
        print(self.matrix)
        
        
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
        - Allows the editing of each person availability.
        - Displays 'self.people', available time slots
        - Inputs person, time slot to edit, and new value
        '''
        
        for i in range(self.numPeople): #Loop prints incrementing numbers, each followed by names from people list
            print("{}. {}".format(i+1, self.people[i]))

        person = input("Select person to edit") #Inputs person name to edit
        
        
        print(TIMESLOTS_AM) #Prints available time slots to edit
        timeslot = int(input("Times lot to edit:")) #Inputs which time slot to edit
        
        value = input("new value:") #Inputs new value for selected person and time slot
        
        self.staffAvail[person][timeslot] = value #Updates value specified above
        
        
        
               
    def refreshRota(self):
        '''
        - Regenerates the rota if availability has been changed
        - Creates a new rota if specified by user 
        '''
        
        #Create an initial matching first
        for i in range(self.numPeople):
            for people in self.people:
                if self.staffAvail == 1:
                    
                
                
                


TIMESLOTS_AM = ["0530","0600","0630","0700"]
            
rota1 = rota(["john", "lewis", "bob", "wayne"])
rota1.printAvailability()
rota1.editAvailability()
rota1.printAvailability()

