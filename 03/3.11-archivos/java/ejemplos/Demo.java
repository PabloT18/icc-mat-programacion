import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.charset.StandardCharsets;
import java.io.IOException;
public class Demo {
    public static void main(String[] args) throws IOException {
        Path carpeta = Files.createTempDirectory("programacion-");
        Path ruta = carpeta.resolve("mediciones.txt");
        try {
            Files.writeString(ruta, "12\n8\n15\n", StandardCharsets.UTF_8);
            int total = 0;
            try (var lector = Files.newBufferedReader(ruta, StandardCharsets.UTF_8)) {
                String linea;
                while ((linea=lector.readLine()) != null) total += Integer.parseInt(linea.strip());
            }
            System.out.println("Total: " + total);
        } finally { Files.deleteIfExists(ruta); Files.deleteIfExists(carpeta); }
    }
}
