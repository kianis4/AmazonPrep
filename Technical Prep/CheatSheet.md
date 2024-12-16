# 📚 **Comprehensive Amazon Interview Prep CheatSheet**

## Table of Contents
1. [Time Complexity (Big O) Cheat Sheet](#time-complexity-big-o-cheat-sheet)
2. [General DS/A Flowchart](#general-dsa-flowchart)
3. [Sorting Algorithms](#sorting-algorithms)
4. [Interview Stages Cheat Sheet](#interview-stages-cheat-sheet)
5. [Code Templates](#code-templates)

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

---

## 🧩 **Code Templates**
### **Sliding Window**
```python
def fn(arr):
    left = ans = curr = 0
    for right in range(len(arr)):
        # logic to update window
        while WINDOW_CONDITION_BROKEN:
            left += 1
        ans = max(ans, curr)
    return ans
```

### **Binary Search**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

---

## 🌟 **Practice Resources**
- [LeetCode CheatSheets](https://leetcode.com/explore/interview/card/cheatsheets/720/resources/4723/)

---

**Happy Studying! 🚀**