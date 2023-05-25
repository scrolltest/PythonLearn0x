with open("output.txt", "w") as file:
    print("Hello", "World", sep="-", end="!", file=file, flush=True)
