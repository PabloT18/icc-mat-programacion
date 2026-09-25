import java.util.List;
public class Demo {
    record Producto(String codigo, int cantidad) {}
    public static void main(String[] args) {
        var productos = List.of(new Producto("P01",8), new Producto("P02",0), new Producto("P03",4));
        for (Producto p : productos) {
            if (p.cantidad() > 0) System.out.println(p.codigo() + ": " + p.cantidad());
        }
    }
}
