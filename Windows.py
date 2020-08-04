from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import subprocess
from tkinter import filedialog
from shutil import copy2
import os
import TextPreProcessing
import Main
import ListSum

class Windows:

    def __init__(self, where, window):
        self.Mainframe = where
        self.sparkIterations = 0


    def logo(self): #IMMAGINE INZIALE
        bg = ImageTk.PhotoImage(Image.open("big_data.png"))
        self.logo = Label(self.Mainframe, image=bg)
        self.logo.photo = bg
        self.logo.pack()

    def logo1(self):  # IMMAGINE INZIALE
        bg1 = ImageTk.PhotoImage(Image.open("big_data 1.png"))
        self.logo1 = Label(self.Mainframe, image=bg1)
        self.logo1.photo = bg1
        self.logo1.pack()

    def logo2(self):  # IMMAGINE INZIALE
        bg2 = ImageTk.PhotoImage(Image.open("big_data 2.png"))
        self.logo2 = Label(self.Mainframe, image=bg2)
        self.logo2.photo = bg2
        self.logo2.pack()
    
    def choise(self): #SCHERMATA PRINCIPALE DOVE VIENE LANCIATO LO SCRIPT

        #suddivisione principale nelle 3 sezioni
        self.insertWord = Frame(self.Mainframe, height=100, width=500, bg="white", highlightthickness=1, highlightbackground="black")
        self.datasets = Frame(self.Mainframe, height=350, width=500, bg="lightblue", pady = 5, borderwidth=5)
        self.buttons = Frame(self.Mainframe, height=100, width=500, bg="lightblue")

        #inserimento parola
        self.labelWord = Label(self.insertWord, text="Insert the word")
        self.entryWord = Entry(self.insertWord)

        self.labelWord.grid(row=1)
        self.entryWord.grid(row=2)

        #lista dataset

        self.dataset1 = Frame(self.datasets, padx=3, bg="lightblue")
        self.dataset2 = Frame(self.datasets, padx=3, bg="lightblue")
        self.dataset3 = Frame(self.datasets, padx=3, bg="lightblue")

        self.dataset1.grid(row=1, column=1)
        self.dataset2.grid(row=1, column=2)
        self.dataset3.grid(row=1, column=3)

        self.classicalTextLabel = Label(self.dataset1, text="Classical", bg="lightblue")
        self.classicalTextLabel.pack()

        self.renaissanceTextLabel = Label(self.dataset2, text="Renaissance", bg="lightblue")
        self.renaissanceTextLabel.pack()

        self.modernTextLabel = Label(self.dataset3, text="Modern", bg="lightblue")
        self.modernTextLabel.pack()

        self.listbox1 = Listbox(self.dataset1)
        self.listbox1.pack()
        a = subprocess.check_output("./script1.sh", shell=True).decode("utf-8")

        for lines in a.splitlines():
            self.listbox1.insert(END, lines.replace(".txt",""))

        self.listbox2 = Listbox(self.dataset2)
        self.listbox2.pack()
        a = subprocess.check_output("./script2.sh", shell=True).decode("utf-8")

        for lines in a.splitlines():
            self.listbox2.insert(END, lines.replace(".txt", ""))

        self.listbox3 = Listbox(self.dataset3)
        self.listbox3.pack()
        a = subprocess.check_output("./script3.sh", shell=True).decode("utf-8")

        for lines in a.splitlines():
            self.listbox3.insert(END, lines.replace(".txt", ""))



        #bottoni

        self.button1 = Frame(self.buttons, bg="lightblue")
        self.button2 = Frame(self.buttons, bg="lightblue")
        self.button3 = Frame(self.buttons, bg="lightblue")


        self.loadDatasetButton = Button(self.button1, text="Add dataset", command=self.addDataset, bg = "white", highlightbackground="lightblue")
        self.synonymousButton = Button(self.button2, text="Find synonymous", command=self.synonymous, bg = "white", highlightbackground="lightblue")
        self.deleteDatasetButton = Button(self.button3, text="Delete Dataset", command=self.deleteDataset, bg = "white", highlightbackground="lightblue")


        self.button1.grid(row=1, column=1, padx=10)
        self.button2.grid(row=1, column=2, padx=10)
        self.button3.grid(row=1, column=3, padx=10)

        self.loadDatasetButton.pack()
        self.synonymousButton.pack()
        self.deleteDatasetButton.pack()

        self.insertWord.grid(row=1)
        self.datasets.grid(row=2)
        self.buttons.grid(row=3)
        
    def unpackMainFrame(self):
        for widget in self.Mainframe.winfo_children():
            widget.destroy()

    def addDataset(self):


        self.unpackMainFrame()
        self.classicalFrame = Frame(self.Mainframe, height=400)
        self.renaissanceFrame = Frame(self.Mainframe, pady=10, bg="lightblue")
        self.modernFrame = Frame(self.Mainframe)

        classicalImg = ImageTk.PhotoImage(Image.open("classical.jpg"))
        self.classicalLabel = Label(self.classicalFrame, image=classicalImg)
        self.classicalLabel.photo = classicalImg
        self.classicalLabel.pack()

        renaissancelImg = ImageTk.PhotoImage(Image.open("renaissance.jpg"))
        self.renaissanceLabel = Label(self.renaissanceFrame, image=renaissancelImg)
        self.renaissanceLabel.photo = renaissancelImg
        self.renaissanceLabel.pack()

        modernImg = ImageTk.PhotoImage(Image.open("modern.jpg"))
        self.modernLabel = Label(self.modernFrame, image=modernImg)
        self.modernLabel.photo = modernImg
        self.modernLabel.pack()

        self.classicalLabel.bind("<Button-1>", self.loadClassicalDataset)
        self.renaissanceLabel.bind("<Button-1>", self.loadReinassanceDataset)
        self.modernLabel.bind("<Button-1>", self.loadModernDataset)

        self.classicalFrame.grid(row=1, column=1)
        self.renaissanceFrame.grid(row=1, column=2)
        self.modernFrame.grid(row=1, column=3)

        Button(self.Mainframe, text="< Back", command=self.abortLoadDataset, highlightbackground = "lightblue").grid(row=2, column=2)

    def abortLoadDataset(self):
        self.unpackMainFrame()
        self.choise()

    def loadClassicalDataset(self, x):

        dir = filedialog.askopenfilename(initialdir = "/",title = "Select dataset",filetypes = (("text files","*.txt"),("all files","*.*")))

        print(dir)


        if (dir!=""):

            file_name = os.path.basename(dir)

            TextPreProcessing.TextPreProcessing(dir).lowFilter()
            copy2("temp.txt", "1/" + file_name)

            TextPreProcessing.TextPreProcessing(dir).filter()
            copy2("temp.txt", "1s/" + file_name)

            self.unpackMainFrame()
            self.choise()

    def loadReinassanceDataset(self, x):

        dir = filedialog.askopenfilename(initialdir = "/",title = "Select dataset",filetypes = (("text files","*.txt"),("all files","*.*")))
        if (dir!=""):

            file_name = os.path.basename(dir)

            TextPreProcessing.TextPreProcessing(dir).lowFilter()
            copy2("temp.txt", "2/" + file_name)

            TextPreProcessing.TextPreProcessing(dir).filter()
            copy2("temp.txt", "2s/" + file_name)
            self.unpackMainFrame()
            self.choise()

    def loadModernDataset(self, x):

        dir = filedialog.askopenfilename(initialdir ="/",title = "Select dataset",filetypes = (("text files","*.txt"),("all files","*.*")))
        if (dir!=""):
            file_name = os.path.basename(dir)

            TextPreProcessing.TextPreProcessing(dir).lowFilter()
            copy2("temp.txt", "3/" + file_name)

            TextPreProcessing.TextPreProcessing(dir).filter()
            copy2("temp.txt", "3s/" + file_name)

            self.unpackMainFrame()
            self.choise()
            
    def deleteDataset(self):

        self.listbox1.get(ACTIVE)
        a = self.listbox1.curselection()

        self.listbox2.get(ACTIVE)
        b = self.listbox2.curselection()

        self.listbox3.get(ACTIVE)
        c = self.listbox3.curselection()

        if (a!=()):
            file = self.listbox1.get(a)
            os.remove("1/"+file+".txt")
            os.remove("1s/"+file+".txt")

        if (b!=()):
            file = self.listbox2.get(b)
            os.remove("2/"+file+".txt")
            os.remove("2s/"+file+".txt")

        if (c!=()):
            file = self.listbox3.get(c)
            os.remove("3/"+file+".txt")
            os.remove("3s/"+file+".txt")

        tkinter.messagebox.showinfo("","Dataset " + file + " deleted!")

        self.unpackMainFrame()
        self.choise()

    def synonymous(self):

        self.word = self.entryWord.get()

        if (self.word == ""):

            tkinter.messagebox.showerror("EMPY WORD", "Empty word is not permitted")


        else:

            self.newWin = Toplevel()
            self.newWin.title("Set Options")
            self.newWin.resizable(False, False)

            self.newWin.grab_set()


            backgroundFrame = Frame(self.newWin, bg="lightblue", width=400, height=100, padx=20, pady=10)
            backgroundFrame.pack()


            titleFrame = Frame(backgroundFrame, bg="lightblue")
            titleFrame.pack()

            optionsFrame = Frame(backgroundFrame, bg="lightblue")
            optionsFrame.pack()

            buttonFrame = Frame(backgroundFrame, bg="lightblue", pady=10)
            buttonFrame.pack()

            self.checkClassic = IntVar()
            self.checkClassic.set(1)
            self.checkRenaissance = IntVar()
            self.checkModern = IntVar()
            self.checkStopwords = IntVar()

            self.iterations = IntVar(optionsFrame)
            self.iterations.set(5)


            Label(titleFrame, text="OPZIONI", bg="lightblue").pack()

            Label(optionsFrame, text="Model Iterations", bg="lightblue").grid(row=1, column=1, pady=5)
            Label(optionsFrame, text="Literary Genres", bg="lightblue").grid(row=2, column=1, pady=5)

            MenuIterations = OptionMenu(optionsFrame, self.iterations, 1, 2, 3, 5, 10, 20)
            MenuIterations.grid(row = 1, column = 2)
            MenuIterations.config(bg="lightblue")

            ClassicButton = Checkbutton(optionsFrame, variable=self.checkClassic, text="Classic", bg="lightblue")

            RenaissanceButton = Checkbutton(optionsFrame, variable=self.checkRenaissance, text="Renaissance", bg="lightblue")

            ModernButton = Checkbutton(optionsFrame, variable=self.checkModern, text="Modern", bg="lightblue")

            stopwordsNoButton = Checkbutton(optionsFrame, text="No stopwords",variable=self.checkStopwords, bg="lightblue")

            ClassicButton.grid(row=2, column=2)
            RenaissanceButton.grid(row=2, column=3)
            ModernButton.grid(row=2, column=4)

            stopwordsNoButton.grid(row=8, column=2)


            Button(buttonFrame, text="Start", command=self.run, bg = "white", highlightbackground="lightblue").pack()
            self.newWin.mainloop()

    def run(self):


        self.ClassicalOk = self.checkClassic.get()
        self.RenaissanceOk = self.checkRenaissance.get()
        self.ModernOk = self.checkModern.get()
        

        self.newWin.grab_release()
        self.unpackMainFrame()
        self.newWin.destroy()

        self.showResults(self.Mainframe)

        if (self.sparkIterations == 0):
            self.a = Main.Main()
            self.sparkIterations = self.sparkIterations + 1


        if (self.ClassicalOk):

            flag1 = TextPreProcessing.TextPreProcessing(1).datasetUnion(self.checkStopwords.get())

            path = "Classical/classical.txt"

            print ("classical elab ")
            print(path)
            print(self.word)
            print(self.iterations.get())

            if (flag1):

                syn_list_Classic = self.a.run(path, self.word, self.iterations.get())

                ListSum.ListSum(syn_list_Classic).stampa()

                self.showClassicalResults(syn_list_Classic)



        if (self.RenaissanceOk):


            flag2 = TextPreProcessing.TextPreProcessing(2).datasetUnion(self.checkStopwords.get())

            path = "Renaissance/renaissance.txt"

            print ("renaissance elab ")
            print(path)
            print(self.word)
            print(self.iterations.get())

            if(flag2):

                syn_list_Renaissance = self.a.run(path, self.word, self.iterations.get())

                ListSum.ListSum(syn_list_Renaissance).stampa()

                self.showRenaissanceResults(syn_list_Renaissance)



        if (self.ModernOk):

            flag3 = TextPreProcessing.TextPreProcessing(3).datasetUnion(self.checkStopwords.get())

            path = "Modern/modern.txt"

            print ("Modern elab ")
            print(path)
            print(self.word)
            print(self.iterations.get())

            if (flag3):

                syn_list_Modern = self.a.run(path, self.word, self.iterations.get())

                ListSum.ListSum(syn_list_Modern).stampa()

                self.showModernResults(syn_list_Modern)

    def showResults(self, master):

        results1 = Frame(master, padx=3, pady=5, bg="lightblue")
        results2 = Frame(master, padx=3, pady=5, bg="lightblue")
        results3 = Frame(master, padx=3, pady=5, bg="lightblue")
        button = Frame(master, pady=5, bg="lightblue")

        results1.grid(column = self.ClassicalOk, row=1)
        results2.grid(column = self.ClassicalOk + self.RenaissanceOk, row=1)
        results3.grid(column = self.ClassicalOk + self.RenaissanceOk + self.ModernOk, row=1)
        button.grid(row=2, column=1)

        Button(button, text="Try with another word", command=self.restart, bg = "white", highlightbackground="lightblue").pack()

        if (self.ClassicalOk):

            self.ClassicalResultListbox = Listbox(results1)
            self.ClassicalResultListbox.grid(row=2)

            classicalTextLabel = Label(results1, text="Classical", bg="lightblue")
            classicalTextLabel.grid(row=1)


        if (self.RenaissanceOk):

            self.RenaissanceResultListbox = Listbox(results2)
            self.RenaissanceResultListbox.grid(row=2)

            renaissanceTextLabel = Label(results2, text="Renaissance", bg="lightblue")
            renaissanceTextLabel.grid(row=1)


        if (self.ModernOk):

            self.ModernResultListbox = Listbox(results3)
            self.ModernResultListbox.grid(row=2)

            modernTextLabel = Label(results3, text="Modern", bg="lightblue")
            modernTextLabel.grid(row=1)

    def showClassicalResults(self, list):

        for x in list:

            self.ClassicalResultListbox.insert(END, x[0])

    def showRenaissanceResults(self, list):

        for x in list:

            self.RenaissanceResultListbox.insert(END, x[0])

    def showModernResults(self, list):

        for x in list:

            self.ModernResultListbox.insert(END, x[0])

    def restart(self):

        self.unpackMainFrame()

        self.choise()














