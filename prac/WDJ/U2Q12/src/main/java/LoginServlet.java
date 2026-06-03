import java.io.*;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

@WebServlet("/LoginServlet")
public class LoginServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException {

        String uname = request.getParameter("username");
        String pass = request.getParameter("password");

        if(uname.equals("admin") && pass.equals("123")) {

            HttpSession session =
                    request.getSession();

            session.setAttribute("username", uname);

            response.sendRedirect("welcome");

        } else {

            response.setContentType("text/html");
            PrintWriter out = response.getWriter();

            out.println("<h3>Invalid Username or Password</h3>");
            out.println("<a href='login.html'>Login Again</a>");
        }
    }
}