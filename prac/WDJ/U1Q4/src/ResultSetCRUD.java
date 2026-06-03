import java.sql.*;
import java.util.Scanner;
/*
 * CREATE TABLE student(
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
 */
public class ResultSetCRUD {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");

            Connection con = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/test",
                    "root",
                    "root");

            Statement stmt = con.createStatement(
                    ResultSet.TYPE_SCROLL_SENSITIVE,
                    ResultSet.CONCUR_UPDATABLE);

            while (true) {

                System.out.println("\n===== MENU =====");
                System.out.println("1. Insert");
                System.out.println("2. Update");
                System.out.println("3. Delete");
                System.out.println("4. Display");
                System.out.println("5. Count");
                System.out.println("6. Search By ID");
                System.out.println("7. Search By Name");
                System.out.println("8. Exit");

                System.out.print("Enter Choice: ");
                int ch = sc.nextInt();

                ResultSet rs;

                switch (ch) {

                    case 1:

                        System.out.print("Enter ID: ");
                        int id = sc.nextInt();
                        sc.nextLine();

                        System.out.print("Enter Name: ");
                        String name = sc.nextLine();

                        rs = stmt.executeQuery("SELECT * FROM student");

                        rs.moveToInsertRow();
                        rs.updateInt("id", id);
                        rs.updateString("name", name);
                        rs.insertRow();

                        System.out.println("Record Inserted");
                        break;

                    case 2:

                        System.out.print("Enter ID to Update: ");
                        int uid = sc.nextInt();
                        sc.nextLine();

                        System.out.print("Enter New Name: ");
                        String newName = sc.nextLine();

                        rs = stmt.executeQuery("SELECT * FROM student");

                        while (rs.next()) {
                            if (rs.getInt("id") == uid) {
                                rs.updateString("name", newName);
                                rs.updateRow();
                                System.out.println("Record Updated");
                            }
                        }
                        break;

                    case 3:

                        System.out.print("Enter ID to Delete: ");
                        int did = sc.nextInt();

                        rs = stmt.executeQuery("SELECT * FROM student");

                        while (rs.next()) {
                            if (rs.getInt("id") == did) {
                                rs.deleteRow();
                                System.out.println("Record Deleted");
                            }
                        }
                        break;

                    case 4:

                        rs = stmt.executeQuery("SELECT * FROM student");

                        System.out.println("\nID\tNAME");

                        while (rs.next()) {
                            System.out.println(
                                    rs.getInt("id") + "\t" +
                                    rs.getString("name"));
                        }
                        break;

                    case 5:

                        rs = stmt.executeQuery("SELECT * FROM student");

                        rs.last();

                        System.out.println(
                                "Total Records = " + rs.getRow());
                        break;

                    case 6:

                        System.out.print("Enter ID: ");
                        int sid = sc.nextInt();

                        rs = stmt.executeQuery("SELECT * FROM student");

                        while (rs.next()) {
                            if (rs.getInt("id") == sid) {
                                System.out.println(
                                        rs.getInt("id") + " " +
                                        rs.getString("name"));
                            }
                        }
                        break;

                    case 7:

                        sc.nextLine();

                        System.out.print("Enter Name: ");
                        String sname = sc.nextLine();

                        rs = stmt.executeQuery("SELECT * FROM student");

                        while (rs.next()) {
                            if (rs.getString("name")
                                    .equalsIgnoreCase(sname)) {

                                System.out.println(
                                        rs.getInt("id") + " " +
                                        rs.getString("name"));
                            }
                        }
                        break;

                    case 8:

                        con.close();
                        System.exit(0);

                    default:
                        System.out.println("Invalid Choice");
                }
            }

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}