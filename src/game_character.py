from dice import d


class Attribute:
    name = "Attribute"

    def __init__(self, value=None):
        self.value = value or self.roll()

    @classmethod
    def roll(cls):
        return d(1, 6)

    def test(self):
        """
        ПРОВЕРКА УДАЧИ: в некоторых местах тебе будет предложено ИСПЫТАТЬ УДАЧУ. Кинь один кубик: если полученное число
                        будет меньше твоей или равно УДАЧЕ, значит тебе повезло, если больше – не повезло. После каждой
                        проверки удача уменьшается на 1.

        :return:
        """
        result = d(1, 6) <= self.value
        return result

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)


class Strength(Attribute):
    """
    СИЛА: кинь один кубик, чтобы узнать начальное значение, и запиши его в поле «СИЛА» на ИГРОВОЙ КАРТЕ.
    """
    name = "Сила"


class Stamina(Attribute):
    """
    ВЫНОСЛИВОСТЬ: кинь один кубик, чтобы узнать начальное значение, и запиши его в поле «ВЫНОСЛИВОСТЬ» на ИГРОВОЙ
                  КАРТЕ.
    """
    name = "Выносливость"


class Luck(Attribute):
    """
    УДАЧА: кинь один кубик, чтобы узнать начальное значение, и запиши его в поле «УДАЧА» на ИГРОВОЙ КАРТЕ.
    """
    name = "Удача"

    def test(self):
        result = super().test()
        self.value -= 1
        return result


class GameCharacter:
    def __init__(self, strength=None, stamina=None, luck=None):
        """
        УРОН: сначала твой УРОН – 0,1.  Если ты найдешь какое нибудь оружие, то он может увеличиться. Если во время
              битвы ты наносишь удар противнику, то отними количество своего УРОНА от его ВЫНОСЛИВОСТИ, и наоборот.
        """
        self.strength = Strength(strength)
        self.stamina = Stamina(stamina)
        self.luck = Luck(luck)

        self.unarmed_damage = .1

        self.money = 50
        self.food = 0
        self.items = []
        self.weapon = None

    def reroll(self):
        self.strength = Strength()
        self.stamina = Stamina()
        self.luck = Luck()

        self.unarmed_damage = .1

        self.money = 50
        self.food = 0
        self.items = []
        self.weapon = None

    @property
    def damage(self):
        if self.weapon is not None:
            return self.weapon.damage
        return self.unarmed_damage

    def fight(self, enemy):
        """
        БИТВЫ:

        1. Во время битвы кинь один кубик и прибавь полученное число к своей СИЛЕ. Это твоя СИЛА УДАРА.
        2. Кинь кубик, и выпавшее число прибавь к СИЛЕ противника. Это его СИЛА УДАРА.
        3. Сравнит значения. Если твоя сила удара больше, ты отнимаешь от ВЫНОСЛИВОСТИ противника число, равное твоему
           УРОНУ.
        4. Повторяй пункты 1 – 3 до полной победы или поражения.

        :param enemy:
        :return:
        """
        while self.stamina.value > 0 and enemy.stamina.value > 0:
            player_attack = d(1, 6) + self.strength.value
            enemy_attack = d(1, 6) + enemy.strength.value
            if player_attack > enemy_attack:
                enemy.get_wound(self.damage)
            elif enemy_attack > player_attack:
                self.get_wound(enemy.damage)

    def get_wound(self, damage):
        self.stamina.value -= damage
        if self.stamina.value < 0:
            self.stamina.value = 0
