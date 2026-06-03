<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<!DOCTYPE html>
<html>
<head><title>Update Employee</title></head>
<body>
    <h2>Update Employee</h2>
    <%
        String eidStr = request.getParameter("eid");
        if(eidStr == null) { response.sendRedirect("index.jsp"); return; }
        int eid = Integer.parseInt(eidStr);

        if("POST".equalsIgnoreCase(request.getMethod())) {
            String ename = request.getParameter("ename");
            double sal = Double.parseDouble(request.getParameter("sal"));
            String dept = request.getParameter("dept");
            try {
                Class.forName("com.mysql.cj.jdbc.Driver");
                Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "Shriyash@11");
                PreparedStatement ps = con.prepareStatement("UPDATE emp SET ename=?, sal=?, dept=? WHERE eid=?");
                ps.setString(1, ename);
                ps.setDouble(2, sal);
                ps.setString(3, dept);
                ps.setInt(4, eid);
                ps.executeUpdate();
                con.close();
                response.sendRedirect("index.jsp");
                return;
            } catch(Exception e) {
                out.println("Error: " + e.getMessage());
            }
        }
        
        String ename = "", dept = "";
        double sal = 0;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "Shriyash@11");
            PreparedStatement ps = con.prepareStatement("SELECT * FROM emp WHERE eid=?");
            ps.setInt(1, eid);
            ResultSet rs = ps.executeQuery();
            if(rs.next()) {
                ename = rs.getString("ename");
                sal = rs.getDouble("sal");
                dept = rs.getString("dept");
            }
            con.close();
        } catch(Exception e) {}
    %>
    <form method="post">
        Name: <input type="text" name="ename" value="<%=ename%>" required><br><br>
        Salary: <input type="number" step="0.01" name="sal" value="<%=sal%>" required><br><br>
        Department: <input type="text" name="dept" value="<%=dept%>" required><br><br>
        <input type="submit" value="Update">
    </form>
    <a href="index.jsp">Back to List</a>
</body>
</html>
