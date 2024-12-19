/**
  Program: Create an aplication that print the current system language.
  @author Lucas P, Crazypingolu
  @version 1.0
 */
import java.util.Locale;
public class IdiomaSistema {
    public static void main(String[] args) {
        Locale local = Locale.getDefault();
        System.out.println("\nSystem language: " + local.getDisplayLanguage());
    }
}
