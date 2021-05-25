# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 14:24:10 2020

App Name:Notes

@author: abhay

Version:0.0.0
1st version of this program

Version:0.0.1
Bugs Found and Cleared
1.n eater Bug Clear
2.Blank list topic cleared
3.Text Box font size increased

Version:0.0.2
1.Multi Screen Resolution Solution Added
  It Supports:
      1366 X 768
2.Code Quality Increased


"""

from tkinter import*
from getpass import getuser
import pyperclip as pc 

class GUI(Tk):
    
####################################################################################################
########################################################FONTEND WORKING#############################
    def __init__(self):#root=self inside class
        super().__init__()
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        self.coordinates = setit(f"{screen_width} X {screen_height}").mkplis()
        
        self.geometry(self.coordinates["geometry"])
        x = int(self.coordinates["geometry"].split('x')[0])
        y = int(self.coordinates["geometry"].split('x')[1])
        self.maxsize(x,y)
        self.minsize(x,y)
        
        self.title("Notes v0.0.2")
    
    def bar(self):
        m0 = Menu()
        m1 = Menu(m0,tearoff = 0)
        m1.add_command(label = "New", command = ftion().new)
        m1.add_command(label = "Save", command = ftion().save)
        m1.add_command(label = "Print", command = ftion().printtt)
        
        m2 = Menu(m0,tearoff=0)
        m2.add_command(label = "Copy Text", command = ftion().cpytxt)
        m2.add_command(label = "Cut Text", command = ftion().ctxt)
        m2.add_command(label = "Delete", command = ftion().delete)
        
        
        m3 = Menu(m0,tearoff=0)
        m0.add_cascade(label = "File", menu = m1)
        m0.add_cascade(label = "Edit", menu = m2)
        m0.add_command(label = "About", command = ftion().abt)
        self.config(menu = m0)
        
    def lab(self):
        lis = self.coordinates["headings"]
        for i in lis:
            if i[3] == None:
                l = Label(text = i[2], font = i[4], bg = "grey", fg = "white")
                l.place(x = i[0], y = i[1])
            else:
                if i[3] == "sticky":
                    l = Label(text = i[2], font = i[4], bg = "red", fg = "white")
                    l.place(x = i[0], y = i[1])
    
    def lbx(self):
        global listbox
        
        
        p1 = self.coordinates["listbx_scrollbar"][0]
        scrollbar = Scrollbar()
        scrollbar.place(x = p1[0], y = p1[1], height = p1[2])

        p2 = self.coordinates["listbx_scrollbar"][1]
        listbox = Listbox(yscrollcommand = scrollbar.set, font = p2[2], height = p2[3], width = p2[4])
        listbox.place(x = p2[0], y = p2[1])
        listbox.bind('<Double-1>',ftion().sel)

        
        scrollbar.config(command = listbox.yview)
    
    def btn(self):#button
        """ 
        txtlst = list of texts of buttons 
        plist = list of positions eg. plist = [(34,324),(123,123),...]
        """
        txtlst = self.coordinates["bottom2_buttons"][0]
        plist = self.coordinates["bottom2_buttons"][1]
        font_lst = self.coordinates["bottom2_buttons"][2]
        width_lis = self.coordinates["bottom2_buttons"][3]
        
        b = Button(text = txtlst[0], font = font_lst[0], width = width_lis[0], bg = "light yellow", command = ftion().new)#command = 
        b.place(x = plist[0][0], y = plist[0][1])
        
        b = Button(text = txtlst[1], font = font_lst[1], width = width_lis[1], bg = "light yellow", command = ftion().save)#command = 
        b.place(x = plist[1][0], y = plist[1][1])
        
    
    def stbar(self):#Status bar
        statusvar = StringVar()
        #initial set
        p1 = self.coordinates["bottom_statusbar"][0]
        statusvar.set(p1[0])
        sbar = Label(textvariable = statusvar, font = p1[1] ,relief = SUNKEN, anchor="e")
        
        p0 = self.coordinates["bottom_statusbar"][1]
        sbar.place(x = p0[0], y = p0[1],width = p0[2])
    
    def txtbx(self):
        global T0,T1
        
        p0 = self.coordinates["notes_heading"]
        T0 = Text(height = p0[2], width = p0[3], font = p0[4])
        T0.place(x = p0[0], y = p0[1])
        
        p1 = self.coordinates["notes_des"]
        T1 = Text(height = p1[2], width = p1[3], font = p1[4])
        T1.place(x = p1[0], y = p1[1])
        #Loading...
        username = getuser()
        saveprh = f"C:\\Users\\{username}\\Documents\\nots.dat"
        f = open(saveprh, "a")
        f.close()
        f = open(saveprh, "r")
        con = f.read()
        if len(con)>0:
            imps=""
            for i in con:
                if i=="\\":
                        continue
                else:
                    imps = imps + i
            st = imps.split("||||")
            for i in range(len(st)):
                stt = st[i].split("::::")
                listbox.insert(END, stt[0])
    
####################################################################################################
########################################################BACKEND WORKING#############################   
class ftion():
    """File"""
    def new(self):
        T0.delete("1.0", "end")
        T1.delete("1.0", "end")
        
    def save(self):
        hding = T0.get("1.0", "end")
        des = T1.get("1.0", "end")
        listbox.insert(END, hding)
        fos = hding + "::::" + des + "||||" #Data format
        username = getuser()
        saveprh = f"C:\\Users\\{username}\\Documents\\nots.dat"
        f = open(saveprh,"a+")
        f.write(fos)
        f.close()
    
    def printtt(self):
        from tkinter import messagebox
        messagebox.showerror("Error", "You do not have printer.")
        
    """Edit"""
    def cpytxt(self):#copy txt
        c1 = T0.selection_get()
        pc.copy(c1)

    def ctxt(self):#cut txt
        c1 = T0.selection_get()
        hding = T0.get("1.0", "end")
        des = T1.get("1.0", "end")
        if c1 in hding:
            T0.delete("1.0","end")
            pc.copy(hding)
        elif c1 in des:
            T1.delete("1.0","end")
            pc.copy(des)
        
    def delete(self):
        label = T0.get("1.0",'end-1c')
        if label != "":
            T0.delete("1.0","end")
            T1.delete("1.0","end")
            idx = listbox.get(0, END).index(label)
            listbox.delete(idx)
            username = getuser()
            saveprh = f"C:\\Users\\{username}\\Documents\\nots.dat"
            f = open(saveprh,"r")
            s = f.read()
            sm = s.split("||||")
            o=[]
            for i in sm:
                if label in i:
                    pass
                else:
                    o.append(i)
            data=""
            for i in range(0,len(o)-1):
                data = data + o[i] + "||||"
            
            f.close()
            f = open(saveprh,"w")
            f.write(data)
            f.close()
        else:
            from tkinter import messagebox
            messagebox.showinfo("Note", "Please double click on it then delete!")
        
        
    """About"""
    def abt(self):
        from tkinter import messagebox
        username = getuser()
        saveprh = f"C:\\Users\\{username}\\Documents\\nots.dat"
        messagebox.showinfo("About", f"Made by Abhay\nYour Data is saved here Keep Backup\n{saveprh}")
        
    """Help"""
    def hlp(self):
        pass
    
    def sel(self,ar):#dont know what os ar
        T0.delete("1.0","end")
        T1.delete("1.0","end")
        s = listbox.selection_get()
        username = getuser()
        saveprh = f"C:\\Users\\{username}\\Documents\\nots.dat"
        f = open(saveprh, "r")
        con = f.read()
        imps=""

        for i in con:
            if i=="\\":
                    continue
            else:
                imps = imps + i
        st = imps.split("||||")
        for i in range(len(st)):
            if s in st[i]:
                stt = st[i].split("::::")
                T0.insert("1.0",stt[0])
                T1.insert("1.0",stt[1])

#####################################Multi-Screen Solution####################################################
class setit:
    
    def __init__(self,screen_resolution):
        self.res = screen_resolution
        self.plist = {}
        
    def mkplis(self):
        
        if self.res == "1366 X 768":
            self.plist["geometry"] = "506x300"
            self.plist["headings"] = [[0, 0, "  T o p i c s  ", None,"bold 20"], [158, 0, "              Description            ", "sticky", "bold 20"]]
            self.plist["listbx_scrollbar"] = [[0,0,300],[17,35,'14',12,15]]
            self.plist["bottom2_buttons"] = [["New", "Save"], [(22, 266), (90, 266)],["bold 15","bold 15"],[5,5]]
            self.plist["bottom_statusbar"] = [["Notes","italic 14"],[158,270,347]]
            self.plist["notes_heading"] = [158,40,1,38,"bold 14"]
            self.plist["notes_des"] = [158,64,11,38,"25"]
            return self.plist


if __name__ == '__main__':
    window = GUI()
    window.bar()
    window.lab()
    window.lbx()
    window.stbar()
    window.btn()
    window.txtbx()
    window.mainloop()