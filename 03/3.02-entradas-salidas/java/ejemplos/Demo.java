import java.util.Locale;
import java.util.Scanner;
public class Demo {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        String producto = entrada.nextLine();
        int cantidad = Integer.parseInt(entrada.nextLine());
        double precio = Double.parseDouble(entrada.nextLine());
        System.out.println("Producto: " + producto);
        System.out.printf(Locale.ROOT, "Total: %.2f%n", cantidad * precio);
    }
}
