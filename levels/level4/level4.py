"""
Day 4!
"""

def assignment_overlap(filename):
    """
    Part 1: Open the file, process each line and turn each range into a list of integers.
    Then check if either list is entirely contained in the other.
    """

    with open(filename, encoding="utf-8") as input_data:
        line = input_data.readline()
        overlap = 0

        while line != '':
            elf_1, elf_2 = line.split(',')
            elf_1 = elf_1.split("-")
            elf_2 = elf_2.split("-")
            elf_1_range = []
            elf_2_range = []

            for i in range(int(elf_1[0]), int(elf_1[1]) + 1):
                elf_1_range.append(i)

            for i in range(int(elf_2[0]), int(elf_2[1]) + 1):
                elf_2_range.append(i)

            if set(elf_1_range).issubset(elf_2_range) or set(elf_2_range).issubset(elf_1_range):
                overlap += 1

            line = input_data.readline()

    print(f"Part 1 answer: {overlap}.")

def assignment_overlap_any(filename):
    """
    Part 1: Open the file, process each line and turn each range into a list of integers.
    Then check if either list is entirely contained in the other.
    """

    with open(filename, encoding="utf-8") as input_data:
        line = input_data.readline()
        overlap = 0

        while line != '':
            elf_1, elf_2 = line.split(',')
            elf_1 = elf_1.split("-")
            elf_2 = elf_2.split("-")
            elf_1_range = []
            elf_2_range = []

            for i in range(int(elf_1[0]), int(elf_1[1]) + 1):
                elf_1_range.append(i)

            for i in range(int(elf_2[0]), int(elf_2[1]) + 1):
                elf_2_range.append(i)

            if (set(elf_1_range).intersection(elf_2_range) 
            or set(elf_1_range).intersection(elf_2_range)):
                overlap +=1

            line = input_data.readline()

    print(f"Part 2 answer: {overlap}.")


assignment_overlap("levels/level4/level4data.txt")
assignment_overlap_any("levels/level4/level4data.txt")
