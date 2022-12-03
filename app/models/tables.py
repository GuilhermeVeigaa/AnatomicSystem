from app import db



class Curso(db.Model):
    __tablename__ = "cursos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return "<Curso %r>" % self.nome 



class Aluno(db.Model):
    __tablename__ = "alunos"

    matricula = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    curso_nome = db.Column(db.String, db.ForeignKey('cursos.nome'))

    curso = db.relationship('Curso', foreign_keys=curso_nome)

    def __init__(self, matricula, nome, curso_nome):
        self.matricula = matricula
        self.nome = nome
        self.curso_nome = curso_nome

    def __repr__(self):
        return "<Aluno %r>" % self.nome




class Peca(db.Model):
    __tablename__ = "peças"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return "%r" % self.nome 



class Reserva(db.Model):
    __tablename__ = "reservas"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    aluno_matricula = db.Column(db.Integer, db.ForeignKey('alunos.matricula'))
    peca_nome = db.Column(db.String, db.ForeignKey('peças.nome'))

    aluno = db.relationship('Aluno', foreign_keys=aluno_matricula)
    curso = db.relationship('Peca', foreign_keys=peca_nome)

    def __init__(self, aluno_matricula, peca_nome):
        self.aluno_matricula = aluno_matricula
        self.peca_nome = peca_nome

    def __repr__(self):
        return "<Reserva %r>" % self.id 
