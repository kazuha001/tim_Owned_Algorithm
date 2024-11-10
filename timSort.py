
# Demo Version By Cordy of tim sorting

def tim_arrays():

    tim_arrays = []

    tim_arrays_elements = []

    tim_arrays_collect1 = []

    tim_arrays_collect2 = []

    tim_arrays_final_sort = []

    input_number = input("Enter Number Seperated with Comas: ")

    print("Your Elements is ", input_number)

    numbers = input_number.split(",")

    # Loopers
    for num in numbers:

        tim_arrays.append(int(num.strip()))

    for index in range(len(tim_arrays)):

        tim_arrays_elements.append(index)

    # Conditional
    if index <= 5:

        # First Process the minimun of 3 elements and sort
        tim_arrays_collect1_process = tim_arrays[0:3]

        for run in tim_arrays_collect1_process:

            tim_arrays_collect1.append(run)

        # Second Process the Last Unsorted Elements and sort
        tim_arrays_collect2_process = tim_arrays[3:6]

        for run in tim_arrays_collect2_process:

            tim_arrays_collect2.append(run)

        # Fast Method of Sorting Mechanism

        tim_arrays_collect1.sort()

        print("1st run ",tim_arrays_collect1)
        
        tim_arrays_collect2.sort()

        print("Sorting the Remains",tim_arrays_collect2)

        # Final Output

        for final in tim_arrays_collect1:
            
            tim_arrays_final_sort.append(final)
        
        for final in tim_arrays_collect2:
            
            tim_arrays_final_sort.append(final)

        print("Combined: ", tim_arrays_final_sort)

        tim_arrays_final_sort.sort()

        print("Sorted: ", tim_arrays_final_sort)


    else:

        print("Only 6 elments")

tim_arrays()
