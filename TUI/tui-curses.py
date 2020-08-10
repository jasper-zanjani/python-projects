import curses

data = [
  [i for i in range(10)],
  [i for i in range(10,20)],
  [i for i in range(20,30)],
]


screen = curses.initscr()

for row in range(len(data)):
  for col in range(len(data[row])):
    try:
      screen.addstr(col * 4, row * 2, str(pow(row,col)))
    except:
      curses.endwin()

screen.refresh()

curses.napms(2000)
curses.endwin()

