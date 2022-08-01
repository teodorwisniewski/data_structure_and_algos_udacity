"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

possible_normal_numbers = set()
for text in texts:
    incoming_number = text[0]
    possible_normal_numbers.add(incoming_number)
    answering_number = text[1]
    possible_normal_numbers.add(answering_number)

for call in calls:
    answering_number = call[1]
    possible_normal_numbers.add(answering_number)

possible_telemarketers_numbers = set()
for call in calls:
    incoming_number = call[0]
    if incoming_number not in possible_normal_numbers:
        possible_telemarketers_numbers.add(incoming_number)

sorted_list = sorted(possible_telemarketers_numbers)
print("These numbers could be telemarketers: ")
for number in sorted_list:
    print(number)
