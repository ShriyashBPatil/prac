<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<%
    String eidStr = request.getParameter("eid");
    if(eidStr != null) {
        int eid = Integer.parseInt(eidStr);
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "Shriyash@11");
            PreparedStatement ps = con.prepareStatement("DELETE FROM emp WHERE eid=?");
            ps.setInt(1, eid);
            ps.executeUpdate();
            con.close();
        } catch(Exception e) {}
    }
    response.sendRedirect("index.jsp");
%>
