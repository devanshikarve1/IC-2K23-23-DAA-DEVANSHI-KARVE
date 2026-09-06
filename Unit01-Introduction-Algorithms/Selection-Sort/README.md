# Selection Sort

## Problem Statement
Implement Selection Sort to sort an array of elements in ascending order.

## Algorithm / Approach
1. Start from the first element of the array.
2. Find the smallest element in the unsorted part of the array.
3. Swap the smallest element with the first element of the unsorted part.
4. Repeat the process until the complete array is sorted.

## Pseudocode
1. For i = 0 to n-2:
2. Set minIndex = i
3. For j = i+1 to n-1:
4. If arr[j] < arr[minIndex], update minIndex = j
5. Swap arr[i] and arr[minIndex]
6. Stop when the array is sorted.

## Time and Space Complexity
- Best Case: O(n²)
- Average Case: O(n²)
- Worst Case: O(n²)
- Space Complexity: O(1)

## Sample Input
5
64 25 12 22 11

## Sample Output
11 12 22 25 64

## Screenshots / Graphs
Add screenshots of the program execution here.

## Experimental Results
Execution results can be recorded for different input sizes.

## Learning Outcomes
- Understand the Selection Sort algorithm.
- Learn how to select the minimum element from an unsorted array.
- Understand time and space complexity.
- Implement a reusable sorting function in C++.
