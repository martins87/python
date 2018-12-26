from collections import Counter

log_data = """1.1.2014 12:01,111-222-333,454-333-222,COMPLETED
1.1.2014 13:01,111-222-333,111-333,FAILED
1.1.2014 13:04,111-222-333,454-333-222,FAILED
1.1.2014 13:05,111-222-333,454-333-222,COMPLETED
2.1.2014 13:01,111-333,111-222-333,FAILED
"""

print(log_data)

lines = log_data.split('\n')

completed_occurrences = []
all_occurrences = []

for line in lines:
    if len(line) > 0:
        line_data = line.split(',')

        # adds occurrence to completed call list
        if line_data[-1] == 'COMPLETED':
            completed_occurrences.append(line_data[1])
            completed_occurrences.append(line_data[2])

        all_occurrences.append(line_data[1])
        all_occurrences.append(line_data[2])

# counts number of times each number appears in the list
completed_dict = dict(Counter(completed_occurrences))
all_dict = dict(Counter(all_occurrences))

print('Completed occurrences: \n{}\n'.format(completed_dict))
print('All occurrences: \n{}\n'.format(all_dict))

result = {}

for k in all_dict:
    if k in completed_dict:
        # gets success ratio
        percentage = float(completed_dict[k]) / float(all_dict[k]) * 100
        result[k] = '{:.2f}%'.format(percentage)
    else:
        result[k] = '0.00%'

print('Result:')
print(result)
