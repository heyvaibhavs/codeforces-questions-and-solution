# problem name : Akku and Binary Numbers
# problem link : https://practice.geeksforgeeks.org/problems/akku-and-binary-numbers0902/0/
# level : easy

public class AkkuBinaryNumber {
    static int count = 0;
    public static void main(String[] args) {
        long L=14, R=24, a=0;

        for(long i=L;i<=R;i++){

            // System.out.println("Digit : "+i);
            //Here a is receivibg final answer.
            //converting every number to binary first between inputs
            a = convertToBinary(i);
        } 
        System.out.println(a);
    }

    private static int convertToBinary(long N) {
        int BinaryNum = 0;
            int count = 0;
            while (N != 0) {
                long rem =  N% 2;
                double c = Math.pow(10, count);
                BinaryNum += rem * c;
                N/= 2;
                count++;
            }
        // System.out.println("Binary : "+BinaryNum);
    
        return checkOne(BinaryNum,1); //checking how many one present in binary number of inputs
    }

    private static int checkOne(int n, int d) {
        int c = 0;
     
        while (n > 0)
        {
            if (n % 10 == d)c++;
            n = n / 10;
        }

        if(c==3){       if binary number between inputs contains three 1s then it increase count by 1 everytime.
            count++;
        }
        return count; 
    }
}
