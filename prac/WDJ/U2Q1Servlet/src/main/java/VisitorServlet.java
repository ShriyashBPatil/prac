import java.io.*;
import java.util.Date;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

@WebServlet("/visit")
public class VisitorServlet extends HttpServlet {

    int count = 0;

    public void init() throws ServletException {
        System.out.println("Servlet Initialized");
    }

    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException {

        count++;

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        out.println("<html><body>");
        out.println("<h2>HTTP Servlet Life Cycle Demo</h2>");
        out.println("<p>Date & Time: " + new Date() + "</p>");
        out.println("<p>Number of Requests: " + count + "</p>");
        out.println("</body></html>");
    }

    public void destroy() {
        System.out.println("Servlet Destroyed");
    }
}