# Design and Analysis of Algorithms Lab

This repository contains implementations of various algorithms as part of the Design and Analysis of Algorithms laboratory course. The implementations are in Python and cover a range of fundamental algorithms and data structures.

## Contents

### Sorting Algorithms

- **Merge Sort (k-way)**: [`merge_sort.py`](merge_sort.py) - Implements k-way merge sort algorithm
- **Quick Sort**: [`quickSort.py`](quickSort.py) - Classic quicksort implementation

### Mathematical Algorithms

- **Fast Modular Exponentiation**:
  - [`fastmodular.py`](fastmodular.py) - Recursive implementation
  - [`fastmodularitr.py`](fastmodularitr.py) - Iterative implementation

### Graph Algorithms

- **Kruskal's Algorithm**: [`kruskalAlgo.py`](kruskalAlgo.py) - Minimum Spanning Tree implementation using Disjoint Set Union

### Combinatorial Problems

- **Josephus Problem**:
  - [`josephusarray.py`](josephusarray.py) - Array-based solution
  - [`josephuslinkedlist.py`](josephuslinkedlist.py) - Linked list-based solution
- **Permutations**:
  - [`goodpermutation.py`](goodpermutation.py) - Generates derangements (permutations with no fixed points)
  - [`maxUpdates.py`](maxUpdates.py) - Calculates max updates in permutations
  - [`permutationComplexity.py`](permutationComplexity.py) - Analyzes permutation complexity

### Dynamic Programming

- **Maximum Subarray Sum**: [`largestblocksum.py`](largestblocksum.py) - Implements brute force and Kadane's algorithm
- **Longest Increasing Subsequence**: [`long_subsequence.py`](long_subsequence.py) - Finds LIS using patience sorting

### Other Algorithms

- **Majority Element**: [`majorityElement.py`](majorityElement.py) - Implements brute force, sorting, and Boyer-Moore voting methods

## Usage

Each algorithm is implemented in its own Python file. To run any algorithm:

```bash
python3 filename.py
```

Most files include example usage within the code and will output results when executed.

## Requirements

- Python 3.x
- No external dependencies required

## Key Implementations

### Kruskal's Algorithm

- Uses Disjoint Set Union with path compression and union by rank
- Efficiently finds Minimum Spanning Tree

### Josephus Problem

- Two implementations (array and linked list) showing different approaches
- Simulates the elimination process

### Fast Modular Exponentiation

- Both recursive and iterative implementations
- Efficiently computes large powers modulo _n_

### Longest Increasing Subsequence

- Implements patience sorting algorithm
- Reconstructs the actual subsequence

### Majority Element

- Three different approaches with varying time complexities
- Includes the efficient Boyer-Moore voting algorithm

## Author

**Leevan Herald**
