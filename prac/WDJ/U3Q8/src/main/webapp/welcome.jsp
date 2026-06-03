<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head><title>Welcome</title></head>
<body>
    <%
        String username = null;
        Cookie[] cookies = request.getCookies();
        if(cookies != null) {
            for(Cookie c : cookies) {
                if(c.getName().equals("username")) {
                    username = c.getValue();
                }
            }
        }
        if(username != null) {
            out.println("<h2>Welcome " + username + "!</h2>");
            out.println("<p>Session tracked using Cookies.</p>");
            out.println("<a href='logout.jsp'>Logout</a>");
        } else {
            response.sendRedirect("index.html");
        }
    %>
</body>
</html>
