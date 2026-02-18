def main():
    # CREATE

    numbers = {2, 3, 2, 5}
    print("Initial Set: ", numbers)

    # ADD
    numbers.add(4)
    print("After adding 4: ", numbers)

    # UPDATE
    numbers.update([5, 6, 7])

    # REMOVE
    numbers.discard(2)

    # CHECK
    print("Is 3 in the set? ", 3 in numbers)
    print("Is 10 in the set? ", 10 in numbers)

    # ITERATE
    for num in numbers:
        print(num)

    # SET OPERATIONS 
    a = {1, 2, 3}
    b = {3, 4, 5}

    print("Union: ", a | b)  # Output: {1, 2, 3, 4, 5}
    print("Intersection: ", a & b)  # Output: {3}
    print("Difference: ", a - b)  # Output: {1, 2}
    print("Symmetric Difference: ", a ^ b)  # Output: {1, 2, 4, 5}

    print("Union using method: ", a.union(b))
    print("Intersection using method: ", a.intersection(b))
    print("Difference using method: ", a.difference(b))
    print("Symmetric Difference using method: ", a.symmetric_difference(b))

if __name__ == "__main__":
    main()

