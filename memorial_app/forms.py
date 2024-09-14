from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, DateField, IntegerField, FloatField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class MemorialProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    date_of_birth = DateField('Date of Birth', validators=[DataRequired()])
    date_of_death = DateField('Date of Death', validators=[DataRequired()])
    biography = TextAreaField('Biography', validators=[DataRequired()])
    profile_photo_url = StringField('Profile Photo URL', validators=[DataRequired()])
    qr_code_url = StringField('QR Code URL', validators=[DataRequired()])
    visibility_status = SelectField('Visibility Status', choices=[('public', 'Public'), ('private', 'Private')], validators=[DataRequired()])

class TimelineEventForm(FlaskForm):
    profile_id = IntegerField('Profile ID', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    event = TextAreaField('Event', validators=[DataRequired()])

class TributeForm(FlaskForm):
    profile_id = IntegerField('Profile ID', validators=[DataRequired()])
    user_id = IntegerField('User ID')
    tribute_message = TextAreaField('Tribute Message', validators=[DataRequired()])

class PaymentSubscriptionForm(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired()])
    stripe_customer_id = StringField('Stripe Customer ID', validators=[DataRequired()])
    subscription_id = StringField('Subscription ID', validators=[DataRequired()])
    payment_amount = FloatField('Payment Amount', validators=[DataRequired()])
    payment_status = StringField('Payment Status', validators=[DataRequired()])
    subscription_start = DateField('Subscription Start', validators=[DataRequired()])
    subscription_end = DateField('Subscription End', validators=[DataRequired()])

class MediaForm(FlaskForm):
    profile_id = IntegerField('Profile ID', validators=[DataRequired()])
    media_type = StringField('Media Type', validators=[DataRequired()])
    media_url = StringField('Media URL', validators=[DataRequired()])

class QRCodeForm(FlaskForm):
    profile_id = IntegerField('Profile ID', validators=[DataRequired()])
    qr_code_url = StringField('QR Code URL', validators=[DataRequired()])

class ActivityLogForm(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired()])
    profile_id = IntegerField('Profile ID', validators=[DataRequired()])
    action = StringField('Action', validators=[DataRequired()])