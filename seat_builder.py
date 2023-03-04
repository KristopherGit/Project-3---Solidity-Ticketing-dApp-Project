import tkinter as tk
from tkinter import ttk
import tkinter.simpledialog as simpledialog
import plotly.graph_objects as go
#from tkmacosx import Button


class SeatGenerator(tk.Frame):

    def __init__(self, master, rows=25, cols=25):
        tk.Frame.__init__(self, master)
        # self.master is parent widget/window -> which is passed onto the SeatGenerator class obj
        self.master = master
        self.rows = rows
        self.cols = cols
        self.gallery = {}
        self.traces = []

        # create a grid of buttons
        self.buttons = []
        # run for-loop to build out buttons across the row (by col index) and then by row as the parent for-loop
        # creates a 2D grid list
        for row in (range(rows)):
            button_row = []
            for col in (range(cols)):
                button = tk.Button(self.master, width=1, height=1,
                                   text=f"({col},{row})",
                                   font=('monospace', 8),
                                   command=lambda row=row, col=col: self.seat_button_action(row, col))
                button.grid(row=row, column=col, padx=1, pady=1)
                button_row.append(button)
            self.buttons.append(button_row)

    def seat_button_action(self, row, col):
        # get button at specific row/column address
        button = self.buttons[row][col]

        # user prompted to enter seat name
        seat_name = simpledialog.askstring(
            'Enter Seat Name', 'Please Enter Seat Name:')

        # if seat_name exists (i.e. if the user instantiates and creates a seat name label, from the above simpledialog)
        if seat_name:
            # add seat to gallery if selected by the user creating the venue layout via grid
            seat = {
                'aisle': col,
                'row': row,
                'name': seat_name,
                'color': '#1E90FF'
            }
            # add seat to gallery whereby 'seat_name' is the key, 'seat' dict obj becomes value
            self.gallery[seat_name] = seat

            #self.gallery[button['text']]['name'] = seat_name
            #print('Current background color:', button.cget('bg'))
            # overwrite the button text with seat_name for clarity
            # (text=seat_name, bg=seat['color'])
            # button.configure(bg=seat['color'], text=seat_name)
            button.configure(fg='#1E90FF', text=seat_name)
            # button = Button(bg='#1E90FF', text=seat_name)
            button.update()
            print('Current background color:', button.cget('bg'))

            # update the color of the seat button
            #seat['color'] = button.cget('bg')

            # update seat name in gallery
            self.gallery[seat_name]['name'] = seat_name

            # instantiate a trace to be added to the traces = [] list
            trace = go.Scatter(
                x=[seat['aisle']],
                y=[seat['row']],
                mode='markers',
                marker=dict(size=6, color=seat['color']),
                textfont=dict(size=20)
            )
            self.traces.append(trace)

            # background color of the button after changes made
            print('new background color:', button.cget('bg'))


if __name__ == '__main__':

    # create instance of the tkinter application
    root = tk.Tk()
    root.title("Venue Layout & Seat Generator App")

    # instantiate SeatGenerator class
    seatGen = SeatGenerator(root)
    seatGen.grid()

    # initiate loop
    root.mainloop()

    # create canvas to reside on master as template for grid layout
    # def create_canvas(self):
    #     self.canvas = tk.Canvas(self.master, width=self.cols * (self.seat_width +
    #                             self.padding), height=self.rows * (self.seat_height + self.padding))
    #     self.canvas.pack()

    # # instantiating each seat with loop assigning x,y-coord & name of each seat based on aisle (x) and row (y) value
    #     for x in range(self.cols):
    #         for y in range(self.rows):
    #             seat = {
    #                 'aisle': x,
    #                 'row': y,
    #                 'name': f'{x}, {y}',
    #                 'color': '#1E90FF'
    #             }
    #             # add seat to gallery (key is the seat name, value is seat dict obj)
    #             self.gallery[seat['name']] = seat

    #             # create button for current seat
    #             button = tk.Button(
    #                 self.canvas, bg=seat['color'], command=lambda seat=seat: self.seat_button_action(seat))

    #             # position & set button at specific position on the canvas grid
    #             button.place(
    #                 x=x*(self.seat_width + self.padding) + self.padding,
    #                 y=y*(self.seat_width + self.padding) + self.padding,
    #                 width=self.seat_width,
    #                 height=self.seat_height
    #             )
