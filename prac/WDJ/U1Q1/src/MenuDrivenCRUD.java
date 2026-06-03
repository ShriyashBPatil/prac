/*
 * 
 * CREATE TABLE student(
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
 */

import java.sql.*;
import java.util.Scanner;

public class MenuDrivenCRUD {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");

            Connection con = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/test",
                    "root",
                    "root");

            Statement stmt = con.createStatement();

            while (true) {

                System.out.println("\n===== MENU =====");
                System.out.println("1. Insert Record");
                System.out.println("2. Update Record");
                System.out.println("3. Delete Record");
                System.out.println("4. Display Records");
                System.out.println("5. Count Records");
                System.out.println("6. Search by ID");
                System.out.println("7. Search by Name");
                System.out.println("8. Exit");
                System.out.print("Enter Choice: ");

                int ch = sc.nextInt();

                switch (ch) {

                    case 1:
                        System.out.print("Enter ID: ");
                        int id = sc.nextInt();
                        sc.nextLine();

                        System.out.print("Enter Name: ");
                        String name = sc.nextLine();

                        String insert =
                                "INSERT INTO student VALUES(" +
                                        id + ",'" + name + "')";

                        stmt.executeUpdate(insert);
                        System.out.println("Record Inserted");
                        break;

                    case 2:
                        System.out.print("Enter ID to Update: ");
                        int uid = sc.nextInt();
                        sc.nextLine();

                        System.out.print("Enter New Name: ");
                        String newName = sc.nextLine();

                        String update =
                                "UPDATE student SET name='" +
                                        newName +
                                        "' WHERE id=" + uid;

                        stmt.executeUpdate(update);
                        System.out.println("Record Updated");
                        break;

                    case 3:
                        System.out.print("Enter ID to Delete: ");
                        int did = sc.nextInt();

                        String delete =
                                "DELETE FROM student WHERE id=" + did;

                        stmt.executeUpdate(delete);
                        System.out.println("Record Deleted");
                        break;

                    case 4:
                        ResultSet rs =
                                stmt.executeQuery("SELECT * FROM student");

                        System.out.println("\nID\tNAME");

                        while (rs.next()) {
                            System.out.println(
                                    rs.getInt(1) + "\t" +
                                    rs.getString(2));
                        }
                        break;

                    case 5:
                        ResultSet countRs =
                                stmt.executeQuery(
                                        "SELECT COUNT(*) FROM student");

                        if (countRs.next()) {
                            System.out.println(
                                    "Total Records = " +
                                            countRs.getInt(1));
                        }
                        break;

                    case 6:
                        System.out.print("Enter ID: ");
                        int sid = sc.nextInt();

                        ResultSet rs1 =
                                stmt.executeQuery(
                                        "SELECT * FROM student WHERE id=" + sid);

                        while (rs1.next()) {
                            System.out.println(
                                    rs1.getInt(1) + " " +
                                    rs1.getString(2));
                        }
                        break;

                    case 7:
                        sc.nextLine();
                        System.out.print("Enter Name: ");
                        String sname = sc.nextLine();

                        ResultSet rs2 =
                                stmt.executeQuery(
                                        "SELECT * FROM student WHERE name='" +
                                                sname + "'");

                        while (rs2.next()) {
                            System.out.println(
                                    rs2.getInt(1) + " " +
                                    rs2.getString(2));
                        }
                        break;

                    case 8:
                        con.close();
                        System.out.println("Program Ended");
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