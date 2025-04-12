import tkinter as tk
import page_frame

def carding():
  
    carding_page_fm = tk.Frame(page_frame)
    card_lb = tk.Label(carding_page_fm, text='card', font=('Bold', 20))
    card_lb.place(x=100, y=0)
    carding_page_fm.pack(fill=tk.BOTH, expand=True)

    for frame in page_frame.winfo_children():
        frame.destroy()

    #page() for carding entries
    carding_page()
    

def carding_page():

    carding_entry_page_fm = tk.Frame(page_frame)
    card_lb = tk.Label(carding_entry_page_fm, text='card', font=('Bold', 20))
    card_lb.place(x=100, y=0)
    carding_entry_page_fm.pack(fill=tk.BOTH, expand=True)

    