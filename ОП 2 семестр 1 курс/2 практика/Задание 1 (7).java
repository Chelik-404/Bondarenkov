public class Задание {
    public static void main(String[] args) {

int ch[] = new int[10] ;
        int ch1[] = new int [10];

        for (int i=0;i<10;i++) {
            ch[i] = i+1;
            System.out.print("a["+(i+1)+"] = " + ch[i] + "\t");
        }

        System.out.print("\n");

        for (int i=0; i< 10; i++) {
            ch1[i]=ch[9-i];
            System.out.print("b["+(i+1)+"] = " + ch1[i] + "\t");
        }
        System.out.print("\n");
    }
}