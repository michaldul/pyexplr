import curses


def _explr(stdscr, obj):
    assert curses.has_colors()
    init_color_pairs()

    stdscr.clear()
    curses.curs_set(0)

    selected = 0

    print_obj(stdscr, obj, selected)

    while True:
        c = stdscr.getch()
        if c == ord('q'):
            break
        elif c == curses.KEY_UP or c == ord('k'):
            selected = max(selected - 1, 0)
        elif c == curses.KEY_DOWN or c == ord('j'):
            selected = min(selected + 1, len(obj) - 1)
        print_obj(stdscr, obj, selected)
        stdscr.refresh()

    stdscr.clear()
    stdscr.refresh()


def init_color_pairs():
    # default
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    # selected
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)


def print_obj(stdsrc, obj, selected):
    for row, el in enumerate(obj):
        color_pair = curses.color_pair(2 if selected == row else 1)
        stdsrc.addstr(row, 0, str(row) + ':', color_pair)
        stdsrc.addstr(row, 3, str(el), color_pair)


def pyexplr(obj):
    curses.wrapper(_explr, obj)
