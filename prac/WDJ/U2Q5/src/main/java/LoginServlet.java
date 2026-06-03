import java.io.*;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

@WebServlet("/login")
public class LoginServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException {

        String email = request.getParameter("email");
        String password = request.getParameter("password");

        // Valid credentials
        if(email.equals("admin@gmail.com") &&
           password.equals("admin123")) {

            response.sendRedirect(
                "welcome?username=" + email);

        } else {
            response.sendRedirect("login.html");
        }
    }
}