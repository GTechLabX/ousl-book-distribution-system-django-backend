from django.core.mail import EmailMessage
from django.conf import settings
from datetime import datetime


def send_staff_account_created_email(to_email, username, password):
    """
    Send a professionally styled HTML email to new staff members.
    """
    subject = "Account Created: OUSL Book Dispatch Staff Portal"
    current_year = datetime.now().year

    html_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 0; }}
            .container {{ max-width: 600px; margin: 20px auto; border: 1px solid #e1e4e8; border-radius: 12px; overflow: hidden; }}
            .header {{ background-color: #003366; color: #ffffff; padding: 30px; text-align: center; }}
            .header h1 {{ margin: 0; font-size: 22px; letter-spacing: 1px; text-transform: uppercase; }}
            .content {{ padding: 30px; background-color: #ffffff; }}
            .welcome-text {{ font-size: 18px; color: #003366; font-weight: bold; }}
            .credentials-box {{ background-color: #f0f4f8; border: 1px dashed #003366; padding: 20px; margin: 20px 0; border-radius: 8px; }}
            .credential-row {{ margin-bottom: 10px; font-family: monospace; font-size: 15px; }}
            .label {{ font-weight: bold; color: #555; font-family: sans-serif; display: inline-block; width: 100px; }}
            .warning {{ font-size: 13px; color: #d32f2f; font-weight: bold; margin-top: 15px; }}
            .footer {{ background-color: #f4f4f4; color: #777; padding: 20px; text-align: center; font-size: 12px; border-top: 1px solid #eeeeee; }}
            .btn {{ display: inline-block; padding: 12px 25px; background-color: #003366; color: #ffffff !important; text-decoration: none; border-radius: 6px; font-weight: bold; margin-top: 10px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Staff Portal Access</h1>
                <p style="margin-top: 5px; opacity: 0.8;">OUSL Book Dispatch System</p>
            </div>
            <div class="content">
                <p class="welcome-text">Welcome to the Team!</p>
                <p>An administrative account has been provisioned for you on the <strong>OUSL Book Dispatch System</strong>. You can now log in to manage student inventory and book issuances.</p>

                <p><strong>Your Access Credentials:</strong></p>
                <div class="credentials-box">
                    <div class="credential-row"><span class="label">Username:</span> {username}</div>
                    <div class="credential-row"><span class="label">Password:</span> {password}</div>
                </div>

                <p class="warning">⚠️ Security Requirement: You are required to change this temporary password immediately after your first login to ensure account security.</p>

                <p style="margin-top: 30px;">Regards,<br>
                <strong>System Administrator</strong><br>
                OUSL Dispatch Team</p>
            </div>
            <div class="footer">
                <p>&copy; {current_year} The Open University of Sri Lanka. All Rights Reserved.</p>
                <p>This is a confidential system email. If you are not the intended recipient, please notify the OUSL IT department.</p>
            </div>
        </div>
    </body>
    </html>
    """

    email = EmailMessage(
        subject=subject,
        body=html_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[to_email]
    )

    email.content_subtype = "html"

    try:
        email.send(fail_silently=False)
        return True
    except Exception as e:
        print(f"Staff Email Error: {e}")
        return False