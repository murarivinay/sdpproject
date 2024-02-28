import csv
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
def send_emails(request):
    csv_file_path = r'C:\Users\Rama Teja\Dropbox\PC\Desktop\Y22-26\SEM4\PFSD\PFSDProject\django\TTM\static\mailapp.csv'
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipient_email = row['email']
            subject = 'Hello KLUian'  # Set your subject here
            message_body = 'Hey, Thanks for contacting rama travels'  # Set your email content here
            send_mail(
                subject,
                message_body,
                '2200032668cseh@gmail.com',
                [recipient_email],
                fail_silently=False,
            )
            print(f'Sent email to {recipient_email}')
    return render(request, 'Emails_sent_successfully.html')