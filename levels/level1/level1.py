""" Solution idea:
Process each line, sum each until you reach a blank line. Then compare the sum
to the max and keep going. """

max_calories = 0

with open('levels/level1/level1data.txt') as input:
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

