import java.util.*;
class test{
    public static void main(String []args){
        Scanner sc= new Scanner(System.in);
        int a=sc.nextInt();
        int b=sc.nextInt();
        long c=0;
        int l[]={6,2,5,5,4,5,6,3,7,6};
        while (a<=b){
            int t=a;
            while(t>0){
                c+=l[t%10];
                t=t/10;
            }
            a++;
        }
        System.out.println(c);
    }
}