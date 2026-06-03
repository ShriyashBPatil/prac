<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head><title>String Reverser</title></head>
<body>
    <h2>Reverse String</h2>
    <form method="post">
        Enter String: <input type="text" name="str" required><br><br>
        <input type="submit" value="Reverse">
    </form>
    <br>
    <%
        String str = request.getParameter("str");
        if (str != null) {
            String reversed = new StringBuilder(str).reverse().toString();
            out.println("<h3>Original: " + str + "</h3>");
            out.println("<h3>Reversed: " + reversed + "</h3>");
        }
    %>
</body>
</html>
