# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 08:06:06 2026

Crifra de César sobte textos comuns.

Essa separação é a ideia de David Parnas (1972): cada módulo esconde uma decisão do projeto.

@author: Marcos Santana
"""

# Alfabeto importado do português Brasil
MAIUSCULAS: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MINUSCULAS: str = "abcdefghijklmnopqrstuvwxyz"
TAMANHO_DO_ALFABETO: int = len(MAIUSCULAS)

def effective_key(key: int) -> int:
    """Reduz a chave ao intervalo de 0 a 25.

    Parameters
    ----------
    chave : int
        Chave da cifra que o usuário insere.

    Returns
    -------
    int
        Retorna a chave modularizada com o tamanho do alfabeto.
        
    >>> effective_key(3)
    3
    >>> effective_key(29)
    3
    >>> effective_key(-3)
    23
    >>> effective_key(26)
    0
    """
    
    return key % TAMANHO_DO_ALFABETO
    
def is_shifted(character: str) -> bool:
    """Indicates whether a character should be shifted by the algorithm.

    Parameters
    ----------
    charactere : str
        DESCRIPTION.

    Returns
    -------
    bool
        DESCRIPTION.
        
    >>> is_shifted("A")
    True
    >>> is_shifted("z")
    True
    >>> is_shifted("á")
    False
    >>> is_shifted(" ")
    False
    >>> is_shifted("7")
    False
    """
    if character.casefold() in MINUSCULAS:
        return True
    else:
        return False
    
def shift_character(character: str, key: int) -> str:
    """Shift a character arround the alphabet 

    Parameters
    ----------
    character : str
        DESCRIPTION.
    key : int
        DESCRIPTION.

    Returns
    -------
    str
        DESCRIPTION.
        
    >>> shift_character("A", 3)
    'D'
    >>> shift_character("z", 3)
    'c'
    >>> shift_character("A", -3)
    'X'
    >>> shift_character("á", 3)
    'á'
    """
    key = effective_key(key)
    
    if not is_shifted(character):
        return character
    
    if character in MAIUSCULAS:
        alphabet = MAIUSCULAS
    else:
        alphabet = MINUSCULAS
    
    original_index = alphabet.index(character)
    shiftedindex = (original_index + key) % TAMANHO_DO_ALFABETO
    
    return alphabet[shiftedindex]

def cipher(text: str, key: int) -> str:
    """
    SUMMARY.

    Parameters
    ----------
    text : str
        DESCRIPTION.
    key : int
        DESCRIPTION.

    Returns
    -------
    str
        DESCRIPTION.
        
    >>> cipher("xyz", 3)
    'abc'
    >>> cipher("xyz", 0)
    'xyz'
    >>> cipher(" á", 3)
    ' á'
    """
    
    key = effective_key(key)
    result = ''
    for character in text:
        result += shift_character(character, key)
        
    return result

def decipher(text: str, key: int) -> str:
    """
    SUMMARY.

    Parameters
    ----------
    text : str
        DESCRIPTION.
    key : int
        DESCRIPTION.

    Returns
    -------
    str
        DESCRIPTION.
        
    >>> decipher("abc", 3)
    'xyz'
    """
    
    return cipher(text, -key)
    
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    
