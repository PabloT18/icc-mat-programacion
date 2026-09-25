import java.util.Locale;
public class Demo {
    static double costoHoras(int horas, double tarifa) {
        if (horas < 0 || tarifa < 0) throw new IllegalArgumentException("Valores negativos");
        return horas * tarifa;
    }
    public static void main(String[] args) {
        System.out.printf(Locale.ROOT, "Costo: %.2f%n", costoHoras(3, 2.5));
        try { costoHoras(-1, 2.5); }
        catch (IllegalArgumentException error) { System.out.println(error.getMessage()); }
    }
}
