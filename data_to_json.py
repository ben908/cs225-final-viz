import json
import re

new_filename = "data1-cleaned-small.json"

data = {}
data['nodes'] = []
data['links'] = []

groups = set()
group_names = { }

all_nodes = set()
added_nodes = set()

identifier = re.compile(r'^(https:\/\/courses\.engr\.illinois\.edu\/cs225\/fa2021\/+([\-_a-zA-Z]*\/+[\-_a-zA-Z0-9]*))')

raw_data_files = ["data1.txt", "data2.txt"]

for old_filename in raw_data_files:
    with open(old_filename, "r") as f:
        lines = f.readlines()

        for line in lines:
            main_info = line.split(": ")
            rest = main_info[1].split(", ")

            source = main_info[0].strip().strip("/").strip("\\").strip(",")
            if "doxygen" in source:
                continue
            if match := identifier.search(source):
                    start, end = match.groups()
                    groups.add(end)
            

            all_nodes.add(source)
            for link in rest:
                target = link.strip().strip("/").strip("\\").strip(",")
                if match := identifier.search(target):
                    start, end = match.groups()
                    groups.add(end)

                all_nodes.add(target)
                data['links'].append({
                    "source": source,
                    "target": target,
                    "value": 1 
                })

print("Read all Data")

for i, group_name in enumerate(groups):
    group_names[group_name] = i + 1

print(group_names)

for node in all_nodes:
    group = 0
    if match := identifier.search(node):
                start, end = match.groups()
                group = group_names[end]

    data['nodes'].append({
        "id": node,
        "group": group
    })

data_formatted = json.dumps(data, indent=4)

with open(new_filename, "w") as f:
    print(data_formatted, file = f)