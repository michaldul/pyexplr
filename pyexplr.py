import curses

def _explr(stdscr, obj):
    stdscr.clear()
    curses.curs_set(0)

    print_obj(stdscr, obj)

    while True:
        c = stdscr.getch()
        if c == ord('q'):
            break

        print_obj(stdscr, obj)
        stdscr.refresh()

    stdscr.clear()
    stdscr.refresh()


def print_obj(stdsrc, obj):
    for row, el in enumerate(obj):
        stdsrc.addstr(row, 0, str(row) + ':')
        stdsrc.addstr(row, 3, str(el))


def pyexplr(obj):
    curses.wrapper(_explr, obj)

