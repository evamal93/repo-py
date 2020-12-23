file_name = "task6.txt"

subjects = {}

try:
    with open(file_name, 'r') as f:
        for line in f.readlines():
            data = line.replace('(', ' ').split()

            subjects[data[0][:-1]] = sum(
                int(i) for i in data if i.isdigit()
            )
except IOError as e:
    print(e)

print(subjects)
