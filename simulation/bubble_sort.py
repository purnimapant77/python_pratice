# Bubble Sort Simulation

def bubble_sort_simulation():

    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements: ").split()))[:n]

    original = arr.copy()

    total_comparisons = 0
    total_swaps = 0
    pass_count = 0

    print("\nOriginal Array:", arr)

    for i in range(n-1):
        pass_count += 1
        swapped = False
        comp_pass = 0
        swap_pass = 0

        print("\nPass", pass_count)

        for j in range(0, n-i-1):
            total_comparisons += 1
            comp_pass += 1

            print("Compare", arr[j], "and", arr[j+1], end=" -> ")

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                total_swaps += 1
                swap_pass += 1
                swapped = True
                print("Swap:", arr)
            else:
                print("No Swap:", arr)

        print("End of pass", pass_count, ":", arr)
        print("Comparisons:", comp_pass, "Swaps:", swap_pass)

        if not swapped:
            print("No swaps in this pass. Array already sorted.")
            break

    print("\nOriginal Array:", original)
    print("Sorted Array:", arr)

    print("\nTotal Passes:", pass_count)
    print("Total Comparisons:", total_comparisons)
    print("Total Swaps:", total_swaps)
    print("Time Complexity: O(n^2)")

bubble_sort_simulation()