'''
Created on 21 Nov 2017

@author: Ethan
'''
from symbol import except_clause
from builtins import enumerate
from flask import *
from flask.templating import render_template


app = Flask(__name__)


class rota:

    def __init__(self,people):
        
        self.timeSlots = ["0530","0600","0630","0700","0730","0800","0830","0900","0930",
                          "1000","1030","1100","1130","1200","1230","1300","1330","1400","1430"]
        
        self.people = people #Saves the list of people as a self var.
        self.numPeople = len(people) #Creates a var for number of people in list.
        
        self.staffAvail = {key: ([1] * 19) for key in self.people} #Creates a dict to store people and their availability.
        self.matrix = {key: ([0] * 19) for key in self.people} #Creates a dict to store people and their jobs.
        
        print(self.staffAvail)
        print(self.matrix)
        
        
        print('Initialisation of new rota done!')




    def printAvailability(self):
        '''
        Loops through and prints:
         - Everyone in list 'people'
         - Their availability in list 'availability'
        '''        
        
        for person in self.people: #Loop round and print every name and availability
            print('\n' + person, end="\t") #Names
            print(self.staffAvail[person], end="\t") #Availability

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
        
        
        print(self.timeSlots) #Prints available time slots to edit
        timeslot = int(input("Times lot to edit:")) #Inputs which time slot to edit
        
        value = input("new value:") #Inputs new value for selected person and time slot
        
        self.staffAvail[person][timeslot] = value #Updates value specified above
        
        
        
               
    def refreshRota(self):
        '''
        - Regenerates the rota if availability has been changed
        - Creates a new rota if specified by user 
        '''
        
        self.poolPos = ["P1","P2","P3","CL"] #Create a temporary list for storing remaining positions to be filled
        print(self.poolPos)
        #Create an initial matching first
        count = 0

        for people in self.people:
            
            for i in range( len(self.timeSlots)):  
                
                if self.staffAvail[people][i] == 1:
                    self.matrix[people][i] = self.poolPos[(count + i) % 4]
                    
                else:
                    self.matrix[people][i] = "CL"
                    
            count += 1       




        
    def printMatrix(self):
        
        for person in self.matrix:
            
            print(person, end="\t")        
            print(self.matrix[person])
            
        
    def getMatrix(self):
        
        return self.matrix       


@app.route("/")
@app.route("/rota")
def home():
    
    session['class']= rota(["john", "lewis", "bob", "wayne","test"])
    
    return render_template('rota.html', result = session['class'].getMatrix()["bob"])

@app.route("/edit")
def edit():
    return render_template('edit.html')

@app.route("/create")
def create():
    return render_template('create.html')
            
rota1 = rota(["john", "lewis", "bob", "wayne","test"])

#rota1.printAvailability()
#rota1.editAvailability()
#rota1.printAvailability()
#rota1.refreshRota()
#rota1.printMatrix()

if __name__ == '__main__':
    app.secret_key = 123
    app.run(debug=True,port=69)