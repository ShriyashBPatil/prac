import java.sql.*;
/*
 * DELIMITER $$

CREATE PROCEDURE demoProc(
    IN num1 INT,
    OUT square INT,
    INOUT num2 INT
)
BEGIN
    SET square = num1 * num1;
    SET num2 = num2 * 2;
END $$

DELIMITER ;
 */
public class CallableDemo {

    public static void main(String[] args) {

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");

            Connection con = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/test",
                    "root",
                    "root");

            CallableStatement cs =
                    con.prepareCall("{call demoProc(?,?,?)}");

            // IN Parameter
            cs.setInt(1, 5);

            // OUT Parameter
            cs.registerOutParameter(2, Types.INTEGER);

            // INOUT Parameter
            cs.setInt(3, 10);
            cs.registerOutParameter(3, Types.INTEGER);

            cs.execute();

            System.out.println("IN Value = 5");
            System.out.println("OUT (Square) = " + cs.getInt(2));
            System.out.println("INOUT (Double Value) = " + cs.getInt(3));

            con.close();

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}