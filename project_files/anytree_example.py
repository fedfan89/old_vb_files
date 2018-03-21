from anytree import Node, RenderTree
import pprint
"""
Here I model attributes of a stock as nodes in a tree using the module anytree. The nodes can have attributes. NodeMixin extends any python class to a tree node.
    Each node is individually named. One issue so far is that the names of the nodes are very long, to the point of being unusable.
    That said, in Python, I can create secondary names for object instances. Can I make a list of protected object names? Can I easily list all the names that point to the same object instance?
By construction, have each Label type be mapped to a class?
So for the outline below, the classes ==> values would be...
    Stock ==> CRBP
    Drugs ==> Anabasum, NewDrug
    CompanyName ==> Corbus_Pharmaceuticals
    Events ==> Ph3_Scleroderma_Data

Features I imagine may be useful:
    Get event calendar across all stocks
    Rank most impacting events by magnitude

To me, a (main) benefit of this framework is that all of the data is centralized and relatable. When working with individual Excel spreadsheets, at least to my understanding, worksheets do not talk to each other. So for example, if a common data point was in two sheets, you woul dneed to change it in both. Here, the data is centralized so that it can talk and be compared and grouped, which is beneficial to organization and preparedness.
"""
#level 1 (top node)
CRBP = Node(name="CRBP", value=0, label=0)

#level 2
CRBP_Drugs = Node(name="Drugs",parent=CRBP, value=0, label=1)
CRBP_CoName = Node(name='Company_Name', parent=CRBP, value=0, label=1)
CRBP_Events = Node(name='Events', parent=CRBP, value=0, label=0)

#level 3
CRBP_Drugs_Anabasum = Node(name="Anabasum", parent=CRBP_Drugs, value=0, label=0)
CRBP_Drugs_NewDrug = Node(name="NewDrug", parent=CRBP_Drugs, value=0, label=0)
CRBP_CoName_CompanyName = Node(name="Corbus_Pharmaceuticals", parent=CRBP_CoName, value=0, label=0)
CRBP_Events_Ph3SclerodermaData = Node(name="Ph3_Scleroderma_Data", parent=CRBP_Events, value=0, label=0)

#level 4
CRBP_Drugs_Anabasum_Indications = Node(name="Indications", parent=CRBP_Drugs_Anabasum, value=0, label=1)
CRBP_Drugs_NewDrug_Indications = Node(name="Indications", parent=CRBP_Drugs_NewDrug, value=0, label=1)
CRBP_Events_Ph3SclerodermaData_Timing = Node(name="Timing", parent=CRBP_Events_Ph3SclerodermaData, value=0, label=1)
CRBP_Events_Ph3SclerodermaData_Distribution = Node(name="Event_Distribution", parent=CRBP_Events_Ph3SclerodermaData, value=0, label=1)

#level 5
CRBP_Drugs_Anabasum_Indications_Scleroderma = Node(name="Scleroderma",parent=CRBP_Drugs_Anabasum_Indications, value=0, label=0)
CRBP_Drugs_Anabasum_Indications_CysticFibrosis = Node(name="CysticFibrosis", parent=CRBP_Drugs_Anabasum_Indications,value=0, label=0)
CRBP_Drugs_Anabasum_Indications_Dermatomyositis = Node(name="Dermatomyositis", parent=CRBP_Drugs_Anabasum_Indications, value=0, label=0)
CRBP_Drugs_NewDrug_Indications_HeartDisease = Node(name="HeartDisease",parent=CRBP_Drugs_NewDrug_Indications, value=0, label=0)
CRBP_Drugs_NewDrug_Indications_Happiness = Node(name="Happiness",parent=CRBP_Drugs_NewDrug_Indications, value=0, label=0)
CRBP_Events_Ph3SclerodermaData_Timing_Timing = Node(name="2018Q1", parent=CRBP_Events_Ph3SclerodermaData_Timing, value=0, label=0)
CRBP_Events_Ph3SclerodermaData_Distribution_Tuple = Node(name="[(.5, 10), (.2, 20), (.3, 2)]", parent=CRBP_Events_Ph3SclerodermaData_Distribution, value=0, label=0)

#attributes include .name, .parent, .value, .children, .ancestors, .descendants

