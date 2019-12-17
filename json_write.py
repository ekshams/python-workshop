# write data to json file
import json

my_data = ["orange","apple","banana"]

with open("test.json","w") as file:
    json.dump(my_data, file)
    
file.close()