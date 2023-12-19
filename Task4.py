# Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
# содержать следующие поля:
# ○ Имя пользователя (обязательное поле)
# ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
# ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
# ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
# После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
# и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
# заполнено или данные не прошли валидацию, то должно выводиться соответствующее
# сообщение об ошибке.
# Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
# базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
# об ошибке.

from flask import Flask, render_template, request
from form4 import Registration
from model4 import db, User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Homework1.sqlite'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Registration()
    if request.method == 'POST' and form.validate():
        username = form.name.data
        email = form.email.data
        password = form.password.data
        if User.query.filter(User.username == username).count() > 0:
            print(f'Пользователь {username} уже зарегистрирован!')
        if User.query.filter(User.email == email).count() > 0:
            print(f'Пользователь {username} уже зарегистрирован!')
        else:
            user = User(username=username, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            print(f'User {username} successfully registered!')
            return render_template(
                'registration.html', form=form)
        return render_template('registration.html', form=form)