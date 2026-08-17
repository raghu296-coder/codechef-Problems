import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
	    Scanner scanner= new Scanner(System.in);
		// your code goes here
		if( scanner.hasNextInt()){
		    int t= scanner.nextInt();
		    
		    
		    while( t-- >0){
		        
		        int w = scanner.nextInt();
		        int x = scanner.nextInt();
		        int y = scanner.nextInt();
		        int z = scanner.nextInt();
		        
		        if( w == x  || w == y || w== z || w== (x+y) || w == (x+z) || w == (y+ z) || w == (x+ y + z)){
		             System.out.println("YES");
		        }else{
		            System.out.println("NO");
		        }		    }
		}

	}
}
