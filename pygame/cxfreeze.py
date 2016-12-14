#-*- coding: UTF-8 -*-
import cx_Freeze

import os
os.environ['TCL_LIBRARY'] = "C:\\Program Files\\Python35\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Program Files\\Python35\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":[r"..\panel\DiceAtk.png",r"..\panel\DiceMov3.png",r"..\panel\DiceHeal3.png",r"..\panel\DiceDef3.png"]}},
    executables = executables

    )