def profile(name, *args, **kwargs):
    print(f"Name: {name}")
    print("Tags (args):", args)
    for k, v in kwargs.items():
        print(f"Details ({k}): {v}")

profile("Alice", "coder", "junior", age=25, city="NY")