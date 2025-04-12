import tkinter as tk
from tkinter import ttk
#import customtkinter
from tkinter import *
#import carding
#import page_frame
from tkinter.messagebox import askyesno

root = tk.Tk()
root.geometry('400x600')
root.title('Tkinter Hub')

menu_bar_colour = '#383838'

# icons
toggle_icon = tk.PhotoImage(file='images/toggle_btn_icon.png')
home_icon = tk.PhotoImage(file='images/home_icon.png')
service_icon = tk.PhotoImage(file='images/services_icon.png')
update_icon = tk.PhotoImage(file='images/updates_icon.png')
contact_icon = tk.PhotoImage(file='images/contact_icon.png')
about_icon = tk.PhotoImage(file='images/about_icon.png')
close_icon = tk.PhotoImage(file='images/close_btn_icon.png')


def switch_indication(indicator_lb, page):
    home_btn_indicator.config(bg=menu_bar_colour)
    service_btn_indicator.config(bg=menu_bar_colour)
    update_btn_indicator.config(bg=menu_bar_colour)
    contact_btn_indicator.config(bg=menu_bar_colour)
    about_btn_indicator.config(bg=menu_bar_colour)
    
    indicator_lb.config(bg="white")

    if menu_bar_frame.winfo_width() > 45:
        fold_menu_bar()

    for frame in page_frame.winfo_children():
        frame.destroy()

    page()


close_btn_icon = tk.PhotoImage(file='images/close_btn_icon.png')

def extending_animation():
    
    current_width = menu_bar_frame.winfo_width()
    if not current_width > 200:

        current_width += 10
        menu_bar_frame.config(width=current_width)

        root.after(ms=8, func=extending_animation)

def extend_menu_bar(): 
    extending_animation()
    toggle_menu_btn.config(image=close_btn_icon)
    toggle_menu_btn.config(command=fold_menu_bar)

def folding_animation():
    current_width = menu_bar_frame.winfo_width()
    if current_width != 45:

        current_width -= 10
        menu_bar_frame.config(width=current_width)
        
        root.after(ms=8, func=folding_animation)

def fold_menu_bar():
    folding_animation()
    toggle_menu_btn.config(image=toggle_icon)
    toggle_menu_btn.config(command=extend_menu_bar )

def home_page():

    home_page_fm = tk.Frame(page_frame)

    lb = tk.Label(home_page_fm, text='Home Page', font=('Bold', 20))
    #lb.place(x=100, y=0)
    lb.grid(row=0, column=0)

    ###################### carding button start ###########################
    
    carding_btn_fm = tk.Frame(home_page_fm)
    carding_btn = tk.Button(carding_btn_fm, text="card", command=carding)
    #carding_btn.place(x=20, y=100, width=80, height=40)
    #carding_btn.pack()
    carding_btn.grid(row=1, column=1)

    payr_btn_fm = tk.Frame(home_page_fm)
    payr_btn = tk.Button(payr_btn_fm, text="Payroll", command=payroll)
    payr_btn.grid(row=3, column=3)
    #payr_btn.place(x=20, y=200, width=80, height=40)
    payr_btn_fm.grid(row=2, column=2)

    home_page_fm.grid()

#carding button func
def carding():
  
    carding_page_fm = tk.Frame(page_frame)
    #card_lb = tk.Label(carding_page_fm, text='card', font=('Bold', 20))
    #card_lb.place(x=100, y=0)
    carding_page_fm.grid()

    #for frame in page_frame.winfo_children():
    #    frame.destroy()

    #page() for carding entries
    #carding_page()
    new_window_carding()
    
#page() for carding entries
#def carding_page():

#    carding_entry_page_fm = tk.Frame(page_frame)
#    card_lb = tk.Label(carding_entry_page_fm, text='card', font=('Bold', 20))
#    card_lb.place(x=100, y=0)
#    carding_entry_page_fm.pack(fill=tk.BOTH, expand=True)
    
