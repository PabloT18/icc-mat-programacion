public class Demo {
    public static void main(String[] args) {
        int total = 0, cantidad = 0;
        for (int numero = 1; numero <= 10; numero++) {
            if (numero % 2 == 0) { total += numero; cantidad++; }
        }
        System.out.println("Cantidad: " + cantidad);
        System.out.println("Suma: " + total);
    }
}
