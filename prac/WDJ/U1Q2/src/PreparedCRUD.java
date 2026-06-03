/*
 * CREATE TABLE student(
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
 */

import java.sql.*;
import java.util.Scanner;

public class PreparedCRUD {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");

            Connection con = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/test",
                    "root",
                    "root");

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

                switch (ch) {

                    case 1:
                        System.out.print("Enter ID: ");
                        int id = sc.nextInt();
                        sc.nextLine();

                        System.out.print("Enter Name: ");
                        String name = sc.nextLine();

                        PreparedStatement ps1 =
                                con.prepareStatement(
                                        "INSERT INTO student VALUES(?,?)");

                        ps1.setInt(1, id);
                        ps1.setString(2, name);

                        ps1.executeUpdate();
                        System.out.println("Record Inserted");
                        break;

                    case 2:
                        System.out.print("Enter ID to Update: ");
                        int uid = sc.nextInt();
                        sc.nextLine();

                        System.out.print("Enter New Name: ");
                        String newName = sc.nextLine();

                        PreparedStatement ps2 =
                                con.prepareStatement(
                                        "UPDATE student SET name=? WHERE id=?");

                        ps2.setString(1, newName);
                        ps2.setInt(2, uid);

                        ps2.executeUpdate();
                        System.out.println("Record Updated");
                        break;

                    case 3:
                        System.out.print("Enter ID to Delete: ");
                        int did = sc.nextInt();

                        PreparedStatement ps3 =
                                con.prepareStatement(
                                        "DELETE FROM student WHERE id=?");

                        ps3.setInt(1, did);

                        ps3.executeUpdate();
                        System.out.println("Record Deleted");
                        break;

                    case 4:
                        PreparedStatement ps4 =
                                con.prepareStatement(
                                        "SELECT * FROM student");

                        ResultSet rs = ps4.executeQuery();

                        System.out.println("\nID\tNAME");

                        while (rs.next()) {
                            System.out.println(
                                    rs.getInt("id") + "\t" +
                                    rs.getString("name"));
                        }
                        break;

                    case 5:
                        PreparedStatement ps5 =
                                con.prepareStatement(
                                        "SELECT COUNT(*) FROM student");

                        ResultSet rsCount = ps5.executeQuery();

                        if (rsCount.next()) {
                            System.out.println(
                                    "Total Records = " +
                                    rsCount.getInt(1));
                        }
                        break;

                    case 6:
                        System.out.print("Enter ID: ");
                        int sid = sc.nextInt();

                        PreparedStatement ps6 =
                                con.prepareStatement(
                                        "SELECT * FROM student WHERE id=?");

                        ps6.setInt(1, sid);

                        ResultSet rs1 = ps6.executeQuery();

                        while (rs1.next()) {
                            System.out.println(
                                    rs1.getInt("id") + " " +
                                    rs1.getString("name"));
                        }
                        break;

                    case 7:
                        sc.nextLine();

                        System.out.print("Enter Name: ");
                        String sname = sc.nextLine();

                        PreparedStatement ps7 =
                                con.prepareStatement(
                                        "SELECT * FROM student WHERE name=?");

                        ps7.setString(1, sname);

                        ResultSet rs2 = ps7.executeQuery();

                        while (rs2.next()) {
                            System.out.println(
                                    rs2.getInt("id") + " " +
                                    rs2.getString("name"));
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