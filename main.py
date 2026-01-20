class SortingClass:
    def __init__(self):
        self.Narr = [5,4,3,2,1]  # store parsed array here, default 5,4,3,2,1

    def parsingInput(self):
        input_str = input("Input numbers, separated by space: ")
        self.Narr = [int(x) for x in input_str.split()]
        
    def callingArr(self):
        return self.Narr
    
    def bubbleSort(self):
        # Analogy: Comparing each of the adjacent element group by group
        # If the current "Bubble" have the situation where the next is smaller
        # then the current element, then proceed to swap them
        # Key Note: A, B = B, A is swapping in place
        arr = self.Narr
        for j in range(len(arr)-1):
            for i in range(len(arr)-1-j):
                if arr[i]>arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
        print(f"Bubble Sort: {arr}")
        
    def insertionSort(self):
        # Analogy: Pick a key, compare and sort, until everything is in place
        # Then pick the key next to one, repeating the process
        # Important Concept: If key<compare, shift right
        # Else, insert the key into the current comparing element
        arr = self.Narr
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while arr[j]>key and j>=0:
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = key
        print(f"Insertion Sort: {arr}")
        
    def selectionSort(self):
        # Selection sort is like arranging books on a shelf by repeatedly finding the thinnest book left.
        # You scan the remaining pile without moving anything.
        # Once the smallest book is identified, you place it in the next empty spot on the shelf.
        # The sorted section grows, and the search space shrinks, one book at a time.
        arr = self.Narr
        for i in range(len(arr)-1):
            min_index = i
            for j in range(i+1,len(arr)):
                if arr[min_index] >arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Selection Sort: {arr}")

def main():
    sorter = SortingClass()  # create instance
    while True:
        sorter.parsingInput()
        sorter.insertionSort()
        sorter.bubbleSort()
        sorter.selectionSort()

if __name__ == "__main__":
    main()
