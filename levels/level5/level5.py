"""
Day 5

stack_1 = deque("SCVN")
stack_2 = deque("ZMJHNS")
stack_3 = deque("MCTGJND")
stack_4 = deque("TDFJWRM")
stack_5 = deque("PFH")
stack_6 = deque("CTZHJ")
stack_7 = deque("DPRQFSLZ")
stack_8 = deque("CSLHDFPW")
stack_9 = deque("DSMPFNGZ")

def organize_crates(number_of_crates, from_stack_crates, to_stack_crates):

    Function will process a single line of instruction.
    from_stack_queue = deque(from_stack_crates)
    to_stack_queue = deque(to_stack_crates)

    while number_of_crates > 0:
        to_stack_queue.append(from_stack_queue.pop())
        number_of_crates -= 1
    
    updated_from_stack_crates = ''.join(from_stack_queue)
    updated_to_stack_crates = ''.join(to_stack_crates)
    
    updated_crates = [updated_from_stack_crates, updated_to_stack_crates]

    return updated_crates
"""
from collections import deque




def rearragement(filename):
    """
    Define all beginning stacks, call organize crates for each line, then print out the last element
    from each stack at the end. 
    """
    stacks = {
    "stack_1": "SCVN",
    "stack_2": "ZMJHNS",
    "stack_3": "MCTGJND",
    "stack_4": "TDFJWRM",
    "stack_5": "PFH",
    "stack_6": "CTZHJ",
    "stack_7": "DPRQFSLZ",
    "stack_8": "CSLHDFPW",
    "stack_9": "DSMPFNGZ",
    }

    replacements = [
        ("move", ""),
        (" ", ""),
        ("from", ","),
        ("to", ","),
        ("\n", "")
    ]

    with open(filename, encoding="utf-8") as input_data:
        line = input_data.readline()
        
        while line != "":
            for old, new in replacements:
                # We need to handle double digit crate movements
                line = line.replace(old, new)
            line = line.split(",")
            number_of_crates = int(line[0])
            from_stack = "stack_" + line[1]
            to_stack = "stack_" + line[2]
            from_stack_crates = stacks[from_stack]
            to_stack_crates = stacks[to_stack]
            from_stack_queue = deque(from_stack_crates)
            to_stack_queue = deque(to_stack_crates)

            while number_of_crates > 0:
                to_stack_queue.append(from_stack_queue.pop())
                number_of_crates -= 1
            
            updated_from_stack_crates = ''.join(from_stack_queue)
            updated_to_stack_crates = ''.join(to_stack_queue)
            
            stacks[from_stack] = updated_from_stack_crates
            stacks[to_stack] = updated_to_stack_crates


            line = input_data.readline()

    #print(stacks)
    answer = ""
    for crates in stacks.values():
        answer += crates[-1]
    
    print(answer)


def rearragement_part2(filename):
    """
    Define all beginning stacks, call organize crates for each line, then print out the last element
    from each stack at the end. 
    """
    stacks = {
    "stack_1": "SCVN",
    "stack_2": "ZMJHNS",
    "stack_3": "MCTGJND",
    "stack_4": "TDFJWRM",
    "stack_5": "PFH",
    "stack_6": "CTZHJ",
    "stack_7": "DPRQFSLZ",
    "stack_8": "CSLHDFPW",
    "stack_9": "DSMPFNGZ",
    }
    replacements = [
        ("move", ""),
        (" ", ""),
        ("from", ","),
        ("to", ","),
        ("\n", "")
    ]

    with open(filename, encoding="utf-8") as input_data:
        line = input_data.readline()
        
        while line != "":
            for old, new in replacements:
                # We need to handle double digit crate movements
                line = line.replace(old, new)
            line = line.split(",")
            number_of_crates = int(line[0])
            from_stack = "stack_" + line[1]
            to_stack = "stack_" + line[2]
            from_stack_crates = stacks[from_stack]
            to_stack_crates = stacks[to_stack]
            from_stack_queue = deque(from_stack_crates)
            to_stack_queue = deque(to_stack_crates)

            crates_to_move = []
            while number_of_crates > 0:
                crates_to_move += from_stack_queue.pop()
                number_of_crates -= 1
            crates_to_move.reverse()
            to_stack_queue.extend(crates_to_move)

            updated_from_stack_crates = ''.join(from_stack_queue)
            updated_to_stack_crates = ''.join(to_stack_queue)
            
            stacks[from_stack] = updated_from_stack_crates
            stacks[to_stack] = updated_to_stack_crates


            line = input_data.readline()

    #print(stacks)
    answer = ""
    for crates in stacks.values():
        answer += crates[-1]
    
    print(answer)

rearragement("levels/level5/movement.txt")
rearragement_part2("levels/level5/movement.txt")