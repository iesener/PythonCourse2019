import re

# open text file of 2008 NH primary Obama speech
with open("obama-nh.txt", "r") as f:
	obama = f.readlines()


## TODO: print lines that do not contain 'the' using what we learned
## (although you ~might~ think you could do something like
## [l for l in obama if "the" not in l]

keyword = re.compile(r"the[a-z]*")

for i, line in enumerate(obama):
  if not keyword.search(line):
    print(line) 
 


# TODO: print lines that contain a word of any length starting with s and ending with e

pattern = re.compile(r'\b[s]\w+[e]\b')
for i, line in enumerate(obama):
	if pattern.search(line):
		print(line)



## TODO: Print the date input in the following format
## Month: MM
## Day: DD
## Year: YY
date = r"Please enter a date in the format 08.14.19: "
only_date = re.findall(r"\d{2}.\d{2}.\d{2}", date)
mdy = re.split(r'\.', only_date[0])
print("Month: %s\n Day: %s\n Year: %s" %(mdy[0], mdy[1], mdy[2]))






