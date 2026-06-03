import java.io.*;
import java.util.Random;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

@WebServlet("/luckynumber")
public class LuckyNumberServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        Random random = new Random();

        out.println("<html><body>");
        out.println("<h2>10 Lucky Numbers</h2>");

        for(int i = 1; i <= 10; i++) {
            int num = random.nextInt(100) + 1; // 1 to 100
            out.println(num + "<br>");
        }

        out.println("</body></html>");
    }
}