#set values (SOTP targets) for each indication
CRBP_Drugs_Anabasum_Indications_Scleroderma.value = 4
CRBP_Drugs_Anabasum_Indications_CysticFibrosis.value = 15
CRBP_Drugs_Anabasum_Indications_Dermatomyositis.value = 2
CRBP_Drugs_NewDrug_Indications_HeartDisease.value = .5
CRBP_Drugs_NewDrug_Indications_Happiness.value = 1.5

#recursively sum the values in child nodes to parent nodes from the bottom up
descendants = list(CRBP.descendants)
descendants.reverse()
descendants.append(CRBP)
for node in descendants:
    if not node.descendants:
        pass
    else:
        node.value = 0
        for child in node.children:
            node.value += child.value

#simple tree diagram provided in the anytree documentation
def printSimpleTree():
    for pre, fill, node in RenderTree(CRBP):
        print("%s%s" % (pre, node.name))

#create tree diagram (text version)
def printTree(include_labels = "No"):
    for pre, fill, node in RenderTree(CRBP):
        if include_labels == "Yes":
            print("%s%s ($%.2f)" % (pre, node.name, node.value))
        elif include_labels == "No":
            if node.label == 0:
                print("%s%s ($%.2f)" % (pre, node.name, node.value))
            else:
                pass
        else:
            raise ValueError("You have inputted a wrong parameter. include_values takes 'yes' or 'no'")

def printTree2(include_labels = "No"):
    for pre, fill, node in RenderTree(CRBP_Drugs):
        if include_labels == "Yes":
            if node.value == 0:
                print("%s%s" % (pre, node.name))
            else:
                print("%s%s ($%.2f)" % (pre, node.name, node.value))
        elif include_labels == "No":
            if node.label == 0:
                if node.value == 0:
                    print("%s%s" % (pre, node.name))
                else:
                    print("%s%s ($%.2f)" % (pre, node.name, node.value))
            else:
                pass
        else:
            raise ValueError("You have inputted a wrong parameter. include_values takes 'yes' or 'no'")

#assign secondary name to the indications
Scleroderma = CRBP_Drugs_Anabasum_Indications_Scleroderma
Scleroderma.value = 25

printTree2(include_labels="No")

#Stock ==> CRBP
#Drugs ==> Anabasum, NewDrug
#CompanyName ==> Corbus_Pharmaceuticals
#Events ==> Ph3_Scleroderma_Data

class Event(object):
    def __init__(self, name = "DefaultEvent")
        self.name = name

    def set_Distribution(self, states=[], probs=[], price_targets=[]):
        self.states = states
        self.probs = probs
        self.price_targets = price_targets

    def set_Distribution_min_estimates
        

class Timing(object):
    def __init__(self, name = "NoneSpecified"):
        self.name = name

#value set for timing parameter:
    Year:
        2018,
        2019,
        2020,
        2021,

    Half:
        1H_18, 2H_18,
        1H_19, 2H_19, 
        1H_20, 2H_20,

    Quarter:
        1Q_18, 2Q_18, 3Q_18, 4Q_18,
        1Q_19, 2Q_19, 3Q_19, 4Q_19,
        1Q_20, 2Q_20, 3Q_20, 4Q_20,

    Month:
        Jan_17, Feb_17, Mar_17, Apr_17, May_17, Jun_17, Jul_17, Aug_17, Sep_17, Oct_17, Nov_17, Dec_17
        Jan_17, Feb_17, Mar_17, Apr_17, May_17, Jun_17, Jul_17, Aug_17, Sep_17, Oct_17, Nov_17, Dec_17
        Jan_17, Feb_17, Mar_17, Apr_17, May_17, Jun_17, Jul_17, Aug_17, Sep_17, Oct_17, Nov_17, Dec_17

    Half_Month:
        1H_Jan, 2H_Jan, 1H_Feb, 2H_Feb, 1H_Mar, 2H_Mar, 1H_Apr, 2H_Apr, 1H_May, 2H_May, 1H_Jun, 2H_Jun, 1H_Jul, 2H_Jul, 1H_Aug, 2H_Aug, 1H_Sep, 2H_Sep, 1H_Oct, 2H_Oct, 1H_Nov, 2H_Nov, 1H_Dec, 2H_Dec

    Optional:
        Set a specific timing function, which is a list of bucketing frames and probabilities

        

















