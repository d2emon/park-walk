def no_action(player):
    pass


class Article:
    def __init__(self, article_id=None, text="", links=(), action=None, shop=None):
        self.article_id = article_id
        self.text = text
        self.links = links
        self.action = action or no_action
        self.shop = shop

    def __str__(self):
        return self.text


class Link:
    def __init__(self, text="", article_id=None):
        self.text = text
        self.article_id = article_id

    def __str__(self):
        return self.text


class GameItem:
    def __init__(self, name, value=0, damage=None):
        self.name = name
        self.value = value
        self.damage = damage

    def __str__(self):
        return self.name


class Shop:
    def __init__(self, *goods):
        self.goods = goods
