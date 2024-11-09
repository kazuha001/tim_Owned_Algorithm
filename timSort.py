

def tim_arrays():

    tim_arrays = []

    tim_arrays1 = []

    input_number = input("Enter Number Seperated with Comas: ")


    numbers = input_number.split(",")

    for num in numbers:
        tim_arrays.append(int(num.strip()))

    for index in range(len(tim_arrays)):
        tim_arrays1.append(index)

    for index1 in range(len(tim_arrays1)):
        
        print(index1)
    
    print(tim_arrays)
    print(tim_arrays1)


tim_arrays()
