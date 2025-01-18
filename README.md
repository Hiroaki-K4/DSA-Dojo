# DSA-Dojo
[Cracking the coding interview](https://www.crackingthecodinginterview.com/) is very good book to learn algorithms and data structures for coding interviews.
In this repository, I have implemented basic problems introduced in that book using python.

<br></br>

# Problems List
The image below shows the minimum knowledge that we should acquire for coding interviews.

<img src="resources/cracking.png" width='600'>

## Bit Manipulation
### Get Bit
This method shifts 1 over by i bits, creating a value that looks like 00010000. By performing an AND with num, we clear all bits other than the bit at bit i. Finally, we compare that to 0. If that new value is not zero, then bit i must have a 1. Otherwise, bit i is a 0.

### Set Bit
Set Bit shifts 1 over by i bits, creating a value like 00010000. By performing an OR with num, only the value at bit i will change. All other bits of the mask are zero and will not affect num.

### Clear Bit
This method operates in almost the reverse of setBi t. First, we create a number like 11101111 by creating the reverse of it (00010000) and negating it. Then, we perform an AND with num. This will clear the ith bit and leave the remainder unchanged.

#### clearBitsMSBthroughI
To clear all bits from the most significant bit through i (inclusive), we create a mask with a 1 at the ith bit (1 << i). Then, we subtract 1 from it, giving us a sequence of 0s followed by i ls. We then AND our number with this mask to leave just the last i bits.

#### clearBitsithrough0
To clear all bits from i through 0 (inclusive), we take a sequence of all ls (which is -1) and shift it left by i + 1 bits. This gives us a sequence of 1 s (in the most significant bits) followed by i 0 bits.

### Update Bit
To set the ith bit to a valuev, we first clear the bit at position i by using a mask that looks like 11101111.
Then, we shift the intended value, v, left by i bits. This will create a number with bit i equal to v and all other bits equal to 0. Finally, we OR these two numbers, updating the ith bit if vis 1 and leaving it as 0 otherwise.

<br></br>

## Math and Logic Puzzles
### Checking for Primality
The task is to determine whether the given number is a prime number.

### Check Prime Numbers
The task is to count the prime numbers less than the given number.

<br></br>

## Recursion and Dynamic Programming
### Bottom-Up Approach
The bottom-up approach is often the most intuitive. We start with knowing how to solve the problem for a simple case, like a list with only one element. Then we figure out how to solve the problem for two elements, then for three elements, and so on. The key here is to think about how you can build the solution for one case off of the previous case (or multiple previous cases).

### Top-Down Approach
The top-down approach can be more complex since it's less concrete. But sometimes, it's the best way to think about the problem.

<br></br>

## Sorting and Searching
### Bubble Sort | Runtime: $O(n^2)$ average and worst case. Memory: $O(1)$.
In bubble sort, we start at the beginning of the array and swap the first two elements if the first is greater than the second. Then, we go to the next pair, and so on, continuously making sweeps of the array until it is sorted. In doing so, the smaller items slowly"bubble" up to the beginning of the list.

### Selection Sort | Runtime: $O(n^2)$ average and worst case. Memory: $O(1)$.
Selection sort is the child's algorithm: simple, but inefficient. Find the smallest element using a linear scan and move it to the front (swapping it with the front element). Then, find the second smallest and move it, again doing a linear scan. Continue doing this until all the elements are in place.

### Merge Sort | Runtime: $O(n\log(n))$ average and worst case. Memory: Depends.
Merge sort divides the array in half, sorts each of those halves, and then merges them back together. Each of those halves has the same sorting algorithm applied to it. Eventually, you are merging just two single­ element arrays. It is the "merge" part that does all the heavy lifting.

### Quick Sort | Runtime: $O(n\log(n))$ average, $O(n^2)$ worst case. Memory: $O(\log(n))$.
In quick sort we pick a random element and partition the array, such that all numbers that are less than the partitioning element come before all elements that are greater than it. The partitioning can be performed efficiently through a series of swaps.

### Binary Search
In binary search, we look for an element x in a sorted array by first comparing x to the midpoint of the array.
If xis less than the midpoint, then we search the left half of the array. If x is greater than the midpoint, then we search the right half of the array. We then repeat this process, treating the left and right halves as subar­ rays. Again, we compare x to the midpoint of this subarray and then search either its left or right side. We repeat this process until we either find x or the subarray has size 0.

<br></br>

## Arrays and Strings
## Linked List
## Stack and Queue
## Trees and Graphs
## Object Oriented Design
