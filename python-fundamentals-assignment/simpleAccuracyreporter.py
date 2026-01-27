try:
    x=float(input("Please enter a floating-point accuracy value  "))
    print(f"Model accuracy is {x}")
except ValueError as e:
    print(e)