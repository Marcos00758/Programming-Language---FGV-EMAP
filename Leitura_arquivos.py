# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 08:54:01 2026

@author: Marcos Santana
"""
"""Operações de leitura e escrita sobre o sistema_de_arquivos simulado.

Este módulo imita a parte do sistema operacional que cuida de arquivos, mas
sem tocar em disco algum. Os nomes das funções são propositalmente parecidos
com as operações reais - listar, ler, gravar, apagar - para que a troca por
arquivos de verdade, numa aula futura, seja apenas troca de implementação.

Funções cujo nome está no imperativo (gravar, apagar) MODIFICAM o acervo de
arquivos. As demais apenas consultam.
"""

__all__ = ["listar", "existe", "ler", "gravar", "apagar", "tamanho"]

_ARQUIVOS: dict[str, str] = {

    "recado.txt":
        "Olá Amiguinhos! Bom dia, como vão vocês?",

    "ordem.txt":
        "Lanche da EMAp atrasado em 30min, Capitão!",

    "aviso.txt":
        "Reunião dos oficiais do CDMC amanhã às nove horas.",

    # Este chegou cifrado, e ninguém informou a chave.
    "interceptado.txt":
        "Wjzsnãt àx staj mtwfx sf xfqf itx kzsitx.",
}

def listar(sufixo: str = "") -> list[str]:
    """Devolve os nomes do sistema_de_arquivos, em ordem alfabética.

    O sistema_de_arquivos NÃO é modificado.

    Parâmetros:
        sufixo: se informado, mantém apenas os nomes terminados por ele.

    Os exemplos abaixo não comparam a lista inteira, de propósito: o conjunto
    é mutável, e uma gravação feita antes do teste mudaria o resultado. Um
    exemplo que depende de estado global é um exemplo que falha sozinho.

    >>> "recado.txt" in listar()
    True
    >>> listar("nao-existe")
    []
    """
    encontrados = []

    for nome in _ARQUIVOS:
        if nome.endswith(sufixo):
            encontrados.append(nome)

    encontrados.sort()
    return encontrados

def existe(nome: str) -> bool:
    """Informa se há um arquivo com esse nome no sistema_de_arquivos.

    >>> existe("recado.txt")
    True
    >>> existe("recado.TXT")
    False
    """
    return nome in _ARQUIVOS

def ler(nome: str) -> str:
    """Devolve o conteúdo do arquivo indicado.

    O sistema_de_arquivos NÃO é modificado.

    Exige que o arquivo exista. Confira antes com existe(): um nome
    inexistente interrompe o programa, e o tratamento de erros ainda não faz
    parte do nosso repertório.

    >>> ler("ordem.txt")
    'Lanche da EMAp atrasado em 30min, Capitão!'
    """
    return _ARQUIVOS[nome]

def gravar(nome: str, conteudo: str) -> bool:
    """Guarda um conteúdo no sistema_de_arquivos sob o nome indicado.

    MODIFICA o conjunto de arquivos. Se o nome já existir, o conteúdo anterior
    é substituído sem aviso, como faria a gravação de um arquivo de verdade.

    Retorno:
        True se o nome era novo, False se algo foi substituído.

    >>> gravar("rascunho.txt", "teste")
    True
    >>> gravar("rascunho.txt", "outro")
    False
    >>> ler("rascunho.txt")
    'outro'
    >>> apagar("rascunho.txt")
    True
    """
    era_novo = nome not in _ARQUIVOS
    _ARQUIVOS[nome] = conteudo
    return era_novo

def apagar(nome: str) -> bool:
    """Remove um arquivo do sistema_de_arquivos.

    MODIFICA o sistema_de_arquivos.

    Retorno:
        True se havia algo para remover, False se o nome não existia.

    >>> apagar("nao-existe.txt")
    False
    """
    if nome not in _ARQUIVOS:
        return False

    del _ARQUIVOS[nome]
    return True

def tamanho(nome: str) -> int:
    """Devolve quantos CARACTERES o arquivo ocupa.

    Atenção: caracteres, não bytes. Um acento ocupa um caractere aqui e dois
    bytes em UTF-8 - a diferença foi discutida na aula de strings.

    >>> tamanho("ordem.txt")
    42
    """
    return len(ler(nome))

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
