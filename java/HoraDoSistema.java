/*
 * Program: Create an aplication that reads and print the current system date time.
 * Programmer: Lucas P, Crazypingolu
 * version: 1.0
 */
import java.util.Date;
public class HoraDoSistema{
    public static void main(String[] args) {
        Date date = new Date();
        System.out.println("\nThe current date time is: " + date.toString());
    }
}
