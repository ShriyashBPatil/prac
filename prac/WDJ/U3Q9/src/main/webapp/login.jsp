<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
    String user = request.getParameter("user");
    if(user != null && !user.trim().isEmpty()) {
        session.setAttribute("username", user);
        response.sendRedirect("welcome.jsp");
    } else {
        response.sendRedirect("index.html");
    }
%>
