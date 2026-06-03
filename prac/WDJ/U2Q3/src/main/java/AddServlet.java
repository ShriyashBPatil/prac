import java.io.*;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

@WebServlet("/AddServlet")
public class AddServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException {

        int num1 = Integer.parseInt(
                request.getParameter("num1"));

        int num2 = Integer.parseInt(
                request.getParameter("num2"));

        int sum = num1 + num2;

        response.setContentType("text/html");

        PrintWriter out = response.getWriter();

        out.println("<h2>Addition of Two Numbers</h2>");
        out.println("Number 1 : " + num1 + "<br>");
        out.println("Number 2 : " + num2 + "<br>");
        out.println("Sum = " + sum);
    }
}