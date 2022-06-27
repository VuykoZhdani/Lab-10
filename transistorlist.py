from doublelinkedlist import DoubleLinkedList
from transistor import Transistor


class TransistorList(DoubleLinkedList):

    def sort_by_current(self, /, rise=True) -> None:

        self.sort(lambda a, b: TransistorList.current_comparator(a, b, rise))

    def sort_by_type(self, /, rise=True) -> None:
        self.sort(lambda a, b: TransistorList.type_comparator(a, b, rise))

    def search_by_model(self, model: str) -> Transistor | None:
        for i in self:
            if i.model == model:
                return i

    def current_comparator(a: Transistor, b: Transistor, rise: bool) -> Transistor:
        result_bool = a.max_current > b.max_current
        if rise:
            result_bool = not result_bool
        if result_bool:
            return a
        else:
            return b

    def type_comparator(a: Transistor, b: Transistor, rise: bool) -> Transistor:
        result_bool = a.type > b.type
        if rise:
            result_bool = not result_bool
        if result_bool:
            return a
        else:
            return b
