jogador = ("Herói", 100, 15)
lista = []
for item in range(len(jogador)):
    if item == 1:
        elemento = jogador[item] - 30
    else:
        elemento = jogador[item]
    lista.append(elemento)
jogador = tuple(lista)
print(jogador)


def ponto_extremo(pontos):
    maximo_atual = pontos[0][0]
    for coordenada in pontos:
        maximo_atual = max(coordenada[0], maximo_atual)
    for index in range(len(pontos)):
        if maximo_atual == pontos[index][0]:
            elemento = pontos[index]
    return elemento
pontos = [(1,3), (5,8), (-1,10), (18,2)]
print(ponto_extremo(pontos))



resultados = [("Time A", 3), ("Time B", 1), ("Time C", 3)]
lista_times = []
def achar_time(resultados):
    maximo_time = resultados[0][1]
    for ordem in resultados:
        maximo_time = max(ordem[1], maximo_time)
    for time in resultados:
        if time[1] == maximo_time:
            lista_times.append(time[0])
    return lista_times
print(achar_time(resultados))

trajeto = [(0,0), (3,4), (3,8), (0,8)]
def distancia(trajeto):
    distancia = 0
    for i in range(len(trajeto)):
        distancia += ((trajeto[i][0]-trajeto[i+1][0])**2 + 
                     (trajeto[i][1]-trajeto[i+1][1])**2) ** 0.5
        return distancia
print(distancia(trajeto))



        