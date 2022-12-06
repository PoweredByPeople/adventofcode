""" Solution ideas.

For each line in the file, split it into two down the middle, then compare the 
compartments and identify which letter is in both and then sum the priorities. 

We'll need two lists to hold the compartment data and a dictionary to store the 
priorty values to return and then sum. 
"""
import string

def sum_priorties(filename):
    total = 0
    compartment_1 = []
    compartment_2 = []
    lowercase_dict = dict(zip(string.ascii_lowercase, range(1, 27)))
    uppercase_dict = dict(zip(string.ascii_uppercase, range(27, 53)))

    with open(filename) as input:
        line = input.readline()

        while line != '':
            midpoint = len(line)//2
            compartment_1 = line[:midpoint]
            compartment_2 = line[midpoint:-1]
            print(compartment_1, compartment_2)
            matching_item = ''.join(set(compartment_1).intersection(compartment_2))
            print(matching_item)

            if matching_item in lowercase_dict.keys():
                priority = lowercase_dict[matching_item]
                print(priority)
                total += priority
                line = input.readline()
            else:
                priority = uppercase_dict[matching_item]
                print(priority)
                total += priority
                line = input.readline() 

    print(f"The sum of the priorities is {total}.")


def sum_badege_priorties(filename):
    total = 0
    lowercase_dict = dict(zip(string.ascii_lowercase, range(1, 27)))
    uppercase_dict = dict(zip(string.ascii_uppercase, range(27, 53)))

    with open(filename) as input:
        input = input.read().splitlines()
        i, j = 0, 3

        while j <= len(input):
            elf_1 = input[i]
            elf_2 = input[i + 1]
            elf_3 = input[i + 2]


            matching_1 = ''.join(set(elf_1).intersection(elf_2))
            matching_item = ''.join(set(matching_1).intersection(elf_3))
            #print(matching_item)

            if matching_item in lowercase_dict.keys():
                priority = lowercase_dict[matching_item]
                #print(priority)
                total += priority
            else:
                priority = uppercase_dict[matching_item]
                #print(priority)
                total += priority

        
            i += 3
            j += 3

    print(f"The sum of the priorities is {total}.")

#sum_priorties("levels/level3/level3data.txt")
sum_badege_priorties("levels/level3/level3data.txt")