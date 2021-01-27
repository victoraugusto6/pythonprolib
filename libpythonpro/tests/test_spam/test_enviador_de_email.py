import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('remetente', ['', 'test'])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'victor_augusto_net2@hotmail.com',
            'Primeiro e-mail enviado usando Python',
            'Olá. Obrigado por insistir! Vai dar certo!!'
        )


@pytest.mark.parametrize('remetente', ['victor.augusto60@gmail.com', 'test@gmail.com'])
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'victor_augusto_net2@hotmail.com',
        'Primeiro e-mail enviado usando Python',
        'Olá. Obrigado por insistir! Vai dar certo!!'
    )
    assert remetente in resultado
