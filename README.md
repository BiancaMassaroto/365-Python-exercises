# 365 Days of Python Engineering

A 1-year personal journey focused on moving from fundamental coding patterns to absolute fluency in Python. The ultimate goal of this repository is to build deep muscle memory, master data structures and algorithms (DSA), and develop the skills required to clear software engineering internships at bigtech companies.

## 🚫 The Rules of this Journey
To maximize learning and build true engineering intuition, every single project in this repository follows strict constraints:
* **No AI Assistants:** GitHub Copilot, Cursor, Windsurf, and ChatGPT are completely banned. Every line of code is thought out and written manually.
* **No Shortcuts / Built-ins:** Standard helper functions like `sum()`, `max()`, `min()`, `.sort()`, or `reverse()` are avoided where algorithmic logic is tested. Everything is built from scratch using pure logic, raw loops, and manual pointer manipulation.

---

## 🗺️ Roadmap

The 365-day roadmap is split into 6 blocks, each scaling in difficulty:

### 🔹 Module 0: Engineering Core (Exercises 1–20)
*Focus: Low-level fundamentals, CPython memory management, stack/heap simulation, pointers, bitwise operations, and empirical efficiency tracking.*

### 🔹 Module 1: Advanced Data Manipulation & Pointer Logic (Exercises 21–70)
*Focus: Optimizing lookup times, building custom Hash Tables, mastering pointer mechanics (e.g., Two Pointers, Sliding Window), and understanding mutable vs. immutable memory constraints.*

### 🔹 Module 2: I/O Streams, Memory Buffers & Parsing (Exercises 71–120)
*Focus: Manipulating files at the byte/line level without breaking RAM limits, managing I/O bottlenecks, writing custom tokenizers, and handling raw data streams.*

### 🔹 Module 3: Object-Oriented Design, SOLID & Design Patterns (Exercises 121–180)
*Focus: Strict encapsulation, polymorphism, decoupling dependencies, and implementing the classic Gang of Four (GoF) design patterns from scratch to build scalable software.*

### 🔹 Module 4: Pure Data Structures & Classic Algorithms (Exercises 181–240)
*Focus: The heart of the Google hiring process. Implementing raw Linked Lists, Trees, Graphs, Heaps, and Tries without native collections, alongside detailed Big-O time and space complexity analysis.*

### 🔹 Module 5: Concurrency, Parallelism & Low-Level Networking (Exercises 241–300)
*Focus: Managing race conditions, preventing deadlocks, thread synchronization (`Locks`, `Semaphores`), asynchronous event loops, and raw TCP/IP socket programming.*

### 🔹 Module 6: Distributed Systems & Clean Architecture (Exercises 301–365)
*Focus: Production-grade software engineering, decoupling code into layers (Clean/Hexagonal Architecture), custom unit test frameworks, and optimizing distributed data components.*

---

## 🚀 Exercises:

Here are the descriptions for the first 5 exercises I've done until now, I'll be weekly updating my progress until I finish all 365 exercises!

### Exercise 1: In-Place Array Reversal (Two Pointers)
* **Objective:** Reverse an array of elements without allocating any extra memory space.
* **Constraint:** Banned from using `.reverse()`, `[::-1]`, or creating a secondary buffer list.

### Exercise 2: Manual Extreme Value Lookup
* **Objective:** Scan a dynamic list of floating-point numbers to find both the maximum and minimum elements.
* **Constraint:** Banned from using the built-in `max()` and `min()` functions.

### Exercise 3: Sorted Array Merge
* **Objective:** Take two separate lists that are already sorted in ascending order and combine them into a single, fully-sorted third list.
* **Constraints:** Banned from using `.sort()`, `sorted()`, or appending everything and running an external sorting algorithm.

### Exercise 4: Element Removal with Manual Shifting
* **Objective:** Scan an array and remove all occurrences of a target value `X`.
* **Constraint:** Banned from using `.remove()`, `.pop()`, or generating a new filtered list via list comprehensions.

### Exercise 5: O(N) Duplicate Detection
* **Objective:** Determine whether a given list contains any duplicate elements in a single pass.
* **Constraint:** Banned from using nested loops (which results in a slow \(O(N^2)\) runtime) or comparing list lengths via `len(set(lst))`.

---

## 📈 Repository Structure
```text
├── README.md
├── Module_0_Core/
│   ├── Day_001_reversal/
│   │   ├── solution.py
│   │   └── test_solution.py  # Manual assert statements for validation
│   └── ...
└── ...
```
