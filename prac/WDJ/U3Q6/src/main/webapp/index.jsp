<%@ page errorPage="errorPage.jsp" language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head><title>Error Demo</title></head>
<body>
    <h2>Error Generating Page</h2>
    <%
        String action = request.getParameter("action");
        if("arithmetic".equals(action)) {
            int a = 10 / 0; // Throws ArithmeticException
        } else if("null".equals(action)) {
            String s = null;
            s.length(); // Throws NullPointerException
        } else if("array".equals(action)) {
            int[] arr = new int[2];
            arr[5] = 10; // Throws ArrayIndexOutOfBoundsException
        }
    %>
    <ul>
        <li><a href="?action=arithmetic">Trigger ArithmeticException</a></li>
        <li><a href="?action=null">Trigger NullPointerException</a></li>
        <li><a href="?action=array">Trigger ArrayIndexOutOfBoundsException</a></li>
    </ul>
</body>
</html>
