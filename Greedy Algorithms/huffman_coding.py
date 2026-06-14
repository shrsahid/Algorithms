import heapq
def huffman(freq):
    heap = [[weight,[char,""]] for char,weight in freq.items()]
    heapq.heapify(heap)

    while len(heap)>1:
        low1=heapq.heappop(heap)
        low2=heapq.heappop(heap)

        for pair in low1[1:]:
            pair[1]='0' + pair[1]

        for pair in low2[1:]:
            pair[1]= '1'+ pair[1]

        heapq.heappush(
            heap,[low1[0]+low2[0]]+low1[1:]+low2[1:]
        )
    return sorted (heap[0][1:],key=lambda p: (len(p[1]),p))
freq = {
    'A': 5,
    'B': 9,
    'C': 12,
    'D': 13,
    'E': 16,
    'F': 45
}

codes = huffman(freq)

for char, code in codes:
    print(char, ":", code)