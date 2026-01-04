import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [" " for _ in range(9)]
        self.jogador_atual = "X"

    def imprimir_tabuleiro(self):
        t = self.tabuleiro
        print(f"\n  {t[0]} | {t[1]} | {t[2]} ")
        print(" ---+---+---")
        print(f"  {t[3]} | {t[4]} | {t[5]} ")
        print(" ---+---+---")
        print(f"  {t[6]} | {t[7]} | {t[8]} \n")

    def verificar_vitoria(self):
        vitorias = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # Linhas
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # Colunas
            (0, 4, 8), (2, 4, 6)             # Diagonais
        ]
        for a, b, c in vitorias:
            if self.tabuleiro[a] == self.tabuleiro[b] == self.tabuleiro[c] and self.tabuleiro[a] != " ":
                return True
        return False

    def jogar(self):
        limpar_tela()
        print("=== Jogo da Velha em Python ===")

        while True:
            self.imprimir_tabuleiro()
            print(f"Vez do Jogador {self.jogador_atual}")

            try:
                escolha = int(input("Escolha uma posição (1-9): ")) - 1
                if escolha < 0 or escolha > 8:
                    print("Por favor, escolha um número entre 1 e 9.")
                    continue
                if self.tabuleiro[escolha] != " ":
                    print("Posição já ocupada!")
                    continue
            except ValueError:
                print("Entrada inválida. Digite um número.")
                continue

            # Realiza a jogada
            self.tabuleiro[escolha] = self.jogador_atual

            # Verifica vitória
            if self.verificar_vitoria():
                limpar_tela()
                self.imprimir_tabuleiro()
                print(f"Parabéns! O jogador {self.jogador_atual} venceu!")
                break

            # Verifica empate
            if " " not in self.tabuleiro:
                limpar_tela()
                self.imprimir_tabuleiro()
                print("O jogo terminou em empate (Velha)!")
                break

            # Troca de jogador
            self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.jogar()
