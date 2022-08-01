from collections import defaultdict
"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

telephone_numbers = defaultdict(lambda: 0)
for call in calls:
    duration = int(call[3])
    incoming_number = call[0]
    answering_number = call[1]
    telephone_numbers[incoming_number] += duration
    telephone_numbers[answering_number] += duration

number_longest_time_spent = max(telephone_numbers, key=telephone_numbers.get)
print(f"{number_longest_time_spent} spent the longest time, {telephone_numbers[number_longest_time_spent]}" \
        "seconds, on the phone during  September 2016.")