import string

def read_file_lines(path):
    f = open(path, "r")
    lines = f.readlines()
    f.close()
    return lines

def create_priority_dict() -> dict:
    alphabet = list(string.ascii_letters)
    priority_dict = {}
    for index, char in enumerate(alphabet):
        priority_dict[char] = index + 1
    return priority_dict


rucksacks = read_file_lines("d3.txt")
item_priorities = []
priority_dict= create_priority_dict()
for rucksack in rucksacks:
    middle_item = int(len(rucksack.strip())/2)
    left_items = rucksack[:middle_item]
    right_items = rucksack[middle_item:]

    duplicates = set(left_items).intersection(set(right_items))
    print(f"duplicates: {duplicates}")
    for item in duplicates:
        p = priority_dict[item]
        print(f"item: {item}, priority: {p}")
        item_priorities.append(p)

print(item_priorities)
total_item_priorities = sum(item_priorities)
print(f" total item priorities: {total_item_priorities}")






