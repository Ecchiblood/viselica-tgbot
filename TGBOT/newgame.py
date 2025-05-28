import random

words = ['моча', 'пенис', 'говно', 'еблан', 'семен', 'эспрессо', 'хуй', 'карбюратор', 'машина', 'автомат', 'троллейбус', 'интерес']

class MyGame:
    def __init__(self):
        self.game_toggle = False

    def start(self):
        self.game_toggle = True
        self.used = []
        self.word = random.choice(words)
        self.censor = ['*'] * len(self.word)
        self.max = 5


    def info(self):
        msg =  ' '.join(self.censor)
        msg += f"\n Кол-во попыток: {self.max}"
        msg += f"\n Использованные буквы: {str(self.used)}"
        msg += "\n Введите букву"
        return msg

    def game_process(self, character):
        if character in self.used:
            return 'Вы уже использовали эту букву!'
        else:
            self.used.append(character)
            if character in self.word:
                msg = f"\n Эта буква есть в слове!\n"
                indxs = [i for i in range(len(self.word)) if self.word[i] == character]
                for indx in indxs:
                    self.censor[indx] = character
                if self.censor.count('*') == 0:
                    msg += f"\n Вы угадали слово: {' '.join(self.censor)}!"
                    self.game_toggle = False
                else:
                    msg += self.info()
            else:
                msg = f"\n Этой буквы нет в слове!\n"
                self.max = self.max - 1
                if self.max <= 0:
                    msg += f"\n Ты проиграл. Загаданное слово: {self.word}"
                    self.game_toggle = False
                else:
                    msg += self.info()
            return msg
