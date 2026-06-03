<%@ page isErrorPage="true" language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head><title>Error</title></head>
<body>
    <h2 style="color:red;">Oops! An Error Occurred.</h2>
    <p><strong>Exception message:</strong> <%= exception.getMessage() %></p>
    <p><strong>Exception type:</strong> <%= exception.getClass().getName() %></p>
</body>
</html>
