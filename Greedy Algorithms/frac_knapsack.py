def frac_knapsack(values,weights,capacity):
    items=[]

    for i in range(len(values)):
        ratio=values[i] / weights[i]
        items.append((ratio,values[i],weights[i]))

    items.sort(reverse=True)

    total_profit=0

    for ratio,value,weight in items:
        if capacity >= weight:
            capacity -= weight
            total_profit += value

        else:
            total_profit += value * (capacity/weight)
            break
    return total_profit
    
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print("Maximum Profit =", frac_knapsack(values,weights,capacity))