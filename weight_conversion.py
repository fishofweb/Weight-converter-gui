from tkinter import *
window = Tk()

window.configure(bg='black')
window.title("Weight Conversion ")
window.geometry("500x500")


Label(window, text= "Convert Weight Kg - Lbs", bg="red",fg="black", font="times 24 bold").grid(row=0,column=100)

Label(window, text= "Enter Weight in kgs", bg="black",fg="white", font="times 16 bold").grid(row=5,column=100)
kg = Entry(window, width=20, bg="blue", fg="white")
kg.grid(row=8, column=100)

def lb():
    kg_ = kg.get()
    result = int(kg_) * 2.20462
    kg_lb=Label(window, text=result, bg = "black",fg="white", font="none 12 bold")
    kg_lb.grid(row= 18 , column=100)
    def clear():
        kg_lb.destroy()
        clear_btn_lb.destroy()
        
    
    clear_btn_lb = Button(window, text= "Clear", width=10, command= clear , bg="black", fg = "white")
    clear_btn_lb.grid(row= 17, column= 100)
lb_button=Button(window, text= "Enter", width=10, command= lb , bg="black", fg = "white")
lb_button.grid(row=9, column=100)
Label(window, text="Weight in lbs:", bg = "black",fg="white", font="none 12 bold").grid(row= 15 , column=100)

Label(window, text= "Convert Weight lbs - kgs", bg="red",fg="black", font="times 24 bold").grid(row=20,column=100)



Label(window, text= "Enter Weight in lbs", bg="black",fg="white", font="times 16 bold").grid(row=30,column=100)
lbs_2_k = Entry(window, width=20, bg="blue", fg="white")
lbs_2_k.grid(row=33, column=100)

def kg_func():
    
    lbs_1 = int(lbs_2_k.get())
    kilo = lbs_1 / 2.20462
    kg_label = Label(window, text=kilo, bg = "black",fg="white", font="none 12 bold")
    kg_label.grid(row= 42 , column=100)
    
    def clear():
        kg_label.destroy()
        clear_btn.destroy()
    
    clear_btn = Button(window, text= "Clear", width=10, command= clear , bg="black", fg = "white")
    clear_btn.grid(row= 45, column= 100)
    
    
k_button=Button(window, text= "Enter", width=10, command= kg_func , bg="black", fg = "white")
k_button.grid(row=35, column=100)
Label(window, text="Weight in kgs:", bg = "black",fg="white", font="none 12 bold").grid(row= 39 , column=100)

window.mainloop()