from tkinter import *
import os
root = Tk()
root.geometry("630x465")
root.resizable(0, 0)
root.config(bg="grey20")
root.title("Manage Computer - All at One Place")


# Title of the GUI...

# Title Image
title_img = PhotoImage(file='manager.png')
# Title Name
title_label = Label(root, text="Computer Manager", font=("elephant", 25, "bold"), bg="grey20", fg="gold2", image=title_img, compound=LEFT, borderwidth=1.5, relief="solid", pady=10)
title_label.pack(fill=X, pady=10)

# Frame where all the button to be packed
frame = Frame(root, bd=1.5, relief="solid", bg="white")
frame.pack(pady=10)

# Task Maager Button
task_image = PhotoImage(file='TaskManager.png')
task_btn = Button(frame, text='Task Manager', font=('Fira Sans', 18, 'bold'), bg='white', fg='red3', image=task_image, compound=LEFT, cursor='hand2', padx=10, bd=0, command= lambda : os.system('taskmgr'))

task_btn.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# ControlPanel Button
ControlPanel_image = PhotoImage(file='ControlPanel.png')
ControlPanel_btn = Button(frame, text='Control Panel', font=('Fira Sans', 18, 'bold'), bg='white', fg='black', image=ControlPanel_image, compound=LEFT, cursor='hand2', padx=10, bd=0, command= lambda : os.system('control'))

ControlPanel_btn.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# DateTime Button
DateTime_image = PhotoImage(file='DateTime.png')
DateTime_btn = Button(frame, text=' Date and Time  ', font=('Fira Sans', 18, 'bold'), bg='white', fg='orange', image=DateTime_image, compound=LEFT, cursor='hand2', padx=10, bd=0, command= lambda : os.system('timedate.cpl'))

DateTime_btn.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# System_Services Button
System_Service_image = PhotoImage(file='System_Service.png')
System_Service_btn = Button(frame, text='System Services', font=('Fira Sans', 18, 'bold'), bg='white', fg='#FB6D48', image=System_Service_image, compound=LEFT, cursor='hand2', padx=10, bd=0, command= lambda : os.system('services.msc'))

System_Service_btn.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# DeviceManager Button
DeviceManager_image = PhotoImage(file='DeviceManager.png')
DeviceManager_btn = Button(frame, text='Device Manager', font=('Fira Sans', 18, 'bold'), bg='white', fg='green', image=DeviceManager_image, compound=LEFT, cursor='hand2', padx=10, bd=0, command= lambda : os.system('devmgmt.msc'))

DeviceManager_btn.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# Window Update Button
WindowUpdate_image = PhotoImage(file='WindowUpdate.png')
WindowUpdate_btn = Button(frame, text='Windows Update', font=('Fira Sans', 18, 'bold'), bg='white', fg='purple', image=WindowUpdate_image, compound=LEFT, cursor='hand2', padx=10, bd=0, command= lambda : os.system('control update'))

WindowUpdate_btn.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# MouseProperties Button
MouseProperty_image = PhotoImage(file='MouseProperty.png')
MouseProperty_btn = Button(frame, text='Mouse Properties', font=('Fira Sans', 18, 'bold'), bg='white', fg='#008DDA', image=MouseProperty_image, compound=LEFT, cursor='hand2', padx=10, bd=0, command= lambda : os.system('main.cpl'))

MouseProperty_btn.grid(row=4, column=0, padx=10, pady=10, sticky="w")

# System_Property Button
SystemProperty_image = PhotoImage(file='SystemProperty.png')
SystemProperty_btn = Button(frame, text='System Properties', font=('Fira Sans', 18, 'bold'), bg='white', fg='#FFC700', image=SystemProperty_image, compound=LEFT, cursor='hand2', padx=10, bd=0, command= lambda : os.system('sysdm.cpl'))

SystemProperty_btn.grid(row=4, column=1, padx=10, pady=10, sticky="w")

# Uninstall Software Button
Uninstall_image = PhotoImage(file='Uninstall.png')
Uninstall_btn = Button(frame, text='Uninstall Software', font=('Fira Sans', 18, 'bold'), bg='white', fg='#365486', image=Uninstall_image, compound=LEFT, cursor='hand2', padx=10, bd=0, command= lambda : os.system('appwiz.cpl'))

Uninstall_btn.grid(row=5, column=0, padx=10, pady=10, sticky="w")

# Network Connections Button
Network_image = PhotoImage(file='Network.png')
Network_btn = Button(frame, text='Network Connections', font=('arial', 18, 'bold'), bg='white', fg='blue', image=Network_image, compound=LEFT, cursor='hand2', padx=10, bd=0, command= lambda : os.system('ncpa.cpl'))

Network_btn.grid(row=5, column=1, padx=10, pady=10, sticky="w")

root.mainloop()