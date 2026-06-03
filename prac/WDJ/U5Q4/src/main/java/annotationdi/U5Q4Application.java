package annotationdi;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class U5Q4Application {

    public static void main(String[] args) {

        ApplicationContext context =
                new AnnotationConfigApplicationContext(AppConfig.class);

        College college = context.getBean(College.class);
        college.show();

        School school = context.getBean(School.class);
        school.show();
    }
}