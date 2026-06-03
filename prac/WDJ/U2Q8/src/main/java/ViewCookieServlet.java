import java.io.*;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

@WebServlet("/viewcookie")
public class ViewCookieServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        Cookie cookies[] = request.getCookies();

        out.println("<html><body>");

        if (cookies != null) {
            for (Cookie c : cookies) {

                if (c.getName().equals("username")) {

                    out.println("<h2>Stored Cookie Information</h2>");
                    out.println("Username : "
                            + c.getValue() + "<br><br>");

                    out.println("<h2>Welcome "
                            + c.getValue() + "</h2>");
                }
            }
        }

        out.println("</body></html>");
    }
}