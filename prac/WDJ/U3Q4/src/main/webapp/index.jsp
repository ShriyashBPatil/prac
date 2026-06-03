<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head><title>Scripting Elements</title></head>
<body>
    <h2>JSP Scripting Elements Demo</h2>
    
    <!-- HTML Comment: Visible in page source -->
    <%-- JSP Comment: Not visible in page source --%>
    
    <%! 
        // Declaration Element
        int count = 0;
        public String getGreeting() {
            return "Hello from declaration!";
        }
    %>
    
    <%
        // Scriptlet Element
        count++;
        String time = new java.util.Date().toString();
    %>
    
    <!-- Expression Element -->
    <h3>Greeting: <%= getGreeting() %></h3>
    <p>Page visits: <%= count %></p>
    <p>Current Time: <%= time %></p>

</body>
</html>
