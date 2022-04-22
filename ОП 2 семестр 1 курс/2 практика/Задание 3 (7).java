import java.util.Random;

public class Nameless {
    public static void main (String[] args) {

        int ir = 1 + new Random().nextInt(10);
        int l = 10 + new Random().nextInt(36);
        System.out.println("\nМаксимально возможное число, на строчке: "+ir+", равно: "+l+"\n");

        int [][] arr1 = new int [10][10];
        for (int i=0; i< arr1.length;i++) {
            for (int j=0; j< arr1[0].length;j++) {

                if (i==ir-1){

                arr1[i][j] = 10 + new Random().nextInt(l-9);
                }else {

                arr1[i][j] = 10 + new Random().nextInt(90);
                }
            System.out.print(arr1[i][j] + "   ");
            }
            System.out.print("\n");
         }
    }
}

