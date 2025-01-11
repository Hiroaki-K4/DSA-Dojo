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
## Recursion and Dynamic Programming
## Sorting and Searching
## Arrays and Strings
## Linked List
## Stack and Queue
## Trees and Graphs
## Object Oriented Design
