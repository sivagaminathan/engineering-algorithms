def main():
    # CREATE
    numbers = (1, 2, 3, 4, 5, 2)
    print(numbers)  # Output: (1, 2, 3, 4, 5)  

    # ACCESS 
    print("First element: ", numbers[0])  # Output: 1
    print("Last element: ", numbers[-1])  # Output: 2

    # COUNT 
    print("Count of 2: ", numbers.count(2))  # Output: 2
    # INDEX 
    print("Index of 3: ", numbers.index(3))  # Output: 2

    # ITERATE 
    for num in numbers:
        print(num)  # Output: 1 2 3 4 5 2

    # RETURNING MULTIPLE VALUES
    
    print("Min and Max of numbers:", min_max(numbers))  # Output: (1, 5)

def min_max(nums):
        return min(nums), max(nums)
    
if __name__ == "__main__":
    main()
    