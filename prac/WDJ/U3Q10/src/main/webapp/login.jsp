<%@ page language="java" %>

<html>
<body>

<h2>Login Form</h2>

<form action="validate.jsp" method="post">
    Username:
    <input type="text" name="uname"><br><br>

    Password:
    <input type="password" name="pass"><br><br>

    <input type="submit" value="Login">
</form>

<%
String msg = request.getParameter("msg");
if(msg != null)
{
    out.println("<font color='red'>" + msg + "</font>");
}
%>

</body>
</html>