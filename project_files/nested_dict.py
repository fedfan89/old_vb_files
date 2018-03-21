# Build an algorithm that allows the user to create a nested dictionary.

def build_nested_dict():
        dict1 = {}
        dict2 = {}

        ticker = input("Enter the stock ticker (as a string): ")
        print(ticker)
        dict1[ticker] = dict2
        print(ticker, dict1, dict2)
        print(type(ticker), type(dict1), type(dict2))

        keys2 = eval(input("For the ticker " + str(ticker) + " please enter a list of the next set of nested keys (as a list of strings as a string): "))
        print(keys2, type(keys2))

        for key in keys2: #enter the values for each key
            value = input("Enter the value for the key " + str(key) + ": ")
            dict2[key] = value
        print(dict1)
        print(dict2)
        return(dict1)

CRBP = build_nested_dict()
print(CRBP)
