import re
import random
import tkinter
from tkinter import filedialog,scrolledtext, messagebox
from tkinter import *
import os

questionfile = open(r"./questions.txt","r+",encoding='utf-8')
answerlist = []
n = 1

window = Tk()
window.title("Forformer")
window.geometry('1382x1047')
library = None
lines = None


def main():
    return None


def library():
    global library
    file0 = filedialog.askopenfilenames(initialdir=os.path.dirname(__file__))
    file1 = "".join(file0)
    library = open(file1,"r",encoding='utf-8').read()

def words():
    global lines
    lines = filedialog.askopenfilenames(initialdir=os.path.dirname(__file__))
    lines1 = "".join(lines)
    lines = open(lines1,"r",encoding='utf-8').readlines()
    for line in lines:
        bringline ="".join(line)
        txtworld.insert(INSERT, bringline)


def getwordsfromtext():
    newlines = txtworld.get()


def printquestion(lines,library):
        global n
        for eachline in lines:
            eachline = "".join(eachline.splitlines(False))
            selflist = []
            while True:
                if eachline.find(',') != -1:
                    selflist.append(eachline[:eachline.find(',')])
                    eachline =eachline[eachline.find(',') + 1:]
                else:
                    selflist.append(eachline)
                    break

            sentences = re.findall("[A-Z]{1}[^.]*.",library)  #分析所有语句
            for i in selflist:
                for sentence in sentences:
                    while True:
                        qword = "".join(random.sample(selflist,1))
                        question = re.sub("\w*"+i+"\w*","_____("+qword+")",sentence)
                        answer = "".join(re.findall("\w*"+i+"\w*",sentence))
                        if qword != answer:
                            break
                    if question != sentence and answer not in answerlist:
    #                        print(question,"\n答案:"+answer)
    #                        questionfile.write(question+"\n答案:"+answer+"\n")
                            answerlist.append(answer)     #避免出答案相同的题目
                            bringquestion = question+"\n"
                            bringanswer = answer+"\n"
                            print (question,answer)
                            txt.insert(INSERT, str(n)+". "+bringquestion+"答案:"+bringanswer+"\n")
                            n+=1




def process():
    global library
    global lines
    if library == None:
        messagebox.showerror('az','你的句库是不是还没导入？')
    elif lines == None:
        messagebox.showerror('az','你的词库是不是还没导入？')
    else:
        printquestion(lines,library)


txt = scrolledtext.ScrolledText(window, width=80, height=50)
txt.place(x=20,y=20)

txtworld = scrolledtext.ScrolledText(window, width=40, height=50)
txtworld.place(x=970,y=20)

btn = Button(window, text="导入句库", command=library)
btn.place(x=850,y=20)

btg = Button(window, text="生成", command=process)
btg.place(x=850,y=970)

btg = Button(window, text="导入词库", command=words)
btg.place(x=850,y=70)



window.mainloop()

if __name__ == "__main__":
    main()
