"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


unique_numbers = set()
for text in texts:
    incoming_number = text[0]
    unique_numbers.add(incoming_number)
    answering_number = text[1]
    unique_numbers.add(answering_number)


for call in calls:
    incoming_number = call[0]
    unique_numbers.add(incoming_number)
    answering_number = call[1]
    unique_numbers.add(answering_number)

bangalore_fixed_lines = [
    number for number in unique_numbers if number.startswith("(080)")
]

area_codes_bangalore = set()
for call in calls:
    incoming_number = call[0]
    if incoming_number.startswith("(080)"):
        answering_number = call[1]
        if "(" in answering_number:
            area_code = re.findall("\(.*?\)", answering_number)[0]
            area_codes_bangalore.add(area_code)
        elif " " in answering_number:
            area_codes_bangalore.add(answering_number[:4])
        else:
            area_codes_bangalore.add("140")


sorted_list = sorted(area_codes_bangalore)
print("The numbers called by people in Bangalore have codes:")
for number in sorted_list:
    print(number)


total_answering_bangalore_calls = 0
total_incoming_bangalore_calls = 0
for call in calls:
    incoming_number = call[0]
    if incoming_number in bangalore_fixed_lines:
        total_incoming_bangalore_calls += 1
        answering_number = call[1]
        if answering_number in bangalore_fixed_lines:
            total_answering_bangalore_calls += 1

percentage = 100 * total_answering_bangalore_calls / total_incoming_bangalore_calls
print(
    f"{percentage:.2f} percent of calls from fixed lines in Bangalore are calls "
    "to other fixed lines in Bangalore."
)
