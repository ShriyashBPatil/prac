<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<%-- 
Database Setup Instructions:
CREATE DATABASE test;
USE test;

CREATE TABLE emp (
    eid INT AUTO_INCREMENT PRIMARY KEY,
    ename VARCHAR(100) NOT NULL,
    sal DOUBLE NOT NULL,
    dept VARCHAR(50) NOT NULL
);

INSERT INTO emp (ename, sal, dept) VALUES ('John Doe', 50000, 'IT');
INSERT INTO emp (ename, sal, dept) VALUES ('Jane Smith', 60000, 'HR');
--%>
<!DOCTYPE html>
<html>
<head><title>Employee CRUD</title></head>
<body>
    <h2>Employee List</h2>
    <a href="add.jsp">Add New Employee</a><br><br>
    <table border="1" cellpadding="5">
        <tr><th>EID</th><th>Name</th><th>Salary</th><th>Department</th><th>Actions</th></tr>
        <%
            try {
                Class.forName("com.mysql.cj.jdbc.Driver");
                Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "Shriyash@11");
                Statement stmt = con.createStatement();
                ResultSet rs = stmt.executeQuery("SELECT * FROM emp");
                while(rs.next()) {
                    int eid = rs.getInt("eid");
                    out.println("<tr>");
                    out.println("<td>" + eid + "</td>");
                    out.println("<td>" + rs.getString("ename") + "</td>");
                    out.println("<td>" + rs.getDouble("sal") + "</td>");
                    out.println("<td>" + rs.getString("dept") + "</td>");
                    out.println("<td><a href='update.jsp?eid=" + eid + "'>Edit</a> | <a href='delete.jsp?eid=" + eid + "'>Delete</a></td>");
                    out.println("</tr>");
                }
                con.close();
            } catch(Exception e) {
                out.println("Error: " + e.getMessage());
            }
        %>
    </table>
</body>
</html>
