# MSCS 532 Alorithms and Data Structure

## Shrisan Kapali

## Student Id : 005032249

### Assignment 3 - Understanding Algorithm Efficiency and Scalability

To run the program, on the terminal run the following command

```
py MSCS_532_assignment4.py
```

### Summary of Quicksort analysis

While sorting 500000 records when the array was in sorted order, the randomized quicksort took around 0.69 seconds and when sorting 500000 records that were in reverse sorted order, the randomized quicksort took about 0.69 seconds.

However, when only 20000 records that were already sorted was sorted using deterministic quicksort where the first element was always chosen as pivot, it took 6.48 seconds and almost same time for when the initial array list was reverse sorted.

From this we can conclude that quicksort using randomized pivot has the average time complexity of O(nlogn) and avoid worst case time complexity O(n^2) which may not be avoided in the deterministic quicksort for cases when the array is already in sorted order.
