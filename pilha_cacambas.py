pilha_cacambas = ["Caçamba 1", "Caçamba 2", "Caçamba 4", "Caçamba 7"]

print("\nMenu de Comandos")
print("Digite 'A' para adicionar uma caçamba à pilha.")
print("Digite 'P' para remover uma caçamba da pilha.")
print("Digite 'V' para ver a caçamba do topo da pilha.")
print("Digite 'S' para sair.")

def adicionar_cacamba(cacamba: str):
    if cacamba.startswith("Caçamba"):
            pilha_cacambas.append(cacamba)
            print(f"Caçamba adicionada: {cacamba}")

def remover_cacamba():
    cacamba_removida = pilha_cacambas.pop()
    print(f"Caçamba removida: {cacamba_removida}")

while True:
    comando = input("Comando: ").strip()
    if comando.lower() == 's':
        print("Encerrando...")
        break

    elif comando.lower() == 'a':
        cacamba = input("Qual caçamba deseja adicionar? (Formato: Caçamba + Número) \n").capitalize()
        adicionar_cacamba(cacamba)

    elif comando.lower() == 'p':
        remover_cacamba()

    elif comando.lower() == 'v':
        cacamba_topo = pilha_cacambas[-1]
        print(f"Caçamba do topo: {cacamba_topo}")

    else:
        print("O comnado não existe. Tente novamente.")