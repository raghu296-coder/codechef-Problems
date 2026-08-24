# Return Length of Arguments Passed

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Write a function `argumentsLength` that returns the count of arguments passed to it.

 

 **Example 1:** 

```
Input: args = [5]
Output: 1
Explanation:
argumentsLength(5); // 1

One value was passed to the function so it should return 1.

```

 **Example 2:** 

```
Input: args = [{}, null, "3"]
Output: 3
Explanation: 
argumentsLength({}, null, "3"); // 3

Three values were passed to the function so it should return 3.

```

 

 **Constraints:** 

- args is a valid JSON array
- 0 <= args.length <= 100

## Solution

**Language:** TypeScript  
**Runtime:** 45 ms  
**Memory:** 52.9 MB  
**Submitted:** 2026-08-24T14:28:37.703Z  

```ts
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };

function argumentsLength(...args: JSONValue[]): number {
    return args.length
};

/**
 * argumentsLength(1, 2, 3); // 3
 */
```

---

[View on LeetCode](https://leetcode.com/problems/return-length-of-arguments-passed/)