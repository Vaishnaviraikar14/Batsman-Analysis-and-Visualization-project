import tkinter
from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image
#from PIL import Image, ImageDraw, ImageFont
from batsman import *

root = Tk()
#root.geometry("900x800")
root.state('zoomed')
#open image
bg=Image.open("C:\\Users\\VAISHNAVI\\Downloads\\ipl pro7.png")
#resize image
resized=bg.resize((1500,1100),Image.ANTIALIAS)
bg1=ImageTk.PhotoImage(resized)
bg = ImageTk.PhotoImage(file ="C:\\Users\\VAISHNAVI\\Downloads\\ipl pro7.png")
label=Label(root,image=bg1)
label.pack(pady=20)

'''def resize_image(e):
    global image, resized, image
    image=Image.open("C:\\Users\\VAISHNAVI\\Downloads\\ipl project.png")
    resized=image.resize((e.width,e.height),Image.ANTIALIAS)
    image2=ImageTk.PhotoImage(resized)
    canvas1.create_image(100,200,image=image2,anchor='nw')
    root.bind("<Configure>",resize_image)'''

root.title("BATSMAN DATA ANLYSIS")
label = Label(root, text="BATSMAN DATA ANLYSIS", bg="black", fg="white", font=("Times", 20))

label4=Label(root, text="    BATSMAN  ANALYSIS    ",  bg="#B7C9F7", fg="red", font=("Georgia", 29))
label4.pack()
label4.place(x=550,y=30)


label5=Label(root, text="  INDIVIDUAL BATSMAN   ", bg="#FACFBE",  fg="blue", font=("Times", 22))
label5.pack()
label5.place(x=610,y=120)

def visual_type(batsman,type1, param1):
    if(type1=="DISMISSAL KIND" and param1=="PIE CHART"):
        dissmisal_pie(batsman)
    elif(type1=="DISMISSAL KIND" and param1=="BAR GRAPH"):
        dissmisal_bar(batsman)
    elif(type1=="RUNS SCORED" and param1=="PIE CHART"):
        runs_pie(batsman)
    elif(type1=="RUNS SCORED" and param1=="BAR GRAPH"):
        runs_bar(batsman)
    else:
        tkinter.messagebox.showerror("Error","Invalid Selection")

def individual(op1):
    if(op1=="Most 4 Runs"):
        most_4()
    elif(op1=="Most 6 Runs"):
        most_6()
    elif(op1=="Maximum Runs"):
        max_runs()
    elif(op1=="Higest Strike-rate"):
        higest_sr()
    else:
        tkinter.messagebox.showerror("Error", "Invalid Selection")


label2 = Label(root, text="         SELECT  A  BATSMAN  :          ",bg="white",  fg="black", font=("Times", 16))
label2.pack()
label2.place(x=550,y=200)

player_list = ('DA Warner','S Dhawan','MC Henriques','V Kohli','Yuvraj Singh','DJ Hooda','BCJ Cutting','CH Gayle','Mandeep Singh','TM Head','KM Jadhav','SR Watson'
,'Sachin Baby','STR Binny','SS Iyer','YS Chahal','PA Patel','JC Buttler','RG Sharma','SR Tendulkar','N Rana','AT Rayudu','KH Pandya','KA Pollard','HH Pandya','AM Rahane',
'MA Agarwal','SPD Smith','BA Stokes','MS Dhoni','R Ashwin','CA Pujara','Ishan Kishan','JJ Roy','BB McCullum','SK Raina','AJ Finch','KD Karthik','G Gambhir','CA Lynn','MK Tiwary','DT Christian',
'HM Amla','M Vohra','WP Saha','AR Patel','GJ Maxwell','DA Miller','AP Tare','SW Billings','KK Nair','SV Samson','RR Pant','CH Morris','CR Brathwaite',
'PJ Cummins','A Mishra','S Nadeem','DR Smith','RV Uthappa','MK Pandey','YK Pathan','SA Yadav','CR Woakes','SP Narine','Harbhajan Singh','AB de Villiers',
'CJ Anderson','F du Plessis','RA Tripathi','R Bhatia','DL Chahar','A Zampa','Imran Tahir','NV Ojha','V Shankar','Rashid Khan','B Kumar','MP Stoinis','MM Sharma',
'VR Aaron','MJ McClenaghan','SN Thakur','DJ Bravo','AC Gilchrist','VVS Laxman','A Symonds','JH Kallis','SC Ganguly','RT Ponting','RA Jadeja')

menu=len(max(player_list,key=len))

clicked1 = StringVar(root)
clicked1.set("select")
drop = OptionMenu(root, clicked1,*player_list)
drop.config(width=menu)
drop.pack()
drop.place(x=930,y=200)


label3 = Label(root, text="     SELECT  ANALYSIS  TYPE  :       ", bg="white", fg="black", font=("Times", 16))
label3.pack()
label3.place(x=550,y=260)

analysis=('DISMISSAL KIND', 'RUNS SCORED')
menu1=len(max(analysis,key=len))

clicked2 = StringVar(root)
clicked2.set("select")
drop1 = OptionMenu(root, clicked2, *analysis)
drop1.config(width=menu1)
drop1.pack()
drop1.place(x=930,y=260)

label3 = Label(root, text=" SELECT  VISUALIZATION  TYPE :  ", bg="white", fg="black", font=("Times", 16))
label3.pack()
label3.place(x=550,y=320)

visualization=('PIE CHART', 'BAR GRAPH')
menu2=len(max(visualization,key=len))

clicked3= StringVar(root)
clicked3.set("select")
drop2 = OptionMenu(root, clicked3, *visualization)
drop2.config(width=menu)
drop2.pack()
drop2.place(x=930, y=320)

button = Button(root, text="ENTER", padx=100, pady=10, command= lambda:visual_type(clicked1.get(),clicked2.get(),clicked3.get()))
myFont=font.Font(family="Times", size=13, weight="bold")
button["font"]=myFont
button.pack()
button.place(x=670, y=390)

label6= Label(root, text="     GENERAL ANALYSIS     ", bg="#FACFBE", fg="blue", font=("Times", 22))
label6.pack()
label6.place(x=610, y=500)

label7= Label(root, text="    SELECT  ANALYTICAL  TYPE :     ", bg="white", fg="black",font=("Times", 16))
label7.pack()
label7.place(x=550,y=580)

list=["Most 4 Runs","Most 6 Runs","Maximum Runs","Higest Strike-rate"]
menu2=len(max(list,key=len))
clicked4= StringVar(root)
clicked4.set("select ")
drop = OptionMenu(root, clicked4, *list)
drop.config(width=menu)
drop.pack()
drop.place(x=930,y=580)

button = Button(root, text="ENTER", padx=100, pady=10,command=lambda:individual(clicked4.get()))
myFont=font.Font(family="Times", size=13, weight="bold")
button["font"]=myFont
button.pack()
button.place(x=680,y=650)

root.config(bg="grey17")
#root.geometry("700x800")
#root.attributes('-fullscreen',True)
#root.state('zoomed')
root.mainloop()

