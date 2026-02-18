def main():
    # CREATE
    student = {
        "name": "Siva",
        "age": 30,
        "languages": ["Python", "Java"]
    }

    # READ
    print(student["name"])  # Output: Siva
    print(student.get("age"))  # Output: 30 
    print(student.get("languages"))

    # UPDATE
    student["age"] = 31
    print(student["age"])  # Output: 31

    # DELETE a key
    student.pop("age")
    print(student)  # Output: {'name': 'Siva', 'age':

    # APPEND value to list in dictionary
    student["languages"].append("C++")
    print(student["languages"])  # Output: ['Python', 'Java', 'C++

    # ITERATE
    for key, value in student.items():
        print(f"{key}: {value}")

    # LENGTH 
    print(len(student))  # Output: 2

if __name__ == "__main__":
    main()