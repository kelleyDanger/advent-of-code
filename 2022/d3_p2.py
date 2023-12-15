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

i = 0
while i < len(rucksacks):
    # read lines in groups of 3
    g1 = rucksacks[i].strip()
    g2 = rucksacks[i+1].strip()
    g3 = rucksacks[i+2].strip()

    # common item between all 3 group is badge
    badge = set(g1).intersection(g2).intersection(g3)
    print(f"badge: {badge}")
    priority = priority_dict.get(badge.pop())
    item_priorities.append(priority)

    # loop through next 3 lines
    i += 3


print(item_priorities)
total_item_priorities = sum(item_priorities)
print(f" total item priorities: {total_item_priorities}")






