from django.core.mail import EmailMessage
from django.conf import settings
from datetime import datetime


def send_student_account_created_email(to_email, username, password, img_path=None):
    """
    Send a professionally styled HTML email to new students with optional attachment.
    """
    subject = "Account Created: OUSL Book Dispatch System"
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
            .credentials-box {{ background-color: #f0f4f8; border: 1px solid #d1d9e0; padding: 20px; margin: 20px 0; border-radius: 8px; }}
            .credential-row {{ margin-bottom: 10px; font-size: 15px; }}
            .label {{ font-weight: bold; color: #555; display: inline-block; width: 100px; }}
            .attachment-note {{ font-size: 13px; color: #666; background: #fff9db; padding: 10px; border-radius: 6px; margin-top: 15px; border: 1px solid #ffec99; }}
            .footer {{ background-color: #f4f4f4; color: #777; padding: 20px; text-align: center; font-size: 12px; border-top: 1px solid #eeeeee; }}
            .btn {{ display: inline-block; padding: 12px 25px; background-color: #003366; color: #ffffff !important; text-decoration: none; border-radius: 6px; font-weight: bold; margin-top: 15px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Welcome to OUSL Dispatch</h1>
                <p style="margin-top: 5px; opacity: 0.8;">The Open University of Sri Lanka</p>
            </div>
            <div class="content">
                <p class="welcome-text">Your Account is Ready!</p>
                <p>Your student portal account for the <strong>Book Dispatch System</strong> has been successfully created. You can now log in to reserve books and track your study material issuances.</p>

                <div class="credentials-box">
                    <div class="credential-row"><span class="label">Username:</span> <code style="color: #d32f2f;">{username}</code></div>
                    <div class="credential-row"><span class="label">Password:</span> <code style="color: #d32f2f;">{password}</code></div>
                </div>

                <p>Please change your password after your first login to secure your account.</p>

                {"<div class='attachment-note'><strong>Note:</strong> We have attached your <b>Digital ID/QR Code</b> to this email. Please save it on your mobile device; you will need to present it at the Regional Center to collect your books.</div>" if img_path else ""}

                <p style="margin-top: 30px;">Regards,<br>
                <strong>OUSL Dispatch Team</strong><br>
                The Open University of Sri Lanka</p>
            </div>
            <div class="footer">
                <p>&copy; {current_year} The Open University of Sri Lanka. All Rights Reserved.</p>
                <p>This is an automated system message. Please do not reply to this email address.</p>
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

    if img_path:
        email.attach_file(img_path)

    try:
        email.send(fail_silently=False)
        return True
    except Exception as e:
        print(f"Student Email Error: {e}")
        return False