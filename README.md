This Django project allows users to send emails from the website. The project utilizes Tailwind CSS for frontend styling.
Views

The project includes a single view - send_email - which handles the email sending process. The view has two parts:

    If the request method is POST, the view retrieves the to_email, subject, and message values from the request. It then sends an email using the Django send_mail function, with the subject, message, and from_email values. The view also adds a success message to the request using the Django messages framework, and redirects the user back to the send_email page.

    If the request method is not POST, the view returns the template senderapp/email_form.html.

Requirements

    Django
    Tailwind CSS
