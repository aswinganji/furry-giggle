from tkinter import*
root = Tk()
root.title("Pqwes")
root.geometry("900x600")

tttt = Label(root,text ="Text")
tttt1 = Label(root,text ="Text2")
tttt2 = Label(root,text ="Text3")
class blah:
    def percentage(self):
        mth = 1
        t = 100
        tikk = mth/t
        tkkk = tikk*100
        tttt['text'] = tkkk
        
        
class blah2:
    def percentage(self):
        mth = 9
        t = 100
        tikk = mth/t
        tkkk = tikk*100
        tttt1['text'] = tkkk
        
class blah3:
    def percentage(self):
        mth = 27
        t = 100
        tikk = mth/t
        tkkk = tikk*100
        tttt2['text'] = tkkk
        

blah12 = blah()
blah13 = blah2()
blah14 = blah3()


y = Button(root,text = "tryu",command = blah12.percentage)
y1 = Button(root,text = "tryu2",command = blah13.percentage)
y2 = Button(root,text = "tryu600",command = blah14.percentage)

tttt.pack()
tttt1.pack()
tttt2.pack()
y.pack()
y1.pack()
y2.pack()

root.mainloop()
    
