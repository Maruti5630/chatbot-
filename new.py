from tkinter import *
# from xyz import response


# chat msg
import random as rd


hlw=['hi','hlw','hello','welcome','hey','hey...','hey!']
hlw_ans=['hi\n    How may i help you','hlw\n   How may i help you','hello\n   How may i help you','welcome\n    How may i help you','hey! How may i help you','hey...','hey! How may i help you']

menu=['menu please','menu','where is menu','food menu']
menu_ans=['sr.  Items     price\n1.   Samosa     10/-\n2.   Tea         8/-\n3.   Sandwich   35/- \n4.   Pizza     399/-\n5.   Dossa     100/-\n']

order=['self service','wetar service','how can i order']
order_ans=['You have self service option \n you can go reception and do your order']


thnk=['okk','thnk','okey','ohk','thanks','thankyou','thnks','thnku']
thnk_ans=['Welcome','have a good day']

def click1():
    user=msg_val.get()
    ust=Label(root,text=user,relief='sunken',padx=10).pack(side='top',anchor='ne')
    if(user.lower() in hlw):
        return(rd.choice(hlw_ans)+'\n')
    elif(user.lower() in menu):
        return(rd.choice(menu_ans)+'\n')
    elif(user.lower() in order):
        return(rd.choice(order_ans)+'\n')
    elif(user.lower() in thnk):
        return(rd.choice(thnk_ans)+'\n')
    else:
        return("Sia:- Can't understand\n")
        


# tkinter

def click2():
    a=click1()
    with open('input1.txt','w')as f:
        return(f.write(f'{a}'))

# window setting
root=Tk()
root.title('Resturant ka chatbot')
root.geometry('560x500')
# root.resizable(width=False,height=False)
# input area
msg_val=StringVar()
msg=Entry(root,textvariable=msg_val,width=60,relief='sunken',bg='orange',fg='black').pack(side='bottom',anchor='sw')

Label(root,text='Bot',padx=5).pack(side='top',anchor='nw')
# output
def click():
    
    click2()
    with open('input1.txt','r') as g:
        (Label(text=g.read(),relief='sunken',padx=5).pack(side='top',anchor='nw'))


# submit button
Button(text='submit',command=click,width=25,height=1,relief='sunken').pack(side='bottom',anchor='se')




root.mainloop()