# new window
def new_window_carding():
    new_window = Toplevel()
    new_window.title('Carding')
    new_window.geometry('400x200')
    
    card_lb = tk.Label(new_window, text='card', font=('Bold', 20))
    card_lb.place(x=100, y=0)
    #new_window = Tk() stand alone window

#    def confirm():
#        ans = askyesno(title='Exit', message='Do You Want To Exit ?')
#        if ans:
#            new_window.destroy()

#    new_window.protocol("WM_DELETE_WINDOW", confirm)



##################### carding button end ################### 

###################### payroll button start ###########################
    

#carding button func
def payroll():
  
    payroll_page_fm = tk.Frame(page_frame)
    #card_lb = tk.Label(carding_page_fm, text='card', font=('Bold', 20))
    #card_lb.place(x=100, y=0)
    payroll_page_fm.pack(fill=tk.BOTH, expand=True)

    #for frame in page_frame.winfo_children():
    #    frame.destroy()

    #page() for carding entries
    #carding_page()
    new_window_payroll()
    
#page() for carding entries
#def carding_page():

#    carding_entry_page_fm = tk.Frame(page_frame)
#    card_lb = tk.Label(carding_entry_page_fm, text='card', font=('Bold', 20))
#    card_lb.place(x=100, y=0)
#    carding_entry_page_fm.pack(fill=tk.BOTH, expand=True)
    
# new window
def new_window_payroll():
    new_window = Toplevel()
    new_window.title('Payroll')
    new_window.geometry('400x200')
    
    card_lb = tk.Label(new_window, text='payr', font=('Bold', 20))
    card_lb.place(x=100, y=0)
    #new_window = Tk() stand alone window

#    def confirm():
#        ans = askyesno(title='Exit', message='Do You Want To Exit ?')
#        if ans:
#            new_window.destroy()

#    new_window.protocol("WM_DELETE_WINDOW", confirm)



##################### carding button end ################### 

def service_page():
    service_page_fm = tk.Frame(page_frame)

    lb = tk.Label(service_page_fm, text='Service Page', font=('Bold', 20))
    lb.place(x=100, y=200)
    
    service_page_fm.pack(fill=tk.BOTH, expand=True)

def update_page():
    update_page_fm = tk.Frame(page_frame)

    lb = tk.Label(update_page_fm, text='Update Page', font=('Bold', 20))
    lb.place(x=100, y=200)
    
    update_page_fm.pack(fill=tk.BOTH, expand=True)

def contact_page():
    contact_page_fm = tk.Frame(page_frame)

    lb = tk.Label(contact_page_fm, text='Contact Page', font=('Bold', 20))
    lb.place(x=100, y=200)
    
    contact_page_fm.pack(fill=tk.BOTH, expand=True)

def about_page():
    about_page_fm = tk.Frame(page_frame)

    lb = tk.Label(about_page_fm, text='About Page', font=('Bold', 20))
    lb.place(x=100, y=200)
    
    about_page_fm.pack(fill=tk.BOTH, expand=True)

page_frame = tk.Frame(root)
page_frame.place(relwidth=1.0, relheight=1.0, x=50)
home_page()


menu_bar_frame =tk.Frame(root, bg=menu_bar_colour)

toggle_menu_btn = tk.Button(menu_bar_frame, image=toggle_icon, bg=menu_bar_colour,
                            bd=0, activebackground=menu_bar_colour,
                            command=extend_menu_bar)
toggle_menu_btn.place(x=4, y=10)

home_btn = tk.Button(menu_bar_frame, image=home_icon, bg=menu_bar_colour,
                            bd=0, activebackground=menu_bar_colour,
                            command=lambda: switch_indication(indicator_lb=home_btn_indicator,
                                                              page=home_page))
home_btn.place(x=9, y=130, width=30, height=40)

home_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_colour)
home_btn_indicator.place(x=3, y=130, height=40, width=3)

