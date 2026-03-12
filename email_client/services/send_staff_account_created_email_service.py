from django.core.mail import EmailMessage
from django.conf import settings


def send_staff_account_created_email(to_email, username, password):

    subject = "OUSL Book Dispatch System – Staff Account Created"

    html_body = f"""
    <html>
      <body>
        <h2>Welcome to OUSL Book Dispatch System</h2>

        <p>Your staff account has been created successfully.</p>

        <p><strong>Login Details</strong></p>
        <ul>
          <li>Username: {username}</li>
          <li>Password: {password}</li>
        </ul>

        <p>Please change your password after first login.</p>

        <p>Regards,<br>
        <b>OUSL Book Dispatch Team</b></p>

      </body>
    </html>
    """

    email = EmailMessage(
        subject,
        html_body,
        settings.DEFAULT_FROM_EMAIL,
        [to_email]
    )

    email.content_subtype = "html"
    email.send(fail_silently=False)
