from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PyPDF2 import PdfWriter, PdfReader
import os


root = Tk()
root.title('PDF PROTECTION SERVICES')
root.geometry("700x430+300+100")
root.resizable(False,False)
root.configure(bg="#404040")
root.wm_iconbitmap('')



def browse():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                      title = 'Select Image File',
                                      filetype=(('PDF File','*.pdf'),('all files','*.*')))
    entry1.insert(END,filename)


def secure():
    mainfile=source.get()
    protectfile=target.get()
    code=password.get()

    if mainfile == "" and protectfile == "" and password.get() == "":
        messagebox.showerror('Invalid','Please fill out all columns')

    elif mainfile == "":
        messagebox.showerror('Invalid','Enter Valid PDF Source')
    
    elif protectfile == "":
        messagebox.showerror('Invalid','Enter Target PDF File Name')
    
    elif password.get() == "":
        messagebox.showerror('Invalid','Enter Valid Password')

    else:
        try:
            out = PdfWriter()
            with open(filename, "rb") as f:
                file = PdfReader(f)
                num = len(file.pages)

                for idx in range(num):
                    page = file.pages[idx]
                    out.add_page(page)

            #Password
            out.encrypt(code)

            if not protectfile.endswith('.pdf'):
                protectfile += '.pdf'

            with open(os.path.join(os.path.dirname(filename), protectfile), "wb") as f:
                out.write(f)

            source.set("")
            target.set("")
            password.set("")

            messagebox.showinfo("Attention", "Your PDF has been protected")

        except Exception as e:
            messagebox.showerror("Invalid", f"An error occurred: {e}")
            print(e)


frame = Frame(root,bg="#404040",width=680,height=290,bd=15,relief=GROOVE)
frame.configure(highlightbackground="white", highlightcolor="white", highlightthickness=7)
frame.place(x=10,y=10)

source = StringVar()
Label(frame,text='ORIGINAL PDF FILE ~',font=('Comic Sans MS', 12, 'bold'), fg='white',bg="#404040").place(x=30,y=50)

entry1 = Entry(frame,width=30,textvariable=source,font=('Comic Sans MS', 12),bd=2)
entry1.place(x=240,y=48)

Button(width=5,bg='#BBD4FF',text='Browse',font=('Comic Sans MS',12),relief=RAISED,bd=2,command=browse).place(x=600,y=73)

target = StringVar()
Label(frame,text='PROTECTED PDF NAME ~',font=('Comic Sans MS', 12, 'bold'), fg='white',bg="#404040").place(x=30,y=130)

entry2 = Entry(frame,width=30,textvariable=target,font=('Comic Sans MS', 12),bd=2)
entry2.place(x=245,y=130)

password = StringVar()
Label(frame,text='SECURED PASSWORD ~',font=('Comic Sans MS', 12, 'bold'), fg='white',bg="#404040").place(x=30,y=210)

entry3 = Entry(frame,width=30,textvariable=password,font=('Comic Sans MS', 12),bd=2)
entry3.place(x=240,y=210)

secure = Button(root,text='PROTECT PDF FILE',compound=RIGHT,width=30,height=2,bd=3,bg='#BBD4FF',font=('Comic Sans MS',14,'italic'),relief=RAISED,command=secure)
secure.pack(side=BOTTOM,pady=40)

root.mainloop()