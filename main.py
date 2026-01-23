class SortingClass:
    import random
    import time
    
    def __init__(self):
        self.Narr = [5,4,3,2,1]  # store parsed array here, default 5,4,3,2,1

    def parsingInput(self):
        input_str = input("Input numbers, separated by space (or a single number >=100 to auto-generate): ")
        
        # If the input is a single number
        if input_str.strip().isdigit() and int(input_str) >= 100:
            # Generate random numbers
            input_str = self.generatingInput(int(input_str))
        
        # Parse input (space-separated numbers)
        self.Narr = [int(x) for x in input_str.split()]

    def callingArr(self):
        return self.Narr
    
    def generatingInput(self, noOfInput):
        numbers = [str(self.random.randint(1, 10000)) for _ in range(noOfInput)]
        output = " ".join(numbers)
        return output
 
    def selectionSort(self, arr):
        # Selection sort is like arranging books on a shelf by repeatedly finding the 
        # thinnest book left. You scan the remaining pile without moving anything.
        # Once the smallest book is identified, you place it in the next empty spot on
        # the shelf. The sorted section grows, and the search space shrinks, one book 
        # at a time.
        # Start Timer
        start = self.time.time()
        for i in range(len(arr)-1):
            min_index = i
            for j in range(i+1,len(arr)):
                if arr[min_index] >arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
         # Display Result
        if len(arr) <= 30:
            end = self.time.time()
            print(f"Selection Sort: {arr}", end = ", ")
            print(f"Time taken: {end-start:.6f} seconds\n")
        else:
            end = self.time.time()
            print(f"Selection Sort -> Time taken: {end-start:.6f} seconds\n")
 
    def insertionSort(self, arr):
        # Analogy: Pick a key, compare and sort, until everything is in place
        # Then pick the key next to one, repeating the process
        # Important Concept: If key<compare, shift right
        # Else, insert the key into the current comparing element
        # Start Timer
        start = self.time.time()
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while arr[j]>key and j>=0:
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = key
        # Display Result
        if len(arr) <= 30:
            end = self.time.time()
            print(f"Insertion Sort: {arr}", end = ", ")
            print(f"Time taken: {end-start:.6f} seconds\n")
        else:
            end = self.time.time()
            print(f"Insertion Sort -> Time taken: {end-start:.6f} seconds\n")

    def bubbleSort(self, arr):
        # Analogy: Comparing each of the adjacent element group by group
        # If the current "Bubble" have the situation where the next is smaller
        # then the current element, then proceed to swap them
        # Key Note: A, B = B, A is swapping in place
        # Start Timer
        start = self.time.time()
        for j in range(len(arr)-1):
            for i in range(len(arr)-1-j):
                if arr[i]>arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
        # Display Result
        if len(arr) <= 30:
            end = self.time.time()
            print(f"Bubble Sort: {arr}", end = ", ")
            print(f"Time taken: {end-start:.6f} seconds\n")
        else:
            end = self.time.time()
            print(f"Bubble Sort -> Time taken: {end-start:.6f} seconds\n")

    def mergeSort(self, arr):
        # Merge sort will fist spliting/slicing the array into each sub-array until
        # the each of the array contains 1 element only. Then, by merging those seperated 
        # array, they will be put together back from pieces, meanwhile comparing the size 
        # and sort. Notice that this function will be used as a recursive one. By that we
        # means that the function will be call by its own under certain condition.
        # Start Timer
        start = self.time.time() if len(arr) == len(self.callingArr()) else None
        # Best case, return the array as given
        if len(arr) == 1:
            return arr
        # Spliting process, and throw the array to lower level recursion
        # Get the array back in the sorted splited format
        mid = len(arr) // 2
        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])
        # Sorting Mechanism happens here
        i = j = 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i+=1
            else:
                merged.append(right[j])
                j+=1
        # Append any leftovers
        merged.extend(left[i:])
        merged.extend(right[j:])
        # Display Result
        if len(merged) == len(self.callingArr()) and len(arr) <= 30:
            end = self.time.time()
            print(f"Merge Sort: {merged}", end=", ")
            print(f"Time taken: {end-start:.6f} seconds\n")
        elif len(arr) == len(self.callingArr()):
            end = self.time.time()
            print(f"Merge Sort -> Time taken: {end-start:.6f} seconds\n")
        else:
            None

        # Sorting finish
        return merged
        
def main():
    sorter = SortingClass()  # create instance
    while True:
        sorter.parsingInput()
        sorter.selectionSort(sorter.callingArr())
        sorter.insertionSort(sorter.callingArr())
        sorter.bubbleSort(sorter.callingArr())
        sorter.mergeSort(sorter.callingArr())

if __name__ == "__main__":
    main()
