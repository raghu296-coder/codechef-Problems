# Modify Columns

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

```
DataFrame employees
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| salary      | int    |
+-------------+--------+

```

A company intends to give its employees a pay rise.

Write a solution to  **modify**  the `salary` column by multiplying each salary by 2.

The result format is in the following example.

 

 **Example 1:** 

```
Input:
DataFrame employees
+---------+--------+
| name    | salary |
+---------+--------+
| Jack    | 19666  |
| Piper   | 74754  |
| Mia     | 62509  |
| Ulysses | 54866  |
+---------+--------+
Output:
+---------+--------+
| name    | salary |
+---------+--------+
| Jack    | 39332  |
| Piper   | 149508 |
| Mia     | 125018 |
| Ulysses | 109732 |
+---------+--------+
Explanation:
Every salary has been doubled.
```

## Solution

**Language:** Python  
**Runtime:** 255 ms (beats 91.67%)  
**Memory:** 66.3 MB (beats 23.96%)  
**Submitted:** 2026-08-26T16:36:53.115Z  

```py
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] =2*employees['salary']
    return employees
    
```

---

[View on LeetCode](https://leetcode.com/problems/modify-columns/)