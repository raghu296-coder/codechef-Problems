import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

       
        int t = scanner.nextInt();

       
        for (int i = 0; i < t; i++) {
            
            int x = scanner.nextInt();
            int n = scanner.nextInt(); 
           
            int planesNeeded = (n + 99) / 100;

           
            int additionalPlanes = planesNeeded - x;

            
            System.out.println(Math.max(0, additionalPlanes));
        }

        scanner.close();
    }
}
