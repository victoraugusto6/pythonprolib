from unittest.mock import Mock
import pytest
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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'victor.augusto60@gmail.com',
        'Primeiro envio de e-mail usando Python',
        'Olá! Tudo certo contigo?'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Victor', email='victor.augusto60@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'ana@gmail.com',
        'Primeiro envio de e-mail usando Python',
        'Olá! Tudo certo contigo?'
    )
    enviador.enviar.assert_called_once_with(
        'ana@gmail.com',
        'victor.augusto60@gmail.com',
        'Primeiro envio de e-mail usando Python',
        'Olá! Tudo certo contigo?'
    )
