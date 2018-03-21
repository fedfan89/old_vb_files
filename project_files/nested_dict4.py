# Build an algorithm that allows the user to create a nested dictionary.
import pprint
import json
import copy
import pprint
from anytree import Node, RenderTree
from anytree.exporter import DotExporter
tabstop = 4


#Data Structure Outline for Stock as a Dict:
original_string = """{
'CRBP':
    {
    'company_name':
        ['Corbus Pharmaceuticals']
    'drugs':
        {
        'Anabasum':
            {
            'indications':
                ['Cystic Fibrosis','Scleroderma','Dermatomyositis']
            'price':
                ['$25,000/year']
            }
        'Lanabasum':
            {
            'indications':
                ['Diabetes', 'Lung Cancer']
            'price':
                ['$15,000/year']
            'next_catalyst:':
                ['2018']
            }
    }
}
"""
##separate the original_string by line and format to only include the spaces and the key name
keys_with_spaces = [x for x in original_string.splitlines() if x[-1] not in ['{', '}',"'"]]
num_keys = len(keys_with_spaces)

for i in range(num_keys):
    key = keys_with_spaces[i]
    if ":" in list(key):
        key = key.replace(':', "")
    keys_with_spaces[i] = key

keys= [x.lstrip(" ") for x in keys_with_spaces] ###create list of key names without the spaces preceding the name

tabs = []   #list of number of tabs before each key
for i in range(num_keys):
    tab_count = int((len(keys_with_spaces[i]) - len(keys_with_spaces[i].lstrip(" "))) / tabstop)
    tabs.append(tab_count)

##create mental map for main_dict decision tree
numerical_codes, key_codes, key_types = [], [], [] 
for i in range(num_keys):
    if i == 0:
        numerical_code = [0]
        key_type = 'reg_key'
        key_code = [keys[0]]
    elif tabs[i] > tabs[i-1]:
        numerical_code = copy.deepcopy(numerical_codes[i-1])
        numerical_code.append(0)
        key_types[i-1], key_type = 'reg_key', 'reg_key'
        key_code = copy.deepcopy(key_codes[i-1])
        key_code.append(keys[i])
    elif tabs[i] < tabs[i-1]:
        numerical_code = copy.deepcopy(numerical_codes[i-1][0:tabs[i]])
        numerical_code.append((numerical_codes[i-1][tabs[i]]+1))
        key_types[i-2], key_types[i-1], key_type = 'last_key', 'terminal_value', 'reg_key'
        key_code = copy.deepcopy(key_codes[i-1][0:tabs[i]])
        key_code.append(keys[i])
    else:
        raise ValueError('There is a misspecified parameter.')
    numerical_codes.append(numerical_code)
    key_types.append(key_type)
    key_codes.append(key_code)
key_types[-2], key_types[-1] = 'last_key', 'terminal_value'

#update apostraphe formatting
for i in range(num_keys):
    keys[i] = keys[i].replace("'", '"')
    keys[i] = keys[i].replace("['", '"[\'')
    keys[i] = keys[i].replace("]'", '\"]"')
##create main dict
main_dict = {}
for i in range(num_keys):
    string1, string2 = "main_dict", ""
    for key in key_codes[i]:
        string2 = string2 + "[" + key + "]"
    
    if key_types[i] == 'reg_key':
        exec(string1 + string2 + " = {}")
    elif key_types[i] == 'last_key':
        exec(string1 + string2 + " = " + keys[i+1])
    elif key_types[i] == 'terminal_value':
        pass
    else:
        raise ValueError('There was a misspecification')

#create graphviz string
stringGraphViz = ""
stringGraphVizIncludes = []
for i in range(num_keys):
    if key_types[i] in ['reg_key','last_key', 'terminal_value']:
        for j in range(len(key_codes[i])-1):
            stringGraphVizInclude = "  " + key_codes[i][j]  + " -> " + key_codes[i][j+1] + "\n"
            stringGraphVizIncludes.append(stringGraphVizInclude)
#    elif key_types[i] == 'terminal_value':
#        pass
    else:
        raise ValueError('There was a misspecification')
stringGraphVizIncludes = list(set(stringGraphVizIncludes))
stringGraphViz = "".join(stringGraphVizIncludes)
stringGraphViz = stringGraphViz.replace("'", '"')
pprint.pprint(main_dict)
print(stringGraphViz)

##create a tree diagram of the data using the module anytree
CRBP = Node("CRBP")
company_name = Node('company_name', parent=CRBP)
Corbus_Pharmaceuticals = Node('Corbus_Pharmaceuticals', parent = company_name)
drugs = Node('drugs', parent=CRBP)
Anabasum = Node('Anabasum', parent = drugs)
Lanabasum = Node('Lanabasum', parent= drugs)
#print(CRBP)
#print(Lanabasum)

for pre, fill, node, in RenderTree(CRBP):
    print("%s%s" % (pre, node.name))

#DotExporter(CRBP).to_dotfile("/home/paul/Environments/CRBP.dot")
