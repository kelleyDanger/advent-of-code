# open file, read lines
# add calories to current count
# if line is newline/blank, get max of currentCount, increment elf id

# question: do all elves have at least 1 item?
# question: are there always at least 1 elf?
# question: there is no possibility of a negative-calorie food item?
# question: what if there is a tie for calories?

f = open("d1.txt", "r")
lines = f.readlines()

result = {"elf": 0, "calories": 0}
current_elf_id = 0;
current_calories = 0;

for line in lines:
	print(line);
	if line == "\n":
		# new high score!
		if (current_calories >= result["calories"] ):
			result["calories"] = current_calories;
			result["elf"] = current_elf_id;
		current_elf_id += 1;
		current_calories = 0;
	else:
		current_calories += int(line);
print(result)

f.close()

#{'elf': 169, 'calories': 69883}

# --- Part Two ---
# By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

# To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

# In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

# now, i can compare current_calories to min( result.keys() ). As long as current is bigger than the weakest link, you can substitue into top 3.

f = open("d1.txt", "r")
lines = f.readlines()

#result = {"elf": 0, "calories": 0}
current_elf_id = 0;
current_calories = 0;
result = {current_elf_id: current_calories}

for line in lines:
	if line == "\n":
		# new high score!
		# if (current_calories >= result["calories"] ):
		if len(result.keys()) < 3:
			result[current_calories] = current_elf_id;
		else:
			weakest_top_three_calories = min(result.keys());

			if (current_calories >=  weakest_top_three_calories):
				# result["calories"] = current_calories;
				# result["elf"] = current_elf_id;
				result.pop(weakest_top_three_calories);
				result[current_calories] = current_elf_id;

		current_elf_id += 1;
		current_calories = 0;
	else:
		current_calories += int(line);
print(result.items())
print(sum(result.keys()))
print(result)

f.close()
