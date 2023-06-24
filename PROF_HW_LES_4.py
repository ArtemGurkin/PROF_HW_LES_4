class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.current_list = 0
        self.current_ind = 0
        return self

    def __next__(self):
        if self.current_list < len(self.list_of_list):
            item = self.list_of_list[self.current_list][self.current_ind]
            self.current_ind += 1
            if self.current_ind >= len(self.list_of_list[self.current_list]):
                self.current_ind = self.current_ind = 0
                self.current_list += 1
            return item
        raise StopIteration

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(FlatIterator(list_of_lists_1), ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
        # print(flat_iterator_item, check_item)
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

import types


def flat_generator(list_of_lists):
    for i in list_of_lists:
        for j in i:
            yield j


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(flat_generator(list_of_lists_1),['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
        print(flat_iterator_item, check_item)

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()