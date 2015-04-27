import re
import json

filename = "wildlife viewing site list.txt"
output_file = "initial_data.json"
output = []

def determine_true(c):
    if c != '' and c in 'Xx':
        return True

    return False

def determine_values(array):
    facilities = []

    for i in range(0, len(array)):
        if determine_true(array[i]):
            facilities.append(i+1)
    return facilities

with open(filename, 'r') as f:
    file_content = f.read()
    file_content = re.split('\r|\n', file_content)


    header = file_content[0].split('\t')

    # Facility Types in Columns 7-19
    count = 1
    for i in range(7, 20):
        obj = {
            "pk": count,
            "model": "facilities.Facility",
            "fields": {
                "name": header[i].capitalize()
            }
        }
        output.append(obj)
        count += 1

    count = 1

    # Animal Types in columns 21-38
    for i in range(21, 39):
        obj = {
            "pk": count,
            "model": "animals.Animal",
            "fields": {
                "name": header[i].capitalize()
            }
        }
        output.append(obj)
        count += 1

    # Columns:
    # 0 - Complete
    # 1 - Name
    # 2 - Owner
    # 3 - Phone Number
    # 4 - Link
    # 5 - Latitude
    # 6 - Longitude
    # 7 - 19 - Facilities
    # 20 - Fee
    # 21 - 38 - Animals
    # 39 - ADA

    count = 1
    for line in file_content[1:]:
        line = line.split('\t')

        if line[0] == '' or line[0] not in 'Yy':
            continue

        if line[5] == '' or line[6] == '':
            continue
        
        obj = {
            "pk": count,
            "model": "viewingsites.ViewSite",
            "fields": {
                "name": line[1],
                "latitude": float(line[5]),
                "longitude": float(line[6]),
                "owner": line[2],
                "owner_link": line[4],
                "telephone": line[3],
                "fee": determine_true(line[20]),
                "ada": determine_true(line[39]),
                "facilities": determine_values(line[7:20]),
                "animals": determine_values(line[21:39]),
                "publish": True
            }
        }

        output.append(obj)
        count += 1


with open(output_file, 'w') as f:
    f.write(json.dumps(output, indent=4))