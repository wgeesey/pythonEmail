import smtplib  # Importing the smtplib module for email sending
from email.message import EmailMessage  # Import EmailMessage for creating the email content

# Create an email message object
email = EmailMessage()

# Set email fields (sender, receiver, and subject)
email['from'] = 'Sender Name or email'  # Sender name, can be customized
email['to'] = 'Receipient email'  # Receiver's email address
email['subject'] = 'Enter the Subject'  # Email subject

# Set the content of the email (plain text)
email.set_content('What you want to say in the email')

# Establish a connection to the SMTP server to send the email - Gmail in this case
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # Send EHLO command to the server to identify the client and check server capabilities
    smtp.starttls()  # Upgrade the connection to a secure TLS (Transport Layer Security) connection
    
    # Login to the SMTP server using Gmail credentials
    smtp.login('your Gmail email', 'your password or App password')  # Use your Gmail email and password or App Password
    
    # Send the email
    smtp.send_message(email)  
    print('Email sent')  # Confirmation message
