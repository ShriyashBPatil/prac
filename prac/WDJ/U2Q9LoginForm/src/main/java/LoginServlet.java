import java.io.*;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

@WebServlet("/LoginServlet")
public class LoginServlet extends HttpServlet {

    protected void doPost(HttpServletRequest request,
                          HttpServletResponse response)
            throws ServletException, IOException {

        String uname = request.getParameter("uname");
        String pass = request.getParameter("pass");

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        if(uname.equals("admin") && pass.equals("123")) {

            RequestDispatcher rd =
                    request.getRequestDispatcher("welcome");

            rd.forward(request, response);

        } else {

            out.println("<h3 style='color:red'>Invalid Username or Password</h3>");

            RequestDispatcher rd =
                    request.getRequestDispatcher("login.html");

            rd.include(request, response);
        }
    }
}