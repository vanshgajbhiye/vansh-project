import tkinter as tk

def black_screen():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='black')

    def exit_screen(event):
        root.destroy()

    root.bind("<Escape>", exit_screen)  # ESC se exit
    root.mainloop()                           











    

    