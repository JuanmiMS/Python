class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # qué items hay en este if? => clases
            item.update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Interfaz():

    def update_quality(self):
        # Comportamiento a implementar en las subclases
        pass

class NormalItem(Item, Interfaz):
    # Herencia múltiple

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def setSell_in(self):
        self.sell_in = self.sell_in - 1

    def setQuality(self, valor):
        if self.quality + valor > 50:
            self.quality = 50
        elif self.quality + valor >= 0:
            self.quality = self.quality + valor
        else:
            self.quality = 0
        assert 0 <= self.quality <= 50, "quality de %s fuera de rango" % self.__class__.__name__

    # Override metodo update_quality de la interfaz
    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)
        self.setSell_in()

class AgedBrie(NormalItem):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)


    # Override metodo setQuality de NormalItem
    def setQuality(self, valor):
        NormalItem.setQuality(self, valor)
        # assert 0 <= self.quality <= 50, "quality de %s fuera de rango" % self.__class__.__name__

    # Override metodo update_quality de la Interfaz
    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)
        self.setSell_in()

if __name__ == '__main__':
    quesoBrie = AgedBrie('Aged Brie', 2, 0)
    print('Día 0', 'valor: ', quesoBrie.name, quesoBrie.sell_in, quesoBrie.quality)
    contador = 1
    while contador != 5:
        quesoBrie.update_quality()
        print('Día', contador, 'valor: ', quesoBrie)
        contador += 1

    assert quesoBrie.sell_in == -2, 'No'
