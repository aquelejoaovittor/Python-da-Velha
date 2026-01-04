# 🎮 Jogo da Velha em Python

Um jogo da velha clássico feito em Python que roda direto no terminal. Perfeito para passar o tempo ou aprender como funciona um jogo por trás dos panos.

 🔥 O que tem de legal?

- **Joga no terminal** - sem instalar nada complicado, só precisa do Python
- **Super simples** - digita um número e já era
- **Funciona em qualquer PC** - Windows, Linux, Mac... tanto faz
- **Código limpo** - dá pra entender tudo mesmo se não for expert em Python

# 🚀 Vamos começar?

# 1. Primeiro, baixa o arquivo
Salva o código num arquivo chamado `jogo_da_velha.py` ou clona direto:

git clone https://github.com/seu-usuario/jogo-da-velha.git
cd jogo-da-velha
```

# 2. Roda o jogo

python jogo_da_velha.py

Se não funcionar com `python`, tenta com `python3`.

## 🎯 Como joga?

É bem fácil:

1. O tabuleiro tem posições de 1 a 9:
   
   1 | 2 | 3
  ---+---+---
   4 | 5 | 6
  ---+---+---
   7 | 8 | 9
   

2. Você vai ver isso no terminal:
   
   Vez do Jogador X
   Escolha uma posição (1-9):
   

3. Digita o número da posição onde quer jogar

4. O jogo alterna entre "X" e "O" automaticamente

5. Ganha quem conseguir fazer uma linha com 3 iguais (na horizontal, vertical ou diagonal)

# 💡 Dicas

- O "X" sempre começa
- Não pode jogar em posição que já tá ocupada
- Se encher todas as posições sem ninguém ganhar, deu velha!
- A tela limpa sozinha a cada jogada pra ficar mais organizado

# 🛠️ Quer mexer no código?

O código tá bem organizado:

- JogoDaVelha - classe principal que controla tudo
- imprimir_tabuleiro() - mostra o tabuleiro bonitinho
- verificar_vitoria() - checa se alguém ganhou
- jogar() - é onde a mágica acontece, o loop principal do jogo

Se quiser dar uma incrementada:
- Troca os "X" e "O" por outros símbolos
- Adiciona cores no terminal
- Faz um placar que conta vitórias
- Cria um modo contra o computador

# ❓ Problemas?

"Não encontrei o comando python"
- Tenta `python3 jogo_da_velha.py`
- Ou instala o Python primeiro: [python.org](https://python.org)

"Não consigo jogar"
- Tem que digitar só números de 1 a 9
- A posição tem que estar vazia
- Se der erro, o jogo te avisa e você tenta de novo


Tá liberado usar, modificar e compartilhar esse código. Se fizer algo legal com ele, me conta!

Feito com 💻 por [@aquelejoaovittor] - se curtir, dá uma estrelinha no repositório!

*"Às vezes as coisas simples são as mais divertidas"*
