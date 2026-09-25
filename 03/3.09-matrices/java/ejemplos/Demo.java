public class Demo {
    static String[][] clasificar(int[][] matriz) {
        String[][] resultado = new String[matriz.length][];
        for (int i=0; i<matriz.length; i++) {
            resultado[i] = new String[matriz[i].length];
            for (int j=0; j<matriz[i].length; j++) {
                resultado[i][j] = matriz[i][j] >= 20 ? "ALTA" : "BAJA";
            }
        }
        return resultado;
    }
    public static void main(String[] args) {
        int[][] original = {{18,22,20},{25,15,19}};
        for (String[] fila : clasificar(original)) System.out.println(String.join(" | ", fila));
        System.out.println("Original: " + original[0][0]);
    }
}
