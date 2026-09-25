public class Demo {
    public static void main(String[] args) {
        for (boolean credencial : new boolean[]{false, true}) {
            for (boolean reserva : new boolean[]{false, true}) {
                boolean permitido = credencial && reserva;
                System.out.println((credencial ? 1 : 0) + " " + (reserva ? 1 : 0) + " " + (permitido ? 1 : 0));
            }
        }
    }
}
