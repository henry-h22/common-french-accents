import tkinter as tk
import pyperclip as pc


def copyy(a):
    pc.copy(a)

    
def make_button(accent: str, r: int, c: int):
    tk.Button(
        text=accent,
        width=3,
        height=1,
        bg="medium turquoise",
        fg="black",
        highlightcolor="DodgerBlue2",
        font=('Times', -40, 'bold'),
        borderwidth=6,
        command=lambda: copyy(accent)
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

e_grave = tk.Button(
    text="è",
    width=3,
    height=1,
    bg="medium turquoise",
    fg="black",
    highlightcolor="DodgerBlue2",
    font=('Times', -40, 'bold'),
    borderwidth=6,
    command=lambda: copyy("è")
)
e_grave.grid(row=1, column=0)

e_aigu = tk.Button(
    text="é",
    width=3,
    height=1,
    bg="medium turquoise",
    fg="black",
    highlightcolor="DodgerBlue2",
    font=('Times', -40, 'bold'),
    borderwidth=6,
    command=lambda: copyy("é")
)
e_aigu.grid(row=1, column=2)

e_hat = tk.Button(
    text="ê",
    width=3,
    height=1,
    bg="medium turquoise",
    fg="black",
    highlightcolor="DodgerBlue2",
    font=('Times', -40, 'bold'),
    borderwidth=6,
    command=lambda: copyy("ê")
)
e_hat.grid(row=1, column=1)

a_grave = tk.Button(
    text="à",
    width=3,
    height=1,
    bg="medium turquoise",
    fg="black",
    highlightcolor="DodgerBlue2",
    font=('Times', -40, 'bold'),
    borderwidth=6,
    command=lambda: copyy("à")
)
a_grave.grid(row=2, column=0)

c_ween = tk.Button(
    text="ç",
    width=3,
    height=1,
    bg="medium turquoise",
    fg="black",
    highlightcolor="DodgerBlue2",
    font=('Times', -40, 'bold'),
    borderwidth=6,
    command=lambda: copyy("ç")
)
c_ween.grid(row=2, column=2)

a_hat = tk.Button(
    text="â",
    width=3,
    height=1,
    bg="medium turquoise",
    fg="black",
    highlightcolor="DodgerBlue2",
    font=('Times', -40, 'bold'),
    borderwidth=6,
    command=lambda: copyy("â")
)
a_hat.grid(row=2, column=1)

i_hat = tk.Button(
    text="î",
    width=3,
    height=1,
    bg="medium turquoise",
    fg="black",
    highlightcolor="DodgerBlue2",
    font=('Times', -40, 'bold'),
    borderwidth=6,
    command=lambda: copyy("î")
)
i_hat.grid(row=3, column=0)

o_hat = tk.Button(
    text="ô",
    width=3,
    height=1,
    bg="medium turquoise",
    fg="black",
    highlightcolor="DodgerBlue2",
    font=('Times', -40, 'bold'),
    borderwidth=6,
    command=lambda: copyy("ô")
)
o_hat.grid(row=3, column=1)

u_grave = tk.Button(
    text="ù",
    width=3,
    height=1,
    bg="medium turquoise",
    fg="black",
    highlightcolor="DodgerBlue2",
    font=('Times', -40, 'bold'),
    borderwidth=6,
    command=lambda: copyy("ù")
)
u_grave.grid(row=3, column=2)

i_dots = tk.Button(
    text="ï",
    width=3,
    height=1,
    bg="medium turquoise",
    fg="black",
    highlightcolor="DodgerBlue2",
    font=('Times', -40, 'bold'),
    borderwidth=6,
    command=lambda: copyy("ï")
)
i_dots.grid(row=4, column=0)

e_dots = tk.Button(
    text="ë",
    width=3,
    height=1,
    bg="medium turquoise",
    fg="black",
    highlightcolor="DodgerBlue2",
    font=('Times', -40, 'bold'),
    borderwidth=6,
    command=lambda: copyy("ë")
)
e_dots.grid(row=4, column=1)

u_dots = tk.Button(
    text="ü",
    width=3,
    height=1,
    bg="medium turquoise",
    fg="black",
    highlightcolor="DodgerBlue2",
    font=('Times', -40, 'bold'),
    borderwidth=6,
    command=lambda: copyy("ü")
)
u_dots.grid(row=4, column=2)

window.mainloop()
