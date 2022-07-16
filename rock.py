#importanto o módulo "random" para que possamos utilizar duas funções
import random

#configurando a variável "winner"
winner = ''

#usando a função "randint" do módulo random
random_choice = random.randint(0,2)

#o computador faz a sua escolha aleatoariamente de acordo com o número gerado na função acima
if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

user_choice = ''
#verifica se a escolha do usuário foi inválida e a solicita novamente
while (user_choice != 'rock' and
        user_choice != 'paper' and
        user_choice != 'scissors'):
    user_choice = input('rock, paper or scissors? ')

#o bloco a seguir define o ganhador e o armazena na variável winner
if computer_choice == user_choice:
    winner = 'Tie'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'
else:
    winner = 'User'

#exibe a mensagem para caso de empate e senão, exibe a mensagem do ganhador junto com a escolha do computador.
if winner == 'Tie':
    print('We both chose', user_choice + ', play again.')
else:
    print(winner, 'won, I chose', computer_choice + '.')
