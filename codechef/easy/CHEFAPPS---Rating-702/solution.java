import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner scanner = new Scanner(System.in);
        
        if (scanner.hasNextInt()) {
            int t = scanner.nextInt();
            
            while (t-- > 0) {
                int s = scanner.nextInt();
                int x = scanner.nextInt();
                int y = scanner.nextInt();
                int z = scanner.nextInt();
                
                
                int usedm = s-(x+ y);
                
                if (usedm >=z){
                    System.out.println(0);
                    
                }
                else if((usedm + x) >= z || (usedm +y) >= z ){
                    System.out.println(1);
                }else{
                    System.out.println(2);
                }
}

	}
scanner.close();
}
    
}
