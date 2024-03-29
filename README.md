# algorithm_python
this repository is about algorithm implementation by python.<br/>more detail description: [https://hey-stranger.tistory.com](https://hey-stranger.tistory.com/category/Computer%20Science/algorithms)
<br/>

### contents
- sorting
- divide-and-conquer
- dynamic programming
- greedy algorithm
- graph algorithm
<br/>

## 0. sorting
주어진 배열을 오름차순(내림차순)으로 정렬하는 문제이다.
- selection sort [[code]](https://github.com/gompaang/algorithm_python/blob/master/selection_sort.py)
- insertion sort [[code]](https://github.com/gompaang/algorithm_python/blob/master/insertion_sort.py)
- quick sort [[code]](https://github.com/gompaang/algorithm_python/blob/master/quick_sort.py) , [[python easy ver.]](https://github.com/gompaang/algorithm_python/blob/master/quick_sort_python.py)
- merge sort
- count sort [[code]](https://github.com/gompaang/algorithm_python/blob/master/count_sort.py)
<br/>

## 1. divide-and-conquer
주어진 문제를 **분할**(divide)하고, **해결**(conquer)하여 결과들을 다시 **합**(combine)하는 방식이다.<br/> 주로, recursive 재귀를 사용하여 구현한다.
- binary search : compare mid  [[code]](https://github.com/gompaang/algorithm_python/blob/master/binary_search.py)
- merge sort 
- quick sort : pivot, recursive  [[code]](https://github.com/gompaang/algorithm_python/blob/master/quick_sort.py)
<br/>


## 2. dynamic programming
주어진 문제를 한 번만 풀도록 하는 방식이다. <br/>큰 문제를 sub-problem으로 나눌 수 있으며, sub-problem을 해결한 정답이 큰 문제에서도 동일하다. <br/>dynamic programming 과 divide-and-conquer 의 가장 큰 차이점은 sub-problem의 **중복여부** 이다.
- Fibonacci numbers : recursive, memoization(top-down), for문(bottom-up) [[code]](https://github.com/gompaang/algorithm_python/blob/master/fibonacci.py)
- shortest paths (Floyd-Warshall)
- longest increasing subsequences
- edit distance
- knapsack
- chain matrix multiplication
- independent sets in trees
<br/>


## 3. greedy algorithm
매 순간마다의 최선의 선택을 하는 방식이다. <br/>매 순간마다의 최선의 선택을 한 것이 최종적인 전체 선택을 보았을 때 최선의 선택이 되는지는 정확하지 않다. greedy algorithm 으로 최적의 솔류션을 도출하는 문제들이 있다.
- MST (Minimum Spanning Tree)
  - Kruskal's algorithm : priority queue - heap [[code]](https://github.com/gompaang/algorithm_python/blob/master/kruskal.py)
  - Prim's algorithm
- Huffman-encoding
<br/>


## 4. graph algorithm
- graph traversal
  - DFS (Depth-first search) : stack  [[code]](https://github.com/gompaang/algorithm_python/blob/master/depth_first_search.py) , recusive [[code]](https://github.com/gompaang/algorithm_python/blob/master/dfs.py)
  - BFS (Bredth-first search) : queue  [[code]](https://github.com/gompaang/algorithm_python/blob/master/bfs.py)
- shortest path
  - Dijkstra's algorithm : greedy (priority queue - heap)  [[code]](https://github.com/gompaang/algorithm_python/blob/master/dijkstra.py)
  - Bellman-Ford's algorithm : include negative edges  [[code]](https://github.com/gompaang/algorithm_python/blob/master/bellman_ford.py)
  - Floyd-Warshall's algorithm : dynamic programming
<br/>
