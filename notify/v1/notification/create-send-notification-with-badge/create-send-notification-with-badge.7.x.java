// Install the Java helper library from twilio.com/docs/java/install

import com.twilio.Twilio;
import com.twilio.converter.Promoter;
import com.twilio.rest.notify.v1.service.Notification;

import java.util.HashMap;

public class Example {
    // Find your Account Sid and Token at twilio.com/console
    public static final String ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";
    public static final String AUTH_TOKEN = "your_auth_token";

    public static void main(String[] args) {
        Twilio.init(ACCOUNT_SID, AUTH_TOKEN);
        Notification notification = 
            Notification.creator("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .setApn(
                new HashMap<String, Object>()
                {{
                    put("aps", "{'alert': {'title': 'Bob alert', 'body': 'Bob, you just received a badge'}, 'badge': 1}");
                }})
            .setIdentity(Promoter.listOfOne("00000001"))
            .create();

        System.out.println(notification.getSid());
    }
}