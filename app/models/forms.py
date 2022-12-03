from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired



class CadastroAlunoForm(FlaskForm):
    matricula = IntegerField("matricula", validators=[DataRequired()])
    nome = StringField("nome", validators=[DataRequired()])
    curso = StringField("curso", validators=[DataRequired()])



class CadastroPecaForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])



class CadastroReservaForm(FlaskForm):
    matriculaAluno = IntegerField("matriculaAluno", validators=[DataRequired()])
    pecanome = StringField("pecanome", validators=[DataRequired()])



class DeleteAlunoForm(FlaskForm):
    matricula = IntegerField("matricula", validators=[DataRequired()])



class DeletePecaForm(FlaskForm):
    id = IntegerField("id", validators=[DataRequired()])

    

class DeleteReservaForm(FlaskForm):
    id = IntegerField("id", validators=[DataRequired()])    