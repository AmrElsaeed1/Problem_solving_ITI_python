def get_numbers_from_user():
    numbers=[]
    max_invalid_attempts = 5 
    for i in range(5):
        invalid_attempts = 0
        while True:
            try:
                num=int(input(f"please enter number {i+1} of 5 "))
                numbers.append(num)
                break
            except ValueError:
                invalid_attempts+=1
                if invalid_attempts >= max_invalid_attempts:
                    raise("you've reached the maximum tries")
                print("Invalid input, please enter a valid number. ")
            except error as e:
                print(e)
        
                
                
    return numbers
        
def sort_list():
    numbers=get_numbers_from_user()
    ascending_numbers = sorted(numbers)
    descending_numbers = sorted(numbers, reverse=True)

    print("\nSorting Results:")
    print(f"Ascending order:  {ascending_numbers}")
    print(f"Descending order: {descending_numbers}")
