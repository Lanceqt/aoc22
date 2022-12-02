# with open("./aoc22/1/input.txt") as f:
#    for line in f:
#        print(line.strip())
#
# if __name__ == "__main__":
#    print("default")
# else:
#    print("Error")

# open AI solution below

# Read the input and split it into a list of strings
with open("./aoc22/1/input.txt") as f:
    lines = f.readlines()

# Initialize variables to keep track of the current Elf and the maximum total number of Calories seen so far
current_elf = 1
max_calories = 0
total_calories = 0

# Iterate over the list of strings
for line in lines:
    # If the current string is a blank line, move on to the next Elf
    if line == "":
        current_elf += 1
        total_calories = 0
    else:
        # Remove the newline character from the end of the current string
        line = line.rstrip()

        # Convert the current string to an integer and add it to the total number of Calories carried by the current Elf
        total_calories += int(line)

# Print the result
print(f"Elf {current_elf} is carrying the most Calories ({total_calories}).")
