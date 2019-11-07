from tkinter import Label, Frame, CENTER
import LOGICS.MOVE_FUNCTIONS as move
import LOGICS.INITIALIZE as start
import GUI.CONSTANTS_FOR_UI as cons


class GAME_UI_2048(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.matrix = [[]]
        self.grid()
        self.master.title('2048')
        self.master.bind('<Key>', self.key)
        self.commands = {cons.KEY_UP: move.move_up, cons.KEY_DOWN: move.move_down,
                         cons.KEY_LEFT: move.move_left, cons.KEY_RIGHT: move.move_right}

        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=cons.BACKGROUND_COLOR_GAME,
                           width=cons.SIZE, height=cons.SIZE)

        background.grid()
        for i in range(cons.GRID_LEN):
            grid_row = []
            for j in range(cons.GRID_LEN):
                cell = Frame(background, bg=cons.BACKGROUND_COLOR_CELL_EMPTY,
                             width=cons.SIZE // cons.GRID_LEN, height=cons.SIZE // cons.GRID_LEN)

                cell.grid(row=i, column=j, padx=cons.GRID_PADDING, pady=cons.GRID_PADDING)

                t = Label(master=cell, text="", bg=cons.BACKGROUND_COLOR_CELL_EMPTY,
                          justify=CENTER, font=cons.FONT, width=5, height=2)

                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix = start.start_game()
        start.add_new(self.matrix)
        start.add_new(self.matrix)

    def update_grid_cells(self):
        for i in range(cons.GRID_LEN):
            for j in range(cons.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text='', bg=cons.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number), fg=cons.CELL_COLOR_DICT[new_number],
                                                    bg=cons.BACKGROUND_COLOR_DICT[new_number])
        self.update_idletasks()

    def key(self, event):
        key = repr(event.char)
        if key in self.commands:
            self.matrix, changed = self.commands[repr(event.char)](self.matrix)
            if changed:
                start.add_new(self.matrix)
                self.update_grid_cells()

                if start.current_state(self.matrix) == 'WON:':
                    self.grid_cells[1][1].configure(text='YOU',
                                                    bg=cons.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text='WIN!',
                                                    bg=cons.BACKGROUND_COLOR_CELL_EMPTY)
                if start.current_state(self.matrix) == 'LOST':
                    self.grid_cells[1][1].configure(text='YOU',
                                                    bg=cons.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text='LOSE!',
                                                    bg=cons.BACKGROUND_COLOR_CELL_EMPTY)