home_page_lb = tk.Label(menu_bar_frame, text='Home', bg=menu_bar_colour, fg='white',
                        font=('Bold', 15), anchor=tk.W)
home_page_lb.place(x=45, y=130, width=100, height=40)

home_page_lb.bind('<Button-1>', lambda e: switch_indication(indicator_lb=home_btn_indicator,
                                                            page=home_page))

service_btn = tk.Button(menu_bar_frame, image=update_icon, bg=menu_bar_colour,
                            bd=0, activebackground=menu_bar_colour,
                            command=lambda: switch_indication(indicator_lb=service_btn_indicator,
                                                              page=service_page))
service_btn.place(x=9, y=190, width=30, height=40)

service_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_colour)
service_btn_indicator.place(x=3, y=190, height=40, width=3)

service_page_lb = tk.Label(menu_bar_frame, text='Service', bg=menu_bar_colour, fg='white',
                        font=('Bold', 15), anchor=tk.W)
service_page_lb.place(x=45, y=190, width=100, height=40)

service_page_lb.bind('<Button-1>', lambda e: switch_indication(indicator_lb=service_btn_indicator,
                                                               page=service_page))

update_btn = tk.Button(menu_bar_frame, image=service_icon, bg=menu_bar_colour,
                            bd=0, activebackground=menu_bar_colour,
                            command=lambda: switch_indication(indicator_lb=update_btn_indicator,
                                                              page=update_page))
update_btn.place(x=9, y=250, width=30, height=40)

update_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_colour)
update_btn_indicator.place(x=3, y=250, height=40, width=3)

update_page_lb = tk.Label(menu_bar_frame, text='Update', bg=menu_bar_colour, fg='white',
                        font=('Bold', 15), anchor=tk.W)
update_page_lb.place(x=45, y=250, width=100, height=40)

update_page_lb.bind('<Button-1>', lambda e: switch_indication(indicator_lb=update_btn_indicator,
                                                              page=update_page))

contact_btn = tk.Button(menu_bar_frame, image=contact_icon, bg=menu_bar_colour,
                            bd=0, activebackground=menu_bar_colour,
                            command=lambda: switch_indication(indicator_lb=contact_btn_indicator,
                                                              page=contact_page))
contact_btn.place(x=9, y=310, width=30, height=40)

contact_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_colour)
contact_btn_indicator.place(x=3, y=310, height=40, width=3)

contact_page_lb = tk.Label(menu_bar_frame, text='Contact', bg=menu_bar_colour, fg='white',
                        font=('Bold', 15), anchor=tk.W)
contact_page_lb.place(x=45, y=310, width=100, height=40)

contact_page_lb.bind('<Button-1>', lambda e: switch_indication(indicator_lb=contact_btn_indicator,
                                                               page=contact_page))

about_btn = tk.Button(menu_bar_frame, image=about_icon, bg=menu_bar_colour,
                            bd=0, activebackground=menu_bar_colour,
                            command=lambda: switch_indication(indicator_lb=about_btn_indicator,
                                                              page=about_page))
about_btn.place(x=9, y=370, width=30, height=40)

about_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_colour)
about_btn_indicator.place(x=3, y=370, height=40, width=3)

about_page_lb = tk.Label(menu_bar_frame, text='About', bg=menu_bar_colour, fg='white',
                        font=('Bold', 15), anchor=tk.W)
about_page_lb.place(x=45, y=370, width=100, height=40)

about_page_lb.bind('<Button-1>', lambda e: switch_indication(indicator_lb=about_btn_indicator,
                                                             page=about_page))

menu_bar_frame.pack(side=tk.LEFT, fill=tk.Y, pady=4, padx=3)
menu_bar_frame.pack_propagate(flag=False)

menu_bar_frame.configure(width=45)

# messagebox for entire window
#def confirm():
#        ans = askyesno(title='Exit', message='Do You Want To Exit ?')
#        if ans:
#            root.destroy()

#root.protocol("WM_DELETE_WINDOW", confirm)

root.mainloop()












 