import java.util.Random;

public class Task4 {
    public static void main (String[] args) {

        int[][] arr1 = new int[5][5];
        for (int i = 0; i < arr1.length; i++) {
            for (int j = 0; j < arr1[0].length; j++) {

                arr1[i][j] = -99 + new Random().nextInt(200);
                System.out.print(arr1[i][j] + "   ");
            }
            System.out.print("\n");
        }

        System.out.println(" ");
        int count = arr1.length - 1;
        double kol = 0;
        double mul=1;

        for (int i = 0; i < arr1.length; i++) {
            for (int j = 0; j < arr1[0].length; j++) {
                if (j == count) {
                    count -= 1;
                    if (arr1[i][j] > 0) {
                        kol++;
                        mul*=arr1[i][j];
                        System.out.print(arr1[i][j]+"; ");
                    }
                }
            }
        }
        double result = Math.pow(mul, 1/kol);
        System.out.println("\nРезультат: "+result);
    }
}