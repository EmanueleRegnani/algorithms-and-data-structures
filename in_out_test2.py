# Read the first line to determine the number of following lines
num_lines = int(input())

# Initialize an empty list to store the lines
lines = []

# Read each line and append it to the list
for _ in range(num_lines):
    line = input()
    lines.append(line)

# Now, lines[] contains all the lines entered by the user.
# You can process them as needed. Below is just a sample of how you might print them:

for line in lines:
    print(f"Processed line: {line}")
