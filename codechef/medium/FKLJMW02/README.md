# FKLJMW02

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-07T16:28:08.953Z  

```py
import numpy as np

# Get the list of exam scores from the user
exam_scores = input().split()

# Convert the input strings to integers
exam_scores = [int(score) for score in exam_scores]

# Create a NumPy array from the list of exam scores
# Your code here
exam_scores_array= np.array(exam_scores)
# Print the resulting NumPy array
print(exam_scores_array)
```

---

[View on CodeChef](https://www.codechef.com/problems/FKLJMW02)