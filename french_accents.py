import tkinter as tk
from pyperclip import *

    
def make_button(character: str, r: int, c: int):
    tk.Button(
        text=character,
        width=3,
        height=1,
        bg="medium turquoise",
        fg="black",
        highlightcolor="DodgerBlue2",
        font=('Times', -40, 'bold'),
        borderwidth=6,
        command=lambda: copy(accent)
    ).grid(row=r, column=c)


window = tk.Tk()
window.title(":)")

icon = tk.PhotoImage(file='accents.png')
window.iconphoto(False, icon)

label = tk.Label(
    text="Accents! :)",
    fg="medium turquoise",
    bg="gray1",
    width=14,
    height=1,
    font=('Courier', -32, 'bold')
)
label.grid(row=0, column=0, columnspan=3)

make_button('è', 1, 0)
make_button('ê', 1, 1)
make_button('é', 1, 2)

make_button('à', 2, 0)
make_button('â', 2, 1)
make_button('ç', 2, 2)

make_button('î', 3, 0)
make_button('ô', 3, 1)
make_button('ù', 3, 2)

make_button('ï', 4, 0)
make_button('ë', 4, 1)
make_button('ü', 4, 2)

window.mainloop()
