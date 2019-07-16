Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random

class Object:
    def __repr__(self):
        return '<%s>' % getattr(self,'__name__',self.__class__.__name__)
   
    
class Agent(Object):
    def __init__(self):
        def program(percept):abstract
        self.program=program

class tableDrivenAgent(Agent):

    def __init__(self,table):
        Agent.__init__(self)
        percepts=[]

        def program(percept):
            percepts.append(percept)
            #print percepts
            action=table.get(tuple(percepts))
            print('Agent perceives %s and does %s')%(percept,action)
            return action

        self.program=program


loc_A,loc_B='A','B'

def tableDrivenVaccumAgent():
    table = {
              ((loc_A,'Clean'),):'Right',
              ((loc_A,'Dirty'),):'Suck',
              ((loc_B,'Clean'),):'Left',
              ((loc_B,'Dirty'),):'Suck',
              ((loc_A, 'Clean'), (loc_A, 'Clean')): 'Right',
              ((loc_A, 'Clean'), (loc_B, 'Clean')): 'Left',
              ((loc_A, 'Clean'), (loc_B, 'Dirty')): 'Right',
              ((loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',
              ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Clean')): 'Right',
              ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',
            }
    return tableDrivenAgent(table)


class reflexVaccumAgent(Agent):
    def __init__(self):
        Agent.__init__(self)

        action=' '

        def program((location,status)):        
            if status=='Dirty': action= 'Suck'
            elif location==loc_A: action= 'Right'
            elif location==loc_B: action= 'Left'

            percept=(location,status)
            print('Agent perceives %s and does %s')%(percept,action)

            return action
        
            
            
        self.program=program

class modelBasedVaccumAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        model={loc_A:None,loc_B:None}

        def program((location,status)):
            model[location]=status
            if model[loc_A]==model[loc_B]=='Clean': return 'NoOp'
            elif status=='Dirty': action= 'Suck'
            elif location==loc_A: action= 'Right'
            elif location==loc_B: action= 'Left'

            percept=(location,status)
            print('Agent perceives %s and does %s')%(percept,action)

            return action                    
            
        self.program=program

        
class vaccumEnvironment:

    def __init__(self):
        self.status={ loc_A:random.choice(['Clean','Dirty']),
                      loc_B:random.choice(['Clean','Dirty'])
                      }
    def add_object(self,object,location=None):
        object.location=location or self.default_location(object)

    def default_location(self,object):
        return random.choice([loc_A,loc_B])

    def percept(self,agent):
        return (agent.location,self.status[agent.location])

    def execute_action(self,agent,action):
        if action=='Right': agent.location=loc_B
        elif action=='Left': agent.location=loc_A
        elif action=='Suck':
            #if self.status[agent.location]=='Dirty'
            self.status[agent.location]='Clean'



Tagent=tableDrivenVaccumAgent()
env=vaccumEnvironment()
env.add_object(Tagent)
for steps in range(10):
    action=Tagent.program(env.percept(Tagent))
    env.execute_action(Tagent,action)
            
##Ragent=reflexVaccumAgent()
##env=vaccumEnvironment()
##env.add_object(Ragent)
##for steps in range(15):
##    action=Ragent.program(env.percept(Ragent))
##    env.execute_action(Ragent,action)



            
##Magent=modelBasedVaccumAgent()
##env=vaccumEnvironment()
##env.add_object(Magent)
##for steps in range(15):
##    action=Magent.program(env.percept(Magent))
##    env.execute_action(Magent,action)








