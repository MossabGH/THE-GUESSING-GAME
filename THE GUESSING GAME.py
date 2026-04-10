from tkinter import *
from tkinter import Toplevel
import random

root=Tk()
root.title("THE GUESSING GAME")
root.geometry("500x430+225+100")
root.config(bg='#E0FFFF')
root.resizable(False,False)
root.iconbitmap("image/The_guess_game_image.ico")
root.focus_set()
 

#title game

label_title_game = Label(root,text="THE GUESSING GAME",bg='#E0FFFF',font=("Impact", 24))
label_title_game.place(x=120,y=30)

image_1 = PhotoImage(file="image/The_guess_game_image.png")

label_image_1 = Label(root,image = image_1,bg="#E0FFFF",width=230,height=230)
label_image_1.place(x=130,y=210)
#
attempts=0
count=10
creator_tap = None
information_tap = None
hint = None
hint_1 = None
info = None
#function

def creator_def(event=None):#pylint: disable=unused-argument
    close_wind()
    def close(event=None):#pylint: disable=unused-argument
            creator_tap.destroy()
    global creator_tap
    creator_tap = Toplevel()
    creator_tap.title("Creator")
    creator_tap.geometry("250x200+350+200")
    creator_tap.config(bg='#E0FFFF')
    creator_tap.resizable(False,False)
    creator_tap.iconbitmap("image/The_guess_game_image.ico")
    creator_tap.focus_set()
    label_creator = Label(creator_tap,text="Enjoy the game!",bg="#E0FFFF",width=15,height=1,font=("Impact", 15),justify='center')
    label_creator.place(x=50,y=30)
    l = Label(creator_tap,text="MossabGH",fg="#adb2b4",bg='#E0FFFF',width=10,height=1,font=("Impact", 12),justify='center')
    l.place(x=90,y=70)
    
    ok=Button(creator_tap,text="OK",command=close,font=("Impact", 14),bg="#87CEEB",width=10)
    creator_tap.bind("<e>", close)
    ok.place(x=80,y=150)
    
    creator_tap.mainloop()

def information_def(event=None):#pylint: disable=unused-argument
    close_wind()
    def close(event=None):#pylint: disable=unused-argument
            information_tap.destroy()
    global information_tap
    information_tap = Toplevel()
    information_tap.title("Information")
    information_tap.geometry("350x430+350+200")
    information_tap.config(bg='#E0FFFF')
    information_tap.resizable(False,False)
    information_tap.iconbitmap("image/The_guess_game_image.ico")
    information_tap.focus_set()
    label_info = Label(information_tap,text="""Some buttons on the panel\n facilitate interaction with the game

Start The Game = Entry

Information = e

Creator = r

OK = e

Entry = Entry

Replay = r

Close = e

? = r
""",bg='#E0FFFF',width=41,height=19,font=("Impact", 12),justify='left')
    label_info.place(x=10,y=10)
    ok=Button(information_tap,text="OK",command=close,font=("Impact", 14),bg="#87CEEB",width=10)
    information_tap.bind("<e>", close)
    ok.place(x=140,y=380)
    information_tap.mainloop()


    
def close_wind():
    if creator_tap is not None :
        creator_tap.destroy()  
    if information_tap is not None :
        information_tap.destroy()

def close_root():
    root.destroy()    
