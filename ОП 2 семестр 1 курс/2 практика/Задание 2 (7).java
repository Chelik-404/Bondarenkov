import java.util.*;
public class Task2 {
    public static void main(String[] args) {

        int k = 0;
        int count = 0;
        int x[] = {2, 3, 86, 45, -46, -23, -8, -9, 0, -123, 4,-1000,23,41,213,-31};

        System.out.println("\nИзначальный массив:");

        for (int i = 0; i < x.length; i++) {
            System.out.print(x[i] + "; ");
            if (x[i] < 0) {
                k++;
            }
        }

        double y[] = new double[k];

        for (int j = 0; j < x.length; j++) {
            if (x[j] < 0) {
                y[count] = (double) x[j] / 2;
                count++;
            }
        }

        System.out.println("\n\nИзменненный массив:");
        Arrays.sort(y);
        for(int i = 0; i <  y.length; i++) {
            System.out.print(y[i] + ";  ");
        }
    }
}

/*Дан массив х (n) . Переписать в массив y(n) отрицательные элементы массива х деленные на 2. (со сжатием., без пустых эzементов внутри). Затем упо- рядочить по возрастанию новый массив.*/