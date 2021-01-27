import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios', [
        [
            Usuario(nome='Victor', email='victor.augusto60@gmail.com'),
            Usuario(nome='Ana', email='ana@gmail.com')
        ],
        [
            Usuario(nome='Victor', email='victor.augusto60@gmail.com'),
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'victor.augusto60@gmail.com',
        'Primeiro envio de e-mail usando Python',
        'Olá! Tudo certo contigo?'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Victor', email='victor.augusto60@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'ana@gmail.com',
        'Primeiro envio de e-mail usando Python',
        'Olá! Tudo certo contigo?'
    )
    assert enviador.parametros_de_envio == (
        'ana@gmail.com',
        'victor.augusto60@gmail.com',
        'Primeiro envio de e-mail usando Python',
        'Olá! Tudo certo contigo?'
    )
