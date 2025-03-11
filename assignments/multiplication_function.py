def mul(number):
    for i in range(1, number + 1):
        print("i,",i)
        for j in range(1, i + 1):
            print("j",j)
            product = i * j
            print(f"{i} x {j} = {product}")
        print("-" * 10)  # Add a separator after each row
