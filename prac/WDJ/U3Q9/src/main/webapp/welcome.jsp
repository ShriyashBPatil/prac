<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head><title>Welcome</title></head>
<body>
    <%
        String username = (String) session.getAttribute("username");
        if(username != null) {
            out.println("<h2>Welcome " + username + "!</h2>");
            out.println("<p>Session tracked using HttpSession.</p>");
            out.println("<a href='logout.jsp'>Logout</a>");
        } else {
            response.sendRedirect("index.html");
        }
    %>
</body>
</html>
