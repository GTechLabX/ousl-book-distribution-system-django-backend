from django.core.mail import EmailMessage
from django.conf import settings


def send_book_issue_email(
    to_email,
    student_name,
    course_code,
    course_name,
    register_year
):
    subject = "OUSL Book Dispatch System – Study Material Issued"

    html_body = f"""
    <html>
      <body>
        <h2>Study Material Issued Successfully</h2>

        <p>Dear <b>{student_name}</b>,</p>

        <p>Your study material has been issued successfully.</p>

        <p><strong>Course Details</strong></p>
        <ul>
          <li>Course Code: {course_code}</li>
          <li>Course Name: {course_name}</li>
          <li>Academic Year: {register_year}</li>
        </ul>

        <p>Please keep the issued material safe.</p>

        <p>Regards,<br>
        <b>OUSL Book Dispatch Team</b></p>
      </body>
    </html>
    """

    email = EmailMessage(
        subject=subject,
        body=html_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[to_email],
    )
    email.content_subtype = "html"
    email.send(fail_silently=False)
