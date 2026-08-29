import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc= new Scanner(System.in);
		 int t= sc.nextInt();
		while(t-- >0 ){
		    
		    int x= sc.nextInt();
		    int y=sc.nextInt();
		    int a = (x-1)/10;
		    
		    int b= (y-1)/10;
		    
		   
		        System.out.println(Math.abs(a-b));
		        
		   
		        System.out.println();
		    
		 
		   
		}
		sc.close();

	}
}
