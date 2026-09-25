import java.util.Locale;
public class Demo {
    static int contarVocales(String texto) {
        int cantidad = 0;
        for (char letra : texto.toLowerCase(Locale.ROOT).toCharArray()) {
            if ("aeiou".indexOf(letra) >= 0) cantidad++;
        }
        return cantidad;
    }
    public static void main(String[] args) {
        String nombre = "  Cuenca  ".strip();
        System.out.println(nombre);
        System.out.println("Vocales: " + contarVocales(nombre));
    }
}
