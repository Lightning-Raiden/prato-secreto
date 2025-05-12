import random

pratos = ["strogonoff", "macarronada", "lasagna", "pizza", "sushi", "feijoada"]

prato_secreto = random.choice(pratos)

tentativas = 5

print(50*"-")
print("Descubra o prato secreto! Você terá 5 tentativas.")
print(50*"-")
print("")

for tentativa in range(1, tentativas + 1):
    palpite = input("Digite o seu palpite: ").lower()
    print("")

    if palpite == prato_secreto:
        print("Parabéns!! Você acertou!")
        print(f"Tentativa final: {tentativa} de {tentativas}")
        print("")
        break

    else:
        print(f"Você errou! Tentativas restantes: {tentativas - tentativa}")
        print("")

print(f"Fim de jogo! O prato secreto era: {prato_secreto}")