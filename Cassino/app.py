from abc import ABC, abstractmethod
import itertools
import random
from time import sleep
import os
import matplotlib.pyplot as plt


def BaseMachine(ABC):
    @abstractmethod
    def _gen_permutations(self):
        ...

    @abstractmethod
    def _get_final_result(self):
        ...

    @abstractmethod
    def _display(self):
        ...

    @abstractmethod
    def _check_result_user(self):
        ...

    @abstractmethod
    def update_balance(self):
        ...

    @abstractmethod
    def emojisize(self):
        ...

    @abstractmethod
    def gain(self):
        ...

    @abstractmethod
    def play(self, amount_bet, player):
        ...

class Player:
    def __init__(self, balance = 0):
        self.balance = balance

class CassaNiquel:
    def __init__(self, level=1, balance = 0):
        self.SIMBOLOS = {
            'money_mouth_face': '1F911',
            'cold_face': '1F62D',
            'alien_face': '1F47D	',
            'heart_on_fire': 'FE0F',
            'colission': '1F4A5'
        }

        self.level = level
        self.permutations = self._gen_permutations()
        self.balance = balance
        self.initial_balance = self.balance

    def _gen_permutations(self):
        # Escolher emojis
        permutations = list(itertools.product(self.SIMBOLOS.keys(), repeat=3))
        # Aumentando as chances do usuário ganhar, para convence-lo de continuar
        # jogando (vicio) 1/13 de vencer ANTES ERA 1/25

        for j in range(self.level):  # para cada level do usuário, aumente a dificuldade
            for i in self.SIMBOLOS.keys():
                permutations.append((i, i, i))
        return permutations

    def _get_final_result(self):
        # Se existe a variavel permutations
        if not hasattr(self, 'permutations'):
            self.permutations = self._gen_permutations()
        # Pegar algum v alor aleatório das 130 casos
        result = list(random.choice(self.permutations))

        # set tranforma em um conjunto; conjuntos não podem ter dados repetidos;
        if len(set(result)) == 3 and random.randint(0, 5) >= 2:
            result[1] = result[0]
        return result


    # Exibir resultado; tempo de execução da roleta na exibição
    def _display(self, amount_bet, result, time=0.1):
        seconds = 1
        for i in range(0, int(seconds/time)):
            print(self._emojize(random.choice(self.permutations)))
            sleep(time)
            os.system('cls')
        print(self._emojize(result))


    #MESSAGEN AO USUARIO
        if self._check_result_user(result):
            print(f'Você ganhou: {amount_bet*3}')
    # Tirar aspas do resultado
        else:
            print("Por pouco! Tente mais uma vez!")


    def _emojize(self, emojis):
        return ''.join(tuple(chr(int(self.SIMBOLOS[code], 16)) for code in emojis))


    #AVALIA OS SIMBOLOS
    def _check_result_user(self, result):
        x = [result[0] == x for x in result]
        # all retorna True somente todos os 3 simbolos forem iguais
        # Retorna True if todos sao iguais ao primeiro x = result[0] senao...
        return True if all(x) else False
    
    #ATUALIZA O SALDO

    def _update_balance(self, amount_bet, result, player: Player):
        if self._check_result_user(result):
            #Se ganhei subtrai o valor apostado da máquina
            self.balance -= (amount_bet*3)
            player.balance += (amount_bet*3)
        else:
            #Se perdi adiciona a máquina
            self.balance += amount_bet
            player.balance -= amount_bet
    
    #Pegar resultado da jogada
    def play(self, amount_bet, player: Player):
        result = self._get_final_result()
      #  self._display(amount_bet, result)
        self._update_balance(amount_bet, result, player)
        
    @property
    def gain(self):
        return self.initial_balance + self.balance

maquina1 = CassaNiquel(level=6)

''' 
maquina1.play(10)
maquina1.play(10)
maquina1.play(10)
maquina1.play(10)
'''



JOGADORES_POR_DIA = 100
APOSTAS_POR_DIA = 5
DIAS = 5
VALOR_MAXIMO = 200

#saldo da máquina de caça-níqueo
saldo = []

players = [Player() for i in range(JOGADORES_POR_DIA)]

#Para cada qtd de apostas por dia
for i in range(0, DIAS):
    #calcule quantos jogadores ...
    for j in players:
        #apostam entre 1 a 5 vezes por dia...
        for k in range(0, random.randint(1, APOSTAS_POR_DIA)):
            #De 5 à 200 reais
            maquina1.play(random.randint(5, VALOR_MAXIMO), j)
    saldo.append(maquina1.gain)
    
#Gerar gráfico
plt.figure()
#Do dia 1 ate o dia 5
x = [i for i in range(1, DIAS + 1)] #1,2,3,4 + 1 = 5 dias

plt.plot(x, saldo)
#Exibir gráfico
plt.show()

plt.plot([i for i in range(JOGADORES_POR_DIA)], [i.balance for i in players])
plt.grid(True)
plt.show()