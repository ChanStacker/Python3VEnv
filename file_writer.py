import os
print("Let's start")
file = r"C:\Users\chann\Documents\Source\Experimental\files\TheStory.txt"
print(file)

with open(file, "w") as f:
    content = f.readlines()

for line in content:
    print(line)

print("The end")