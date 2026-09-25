import java.util.ArrayList;
import java.util.List;
public class Demo {
    static void mostrar(String titulo, List<Integer> datos) {
        System.out.print(titulo);
        for (int x : datos) System.out.print(" " + x);
        System.out.println();
    }
    public static void main(String[] args) {
        var mediciones = new ArrayList<Integer>(List.of(18, 21, 19));
        var copia = new ArrayList<Integer>(mediciones);
        copia.add(22);
        mostrar("Original:", mediciones);
        mostrar("Copia:", copia);
    }
}
