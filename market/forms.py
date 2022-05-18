from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models  import User


class RegisterForm(FlaskForm):
    def validate_username(self,username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Kullanıcı adı zaten mevcut! Farklı bir kullanıcı adı deneyin.')

    def validate_email_address(self,email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email adresi mevcut! Farklı bir email adresi giriniz')



    username = StringField(label='Kullanıcı Adı:', validators=[Length(min=2,max=30), DataRequired()])
    email_address = StringField(label='Email Adres:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Şifre:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Şifre Tekrar:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Kullanıcı Oluştur')

class LoginForm(FlaskForm):
    username = StringField(label='Kullanıcı Adı:', validators=[DataRequired()])
    password = PasswordField(label='Şifre:', validators=[DataRequired()])
    submit = SubmitField(label='Giriş Yap')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Satın Al')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Ürünü Sat')

