from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
from flask_login.utils import login_required
from flaskr.db import DB_Commands
from flaskr.forms import EmailForm
from flask_mail import Mail, Message
from . import mail
bp = Blueprint('marketing', __name__, url_prefix='/marketing')

@login_required
@bp.route('/', methods=('GET', 'POST'))
def marketing():
    """
    Route for the 'product' landing page
    :return: rendered template
    """
    email_campaign_form = EmailForm(request.form)
    if request.method == 'POST':
        subject = email_campaign_form.data['subject']
        body = email_campaign_form.data['body']
        if email_campaign_form.data != None:
            send_email(subject, body)
            return render_template("marketing/success.html")
        return redirect(url_for('marketing.marketing'))
    return render_template("marketing/email.html", form = email_campaign_form)


def send_email(subject, body):
    emails_list = DB_Commands.get_all_customer_emails()
    msg = Message(subject=subject, body=body)
    for recipient in emails_list:
        msg.add_recipient(recipient)
    try:
        mail.send(msg)
    except:
        flash("Connection refused. Set up mail configuration settings in order to send emails.")