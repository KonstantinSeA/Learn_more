line = input()
a, b, c = map(int, list(line))
if len(set(a, b, c)) != 3):
    print(len(data) - len(set(data)) + 1)
elif '0' in line:
    print(max(data) - min(data))
else:
    print(data[0] * data[1] * data[2])
