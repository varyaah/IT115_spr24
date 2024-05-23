import json

#create data dictionary
data = {

    'name': 'John Doe',
    'age': 30,
    'city': 'New York, NY',
    'interests': ['Golf','Running','Football','Traveling'],
    'is_student': False


}
with open('data.json','w') as json_file:
#opens a file named data.json in write mode
	json.dump(data,json_file,indent=4)
#json.dump is a function from json module used to format python objects to json format
print("Data has been written to data.json")

with open('data.json', 'r') as json_file:
	loaded_data = json.load(json_file)

#indicates it was able to read the json file, loaded_data prints json data
print("Successfully able to read data.json")
print(loaded_data)

loaded_data['age'] = 34
loaded_data['interests'].append('History')

#rewriting changes to the json file
with open('data.json', 'w') as json_file:
	
    json.dump(loaded_data,json_file,indent=4)
	
print("data has been re-written to data.json")
	