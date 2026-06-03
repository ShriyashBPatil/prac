<%@ page import="java.sql.*" %>

<%
String uname = request.getParameter("uname");
String pass = request.getParameter("pass");

Class.forName("com.mysql.cj.jdbc.Driver");

Connection con = DriverManager.getConnection(
"jdbc:mysql://localhost:3306/sem",
"root",
"Shriyash@11");

PreparedStatement ps = con.prepareStatement(
"select * from users where username=? and password=?");

ps.setString(1, uname);
ps.setString(2, pass);

ResultSet rs = ps.executeQuery();

if(rs.next())
{
    response.sendRedirect("welcome.jsp?user=" + uname);
}
else
{
    response.sendRedirect("login.jsp?msg=Invalid Login");
}

con.close();
%>