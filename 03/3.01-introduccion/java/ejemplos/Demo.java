import java.util.Locale;
public class Demo {
    public static void main(String[] args) {
        int cantidad = 4;
        double precio = 1.75;
        double total = cantidad * precio;
        System.out.println("Cantidad: " + cantidad);
        System.out.printf(Locale.ROOT, "Total: %.2f%n", total);
    }
}
