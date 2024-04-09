
with open('dna.txt', 'r') as f:
    count_dict = {}
    count = 0
    for line in f:
        line.replace("\n", "")
        for i in line:
            if i not in count_dict:
                count_dict[i] = 1
                count += 1
            elif i in count_dict:
                count_dict[i] += 1
                count += 1

print("Total length:" )