# 📚 **Comprehensive Amazon Interview Prep CheatSheet**

## Table of Contents
1. [Time Complexity (Big O) Cheat Sheet](#time-complexity-big-o-cheat-sheet)
2. [General DS/A Flowchart](#general-dsa-flowchart)
3. [Sorting Algorithms](#sorting-algorithms)
4. [Interview Stages Cheat Sheet](#interview-stages-cheat-sheet)
5. [Code Templates](#code-templates)
6. [Practice Resources](#practice-resources)

---

## 📊 **Time Complexity (Big O) Cheat Sheet**
![Time Complexity Chart](/Technical%20Prep/Leetcode%20CheatSheet/Time%20complexity%20(Big%20O)%20Chart.png)

### **Common Operations by Data Structure**
#### **Arrays (Dynamic Array/List)**
| Operation                               | Complexity       |
|----------------------------------------|------------------|
| Add/remove element at the end           | O(1) amortized   |
| Add/remove element at arbitrary index   | O(n)             |
| Access/modify element                   | O(1)             |
| Check if element exists                 | O(n)             |
| Build a prefix sum                      | O(n)             |
| Finding sum of a subarray with prefix   | O(1)             |

#### **Strings (Immutable)**
| Operation                               | Complexity       |
|----------------------------------------|------------------|
| Add/remove character                    | O(n)             |
| Access element                          | O(1)             |
| Concatenate two strings                 | O(n + m)         |
| Create substring                        | O(m)             |

#### **Linked Lists**
| Operation                               | Complexity       |
|----------------------------------------|------------------|
| Add/remove element at pointer location  | O(1)             |
| Add/remove element without pointer      | O(n)             |
| Check if element exists                 | O(n)             |
| Reverse a sublist                       | O(j - i)         |
| Detect a cycle (fast/slow pointers)     | O(n)             |

#### **Hash Table/Dictionary**
| Operation                               | Complexity       |
|----------------------------------------|------------------|
| Add/remove key-value pair               | O(1)             |
| Check if key exists                     | O(1)             |
| Check if value exists                   | O(n)             |

#### **Binary Search Tree**
| Operation                               | Complexity       |
|----------------------------------------|------------------|
| Add/Remove element (average)            | O(log n)         |
| Add/Remove element (worst)              | O(n)             |
| Check if element exists                 | O(log n)         |

#### **Heap/Priority Queue**
| Operation                               | Complexity       |
|----------------------------------------|------------------|
| Add an element                          | O(log n)         |
| Delete the minimum element              | O(log n)         |
| Find the minimum element                | O(1)             |

#### **Binary Search**
| Operation                               | Complexity       |
|----------------------------------------|------------------|
| Search                                  | O(log n)         |

---

## 🛠 **General DS/A Flowchart**
![General DS/A Flowchart](/Technical%20Prep/Leetcode%20CheatSheet/General%20DS:A%20flowchart.png)

This flowchart helps decide the **right algorithm or data structure** based on problem requirements.

---

## 🗂 **Sorting Algorithms**
### **Complexity Comparison**
| Algorithm       | Best       | Average    | Worst      | Space | Stable |
|-----------------|------------|------------|------------|-------|--------|
| QuickSort       | O(n log n) | O(n log n) | O(n^2)     | O(log n) | No     |
| MergeSort       | O(n log n) | O(n log n) | O(n log n) | O(n)   | Yes    |
| HeapSort        | O(n log n) | O(n log n) | O(n log n) | O(1)   | No     |
| BubbleSort      | O(n)       | O(n^2)     | O(n^2)     | O(1)   | Yes    |
| InsertionSort   | O(n)       | O(n^2)     | O(n^2)     | O(1)   | Yes    |

![Sorting Algorithms Chart](/Technical%20Prep/Leetcode%20CheatSheet/Sorting%20algorithms.png)

---

## 🚀 **Interview Stages Cheat Sheet**
### **Stage 1: Introductions**
- Rehearse a concise 30-60 second self-introduction.
- Speak confidently and engage actively.

### **Stage 2: Problem Statement**
1. Paraphrase the problem.
2. Clarify input size, edge cases, and invalid inputs.

### **Stage 3: Brainstorming DS&A**
- Think aloud and break the problem into steps.

### **Stage 4: Implementation**
- Write clean, modular code.

### **Stage 5: Testing & Debugging**
- Walk through test cases methodically.

### **Stage 6: Explanations and Follow-ups**
- Be prepared to discuss time and space complexity.

### **Stage 7: Outro**
- Have questions regarding the company prepared.

---

## 🧩 **Code Templates**
### **Two Pointers: One Input, Opposite Ends**
```python
def fn(arr):
    left = ans = 0
    right = len(arr) - 1

    while left < right:
        # do some logic here with left and right
        if CONDITION:
            left += 1
        else:
            right -= 1
    
    return ans
```

### **Two Pointers: Two Inputs, Exhaust Both**
```python
def fn(arr1, arr2):
    i = j = ans = 0

    while i < len(arr1) and j < len(arr2):
        # do some logic here
        if CONDITION:
            i += 1
        else:
            j += 1
    
    while i < len(arr1):
        # do logic
        i += 1
    
    while j < len(arr2):
        # do logic
        j += 1
    
    return ans
```

### **Sliding Window**
```python
def fn(arr):
    left = ans = curr = 0

    for right in range(len(arr)):
        # do logic here to add arr[right] to curr

        while WINDOW_CONDITION_BROKEN:
            # remove arr[left] from curr
            left += 1

        # update ans
    
    return ans
```

### **Build a Prefix Sum**
```python
def fn(arr):
    prefix = [arr[0]]
    for i in range(1, len(arr)):
        prefix.append(prefix[-1] + arr[i])
    
    return prefix
```

### **Efficient String Building**
```python
# arr is a list of characters
def fn(arr):
    ans = []
    for c in arr:
        ans.append(c)
    
    return "".join(ans)
```

### **Linked List: Fast and Slow Pointer**
```python
def fn(head):
    slow = head
    fast = head
    ans = 0

    while fast and fast.next:
        # do logic
        slow = slow.next
        fast = fast.next.next
    
    return ans
```

### **Reversing a Linked List**
```python
def fn(head):
    curr = head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node 
        
    return prev
```

### **Find Number of Subarrays that Fit an Exact Criteria**
```python
from collections import defaultdict

def fn(arr, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in arr:
        # do logic to change curr
        ans += counts[curr - k]
        counts[curr] += 1
    
    return ans
```

### **Monotonic Increasing Stack**
```python
def fn(arr):
    stack = []
    ans = 0

    for num in arr:
        # for monotonic decreasing, just flip the > to <
        while stack and stack[-1] > num:
            # do logic
            stack.pop()
        stack.append(num)
    
    return ans
```

### **Binary Tree: DFS (Recursive)**
```python
def dfs(root):
    if not root:
        return
    
    ans = 0

    # do logic
    dfs(root.left)
    dfs(root.right)
    return ans
```

### **Binary Tree: DFS (Iterative)**
```python
def dfs(root):
    stack = [root]
    ans = 0

    while stack:
        node = stack.pop()
        # do logic
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return ans
```

### **Binary Tree: BFS**
```python
from collections import deque

def fn(root):
    queue = deque([root])
    ans = 0

    while queue:
        current_length = len(queue)
        # do logic for current level

        for _ in range(current_length):
            node = queue.popleft()
            # do logic
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return ans
```

### **Graph: DFS (Recursive)**
```python
def fn(graph):
    def dfs(node):
        ans = 0
        # do some logic
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                ans += dfs(neighbor)
        
        return ans

    seen = {START_NODE}
    return dfs(START_NODE)
```

### **Graph: DFS (Iterative)**
```python
def fn(graph):
    stack = [START_NODE]
    seen = {START_NODE}
    ans = 0

    while stack:
        node = stack.pop()
        # do some logic
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    
    return ans
```

### **Graph: BFS**
```python
from collections import deque

def fn(graph):
    queue = deque([START_NODE])
    seen = {START_NODE}
    ans = 0

    while queue:
        node = queue.popleft()
        # do some logic
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    
    return ans
```

### **Find Top K Elements with Heap**
```python
import heapq

def fn(arr, k):
    heap = []
    for num in arr:
        # do some logic to push onto heap according to problem's criteria
        heapq.heappush(heap, (CRITERIA, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [num for num in heap]
```

### **Binary Search**
```python
def fn(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            # do something
            return
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    # left is the insertion point
    return left
```

### **Binary Search: Duplicate Elements, Left-most Insertion Point**
```python
def fn(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left
```

### **Binary Search: Duplicate Elements, Right-most Insertion Point**
```python
def fn(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left
```

### **Binary Search: For Greedy Problems**
#### If looking for a minimum:
```python
def fn(arr):
    def check(x):
        # this function is implemented depending on the problem
        return BOOLEAN

    left = MINIMUM_POSSIBLE_ANSWER
    right = MAXIMUM_POSSIBLE_ANSWER
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    
    return left
```

#### If looking for a maximum:
```python
def fn(arr):
    def check(x):
        # this function is implemented depending on the problem
        return BOOLEAN

    left = MINIMUM_POSSIBLE_ANSWER
    right = MAXIMUM_POSSIBLE_ANSWER
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    
    return right
```

### **Backtracking**
```python
def backtrack(curr, OTHER_ARGUMENTS...):
    if (BASE_CASE):
        # modify the answer
        return
    
    ans = 0
    for (ITERATE_OVER_INPUT):
        # modify the current state
        ans += backtrack(curr, OTHER_ARGUMENTS...)
        # undo the modification of the current state
    
    return ans
```

### **Dynamic Programming: Top-down Memoization**
```python
def fn(arr):
    def dp(STATE):
        if BASE_CASE:
            return 0
        
        if STATE in memo:
            return memo[STATE]
        
        ans = RECURRENCE_RELATION(STATE)
        memo[STATE] = ans
        return ans

    memo = {}
    return dp(STATE_FOR_WHOLE_INPUT)
```

### **Build a Trie**
```python
class TrieNode:
    def __init__(self):
        # you can store data at nodes if you wish
        self.data = None
        self.children = {}

def fn(words):
    root = TrieNode()
    for word in words:
        curr = root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        # at this point, you have a full word at curr
        # you can perform more logic here to give curr an attribute if you want
    
    return root
```

### **Dijkstra's Algorithm**
```python
from math import inf
from heapq import *

distances = [inf] * n
distances[source] = 0
heap = [(0, source)]

while heap:
    curr_dist, node = heappop(heap)
    if curr_dist > distances[node]:
        continue
    
    for nei, weight in graph[node]:
        dist = curr_dist + weight
        if dist < distances[nei]:
            distances[nei] = dist
            heappush(heap, (dist, nei))
```

---

## 🌟 **Practice Resources**
- [LeetCode CheatSheets](https://leetcode.com/explore/interview/card/cheatsheets/720/resources/4723/)

---

**Happy Studying! 🚀**