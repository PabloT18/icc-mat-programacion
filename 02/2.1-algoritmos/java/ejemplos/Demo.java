public class Demo {
    public static void main(String[] args) {
        int minutos = 125;
        if (minutos < 0) {
            System.out.println("Duración inválida");
        } else {
            int horas = (minutos + 59) / 60;
            System.out.println("Horas: " + horas);
            System.out.println("Costo: " + horas * 2);
        }
    }
}
