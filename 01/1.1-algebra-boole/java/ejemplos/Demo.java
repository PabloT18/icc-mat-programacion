public class Demo {
    public static void main(String[] args) {
        boolean[] valores = {false, true};
        System.out.println("A B ORIGINAL REDUCIDA IGUALES");
        for (boolean A : valores) {
            for (boolean B : valores) {
                boolean original = (A && B) || (A && !B) || (!A && B);
                boolean reducida = A || B;
                System.out.printf("%d %d %d %d %d%n",
                    A ? 1 : 0, B ? 1 : 0, original ? 1 : 0,
                    reducida ? 1 : 0, original == reducida ? 1 : 0);
            }
        }
        System.out.println("A B C ORIGINAL REDUCIDA IGUALES");
        for (boolean A : valores) {
            for (boolean B : valores) {
                for (boolean C : valores) {
                    boolean original = !((A || B) && (A || !B)) || (!A && C);
                    boolean reducida = !A;
                    System.out.printf("%d %d %d %d %d %d%n",
                        A ? 1 : 0, B ? 1 : 0, C ? 1 : 0, original ? 1 : 0,
                        reducida ? 1 : 0, original == reducida ? 1 : 0);
                }
            }
        }
    }
}
