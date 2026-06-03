import java.io.*;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

@WebServlet("/student")
public class StudentServlet extends HttpServlet {

    protected void doGet(HttpServletRequest req,
                         HttpServletResponse res)
            throws ServletException, IOException {

        res.setContentType("text/html");
        PrintWriter out = res.getWriter();

        // ServletConfig
        ServletConfig config = getServletConfig();

        String name = config.getInitParameter("studentName");
        String roll = config.getInitParameter("rollNo");

        // ServletContext
        ServletContext context = getServletContext();

        String college = context.getInitParameter("collegeName");
        String course = context.getInitParameter("course");

        out.println("<h2>Student Information</h2>");

        out.println("<h3>Using ServletConfig</h3>");
        out.println("Name : " + name + "<br>");
        out.println("Roll No : " + roll + "<br><br>");

        out.println("<h3>Using ServletContext</h3>");
        out.println("College : " + college + "<br>");
        out.println("Course : " + course);
    }
}