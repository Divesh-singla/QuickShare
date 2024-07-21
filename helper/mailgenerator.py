from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

# mail_intergration website: https://app.brevo.com/campaigns/listing/email


def __sendMail(name,email,otp):

    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'

    # Create an instance of the API class
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    # Define the email parameters
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": f"{email}", "name": f"{name}"}],  # Replace with recipient's email and name
        sender={"email": "diveshsingla9@gmail.com", "name": "Support Demo Django"},
        subject="test email",
        html_content='<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Password Reset Verification</title> <style> body { font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0; } .container { width: 100%; max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); border-radius: 5px; } .header { text-align: center; padding: 10px 0; } .header img { max-width: 150px; } .content { padding: 20px; } .content h1 { color: #333333; font-size: 24px; } .content p { color: #666666; font-size: 16px; } .otp { font-size: 24px; font-weight: bold; color: #ff6f61; text-align: center; margin: 20px 0; } .footer { text-align: center; padding: 10px 0; font-size: 12px; color: #999999; } .footer a { color: #ff6f61; text-decoration: none; } </style> </head> <body> <div class="container"> <div class="header"> </div> <div class="content"> <h1>Password Reset Verification</h1> <p>Dear'+name+',</p> <p>We received a request to reset your password. Use the following OTP (one time password) to complete the process:</p> <div class="otp">'+otp+'</div> <p>This OTP is valid for the next 10 minutes. If you did not request a password reset, please ignore this email.</p> <p>Thank you,<br>Quick Share</p> </div> <div class="footer"> <p>If you have any questions, feel free to <a href="https://com/contact">contact us</a>.</p> <p>&copy; 2024 Quick Share. All rights reserved.</p> </div> </div> </body> </html>'
    )

    # Send the email
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        return(api_response)
    except ApiException as e:
        return("Exception when calling TransactionalEmailsApi->send_transac_email: %s\n" % e,"error raised")
    
