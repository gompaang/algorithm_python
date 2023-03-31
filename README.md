# algorithm_python
this repository is about algorithm implementation by python.<br/>more detail description: [https://hey-stranger.tistory.com](https://hey-stranger.tistory.com/category/Computer%20Science/algorithms)
<br/>
### contents
- divide-and-conquer
- graph algorithm
- greedy algorithm
- dynamic programming
<br/>


## 1. divide-and-conquer
주어진 문제를 **분할**(divide)하고, **해결**(conquer)하여 결과들을 다시 **합**(combine)하는 방식이다.<br/> 주로, recursive 재귀를 사용하여 구현한다.
### binary search
- binary search : compare mid  [[code]](https://github.com/gompaang/algorithm_python/blob/master/binary_search.py)
### sort
- merge sort 
- quick sort : pivot, recursive  [[code]](https://github.com/gompaang/algorithm_python/blob/master/quick_sort.py)
### etc
- Fibonacci numbers
<br/>

## 2. graph algorithm
- search
  - Depth-first search (DFS) : stack  [[code]](https://github.com/gompaang/algorithm_python/blob/master/depth_first_search.py)
  - Bredth-first search (BFS) : queue  [[code]](https://github.com/gompaang/algorithm_python/blob/master/breadth_first_search.py)
- shortest path
  - Dijkstra's algorithm : shortest path (priority queue - heap)  [[code]](https://github.com/gompaang/algorithm_python/blob/master/dijkstra.py)
  - Bellman-Ford's algorithm : shortest path (include negative edges)  [[code]](https://github.com/gompaang/algorithm_python/blob/master/bellman_ford.py)
<br/>

## 3. greedy algorithm
- MST (Minimum Spanning Tree)
  - Kruskal's algorithm : priority queue - heap [[code]](https://github.com/gompaang/algorithm_python/blob/master/kruskal.py)
  - Prim's algorithm
- Huffman-encoding
<br/>

## 4. dynamic programming
주어진 문제를 한 번만 풀도록 하는 방식이다. <br/>하나의 문제를 sub-problem으로 계속해서 쪼개어 가장 작은 sub-probelm을 해결하여 최종적인 problem이 해결되는 방식이다.
- shortest paths in dags
- longest increasing subsequences
- edit distance
- knapsack
- chain matrix multiplication
- independent sets in trees
<br/>

