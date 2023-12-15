# --- Day 1: Trebuchet?! ---
# Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

# You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?


# 9sixsevenz3
# seven1cvdvnhpgthfhfljmnq
# 6tvxlgrsevenjvbxbfqrsk4seven
# 9zml


import re

def find_calibration_values(lines: list[str]) -> int:
	calibration_numbers = []

	for line in lines:
		left=0
		right=len(line)-1
		r_decimal = "\d"

		first_left = 0
		first_right = 0

		# 52sevenone
		while (left<len(line)-1) and (right>=0) and not (first_left and first_right):
			left_decimal = re.match(r_decimal, line[left])
			right_decimal = re.match(r_decimal, line[right])

			# 1 2
			if left_decimal and not first_left:
				first_left = line[left]

			if right_decimal and not first_right:
				first_right = line[right]

			left += 1
			right -= 1
				
		if not first_right:
			calibration_num = int(f"{first_left}{first_left}") 
		else:
			calibration_num = int(f"{first_left}{first_right}")
		calibration_numbers.append(calibration_num)

	print(f"calibration_numbers: {calibration_numbers}")
	return sum(calibration_numbers)

def is_written_number(s: str, d: dict) -> str:
	answer = ""

	for k in d.keys():
		x = re.search(k, s)
		if x:
			answer = x.group()

	return answer
			

def find_calibration_values_2(lines: list[str]) -> int:
	d = {
		"one": 1,
		"two": 2,
		"three": 3,
		"four": 4,
		"five": 5,
		"six": 6,
		"seven": 7, 
		"eight": 8,
		"nine": 9
	}
	longest_number_length = 0
	for k in d.keys():
		longest_number_length = max(longest_number_length, len(k))
	print(f"longest_number_length: {longest_number_length}")

	calibration_numbers = []

	for line in lines:
		# two1nine
		# eightwothree
		# 4nineeightseven2
		# 7pqrstsixteen
		# 1six5
		left = right = 0
		nums = []
		curr = ""

		while left in range(len(line)) and right in range(len(line)):
			curr += line[right]
			print(f"left: {left}, right: {right}, curr: {curr}")

			if line[right].isdigit():
				nums.append(line[right])
				curr=""
				left+=1

			written_number = is_written_number(curr, d)
			if written_number:
				nums.append(d[written_number])
				left = right
				#eightfour2fourvzksqhxmlkpkfktmdzpmthreetwonehv
				# left: 38, right: 41, curr: etwo
				# left: 41, right: 42, curr: on
				# left: 41, right: 43, curr: one
				curr=line[left] 

			# hit the end of window [left....end_of_line]
			# no words found, move left, reset right 
			if right-left > longest_number_length:
				left+=1
				right=left
				curr=""
			else:
				right += 1

		
		if len(nums) >= 2:
			cal_num = int(f"{nums[0]}{nums[-1]}")
		else:
			cal_num = int(f"{nums[0]}{nums[0]}")
		calibration_numbers.append(cal_num)

	for index, value in enumerate(calibration_numbers):
		print(f"{value} | {lines[index]}")
	return sum(calibration_numbers)

			
if __name__ == "__main__":
	f = open("d1.txt")
	lines = f.readlines()
	# calibration_values = find_calibration_values(lines)
	# print("PART 1")
	# print(calibration_values)

	print("PART 2")
	calibration_values = find_calibration_values_2(lines)
	print(calibration_values)



# PART 2
#Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.



