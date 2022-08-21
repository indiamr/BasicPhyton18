#used module
import smtplib, ssl

#module to read image
import imghdr
from email.message import EmailMessage

#acc & password
acc_email = "enj.indi@gmail.com"
pass_email = "fzjrjrmeehdnptez"

#reciever list in txt file
receiver = open("email_address_list.txt", "r")
data = receiver.read()
email_receiver = data.split("\n")
receiver.close()

#email content
subject = "Sending Email with Python for Final Project"
body = """
These is My Final Project for Basic Python Batch 18, please find the attachment
"""
#email sender main function
em = EmailMessage()
em['From'] = acc_email
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

#attach image
images_files =["Basic Pyhton.png"]


for image in images_files:
    with open(image, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name

        em.add_attachment(image_data, maintype = 'image', subtype = image_type, filename = image_name)

#attach pdf
pdf_files = ["Basic Python.pdf"]

for pdf in pdf_files:
    with open(pdf, 'rb') as f:
        pdf_data = f.read()
        pdf_name = f.name

        em.add_attachment(pdf_data, maintype = 'pdf', subtype = "octret-stream", filename = pdf_name)

#handling login prot sssl on gmail
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(acc_email, pass_email)
    smtp.sendmail(acc_email, email_receiver, em.as_string())
    print("Email Sent \n"+ data)