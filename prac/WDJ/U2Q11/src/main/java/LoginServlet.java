/*
 CREATE TABLE users(
    username VARCHAR(50),
    password VARCHAR(50)
);

INSERT INTO users VALUES('admin','123');
 */

import java.io.*;
import java.sql.*;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

@WebServlet("/LoginServlet")
public class LoginServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        String uname = request.getParameter("username");
        String pass = request.getParameter("password");

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");

            Connection con =
                DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/sem",
                "root",
                "Shriyash@11");

            PreparedStatement ps =
                con.prepareStatement(
                "select * from users where username=? and password=?");

            ps.setString(1, uname);
            ps.setString(2, pass);

            ResultSet rs = ps.executeQuery();

            if(rs.next()) {

                out.println("<h3>Welcome " + uname + "</h3>");

                RequestDispatcher rd =
                    request.getRequestDispatcher("welcome.html");

                rd.include(request, response);

            } else {

                out.println("<h3 style='color:red'>Invalid Username or Password</h3>");

                RequestDispatcher rd =
                    request.getRequestDispatcher("login.html");

                rd.forward(request, response);
            }

            con.close();

        } catch(Exception e) {
            out.println(e);
        }
    }
}