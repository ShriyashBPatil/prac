<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
    String user = request.getParameter("user");
    if(user != null && !user.trim().isEmpty()) {
        Cookie c = new Cookie("username", user);
        c.setMaxAge(60 * 60); // 1 hour
        response.addCookie(c);
        response.sendRedirect("welcome.jsp");
    } else {
        response.sendRedirect("index.html");
    }
%>
