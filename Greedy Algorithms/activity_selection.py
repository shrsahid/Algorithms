def activity_selection(start,finish):
    n = len(start)

    print("Selected Activities: ")

    i= 0
    print("A1\n",end="")

    for j in range(1,n):
        if start[j]>=finish[i]:
            print(f"A{j+1}\n",end="")
            i=j

start  = [1, 2, 3, 0, 5, 8]
finish = [3, 4, 5, 7, 8, 9]

activity_selection(start, finish)