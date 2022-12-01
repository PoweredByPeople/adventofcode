""" Solution idea:
Process each line, sum each until you reach a blank line. Then compare the sum
to the max and keep going. """



def single_elf():
    with open('levels/level1/level1data.txt') as input:
        max_calories = 0
        line = input.readline()
        elf_calories = 0

        while line != '': # The EOF char is an empty string
            if line == "\n":
                #print(f"Current elf_calories is {elf_calories}. Current max_calories is {max_calories}. Updating max_calories if necessary.")
                max_calories = max(max_calories, elf_calories)
                elf_calories = 0
                line = input.readline()

            else:
                #print(line, end='')
                elf_calories += int(line)
                line = input.readline()
        
        #print(f"Current elf_calories is {elf_calories}. Current max_calories is {max_calories}. Updating max_calories if necessary.")
        max_calories = max(max_calories, elf_calories)
        

    print(f"Max calories brought by any elf was: {max_calories}!")


def three_elves():
    with open('levels/level1/level1data.txt') as input:
        total_calories = 0
        line = input.readline()
        elf_calories = 0
        calories_list = []

        while line != '': # The EOF char is an empty string
            if line == "\n":
                #print(f"Current elf_calories is {elf_calories}. Current max_calories is {max_calories}. Updating max_calories if necessary.")
                calories_list.append(elf_calories)
                #max_calories = max(max_calories, elf_calories)
                elf_calories = 0
                line = input.readline()

            else:
                #print(line, end='')
                elf_calories += int(line)
                line = input.readline()
        
        calories_list.sort(reverse=True)
        total_calories = sum(calories_list[:3])
        #print(f"Current elf_calories is {elf_calories}. Current max_calories is {max_calories}. Updating max_calories if necessary.")
        #max_calories = max(max_calories, elf_calories)
        

    print(f"Total calories brought by the top three elves was: {total_calories}!")

single_elf()
three_elves()

