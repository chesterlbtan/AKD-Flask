from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class AddSeriesForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    link = StringField('Link', validators=[DataRequired()])
    submit = SubmitField('Add')


class AddRMForm(FlaskForm):
    episode = IntegerField('Episode', validators=[DataRequired()])
    link = StringField('Link', validators=[DataRequired()])
    submit = SubmitField('Add')


class EditEpisodeForm(FlaskForm):
    status = StringField('Status', validators=[DataRequired()])
    dl_link = TextAreaField('DL Link', validators=[DataRequired()])
    submit = SubmitField('Update')
