
import json
filename = 'country_code.json'

with open('./countries_code.json') as f:
    codeDict = json.load(f)
engDict = {}

for key in codeDict:
    engDict[codeDict[key]] = key

with open(filename, 'w') as json_file:
    json.dump(engDict, json_file)
