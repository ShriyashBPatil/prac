<%@ page language="java" %>

<html>
<body>

<%
String user = request.getParameter("user");
%>

<h2>Welcome <%= user %></h2>

</body>
</html>