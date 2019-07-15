# -*- coding: utf-8 -*-

import sys
python_ver = sys.version_info[0]
print("Current python version : ", python_ver)

if python_ver == 3:
    from tkinter import *
    from tkinter import ttk

if python_ver == 2:
    from Tkinter import *
    import ttk
    import sys; reload(sys); sys.setdefaultencoding('utf8')

import re
import webbrowser as wb



# ---------------------------------------
# ---------------------------------------
# --- Global var



# ---------------------------------------
# ---------------------------------------
# --- Function definition




# ---------------------------------------
# ---------------------------------------
# --- root
# -
root = Tk()
root.title("Tkinter Combobox Template")


# ---------------------------------------
# ---------------------------------------
# --- frame


# ---------------------------------------
# ---------------------------------------
# --- frame

# -- frame 1
frame1 = ttk.Frame(root, padding=8)

# -- frame 2
frame2 = ttk.Frame(root, padding=8)

# -- frame 3
frame3 = ttk.Frame(root, padding=8)

# -- frame 4
frame4 = ttk.Frame(root, padding=8)

# -- frame 5
frame5 = ttk.Frame(root, padding=8)





# ---------------
# --- combo box

# - combo box1 / workspace list

# -
combo1_itmes = [1, 2, 3, 4]
combo1_itmes.sort()
cb1_val = StringVar()
cb1_val.set("combo 1 list")
cb1 = ttk.Combobox(frame1, textvariable=cb1_val, height=10, width=43)
cb1['values'] = combo1_itmes
frame1.grid()
cb1.grid(row=1)
cb1.bind('<<ComboboxSelected>>', lambda e:[select_ui_language(combo1_itmes, int(cb.current()))])

# - combo box2 / action list for selected workspace
combo2_itmes = [1, 2, 3, 4]
combo2_itmes.sort()
cb2_val = StringVar()
cb2_val.set("combo 2 list")
cb2 = ttk.Combobox(frame2, textvariable=cb2_val, height=10, width=43)
cb2['values'] = combo2_itmes
frame2.grid()
cb2.grid(row=1)
cb2.bind('<<ComboboxSelected>>', lambda e:[select_ui_language(combo2_itmes, int(cb.current()))])


# - combo box3 / channel list of selected workspace
combo3_itmes = [1, 2, 3, 4]
combo3_itmes.sort()
cb3_val = StringVar()
cb3_val.set("combo 3 list")
cb3 = ttk.Combobox(frame3, textvariable=cb3_val, height=10, width=43)
cb3['values'] = combo3_itmes
frame3.grid()
cb3.grid(row=1)
cb3.bind('<<ComboboxSelected>>', lambda e:[select_ui_language(combo3_itmes, int(cb.current()))])


# - combo box4 / action list about selected workspace
combo4_itmes = [1, 2, 3, 4]
combo4_itmes.sort()
cb4_val = StringVar()
cb4_val.set("combo 4 list")
cb4 = ttk.Combobox(frame4, textvariable=cb4_val, height=10, width=43)
cb4['values'] = combo4_itmes
frame4.grid()
cb4.grid(row=1)
cb4.bind('<<ComboboxSelected>>', lambda e:[select_ui_language(combo4_itmes, int(cb.current()))])


# - combo box5 / xxx
combo5_itmes = [1, 2, 3, 4]
combo5_itmes.sort()
cb5_val = StringVar()
cb5_val.set("combo 5 list")
cb5 = ttk.Combobox(frame5, textvariable=cb5_val, height=10, width=43)
cb5['values'] = combo5_itmes
frame5.grid()
cb5.grid(row=1)
cb5.bind('<<ComboboxSelected>>', lambda e:[select_ui_language(combo5_itmes, int(cb.current()))])


# ---------------
# --- label




# ---------------
# --- butoon



# ---------------------------------------
# ---------------------------------------
# --- call main

root.mainloop()







