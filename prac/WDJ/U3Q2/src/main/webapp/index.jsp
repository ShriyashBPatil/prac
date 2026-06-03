<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head><title>Factorial Calculator</title></head>
<body>
    <h2>Factorial</h2>
    <form method="post">
        Enter Number: <input type="number" name="num" required><br><br>
        <input type="submit" value="Calculate Factorial">
    </form>
    <br>
    <%
        String numStr = request.getParameter("num");
        if (numStr != null) {
            int n = Integer.parseInt(numStr);
            long fact = 1;
            for(int i = 1; i <= n; i++) {
                fact *= i;
            }
            out.println("<h3>Factorial of " + n + " is " + fact + "</h3>");
        }
    %>
</body>
</html>
