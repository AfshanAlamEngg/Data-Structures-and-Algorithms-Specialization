# Comparison of Greedy Algorithm, Divide and Conquer, and Dynamic Programming

## 1. Problem-Solving Approach
- **Greedy Algorithm**: Makes the locally optimal choice at each step, aiming for a globally optimal solution.
- **Divide and Conquer**: Breaks problems into independent sub-problems, solves them recursively, and combines solutions.
- **Dynamic Programming**: Tackles overlapping sub-problems by storing intermediate results for reuse.

## 2. Sub-problem Dependency
- **Greedy Algorithm**: Often doesn't split the problem into sub-problems and relies on immediate decisions rather than dependency.
- **Divide and Conquer**: Sub-problems are independent.
- **Dynamic Programming**: Sub-problems are dependent, requiring solutions to earlier sub-problems.

## 3. Efficiency
- **Greedy Algorithm**: Usually efficient, but may not always lead to the optimal solution.
- **Divide and Conquer**: Can be less efficient due to recomputation in overlapping sub-problems.
- **Dynamic Programming**: Highly efficient due to memoization or tabulation.

## 4. Example Algorithms
- **Greedy Algorithm**: Dijkstra's algorithm, Huffman coding, Kruskal’s Minimum Spanning Tree.
- **Divide and Conquer**: Merge Sort, Quick Sort, Binary Search.
- **Dynamic Programming**: Knapsack problem, Fibonacci sequence, Longest Common Subsequence.

## 5. Use Case
- **Greedy Algorithm**: Works best for problems where locally optimal decisions lead to the globally optimal solution.
- **Divide and Conquer**: Suitable for problems with independent sub-problems.
- **Dynamic Programming**: Ideal for overlapping sub-problems and optimal substructure.
