from data import articles
from game_character import GameCharacter


class Game:
    def __init__(self):
        self.player = GameCharacter()
        self.article = None

        self.show_player()
        self.load_article(0)

    def show_inventory(self):
        for item_id, item in enumerate(self.player.items):
            print("{}. {}".format(item_id, item))

    def show_player(self):
        for attribute in [self.player.strength, self.player.stamina, self.player.luck]:
            print("{}:\t{}".format(attribute.name, attribute))
        print("Деньги:\t{}".format(self.player.money))
        self.show_inventory()

    def show_article(self):
        print("{}".format(self.article))
        self.show_shop()
        for link_id, link in enumerate(self.article.links):
            print("{}. {}".format(link_id, link))

    def show_shop(self):
        if self.article.shop is None:
            return
        shop = self.article.shop
        print("Товар\tцена в рублях")
        for item_id, item in enumerate(shop.goods):
            print("{}. {}\t{}".format(item_id, item, item.value))
        print("Чтобы что – нибудь купить, вычеркни на своей ИГРОВОЙ КАРТЕ необходимую сумму денег, и впиши купленный "
              "предмет.")

    def load_article(self, article_id):
        self.article = articles[article_id]
        self.article.action(self.player)
        self.show_article()

    def go_link(self, link_id=None):
        if link_id is None:
            return
        if link_id < 0:
            return
        if link_id >= len(self.article.links):
            return
        self.load_article(self.article.links[link_id].article_id)

    def buy(self, item_id=None):
        if self.article.shop is None:
            return
        if item_id is None:
            return
        if item_id < 0:
            return
        if item_id >= len(self.article.shop.goods):
            return
        item = self.article.shop.goods[item_id]
        if self.player.money < item.value:
            return
        self.player.money -= item.value
        self.player.items.append(item)
