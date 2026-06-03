<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
    Cookie[] cookies = request.getCookies();
    if(cookies != null) {
        for(Cookie c : cookies) {
            if(c.getName().equals("username")) {
                c.setMaxAge(0);
                response.addCookie(c);
            }
        }
    }
    response.sendRedirect("index.html");
%>
