import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import  mail

def save_picture(form_picture):
    #import pdb;pdb.set_trace()
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    print("app root path", current_app.root_path)
    picture_path = os.path.join(current_app.root_path, 'static/profile_pic', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


def send_reset_email(user):
    # import pdb;pdb.set_trace()
    token = user.get_reset_token()
    msg = Message("Password reset request", sender= "limgirevishal@gmail.com", recipients=[user.email])
    msg.body = f'''
               To reset your password please visit following link: {url_for("users.reset_token", token = token, _external = True)}
               If you did not make this request then simply ignore this email and no changes will made.
    '''
    mail.send(msg)
