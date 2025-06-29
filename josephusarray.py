def josephus(n):
    people = [i for i in range(1, n + 1)]  # Create an array of people
    turn = False  # Boolean to track whether to remove or rotate

    while len(people) > 1:
        if turn:
            people.pop(0)  # Remove the first person
        else:
            people.append(people.pop(0))  # Move the first person to the end
        turn = not turn  # Toggle turn

    return people[0]  # Return the last remaining person


if __name__ == "__main__":
    for i in range(2, 26):
        print(f"n={i}, Josephus = {josephus(i)}")
