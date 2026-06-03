import java.io.*;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

@WebServlet("/calculator")
public class CalculatorServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        try {
            int num1 = Integer.parseInt(request.getParameter("num1"));
            int num2 = Integer.parseInt(request.getParameter("num2"));
            String op = request.getParameter("op");

            int result = 0;

            switch (op) {
                case "+":
                    result = num1 + num2;
                    break;

                case "-":
                    result = num1 - num2;
                    break;

                case "*":
                    result = num1 * num2;
                    break;

                case "/":
                    if (num2 != 0)
                        result = num1 / num2;
                    else {
                        out.println("<h3>Cannot divide by zero</h3>");
                        return;
                    }
                    break;

                default:
                    out.println("<h3>Invalid Operation</h3>");
                    return;
            }

            out.println("<html><body>");
            out.println("<h2>Calculator Result</h2>");
            out.println("<p>Number 1: " + num1 + "</p>");
            out.println("<p>Number 2: " + num2 + "</p>");
            out.println("<p>Operation: " + op + "</p>");
            out.println("<h3>Result = " + result + "</h3>");
            out.println("</body></html>");

        } catch (Exception e) {
            out.println("<h3>Invalid Input</h3>");
        }
    }
}