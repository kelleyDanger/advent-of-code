# After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

# The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

# To save your vacation, you need to get all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

# For example, suppose your expense report contained the following:

# 1721
# 979
# 366
# 299
# 675
# 1456
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

# Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

# --- Part Two ---
# The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

# Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

# In your expense report, what is the product of the three entries that sum to 2020?

class Day1():

    def part1(self):
        f = open("d1.txt", "r")
        data = {}
        for line in f:
            data[int(line)] = True

        for key in data.keys():
            diff = 2020 - key
            if diff in data.keys():
                print(key*diff)

    def part2(self):
        f = open("d1.txt", "r")
        data = {}
        for line in f:
            data[int(line)] = True

        # two pointers
        #[1721, 979, 366, 299, 675, 1456, ....]
        # 1721 + 979 + x, 1721 + 366 + x, 1721 + 366 + x....
        keys = list(data.keys())
        print(keys)
        for k1 in range(len(keys)):
            for k2 in range(1, len(keys)):
                key1 = keys[k1]
                key2 = keys[k2]
                diff = 2020 - key1 - key2
                print(f"key1: {key1}, key2: {key2}, diff: {diff}")
                if diff in data.keys():
                    print(key1*key2*diff)
                    return


if __name__ == "__main__":
    day = Day1()
    part1 = day.part1()
    part2 = day.part2()