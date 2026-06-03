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

            response.sendRedirect(
                "welcome?username=" + uname);

        } else {

            response.sendRedirect(
                "error.html");
        }
    }
}