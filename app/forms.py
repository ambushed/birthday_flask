from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class StarterForm(Form):

    text = 'The quick brown fox jumps over the lazy dog.'

    def __init__(self,text):
        super(StarterForm,self).__init__()
        self.text = text


    Puzzle = StringField("Modify This: ", default = text)
    Password = StringField("Password: ")
    Message = TextAreaField("Message: ")
    Submit = SubmitField("Submit")




