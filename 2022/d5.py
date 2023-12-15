# --- Day 5: Supply Stacks ---
# The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

# The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

# The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

# They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:



# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

# Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

# [D]        
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

#         [Z]
#         [N]
#     [C] [D]
#     [M] [P]
#  1   2   3
# Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

#         [Z]
#         [N]
# [M]     [D]
# [C]     [P]
#  1   2   3
# Finally, one crate is moved from stack 1 to stack 2:

#         [Z]
#         [N]
#         [D]
# [C] [M] [P]
#  1   2   3
# The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

# After the rearrangement procedure completes, what crate ends up on top of each stack?


# create initial stack columns
## data struct: [ [stack1], [stack2], [stack3] ]


import re

SAMPLE_INPUT = [
"    [D]    ",
"[N] [C]    ",
"[Z] [M] [P]",
" 1   2   3 ",
"",
"move 1 from 2 to 1",
"move 3 from 1 to 3",
"move 2 from 2 to 1",
"move 1 from 1 to 2",
]


# questions: 
## will there always be a crate at the top of each stack? if not, how should we represent?
## will it always start with a crate in each stack?
def solve(lines: list) -> str: 
    """
    Returns string of characters representing crates on the top of each stack

    Parameters:
    lines: list of strings, representing starting stack and instructions

    Return:
    result: str of characters representing crates on top of each stack
    """


    # Find where empty line separates starting_stack and instructions
    int_line_break = 0
    for index, line in enumerate(lines):
        if line == "" or line == "\n":
            int_line_break = index
            break


    # Create crate_stacks
    num_of_stacks = int(max( lines[int_line_break - 1] ))
    crate_stacks = []
    for n in range(num_of_stacks):
        crate_stacks.append([])


    # Add crates crate stacks
    i = int_line_break - 2 # read bottom to top so bottom crates are first in stack
    while i >= 0:
        crates = list(lines[i])
        # loop through every 4 character (end of crate)
        # check 2 back to find either letter or whitespace 
        # add to crate_stacks
        # "    [D]    " ----[D]----
        # "[N] [C]    " [N]-[C]----
        # "[Z] [M] [P]" [Z]-[M]-[P]
        start = 3
        stop = len(crates) + 1
        step = 4
        stack = 0
        for n in range(start, stop, step):
            crate = crates[n-2]
            if crate != ' ':
                crate_stacks[stack].append(crate)
            stack += 1
        i-=1


    # Loop through instructions
    i = int_line_break + 1
    while i < len(lines):
        # pop off the end of the "from" stack and append to the end of the "to" stack n number of times
        # where n is "move n"
        # crate_stacks: [['Z', 'N', 'D'], ['M', 'C'], ['P']]
        # "move 3 from 1 to 3",
        # "move 2 from 2 to 1",
        # "move 1 from 1 to 2",
        instruction_string = lines[i]
        how_many, from_stack, to_stack = list(map(lambda x: int(x), re.findall("\d{1,2}", instruction_string) ))
        print(f"how_many: {how_many}, from_stack: {from_stack}, to_stack: {to_stack}")
        ## PART 1
        # for n in range(how_many):
        #     crate = crate_stacks[int(from_stack) - 1].pop()
        #     crate_stacks[int(to_stack) - 1].append(crate)
        ## PART 2
        # ability to pick up and move multiple crates at once
        while how_many > 0:
            stack = crate_stacks[int(from_stack) - 1] #['Z', 'N', 'D']
            which_index = len(stack) - how_many
            print(f"crate_stacks: {crate_stacks}")
            print(f"which index: {which_index}")
            crate = crate_stacks[int(from_stack) - 1].pop(which_index)
            crate_stacks[int(to_stack) - 1].append(crate)
            how_many -= 1

        i+=1

    print(f"all moved, crate_stacks: {crate_stacks}")

    # When at end, loop through starting stack, pop off crate representing top of stack
    top_crates = ""
    for n in range(num_of_stacks):
        top_crate = crate_stacks[n].pop()
        top_crates += top_crate


    print(f"top_crates: {top_crates}")

# test = solve(SAMPLE_INPUT)

f = open("d5.txt", "r")
p1_lines = f.readlines()
part_1 = solve(p1_lines)



# --- Part Two ---
# As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

# Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

# The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

# Again considering the example above, the crates begin in the same configuration:

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# Moving a single crate from stack 2 to stack 1 behaves the same as before:

# [D]        
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

#         [D]
#         [N]
#     [C] [Z]
#     [M] [P]
#  1   2   3
# Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

#         [D]
#         [N]
# [C]     [Z]
# [M]     [P]
#  1   2   3
# Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

#         [D]
#         [N]
#         [Z]
# [M] [C] [P]
#  1   2   3
# In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

# Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?