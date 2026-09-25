import java.nio.file.Files;
import java.nio.charset.StandardCharsets;
import java.io.IOException;
public class Demo {
    public static void main(String[] args) throws IOException {
        var ruta = Files.createTempFile("programacion-", ".txt");
        try {
            Files.writeString(ruta, "Entorno listo", StandardCharsets.UTF_8);
            System.out.println(Files.readString(ruta, StandardCharsets.UTF_8));
        } finally { Files.deleteIfExists(ruta); }
    }
}
