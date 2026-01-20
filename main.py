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

def main():
    sorter = SortingClass()  # create instance
    while True:
        sorter.parsingInput()
        sorter.insertionSort()
        sorter.bubbleSort()

if __name__ == "__main__":
    main()
