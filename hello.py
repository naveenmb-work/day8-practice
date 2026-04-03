def greet(name):
    if not name:
        print("Name cannot be empty")
    else:
        print(f"Hello, {name}!")

name = input("Enter your name: ").strip()
greet(name)
