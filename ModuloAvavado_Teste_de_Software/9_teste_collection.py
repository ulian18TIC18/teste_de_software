import pytest

class Item:
    def __init__(self, name):
        self.name = name

class ItemCollection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if not item or not isinstance(item, Item):
            raise ValueError("Item must be a valid Item instance")
        self.items.append(item)

    def remove_item(self, item):
        if item not in self.items:
            raise ValueError("Item not found in the collection")
        self.items.remove(item)

    def get_items(self):
        return self.items
    
def teste_adicionar_item():
    colecao = ItemCollection()
    item = Item('item')
    colecao.add_item(item)
    assert item in colecao.get_items()

def teste_remover_item():
    colecao = ItemCollection()
    item = Item('item2')
    colecao.add_item(item)
    colecao.remove_item(item)
    assert item not in colecao.get_items()

def teste_item_invalido():
    colecao = ItemCollection()
    with pytest.raises(ValueError):
        colecao.add_item('Item_invalido')

def teste_remover_item_inexistente():
    colecao = ItemCollection()
    item = Item('item3')
    with pytest.raises(ValueError):
        colecao.remove_item(item)