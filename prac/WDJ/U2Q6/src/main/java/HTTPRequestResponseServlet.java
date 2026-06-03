import java.io.*;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

@WebServlet("/httpinfo")
public class HTTPRequestResponseServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        // HTTP Request Methods
        String method = request.getMethod();
        String protocol = request.getProtocol();
        String serverName = request.getServerName();
        int serverPort = request.getServerPort();
        String remoteHost = request.getRemoteHost();

        // HTTP Response Methods
        response.setHeader("Developer", "Student");
        response.setStatus(HttpServletResponse.SC_OK);

        out.println("<html><body>");
        out.println("<h2>HTTP Request Information</h2>");
        out.println("Method : " + method + "<br>");
        out.println("Protocol : " + protocol + "<br>");
        out.println("Server Name : " + serverName + "<br>");
        out.println("Server Port : " + serverPort + "<br>");
        out.println("Remote Host : " + remoteHost + "<br>");

        out.println("<h2>HTTP Response Information</h2>");
        out.println("Content Type : " + response.getContentType() + "<br>");
        out.println("Status : 200 OK<br>");

        out.println("</body></html>");
    }
}