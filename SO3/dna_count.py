sequence = input("Introduce the sequence:").upper()

print("Total length:", len(sequence))

count_dict = {}
for i in sequence:
    if i not in count_dict:
        count_dict[i] = 1
    elif i in count_dict:
        count_dict[i] += 1

for key, value in count_dict.items():
    print(key, ":", value)
