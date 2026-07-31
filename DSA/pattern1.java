import java.util.Scanner;
class pattern1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int row = sc.nextInt();
        System.out.print("Enter the number of columns: ");
        int column = sc.nextInt();

        for (int outer = 0; outer < row; outer++) {
            for (int inner = 0; inner < column; inner++) {
                System.out.print("* ");
            }
            System.out.println();
        }

        sc.close();
    }
}