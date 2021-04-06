from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os

def uncorrected_data():
    label_6['text'] = 'Uncorrected data'
    label_6['bg'] = 'aqua'
    label_bmi_result.place(x=370,y=190)
    label_bmi_result['text'] ='Your BMI is unavalaible'
    label_bmi_result['bg'] = 'aqua'
    
root = Tk()
root.title('Fitness app')
root.geometry('700x400')
root['bg'] = 'dark green'

height = StringVar()
weight = StringVar()
age = StringVar()
active = StringVar()
r_var = BooleanVar()
r_var.set(1)

# select your sex - man or woman
label_sex = Label(root,text='Choose gender')
label_sex.place(x=420,y=20)
r1 = Radiobutton(text='Man', variable=r_var, value=0)
r1.place(x=400,y=50)
r2 = Radiobutton(text='Woman', variable=r_var, value=1)
r2.place(x=460,y=50)

def calc_normal_weight():
    h = float(height.get())
    w = float(weight.get())
    ag = float(age.get())
    if active.get() == 'Low':
        k = 1.9
    elif active.get() == 'Normal':
        k = 1.5
    else:
        k = 1.1
    if r_var.get() == 0:
        calories_normal = 66+(13.7*w)+(5*h)-(6.76*ag)*k
        return calories_normal
    else:
        calories_normal = 655+(9.5*w)+(1.8*h)-(4.7*ag)*k
        return calories_normal
    
def to_lose_weight():
    calories_normal = calc_normal_weight()
    calories_to_lose = calories_normal - calories_normal*0.15
    return calories_to_lose

def to_crease_weight():
    calories_normal = calc_normal_weight()
    calories_to_crease = calories_normal + calories_normal*0.15
    return calories_to_crease
    

def calc():
    """ function for calculating IBM """
    try:
        h = float(height.get())/100
        w = float(weight.get())
    except ValueError:
        h,w = 0,0
    try:
        index = w/(h*h)
        index = round(index, 2)
    except ZeroDivisionError:
        index = 0
        
    if 1 < h < 3 and 20 < w < 300:
        label_6['text'] = index
        if 18.5 <= index < 25:
            label_6['bg'] = 'light green'
            label_bmi_result['text'] ='Your BMI is normal'
            label_bmi_result['bg'] = 'light green'
            label_bmi_result.place(x=320,y=190)
        elif 0 < index < 18.5:
            label_6['bg'] = 'yellow'
            label_bmi_result['text'] ='Your BMI is low'
            label_bmi_result['bg'] = 'yellow'
            label_bmi_result.place(x=320,y=190)
        elif 25 < index < 100:
            label_6['bg'] = 'red'
            label_bmi_result['text'] ='Your BMI is high'
            label_bmi_result['bg'] = 'red'
            label_bmi_result.place(x=320,y=190)
    else:
        uncorrected_data()
    
    label_8['text'] = int(calc_normal_weight())
    label_10['text'] = int(to_lose_weight())
    label_12['text'] = int(to_crease_weight())
    
# add the picture to the right
img_1 = ImageTk.PhotoImage(Image.open("img_1.png"))
panel_1 = Label(root, image = img_1)
panel_1.place(x=540,y=180)
# add the pictire to the left
img_2 = ImageTk.PhotoImage(Image.open("img_2.png"))
panel_2 = Label(root, image = img_2)
panel_2.place(x=2,y=2)

name_app = 'Fitness Calculator'
product_owner = 'by VolodymyrHeraskin'

label_main = Label(root,text=name_app,font='Arial 14').place(x=200,y=10)
label_product_owner = Label(root,text=product_owner,font='Arial 10 italic',fg='dark blue',bg='yellow').place(x=480,y=370)

label_weight = Label(root,text='Enter your weight: ').place(x=200,y=50)
entry_weight = Entry(root,width=7,textvariable=weight).place(x=310,y=50)
label_kg = Label(root,text='kg').place(x=365,y=50)

label_height = Label(root,text='Enter your height: ').place(x=200,y=90)
entry_height = Entry(root,width=7,textvariable=height).place(x=310,y=90)
label_cm = Label(root,text='cm').place(x=365,y=90)

label_age = Label(root,text='Enter your age: ')
label_age.place(x=420,y=90)
entry_age = Entry(root,width=7,textvariable=age)
entry_age.place(x=510,y=90)

label_active = Label(root, text='Select your activity:')
label_active.place(x=560,y=20)
combo_active = ttk.Combobox(root,values=['Low','Normal','High'], textvariable = active, width=9)
combo_active.place(x=570,y=50)
combo_active.current(1)
    
btn_calc = Button(root,text='Calculating',command=calc).place(x=310,y=130)

label_bmi = Label(root,text='Your Body Mass Index (BMI): ').place(x=100,y=190)
label_6 = Label(root,text='Texy')
label_6.place(x=260,y=190)
    
label_bmi_result = Label(root,text='Your BMI: ')
label_bmi_result.place(x=340,y=190)

label_7 = Label(root,text='The number of calories to maintain weight: ').place(x=25,y=220)
label_8 = Label(root,text='(Your Body Mass Index (BMI))')
label_8.place(x=260,y=220)

label_9 = Label(root,text='The number of calories to lose weight: ').place(x=50,y=250)
label_10 = Label(root,text='(Your Body Mass Index (BMI))')
label_10.place(x=260,y=250)

label_11 = Label(root,text='The number of calories for weight gain: ').place(x=45,y=280)
label_12 = Label(root,text='(Your Body Mass Index (BMI))')
label_12.place(x=260,y=280)






