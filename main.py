n = int(input())

data = []
front = end = front_rev = end_rev = 0

for i in range(n):
    data.append(input())

for i, dishes in enumerate(data):
    master = []
    for j in range(1, len(dishes)):
        front = dishes[:j]
        end = dishes[j:]
        front_rev = front[::-1]
        end_rev = end[::-1]
        #print("{} | {} | {} | {}".format(front, end, front_rev, end_rev))

        master.append(front + end)
        master.append(end + front)
        master.append(front_rev + end)
        master.append(end + front_rev)
        master.append(front + end_rev)
        master.append(end_rev + front)
        master.append(front_rev + end_rev)
        master.append(end_rev + front_rev)


    print(len(list(set(master))))