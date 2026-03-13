from django.core.mail import EmailMessage
from django.conf import settings


def send_book_issued_email_service(
        student_id: str,
        student_name: str,
        email: str,
        book_name: str,
        course_code: str,
        center_name: str,
        issue_date,
        issue_time
):
    """
    Send a professionally styled HTML email for OUSL Book Dispatch.
    """
    subject = f"Book Issued: {course_code} - OUSL Dispatch"

    # Using an f-string with CSS for a "beautiful" look
    html_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 0; }}
            .container {{ max-width: 600px; margin: 20px auto; border: 1px solid #e1e4e8; border-radius: 12px; overflow: hidden; }}
            .header {{ background-color: #003366; color: #ffffff; padding: 30px; text-align: center; }}
            .header h1 {{ margin: 0; font-size: 24px; letter-spacing: 1px; }}
            .content {{ padding: 30px; background-color: #ffffff; }}
            .student-name {{ color: #003366; font-weight: bold; font-size: 18px; }}
            .details-box {{ background-color: #f8f9fa; border-left: 4px solid #003366; padding: 20px; margin: 20px 0; border-radius: 4px; }}
            .details-row {{ margin-bottom: 10px; display: flex; }}
            .label {{ font-weight: bold; width: 120px; color: #555; }}
            .footer {{ background-color: #f4f4f4; color: #777; padding: 20px; text-align: center; font-size: 12px; border-top: 1px solid #eeeeee; }}
            .highlight {{ color: #d32f2f; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>OUSL DISPATCH SYSTEM</h1>
                <p style="margin-top: 5px; opacity: 0.8;">The Open University of Sri Lanka</p>
            </div>
            <div class="content">
                <p>Dear <span class="student-name">{student_name}</span>,</p>
                <p>This is to formally notify you that the following study material has been successfully issued from the regional center.</p>

                <div class="details-box">
                    <div class="details-row"><span class="label">Course:</span> <span>{course_code}</span></div>
                    <div class="details-row"><span class="label">Book Name:</span> <span><strong>{book_name}</strong></span></div>

                    <div class="details-row"><span class="label">Issued At:</span> <span>{center_name}</span></div>
                    <div class="details-row"><span class="label">Date:</span> <span>{issue_date}</span></div>
                    <div class="details-row"><span class="label">Time:</span> <span>{issue_time}</span></div>
                </div>

                <p>Please ensure that you keep this receipt for your records. If you have any discrepancies regarding this issuance, please contact your Regional Center office immediately.</p>

                <p style="margin-top: 30px;">Regards,<br>
                <strong>OUSL Dispatch Team</strong><br>
                The Open University of Sri Lanka</p>
            </div>
            <div class="footer">
                <p>&copy; {issue_date[:4] if isinstance(issue_date, str) else "2026"} The Open University of Sri Lanka. All Rights Reserved.</p>
                <p>This is an automated notification. Please do not reply to this email.</p>
            </div>
        </div>
    </body>
    </html>
    """

    email_message = EmailMessage(
        subject=subject,
        body=html_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email],
    )
    email_message.content_subtype = "html"

    try:
        email_message.send(fail_silently=False)
        return True
    except Exception as e:
        print(f"Email Error: {e}")
        return False