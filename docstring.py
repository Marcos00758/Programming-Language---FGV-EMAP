def contar(a, b=2, c=3):
    print(a,b,c)

contar(1,2,3)
print(contar.__defaults__)


def adicionar_musica(fila: list, musica: str) -> bool:
   """Adiciona uma música inédita ao final da fila.
    
    Vou colocar um texto muito criativo sobre a minha pessoa
    e sua história de vida.
    
    Parâmetros:
        fila: lista de strings, em ordem de execução, das músicas
        musica: string com o nome da música
        
    Retorno:
        True se a música foi adicionada
        False se não foi adicionda por ser vazia ou já existir
    """
    
   musica = musica.strip()
    
   if musica == "":
       return False
    
   for each_musica in fila:
       if each_musica.casefold() == musica.casefold():
           return False
   fila.append(musica)
   return True

def adicionar_musicas(fila, *musicas):
    
   for each_musica in musicas:
       adicionar_musica(fila, each_musica)
   return fila

fila_musica = []

print(adicionar_musica(fila_musica, "  Purple rain"))
print(adicionar_musica(fila_musica, "   Tempos Modernos"))
print(adicionar_musicas(fila_musica, "Roxo", "Azul", "Azul", "Amarelo"))
print(adicionar_musica.__annotations__)




