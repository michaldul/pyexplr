
# TODO: refactor

class Selection:
    def __init__(self, obj):
        self.obj = obj
        self.position = [[0, len(self.obj)]]
        self.expanded = {}

    def move_up(self):
        if self.position[-1][0] == 0:
            self.position = self.position[:-1] if len(self.position) > 1 else self.position[:1]
        else:
            self.position[-1][0] -= 1

    def move_down(self):
        if self.is_selection_expanded():
            self.position.append([0, len(self.get_selected())])
        elif self.position[-1][0] < self.position[-1][1] - 1:
            self.position[-1][0] += 1
        else:
            if len(self.position) == 1: return
            i = len(self.position) - 1
            while self.position[i][0] == self.position[i][1] - 1:
                i -= 1
            if i >= 0:
                self.position = self.position[:i + 1]
                self.position[-1][0] += 1

    def expand(self):
        selected = self.get_selected()
        if isinstance(selected, list):
            expd = self.expanded
            for i in self.position[:-1]:
                expd = expd[i[0]]
            expd[self.position[-1][0]] = {}

    def is_selection_expanded(self):
        expand = self.expanded
        for i in self.position:
            if i[0] in expand:
                expand = expand[i[0]]
            else:
                return False
        return True

    def get_selected(self):
        ref = self.obj
        for i in self.position:
            ref = ref[i[0]]
        return ref


def test_selection():
    s = Selection([1, [2, 3], 4])
    s.move_up()
    assert s.position == [[0, 3]]
    s.move_down()
    assert s.position == [[1, 3]]
    assert s.expanded == {}
    s.expand()
    assert s.expanded == {1: {}}
    s.move_down()
    assert s.position == [[1, 3], [0, 2]]
    s.move_up()
    assert s.position == [[1, 3]]
    s.move_down()
    s.move_down()
    s.move_down()
    assert s.position == [[2, 3]]
    s.move_down()
    assert s.position == [[2, 3]]

    print('navigation test passed')


# test_selection()
