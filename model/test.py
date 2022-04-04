from ycappuccino.core.model.decorators import Item, Property
from ycappuccino.core.model.model import Model


@Item(collection="tests",name="test", plural="tests")
class Test(Model):
    def __init__(self, a_dict):
        super().__init__(a_dict)
        self._name = None

    @Property(name="name")
    def name(self, a_value):
        self._name = a_value


@Item(collection="tests",name="test2",plural="tests2")
class TestExtend(Test):
    def __init__(self, a_dict):
        super().__init__(a_dict)
        self._name = None

    @Property(name="name2")
    def name2(self, a_value):
        self._name = a_value