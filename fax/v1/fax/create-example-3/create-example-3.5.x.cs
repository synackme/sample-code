// Install the C# / .NET helper library from twilio.com/docs/csharp/install

using System;
using Twilio;
using Twilio.Rest.Fax.V1;


class Program 
{
    static void Main(string[] args)
    {
        // Find your Account Sid and Token at twilio.com/console
        const string accountSid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";
        const string authToken = "your_auth_token";

        TwilioClient.Init(accountSid, authToken);

        var fax = FaxResource.Create(
            from: "Jack",
            mediaUrl: new Uri("https://www.twilio.com/docs/documents/25/justthefaxmaam.pdf"),
            to: "sip:kate@example.com?hatchkey=4815162342;transport=TCP"
        );

        Console.WriteLine(fax.Sid);
    }
}
