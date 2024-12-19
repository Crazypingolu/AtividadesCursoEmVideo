/**
  Program: Create an aplication that verifeis the screen dimension values.
  @author Lucas P, Crazypingolu
  @version 1.0
 */
import java.awt.Dimension;
import java.awt.Toolkit;
public class ResolucaoDaTela {
    public static void main(String[] args) {
        Dimension screen = Toolkit.getDefaultToolkit().getScreenSize();
        int wid = (int) screen.getWidth();
        int hei = (int) screen.getHeight();
        System.out.println("\nScreen dimension values: " + wid + "x" + hei);
    }
}
