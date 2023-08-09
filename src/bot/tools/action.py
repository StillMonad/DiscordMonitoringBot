import random
from datetime import datetime


class Action:
    def __init__(self, name, guild, channel, action, message=""):
        self.time = datetime.now()
        self.name = name
        self.guild = guild
        self.channel = channel
        self.action = action
        self.message = message

    def __repr__(self):
        return (
            "[created='%s'] guild='%s', channel='%s', name='%s', action='%s', message='%s'"
            % (
                self.time,
                self.guild,
                self.channel,
                self.name,
                self.action,
                self.message,
            )
        )

    def verbose(self):
        if self.action in ["joined", "left"]:
            #  return f"{self.name} {self.action} channel {self.channel} in {self.guild}"
            return self.__randomize()
        elif self.action in ["message"]:
            return f"{self.name} sent message in channel {self.channel} in {self.guild}: {self.message}"
        else:
            return f"{self.name} {self.action}"

    # returning random phrases on join/leave events
    def __randomize(self):
        variants_join = [
            '{0} влетел с двух ног в комнату "{1}"... Без комментариев.',
            'Вы не поверите, кто наконец зашел в комнату "{1}"! {0}! ',
            'Открывайте форточки! {0} заходит в комнату "{1}"!',
            'Поздаровайтесь с {0}! Он уже в комнате "{1}"!',
            'Никто его не звал, но {0} уже в комнате "{1}"! Как всегда... ха!',
            'Ладно, раз пришел {0}, то надо валить из "{1}"...',
            'Встречайте... трррррр.... {0}!!! Из комнаты "{1}", при его появлении, выбежали даже тараканы.',
            'Бегите, гупцы! {0} завалился в комнату "{1}! Я его задержу... Претворюсь за- за- за- икой.',
            'Королевство обезьян в комнате "{1}" пополнилось еще одной обезъянкой. Вы можете звать его {0}.',
            'Следите за руками... Вжух, и я телепортировал {0} в комнату "{1}"!',
            "Падите ниц, чернь, ведь {0} уже зашел в {1}!",
            'Что это за навозная муха влетела в комнату "{1}? А... это всего лишь {0}..."',
            "{0} зашел в {1}. Прям слезы наворачиваются. Слезы отчаяния.",
            'Кусок мяса, ой, то есть {0}, зашел в комнату "{1}". Простите.',
            'Лучший человек! Первый среди живых организмов, {0}! Вся комната "{1}" бъется в конвульсиях восторга!',
            'Прям анекдот какой-то: заходят как-то в бар программист, политик и {0}. А это не бар, а "{1}"!',
        ]

        variants_leave = [
            'Все наконец выдохнули... {0} вышел из комнаты "{1}"...',
            'Комната "{1}"! Помахайте {0} на прощанье!',
            '{0} покинул в комнату "{1}". На ко нец то.',
            '{0} захотел сбежать из комнаты "{1}". И сбежал. Ха.',
        ]

        if self.action == "joined":
            return variants_join[random.randint(0, len(variants_join) - 1)].format(
                self.name, self.channel
            )
        elif self.action == "left":
            return variants_leave[random.randint(0, len(variants_leave) - 1)].format(
                self.name, self.channel
            )
