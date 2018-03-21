# Build an algorithm that allows the user to create a nested dictionary.
import pprint
import json
import copy
import pprint
tabstop = 4


#Data Structure Outline for Stock as a Dict:
example_string = """
{
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
                '$25,000/year'
            }
        'Lanabasum':
            {
            'indications':
                ['Diabetes', 'Lung Cancer']
            'price':
                ['$15,000/year]
            }
    }
}
"""

example_string = example_string.split('\n')
example_string = [x for x in example_string if str(x)[-1:] not in ('{','}','',)]
key_names = [x.lstrip(' ') for x in example_string]
for i in range(len(key_names)):
    if key_names[i].endswith(':'):
        key_names[i] = key_names[i][:-1]
        key_names[i] = key_names[i].replace("'", "")
    if '"' in key_names:
        key_names.remove('"')
print(key_names)
indentation_sequence = [(len(x) - len(x.lstrip(' '))) / tabstop for x in example_string]
indentation_sequence_codes = []

name_sequences = []
for i in range(len(indentation_sequence)):
    code = []
    name_sequence =[]
    if i == 0:
        code.append(0)
        ##
        name_sequence.append(key_names[i])
    elif indentation_sequence[i] > indentation_sequence[i-1]:
        code = copy.deepcopy(indentation_sequence_codes[i-1])
        code.append(0)
        ##
        name_sequence = copy.deepcopy(name_sequences[i-1])
        name_sequence.append(key_names[i])
    elif indentation_sequence[i] < indentation_sequence[i-1]:
        num_tabs = int(indentation_sequence[i])
        code = (copy.deepcopy(indentation_sequence_codes)[i-1])[0:num_tabs+1]
        code[-1] = code[-1] + 1
        ##
        name_sequence = (copy.deepcopy(name_sequences)[i-1])[0:num_tabs]
        name_sequence.append(key_names[i])
    else:
        raise ValueError
    indentation_sequence_codes.append(code)
    ##
    name_sequences.append(name_sequence)
    code=[]
pprint.pprint(indentation_sequence_codes)
pprint.pprint(name_sequences)

key_code_pairs = [(indentation_sequence_codes[i], key_names[i]) for i in range(len(indentation_sequence_codes))]

main_dict = {}
sequence_pairs = list(zip(name_sequences, indentation_sequence_codes))
for i in range(len(sequence_pairs)):
    print(len(sequence_pairs[i]), len(sequence_pairs[i+1])
            keys, binary = sequence_pairs[i][0], sequence_pairs[i][1]
    num_keys = len(keys)
    string1 = 'main_dict'
    for i in range(num_keys): 
        string1 = string1 + '["' + keys[i] + '"]'
    try:
        if len(sequence_pairs[i+1][1]) < num_keys:
            string1 = string1 + " = 'default value'"
        elif len(sequence_pairs[i+1][1]) > num_keys:
            string1 = string1 + " = {}"
        else:
            raise ValueError
    except:
        pass
        #print(string1)
        #exec(string1)
pprint.pprint(main_dict)

"""
<ticker>
    <company_name>
    <is_optionable>
    <sector>
    <ceo>
    <subsector>
    <industry>
    <call_open_interest>
    <put_open_interest>
    <total_open_interest>
    <best_index>
    <drug>
        <indication>
            <market>
                <US_market>
                    <stage_of_development>
                    <prob_success>
                    <US_patient_population>
                    <US_peak_penetration_est>
                    <US_peak_penetration_year>
                    <US_patent_expiration_year>
                    <US_price_est>
                    <US_gross_margin_est>
                <Europe_market>
            <competitor>
                <drug_name>
                <company_name>
                <drug_price>
                <market_share>
                <efficacy>
                <safety>
                <stage_of_development>
                <prob_success>
        <upcoming_catalyst>
            <indication>
            <catalyst_name>
            <timing>
            <probability_distribution>
"""
#beg = [pos for pos, char in enumerate(list(string)) if char =='<']
#end = [pos for pos, char in enumerate(list(string)) if char =='>']
#pairs = list(zip(beg, end))
#keys = [string[beg+1:end] for beg,end in pairs]
#
#print(pairs)
#diffs = [(pairs[i][0] - pairs[i-1][1]) for i in range(0, len(pairs))]
#diffs[0] = 0
#key_location_pairs = list(zip(keys,diffs))
#unique_locations = list(set(diffs))
#unique_locations.sort()
#num_levels = len(unique_locations)
#location_frequency_pairs = [(i,diffs.count(i)) for i in unique_levels]
#
##here, attempt to make a nested dictionary
#dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8, dict9, dict10 = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
#location_array = enumerate(unique_locations)
#original_dict = {}
#for level in unique_locations:
#    for i in range(len(key_location_pairs)):
#        key, location = pair[i][0], pair[i][1]
#        
#        if location == level:i
#        original_dict[key] = dict1
#    elif location == 
#        # check if there already exists a dict for this level
#        try:
#            
#        original_dict[key] = {}
#    elif location > pair[i-1][1]:
#
#
#
#    
#
##create a nested 
#def build_nested_dict():
#        dict1 = {}
#        dict2 = {}
#
#        ticker = input("Enter the stock ticker: ")
#        dict1[ticker] = dict2
#
#        print(ticker, dict1, dict2)
#        print(type(ticker), type(dict1), type(dict2))
#
#        #keys2 = eval(input("For the ticker " + str(ticker) + " please enter a list of the next set of nested keys: "))
#        keys2_t = ['company_name', 'market_cap', 'is_optionable']
#        keys2_k = ['drugs', 'competitors']
#        #these keys have a terminal value
#        for key in keys2_t: #enter the values for each key
#            value = input("For " + str(ticker) + ", please enter the value for " + str(key) + ": ")
#            dict2[key] = value
#
#        print(dict1)
#        print(dict2)
#        return(dict1)

#CRBP = build_nested_dict()
#print(CRBP)
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(CRBP)
#print(json.dumps(CRBP, sort_keys=True, indent=4))
#print(json.dumps(CRBP, sort_keys=False, indent=4))
