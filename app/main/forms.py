from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, SelectField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo


class CfgNotifyForm(FlaskForm):
    check_order = StringField('排序', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    notify_type = SelectField('通知类型', choices=[('MAIL', '邮件通知'), ('SMS', '短信通知')],
                              validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    notify_name = StringField('通知人姓名', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    notify_number = StringField('通知号码', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    status = BooleanField('生效标识', default=True)
    submit = SubmitField('提交')


class userForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 64), ])
    password = PasswordField('密码', validators=[DataRequired()])
    fullname = StringField('用户全名', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Length(1, 64), ])
    phone = StringField('手机号码', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    status = BooleanField('生效标识', default=True)
    submit = SubmitField('提交')

class menuForm(FlaskForm):
    menu_label = StringField('菜单名称', validators=[DataRequired(), Length(1, 64), ])
    menu_list_url = StringField('查询url', validators=[DataRequired()])
    menu_edit_url = StringField('编辑url', validators=[DataRequired()])
    menu_desc = StringField('菜单备注', )
    enable_flag = BooleanField('生效标识', default=True)
    submit = SubmitField('提交')

class usermenuForm(FlaskForm):
    user_id = StringField('用户ID', validators=[DataRequired()])
    menu_id = StringField('菜单ID', validators=[DataRequired()])
    submit = SubmitField('提交')
