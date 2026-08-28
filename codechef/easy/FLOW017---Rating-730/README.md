# FLOW017 - Rating 730

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Second Largest

Three numbers  **A**,  **B**  and  **C**  are the inputs. Write a program to find second largest among them.

### Input Format

The first line contains an integer  **T**, the total number of testcases. Then  **T**  lines follow, each line contains three integers  **A**,  **B**  and  **C**.

### Output Format

For each test case, display the second largest among  **A**,  **B**  and  **C**, in a new line.

### Constraints
- 1 ≤ T ≤ 1000
- 1 ≤ A,B,C ≤ 1000000
### Sample 1:
Input
Output

```
3 
120 11 400
10213 312 10
10 3 450
```

```
120
312
10
```

## Solution

**Language:** Java  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-28T16:16:01.364Z  

```java
import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc =new Scanner(System.in);
		int t=sc.nextInt();
		while(t-- > 0){
		    int x= sc.nextInt();
		    int y= sc.nextInt();
		    int z= sc.nextInt();
		    if (x>=y && x>=z){
		        System.out.println(Math.max(y,z));
		    }
		    
		     else if(y>=x && y >=z){
		        System.out.println(Math.max(x,z));
		    }else {
		        System.out.println( Math.max(x,y));
	       	}
	       	System.out.println();
		    
    
	}
	sc.close();
}
}
```

---

[View on CodeChef](https://www.codechef.com/problems/FLOW017)