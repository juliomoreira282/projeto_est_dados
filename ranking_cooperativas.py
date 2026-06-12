cooperativas = {
    "RecicleMais": 36,
    "CoopReci": 12,
    "MundoDaReciclagem": 20,
    "24hRecicle": 63,
    "UltraReciclagem": 49,
    "AGJReciclagem": 80
}

def podio_ranking_cooperativas(cooperativas: dict, n=3):
    coops_ranqueadas = dict(sorted(cooperativas.items(), key=lambda item: item[1], reverse=True))

    for indice, (chave, valor) in enumerate(coops_ranqueadas.items()):
        if indice >= n:
            break
        print(f"{indice + 1}. {chave}: {valor}")

podio_ranking_cooperativas(cooperativas)