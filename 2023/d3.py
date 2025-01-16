# <!-- --- Day 3: Gear Ratios ---
# You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

# It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

# "Aaah!"

# You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

# The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

# The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

# Here is an example engine schematic:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

# Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
#  -->

import re


def parse_engine_schematic(grid):
    # 467..114..
    part_numbers = []
    
    for row, line in enumerate(grid):
        start = 0
        end = 0
        col = 0
        digit_s = ""
        valid_part = False

        while col < len(line):
            c = line[col]
             
            if c.isdigit(): 
                digit_s += c
            elif (c == "." and digit_s) or col == len(line) - 1:
                # look diagonally above, below, left, and right for symbol
                start = col - len(digit_s) - 1
                end = col + 1
                print(f"row: {row}, col: {col}, len(digit_s): {len(digit_s)}, digit_s: {digit_s}, start: {start}, end: {end}")
                if row > 0:
                    above = grid[row - 1][start:end]
                    if bool(re.search(r'[^0-9.]', ''.join(above))):
                        valid_part = True
                if row < len(grid) - 1:
                    below = grid[row + 1][start:end]
                    if bool(re.search(r'[^0-9.]', ''.join(below))):
                        valid_part = True
                if start > 0:
                    left = grid[row][start-1]
                    if bool(re.search(r'[^0-9.]', ''.join(left))):
                        valid_part = True
                if end < len(line) - 1:
                    right = grid[row][end+1]
                    if bool(re.search(r'[^0-9.]', ''.join(right))):
                        valid_part = True

                # we only want to add part once
                if valid_part:
                    print(f"adding part: {digit_s}")
                    part_numbers.append(int(digit_s))
                    valid_part = False

                # reset digit_s
                digit_s = ""
            
            # increase col
            col += 1
                
            
    print(f"Part Numbers: {part_numbers}")
    print(f"Sum Part Numbers: {sum(part_numbers)}")


if __name__ == "__main__":
    with open('d3.txt', 'r') as file:
        grid = [list(line.strip()) for line in file]
    parse_engine_schematic(grid)
    
