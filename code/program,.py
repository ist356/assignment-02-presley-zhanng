from packaging import parse_packaging, calc_total_units, get_unit
import json
'''
This is the main program. 
You should read the packaging.txt in the data folder.
Each line contains one package description. 
You should parse the package description using parse_packaging()
print the total number of items in the package using calc_total_units()
along with the unit using get_unit()
place each package in a list and save in JSON format.

Example:

    INPUT (example data/packaging.txt file):
    
    12 eggs in 1 carton
    6 bars in 1 pack / 12 packs in 1 carton

    OUTPUT: (print to console)

    12 eggs in 1 carton => total units: 12 eggs
    6 bars in 1 pack / 12 packs in 1 carton => total units: 72 bars

    OUTPUT (example data/packaging.json file):
    [
        [{ 'eggs' : 12}, {'carton' : 1}],
        [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}],
    ]    
'''
input_path = "data\packaging.txt"
output_path = "data\packaging.json"
output = []
with open(input_path, 'r') as f:
    for line in f.readlines():
        package = line.strip()
        parsed = parse_packaging(package)
        output.append(parsed)
        unit = get_unit(parsed)
        total = calc_total_units(parsed)
        print(f"{package} => total units: {total} {unit}")

with open(output_path, 'w') as fout:
    json.dump(output, fout, indent = 4)
        