def start_the_gam():

    guess_number=random.randint(1,100)
    start = Tk()
    start.title("START THE GAME")
    start.geometry("500x430+225+100")
    start.config(bg='#E0FFFF')
    start.resizable(False,False)
    start.iconbitmap("image/The_guess_game_image.ico")
    start.focus_set()
    image_2 = PhotoImage(file="image/image_2.png")
    label_image_2 = Label(start,image = image_2,bg="#E0FFFF",width=230,height=230)
    label_image_2.place(x=10,y=210)
    
    
    global count
    global attempts
    global info
     
    
    attempts=0
    count=10
    
    def validate_entry(value):
        try:
            if value is None or value=="":
                return True
            val=int(value)
            if(0<=val<=100):
                return True
                     
            else:
                return False
        except ValueError:
            return False
    valid_command = start.register(validate_entry)
    
    
    
    def close_wind_2():
        if info is not None :
            info.destroy()

    
    def info_def(event=None):#pylint: disable=unused-argument
        close_wind_2()
        global info
        def close(event=None):#pylint: disable=unused-argument
            info.destroy()
        info = Toplevel()
        info.title("How to play")
        info.config(bg='#E0FFFF')
        info.geometry("350x250+350+200")
        info.resizable(False,False)
        info.iconbitmap("image/The_guess_game_image.ico")
        info.focus_set()
        label_info = Label(info, text="""How to play:
The computer guesses a random number
between 1 and 100,and
you try to guess it.
It then guides you to
the largest and smallest number.
You only have 10 switches and
you lose the game.
""", bg='#E0FFFF', width=41,height=9,font=("Impact", 12),justify='left')
        label_info.place(x=10,y=10)
        ok=Button(info,text="OK",command=close,font=("Impact", 14),bg="#87CEEB",width=10)
        info.bind("<e>", close)
        ok.place(x=130,y=200)
        info.mainloop()
    #button info = ?
    button_info = Button(start,text="?",bg="#87CEEB",font=("Impact", 16),command=info_def,width=3,height=1)
    button_info.place(x=455,y=5)
    start.bind("<r>",info_def)
        


    
    label_start_game = Label(start,text=""" Guess a number from 1 to 100
    and win the game """,bg='#E0FFFF',font=("Impact", 16))
    label_start_game.place(x=110,y=60)
    
    label_count = Label(start, text=f"Remaining attempts : {count}",bg='#E0FFFF',font=("Impact", 16))
    label_count.place(x=10,y=10)
    
    



    def valid_number(event=None):#pylint: disable=unused-argument

        global count
        global attempts
         
        global hint
        global hint_1
        attempts+=1
        count-=1

        entry_number_get = int(entry_number.get())
        label_count.config(text=f"Remaining attempts : {count}",bg='#E0FFFF',font=("Impact", 16))
        if attempts<10:

            if entry_number_get==guess_number:
                try:
                    start.destroy()
                except:
                    pass
                def close(event=None):#pylint: disable=unused-argument
                    end_win.destroy()
                    
                def replay(event=None):#pylint: disable=unused-argument
                    end_win.destroy()
                    start_the_gam()
                    
                    
                    
                end_win = Tk()
                end_win.title("END THE GAME")
                end_win.geometry("500x430+225+100")
                end_win.config(bg='#E0FFFF')
                end_win.resizable(False,False)
                end_win.iconbitmap("image/The_guess_game_image.ico")
                image_3 = PhotoImage(file="image/The_guess_game_image.png")
                label_image_3 = Label(end_win,image = image_3,bg="#E0FFFF",width=230,height=230)
                label_image_3.place(x=130,y=210)
                end_win.focus_set()
                label_win = Label(end_win,text="You Win",fg="yellow",bg='#E0FFFF',font=("Impact", 50))
                label_win.place(x=120,y=30)
                
                label_attempts = Label(end_win,text="Number of attempts  : ",bg='white',font=("Impact", 16),width=20,justify='left')
                label_attempts.place(x=100,y=150)
                
                label_attempts_number = Label(end_win,text=attempts,bg="white",font=("Impact",16),width=5,justify='left')
                label_attempts_number.place(x=310,y=150)
                
                label_guess = Label(end_win,text="Real number :                ",bg='white',font=("Impact", 16),width=20,justify='left')
                label_guess.place(x=100,y=190)
                
                label_guess_number = Label(end_win,text=guess_number,bg="white",font=("Impact",16),width=5,justify='left')
                label_guess_number.place(x=310,y=190)
                

                button_replay= Button(end_win,text="Replay",bg='#4dff00',font=("Impact", 12),width="15",height="1",command=replay)
                button_replay.place(x=10,y=380)
                
                button_close=Button(end_win,text="Close",bg='red',font=("Impact", 12),width="15",height="1",command=close)
                button_close.place(x=350,y=380)
                end_win.bind("<r>", replay)
                end_win.bind("<e>", close) 
                end_win.mainloop()
                        
            elif entry_number_get>guess_number:
                def ok_def(event=None):#pylint: disable=unused-argument
                    hint.destroy()
                
                try:
                    entry_number.delete(0,END)
                except:
                    pass
                hint = Toplevel()
                hint.title("The answer is wrong")
                hint.geometry("300x100+300+250")
                hint.config(bg="#E0FFFF")
                hint.resizable(False,False)
                hint.iconbitmap("image/The_guess_game_image.ico")
                hint.focus_set()
                lab_message = Label(hint,text="The number is smaller than that",font=("Impact", 16),bg="#E0FFFF")
                lab_message.place(x=10,y=10)
                ok=Button(hint,text="OK",command=ok_def,font=("Impact", 14),bg="#87CEEB",width=10)
                ok.place(x=100,y=50)
                hint.bind("<e>",ok_def)
                hint.mainloop()
                    


                
            else:
                def ok_def(event=None):#pylint: disable=unused-argument
                    hint_1.destroy()

                    
                try:
                    entry_number.delete(0,END)
                except:
                    pass
                hint_1 = Toplevel()
                hint_1.title("The answer is wrong")
                hint_1.geometry("300x100+300+250")
                hint_1.config(bg="#E0FFFF")
                hint_1.resizable(False,False)
                hint_1.iconbitmap("image/The_guess_game_image.ico")
                hint_1.focus_set()
                lab_message = Label(hint_1,text="The number is greater than that",font=("Impact", 16),bg="#E0FFFF")
                lab_message.place(x=10,y=10)
                ok=Button(hint_1,text="OK",command=ok_def,font=("Impact", 14),bg="#87CEEB",width=10)
                ok.place(x=100,y=50)
                hint_1.bind("<e>",ok_def)
                hint_1.mainloop()
        else:
            
            try:
                start.destroy()
            except:
                pass
            def close(event=None):#pylint: disable=unused-argument
                end_lose.destroy()
                #hint_1.destroy()
                
            def replay(event=None):#pylint: disable=unused-argument
                end_lose.destroy()
                start_the_gam()

            
            end_lose = Tk()
            end_lose.title("END THE GAME")
            end_lose.grab_set()
            end_lose.geometry("500x430+225+100")
            end_lose.config(bg='#E0FFFF')
            end_lose.resizable(False,False)
            end_lose.iconbitmap("image/The_guess_game_image.ico")
            image_4 = PhotoImage(file="image/The_guess_game_image.png")
            label_image_4 = Label(end_lose,image = image_4,bg="#E0FFFF",width=230,height=230)
            label_image_4.place(x=130,y=210)
        
        
            label_lose = Label(end_lose,text="You Lose",fg="red",bg='#E0FFFF',font=("Impact", 50))
            label_lose.place(x=120,y=30)
            
            label_attempts = Label(end_lose,text="Number of attempts  : ",bg='white',font=("Impact", 16),width=20,justify='left')
            label_attempts.place(x=100,y=150)
            
            label_attempts_number = Label(end_lose,text=attempts,bg="white",font=("Impact",16),width=5,justify='left')
            label_attempts_number.place(x=310,y=150)
            
            label_guess = Label(end_lose,text="Real number :                ",bg='white',font=("Impact", 16),width=20,justify='left')
            label_guess.place(x=100,y=190)
            
            label_guess_number = Label(end_lose,text=guess_number,bg="white",font=("Impact",16),width=5,justify='left')
            label_guess_number.place(x=310,y=190)


            button_replay= Button(end_lose,text="Replay",bg='#4dff00',font=("Impact", 12),width="15",height="1",command=replay)
            button_replay.place(x=10,y=380)
            
            button_close=Button(end_lose,text="Close",bg='red',font=("Impact", 12),width="15",height="1",command=close)
            button_close.place(x=350,y=380)
            end_lose.bind("<r>", replay)
            end_lose.bind("<e>", close)
            
            end_lose.mainloop()

            
            
 
    


    

            

            
        
        
    entry_number = Entry(start,width=10,bg="white",font=("Impact", 24),justify="center",validate="key",validatecommand=(valid_command,'%P'))
    entry_number.place(x=155,y=150)
    entry_number.focus_set()
    entry_number.bind("<Return>", valid_number)
 
    button_entry = Button(start,text="Entry",command=valid_number,font=("Impact", 16),bg="#4dff00",width=10,state=NORMAL)
    button_entry.place(x=180,y=200)
    
    
    
    start.mainloop()


def mediator(event=None):#pylint: disable=unused-argument
    close_root()
    start_the_gam()
    

#button start
    
start_game=Button(root,text="Start The Game",bg="#4dff00",width="30",height="2",font=("Impact", 16),command=mediator )
start_game.place(x=100,y=150)

#button information

information = Button(root,text="Information",bg="#87CEEB",width="20",height="1",font=("Impact", 10),command=information_def)
information.place(x=360,y=380)

#button creator

creator = Button(root,text="Creator",bg="#87CEEB",width="20",height="1",font=("Impact", 10),command=creator_def)
creator.place(x=10,y=380)
root.bind("<Return>", mediator)
root.bind("<e>", creator_def)
root.bind("<r>", information_def)

root.mainloop()


