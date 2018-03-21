import csv
symbol_list = []
file_object = open('optionable_symbols_clean.csv')
for line in file_object:
    line = line.replace('\n', '')
    symbol_list.append(line)
file_object.close()
print(symbol_list)

