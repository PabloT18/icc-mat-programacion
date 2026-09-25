import java.util.ArrayList;
import java.util.List;
public class Demo {
    static List<Integer> filtrarPositivos(int[] datos) {
        var resultado = new ArrayList<Integer>();
        for (int valor : datos) if (valor > 0) resultado.add(valor);
        return resultado;
    }
    public static void main(String[] args) {
        var resultado = filtrarPositivos(new int[]{-2,5,0,8,5});
        int suma = 0;
        for (int i=0; i<resultado.size(); i++) {
            if (i > 0) System.out.print(" ");
            System.out.print(resultado.get(i)); suma += resultado.get(i);
        }
        System.out.println();
        System.out.println("Suma: " + suma);
    }
}
