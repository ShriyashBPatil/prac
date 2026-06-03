<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<!DOCTYPE html>
<html>
<head><title>Add Employee</title></head>
<body>
    <h2>Add Employee</h2>
    <%
        if("POST".equalsIgnoreCase(request.getMethod())) {
            String ename = request.getParameter("ename");
            double sal = Double.parseDouble(request.getParameter("sal"));
            String dept = request.getParameter("dept");
            try {
                Class.forName("com.mysql.cj.jdbc.Driver");
                Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "Shriyash@11");
                PreparedStatement ps = con.prepareStatement("INSERT INTO emp (ename, sal, dept) VALUES (?, ?, ?)");
                ps.setString(1, ename);
                ps.setDouble(2, sal);
                ps.setString(3, dept);
                ps.executeUpdate();
                con.close();
                response.sendRedirect("index.jsp");
            } catch(Exception e) {
                out.println("Error: " + e.getMessage());
            }
        }
    %>
    <form method="post">
        Name: <input type="text" name="ename" required><br><br>
        Salary: <input type="number" step="0.01" name="sal" required><br><br>
        Department: <input type="text" name="dept" required><br><br>
        <input type="submit" value="Add">
    </form>
    <a href="index.jsp">Back to List</a>
</body>
</html>
