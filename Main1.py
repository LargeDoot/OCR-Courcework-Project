'''
Created on 10 Jan 2018

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
                              "1000","1030","1100","1130","1200","1230","1300","1330","1400"]
            
            self.people = people #Saves the list of people as a self var.
            self.numPeople = len(people) #Creates a var for number of people in list.
            
            self.delAvailability() #Creates a dict to store people and their availability.
            self.matrix = {key: ([""] * 18) for key in self.people} #Creates a dict to store people and their jobs.
            self.staffPosCount = {key: (0) for key in self.people}

            
            
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
            
            
        def editAvailability(self, person, editList):
            '''
            - Allows the editing of each person availability.
            - Takes a list containing numbers 0-15 of which availability needs to be removed for
            - ie parse list [0, 1] to remove availability for 0530 and 0600
            '''
            
            for timeslot in editList: #Loops through editList parsed to function
                self.staffAvail[person][int(timeslot)] = 0 #Updates value specified above
                
            
            
                   
        def refreshRota(self):
            '''
            - Regenerates the rota if availability has been changed
            - Creates a new rota if specified by user 
            '''
            
            self.poolPos = ["P1","P2","P3","CL"] #Create a temporary list for storing remaining positions to be filled
            print(self.poolPos)
            #Create an initial matching first


            for count, people in enumerate(self.people): #Loop through list of people on a shift, enumerate used to save using a count variable

                for i in range(len(self.timeSlots)):   #Loop through each persons time slots (i.e. 06:00->14:30)
                    
                    if self.staffAvail[people][i] == 1: #Checks the current time slot and if the person is available
                        self.matrix[people][i] = self.poolPos[(count + i) % 4] #Loops through a 'circular' list of positions and assigns them
                        
                    else: #If they aren't available then assign "CL"
                        self.matrix[people][i] = "CL"
                        

            print("Initial matrix created successfully, improving...")
            self.poolPos = ["P1","P2","P3"]
            
            for i in range(len(self.timeSlots)): #Loops through each time slot
                posFilled = [] #Creates a temporary list for storing positions filled on each cycle
                staffFilled = []
                missingItems = []
                
                for people in self.people: #Loops through each row of the current time slot
                    
                    if self.matrix[people][i] in self.poolPos:
                        print("found", self.matrix[people][i], "at", i)
                        posFilled.append(self.matrix[people][i])
                        staffFilled.append(people)
                        
                
                if set(posFilled) == set(self.poolPos): #Compares the two lists regardless of the order they are in  using 'set'
                    print('all positions filled')
                    
                    
                    self.incrementPosCount(staffFilled)
                    print(self.staffPosCount)
                    
                else:
                    missingItems = set(self.poolPos)^set(posFilled)      
                    print('Items missing: {}'.format(missingItems))
                    self.completeMissingItems(missingItems, i)
                            
                    
                            
                            
                for person in self.people:
                    if self.staffPosCount[person] <= 3:
                        self.staffPosCount[person] = 0
                        try:
                            self.staffAvail[person][i+1] = 0
                        except IndexError:
                            False
                               
        def completeMissingItems(self, missingItems, i):            
            
            for people in self.people:
                #print(self.matrix[people][i], self.staffAvail[people][i])
                        
                if self.matrix[people][i] == "CL" and self.staffAvail[people][i] == 1:
                    self.matrix[people][i] = missingItems.pop()
                    
    
        def incrementPosCount(self, staff):
            
            for person in staff:
                self.staffPosCount[person] += 1
    
            
        def printMatrix(self):
            
            for person in self.matrix: #Loops through dictionary fo names
                
                print(person, end="\t") #Prints each persons name
                print(self.matrix[person]) #Prints list of availability of that person
                
            
        def getMatrix(self):
            
            return self.matrix   #returns the matrix
        
        def getPeople(self):
            
            return self.people  #returns list of peoples names   
        
        def delAvailability(self):
            
            self.staffAvail = {key: ([1] * 18) for key in self.people}
            return True
        
        def changeNames(self, staff):
            
            self.people = staff
            self.__init__(staff)



@app.route("/")
def home():
    '''
    Code for the index page for the system
    '''
    
    global rotaInstance
    rotaInstance = rota(["name1","name2","name3","name4"])
    
    return render_template('index.html')

@app.route("/rota")
def view_rota():
    '''
    Code for the viewing screen, where the matrix as it is will be displayed in full.
    '''
    global rotaInstance
    print(rotaInstance.getMatrix())
    return render_template('rota.html', rotaList = rotaInstance.getMatrix())


@app.route("/edit")
def edit():
    '''
    Code or editing screen where matrix will be available to edit manually.
    '''
    return render_template('edit.html')

@app.route("/create", methods=['GET', 'POST'])
def create():
    '''
    Code for the creation screen that will mainly take data from a html form and use this with the 
    rota class to generate a new rota.
    '''
    global rotaInstance
    rotaInstance.delAvailability()
    
    if request.method == 'POST':
        peopleList = []
        
        #Import data from form, and assign data to variables 
        for i in range(1, len(rotaInstance.getPeople()  ) + 1 ): #Loops from i=1 to the length of the list of people 
            peopleList.append( request.form[str(i)] ) #Adds each name to a list, will be used in displaying matrix
            
            print("***", request.form[str(i)]) #Request data from text forms that should contain names of people

                    
        print(peopleList)
        rotaInstance.changeNames(peopleList)
        
        for person in rotaInstance.getPeople():
            print(person)
            print(request.form.getlist(person))
            rotaInstance.editAvailability(person, request.form.getlist(person))
            
        rotaInstance.refreshRota()
        
    return render_template('create.html', people = rotaInstance.getPeople())


if __name__ == '__main__':
    app.secret_key = 123
    app.run(debug=True,port=69)