from collections import Counter

log_data = """1.1.2014 12:01,111-222-333,454-333-222,COMPLETED
1.1.2014 13:01,111-222-333,111-333,FAILED
1.1.2014 13:04,111-222-333,454-333-222,FAILED
1.1.2014 13:05,111-222-333,454-333-222,COMPLETED
2.1.2014 13:01,111-333,111-222-333,FAILED
"""

print(log_data)

lines = log_data.split('\n')

completed_ocurrences = []
all_ocurrences = []

for line in lines:
    if len(line) > 0:
        line_data = line.split(',')

        # adds ocurrence to completed call list
        if line_data[-1] == 'COMPLETED':
            completed_ocurrences.append(line_data[1])
            completed_ocurrences.append(line_data[2])

        all_ocurrences.append(line_data[1])
        all_ocurrences.append(line_data[2])

# counts number of times each number appears in the list
completed_dict = dict(Counter(completed_ocurrences))
all_dict = dict(Counter(all_ocurrences))

print('Completed ocurrences: \n{}\n'.format(completed_dict))
print('All ocurrences: \n{}\n'.format(all_dict))

result = {}

for k in all_dict:
    if k in completed_dict:
        percentage = float(completed_dict[k]) / float(all_dict[k]) * 100
        result[k] = '{:.2f}%'.format(percentage)
    else:
        result[k] = '0.00%'

print('Result:')
print(result)
