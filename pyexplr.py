import curses

from navigation import Navigation


def _explr(stdscr, obj):
    assert curses.has_colors()
    init_color_pairs()

    stdscr.clear()
    curses.curs_set(0)

    selection = Navigation(obj)

    print_obj(stdscr, obj, selection.expanded, selection.position)

    while True:
        c = stdscr.getch()
        if c == ord('q'):
            break
        elif c == curses.KEY_UP or c == ord('k'):
            selection.move_up()
        elif c == curses.KEY_DOWN or c == ord('j'):
            selection.move_down()
        elif c == curses.KEY_RIGHT or c == ord('l'):
            selection.expand()
        stdscr.clear()
        print_obj(stdscr, obj, selection.expanded, selection.position)
        stdscr.refresh()

    stdscr.clear()
    stdscr.refresh()


def init_color_pairs():
    # default
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    # selected
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)


def get_limited_repr(obj, limit):
    original = repr(obj)
    if len(original) > limit:
        return original[:limit - 3] + '...'
    return original


# TODO: refactor (Navigation refactoring)
def print_obj(stdsrc, obj, expanded, selection, zero_row=0, level=0):
    inner_rows = 0

    for row, el in enumerate(obj):

        if selection and len(selection) == 1 and selection[0][0] == row:
            color_pair = curses.color_pair(2)
        else: color_pair = curses.color_pair(1)

        indent = 3 * level
        stdsrc.addstr(zero_row + row + inner_rows, indent, str(row) + ':', color_pair)
        stdsrc.addstr(zero_row + row + inner_rows, indent + 4, get_limited_repr(el, 30), color_pair)
        stdsrc.addstr(zero_row + row + inner_rows, 50, str(type(el)), color_pair)

        if row in expanded:
            inner_rows += print_obj(stdsrc, obj[row], expanded[row],
                                    selection[1:] if selection[0][0] == row else None,
                                    zero_row=zero_row + inner_rows + row + 1,
                                    level=level + 1)

    return inner_rows + len(obj)


def pyexplr(obj):
    curses.wrapper(_explr, obj)
