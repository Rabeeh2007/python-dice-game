#Dice Game
import tkinter as tk
import random

root=tk.Tk()
root.title("Dice Game")
root.geometry("400x500")
root.resizable(False,False)

choices=[1,2,3,4,5,6]
user_score=0
computer_score=0
user_points=0
computer_points=0
game_over = False

def roll(user_opt):
    global game_over
    if game_over:
        reset("N")
        return
    global user_score,computer_score
    global user_points,computer_points
    computer_choice=random.choice(choices)
    comp_lab.config(text=f"Computer Choice: {computer_choice}")
    if(user_opt=="Roll"):
        user_choice=random.choice(choices)
        user_lab.config(text=f"Your Choice: {user_choice}")
        if(user_choice==1 or user_choice==5):
            user_points=0
        elif(user_choice==4): user_points+=user_choice*3
        elif(user_choice==6): user_points+=3
        elif(user_choice==2): user_points+=user_choice*7
        else:
            user_points+=user_choice
    else:
        user_lab.config(text=f"Your Choice: hold")

    if(computer_choice==1 or computer_choice==5):
        computer_points=0
    elif(computer_choice==4): computer_points+=computer_choice*3
    elif(computer_choice==6): computer_points+=3
    elif(computer_choice==2): computer_points+=computer_choice*7
    else:
        computer_points+=computer_choice
    
    point_lab.config(
        text=f"Points\nYou: {user_points}  |  Computer: {computer_points}"
    )
    if(user_points>70):
        user_score+=1
        result_lab.config(text="You Win")
        game_over = True
    elif(computer_points>70):
        computer_score+=1
        result_lab.config(text="Computer Win")
        game_over = True
    score_lab.config(
        text=f"Score\nYou: {user_score}  |  Computer: {computer_score}"
    )

def reset(opt):
    if(opt=="Y"):
        global user_score,computer_score
        user_score=0
        computer_score=0
        score_lab.config(text="Score\nYou: 0  |  Computer: 0")
    global user_points,computer_points,game_over
    game_over = False
    user_points=0
    computer_points=0
    result_lab.config(text="")
    point_lab.config(text="Points\nYou: 0  |  Computer: 0")
    user_lab.config(text="Your Choice: ")
    comp_lab.config(text="Computer Choice: ")

title=tk.Label(root,text="Dice Game",font=("Arial",18,"bold"))
title.pack(pady=10)

score_lab=tk.Label(root,text="Score\nYou: 0  |  Computer: 0",font=("Arial",14))
score_lab.pack(pady=10)

result_lab=tk.Label(root,text="",font=("Arial",14))
result_lab.pack(pady=10)

point_lab=tk.Label(root,text="Points\nYou: 0  |  Computer: 0",font=("Arial",14))
point_lab.pack(pady=10) 

user_lab=tk.Label(root,text="Your Choice: ",font=("Arial",14))
user_lab.pack(pady=10)  

comp_lab=tk.Label(root,text="Computer Choice: ",font=("Arial",14))
comp_lab.pack(pady=10)  

btn_frame=tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame,text="Roll",command=lambda:roll("Roll"),font=("Arial",14),relief="flat",bg="#2196F3",fg="white").grid(row=0, column=0, padx=10)
tk.Button(btn_frame,text="Hold",command=lambda:roll("Hold"),font=("Arial",14),relief="flat",bg="#2196F3",fg="white").grid(row=0, column=1, padx=10)
tk.Button(root, text="New Game", width=15, command=reset("Y")).pack(pady=20)

root.mainloop()