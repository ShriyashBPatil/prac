import java.io.*;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

@WebServlet("/welcome")
public class WelcomeServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        HttpSession session =
                request.getSession(false);

        String uname =
                (String)session.getAttribute("username");

        out.println("<html><body>");
        out.println("<h2>Welcome " + uname + "</h2>");
        out.println("</body></html>");
    }
}