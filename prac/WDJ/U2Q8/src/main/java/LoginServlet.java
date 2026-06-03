import java.io.*;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

@WebServlet("/login")
public class LoginServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        String username = request.getParameter("username");
        String password = request.getParameter("password");

        Cookie ck = new Cookie("username", username);
        response.addCookie(ck);

        out.println("<html><body>");
        out.println("<h2>Cookie Created Successfully</h2>");
        out.println("<a href='viewcookie'>View Cookie</a>");
        out.println("</body></html>");
    }
}