import random
import pickle
import os
import time
import string
import pygame

arquivo_dados_placas = 'dados_placas.pkl'

def gerar_placas():
    letras_1 = "".join(random.choices(string.ascii_uppercase, k=3))
    numero_1 = str(random.randint(0, 9))
    letra_2 = random.choice(string.ascii_uppercase)
    numeros_2 = "".join(random.choices(string.digits, k=2))

    return f"{letras_1}{numero_1}{letra_2}{numeros_2}"

if os.path.exists(arquivo_dados_placas):
    print(f"{arquivo_dados_placas} existe. Carregando valores armazenados.")
    with open(arquivo_dados_placas, 'rb') as arquivo_bin:
        lista_caminhoes = pickle.load(arquivo_bin)

else:
    print(f"{arquivo_dados_placas} não existe. Criando novos valores.")
    tamanho_lista = 3000

    lista_caminhoes = []
    while len(lista_caminhoes) < tamanho_lista:
        placa = gerar_placas()
        if placa not in lista_caminhoes:
            lista_caminhoes.append(placa)

    with open(arquivo_dados_placas, 'wb') as arquivo_bin:
        pickle.dump(lista_caminhoes, arquivo_bin)
    print("Novos valores criados com sucesso.")

pygame.init()
largura, altura = 800, 300
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Comparação Inserir No Final X No Início")

fonte_titulo = pygame.font.SysFont("arial", 28, bold=True)
fonte_texto = pygame.font.SysFont("arial", 22)

mensagem = "Pressione [ESQUERDA] p/ início ou [DIREITA] p/ final"
resultado_tempo = ""
estado_lista = f"Tamanho atual: {len(lista_caminhoes)}"

executando = True
while executando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                inicio_t = time.perf_counter()
                nova_placa = gerar_placas()
                lista_caminhoes.insert(0, nova_placa)
                fim_t = time.perf_counter()
                tempo_execucao = fim_t - inicio_t
                
                mensagem = f"Placa [{nova_placa}] adicionada no início."
                resultado_tempo = f"Tempo: (O(n)): {tempo_execucao:.9f} seg."

            elif event.key == pygame.K_RIGHT:
                inicio_t = time.perf_counter()
                nova_placa = gerar_placas()
                lista_caminhoes.append(nova_placa)
                fim_t = time.perf_counter()
                tempo_execucao = fim_t - inicio_t

                mensagem = f"Placa [{nova_placa}] adicionada ao final."
                resultado_tempo = f"Tempo: (O(1)): {tempo_execucao:.9f} seg."

        estado_lista = f"Tamanho atual: {len(lista_caminhoes)}"

    tela.fill((30, 30, 30))

    tela.blit(fonte_titulo.render("Comparação de Desempenho Append X Insert 0", True, (255, 255, 255)), (30, 40))
    tela.blit(fonte_texto.render(mensagem, True, (200, 200, 200)), (30, 100))
    tela.blit(fonte_texto.render(resultado_tempo, True, (100, 255, 100)), (30, 140))
    tela.blit(fonte_texto.render(estado_lista, True, (200, 200, 200)), (30, 180))

    pygame.display.flip()

pygame.quit()