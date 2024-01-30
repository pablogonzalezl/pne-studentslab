def fibon(n):
    list = []
    for i in range(12):
        if len(list) < 11:
            if len(list) < 2:
                list.append(i)
                print(i)
            else:
                variable = list[i - 1] + list[i - 2]
                list.append(variable)
                print(variable)