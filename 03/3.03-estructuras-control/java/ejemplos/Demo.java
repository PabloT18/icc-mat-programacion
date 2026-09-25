public class Demo {
    public static void main(String[] args) {
        int medicion = 72;
        String categoria;
        if (medicion < 0 || medicion > 100) categoria = "Inválida";
        else if (medicion < 40) categoria = "Baja";
        else if (medicion <= 75) categoria = "Adecuada";
        else categoria = "Alta";
        System.out.println(categoria);
    }
}
