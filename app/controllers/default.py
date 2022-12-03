from flask import render_template, flash
from app import app, db
from app.models.tables import Peca, Aluno, Reserva
from app.models.forms import CadastroAlunoForm, CadastroPecaForm, CadastroReservaForm, DeleteAlunoForm, DeletePecaForm, DeleteReservaForm

### Página Principal 

@app.route("/index")
@app.route("/")

def index():
    return render_template('index.html')


#Campo do Gerenciamento de Alunos

@app.route("/aluno")

def aluno():
    return render_template('aluno/aluno.html')


### Cadastrar Aluno

@app.route("/cadastro", methods=["GET","POST"])
def cadastro(): 
    form = CadastroAlunoForm()
    if form.validate_on_submit():
       r = Aluno(form.matricula.data, form.nome.data, form.curso.data)
       db.session.add(r)
       db.session.commit()
       flash("Aluno Cadastrado")
    return render_template("aluno/cadastro.html", form=form)  


### Deletar Aluno

@app.route("/deletealuno",  methods=["GET","POST"])
def deletealuno():
    form = DeleteAlunoForm()
    if form.validate_on_submit():
        r = Aluno.query.filter_by(matricula=form.matricula.data).first()
        db.session.delete(r)
        db.session.commit()
        flash("Aluno Excluído")
    return render_template("aluno/deletealuno.html", form=form)






### Campo do Gerenciamento de Peças

@app.route("/peca")
def peca():
    return render_template('peca/peca.html')


### Cadastrar Peça

@app.route("/cadastropeca", methods=["GET","POST"])
def cadastropeca():
    form = CadastroPecaForm()
    if form.validate_on_submit():
        r = Peca(nome=form.nome.data)
        db.session.add(r)
        db.session.commit()
        flash("Peça Cadastrada")
    return render_template('peca/cadastropeca.html', form=form)


### Deletar Peça

@app.route("/deletepeca",  methods=["GET","POST"])
def deletepeca():
    form = DeletePecaForm()
    if form.validate_on_submit():
        r = Peca.query.filter_by(id=form.id.data).first()
        db.session.delete(r)
        db.session.commit()
        flash("Peça Excluída")
    return render_template("peca/deletepeca.html", form=form)

## Visualizar Peças

@app.route("/viewpeca")
def viewpeca():
    v = Peca.query.all()
    return render_template('peca/viewpeca.html', v=v)






### Campo de gerenciamento de Reserva

@app.route('/reserva')
def reserva():
    return render_template('reserva/reserva.html')


### Cadastrar Reserva

@app.route("/reservapeca",  methods=["GET", "POST"])
def reservapeca():
    form = CadastroReservaForm()
    if form.validate_on_submit():
        p = Peca.query.filter_by(nome=form.pecanome.data).first()
        a = Aluno.query.filter_by(matricula=form.matriculaAluno.data).first()
        if p != None and a != None:
            if p.nome == form.pecanome.data and a.matricula == form.matriculaAluno.data:
                r = Reserva(form.matriculaAluno.data,form.pecanome.data )    
                db.session.add(r)
                db.session.commit()
                flash("Peça Reservada")
        else:
            flash("Peça não disponível")

    return render_template('reserva/reservapeca.html', form=form)


### Excluir Reservar

@app.route('/deletereserva', methods=["GET", "POST"])
def deletereserva():
    form = DeleteReservaForm()
    if form.validate_on_submit():
        r = Reserva.query.filter_by(id=form.id.data).first()
        db.session.delete(r)
        db.session.commit()
        flash("Reserva Excluída")
    return render_template('reserva/deletereserva.html', form=form)


## Vusuializar Reservas

@app.route('/viewreserva')
def viewreserva():
    v = Reserva.query.all()
    return render_template('reserva/viewreserva.html', v=v)

###Testes

@app.route("/delete/<info>")
@app.route("/delete", defaults={"info": None})
def delete(info):
    r = Aluno.query.filter_by(nome="Joãozin Rei Delas").first()
    db.session.delete(r)
    db.session.commit()
    return "OK"