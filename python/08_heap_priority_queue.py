import heapq

def main():

    heap = [] 

    # PUSH 
    heapq.heappush(heap, 5)
    heapq.heappush(heap, 2)
    heapq.heappush(heap, 8)

    # PEEK
    print("Smallest element in heap:", heap[0])

    # POP 
    while heap:
        print("Popped element:", heapq.heappop(heap))

if __name__ == "__main__":
    main()