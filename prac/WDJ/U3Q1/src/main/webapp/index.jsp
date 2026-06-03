<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head><title>JSP Calculator</title></head>
<body>
    <h2>Calculator</h2>
    <form method="post">
        Number 1: <input type="number" name="num1" required><br><br>
        Number 2: <input type="number" name="num2" required><br><br>
        Operation: 
        <select name="op">
            <option value="ADD">Add</option>
            <option value="SUBTRACT">Subtract</option>
            <option value="MULTIPLY">Multiply</option>
            <option value="DIVIDE">Divide</option>
        </select><br><br>
        <input type="submit" value="Calculate">
    </form>
    <br>
    <%
        String n1 = request.getParameter("num1");
        String n2 = request.getParameter("num2");
        String op = request.getParameter("op");
        if (n1 != null && n2 != null && op != null) {
            double a = Double.parseDouble(n1);
            double b = Double.parseDouble(n2);
            double result = 0;
            switch(op) {
                case "ADD": result = a + b; break;
                case "SUBTRACT": result = a - b; break;
                case "MULTIPLY": result = a * b; break;
                case "DIVIDE": result = a / b; break;
            }
            out.println("<h3>Result: " + result + "</h3>");
        }
    %>
</body>
</html>
