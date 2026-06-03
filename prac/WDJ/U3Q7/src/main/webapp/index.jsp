<%@ page language="java" contentType="text/html; charset=UTF-8" 
    pageEncoding="UTF-8" 
    import="java.util.Date, java.util.ArrayList" 
    session="true" 
    buffer="8kb" 
    autoFlush="true" 
    isThreadSafe="true" 
    info="This is a demo page for directives" 
    errorPage="" 
%>
<!DOCTYPE html>
<html>
<head><title>Page Directives</title></head>
<body>
    <h2>Page Directive Attributes Demo</h2>
    <p><strong>Date imported:</strong> <%= new Date() %></p>
    <p><strong>Page Info:</strong> <%= getServletInfo() %></p>
    <p><strong>Session ID:</strong> <%= session.getId() %></p>
</body>
</html>
