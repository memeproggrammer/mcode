print ("mscript 1.0")
tkinterimported = False
while True:
    terminal = input(">")
    if (":") in terminal:
        variablename = terminal.replace(":", "")
        (variablename) = ("False")
    elif (" >>") in terminal:
        varname = terminal.replace(" >>", "")
        whatvalue = input("New Value:")
        if ("numb()") in whatvalue:
            numb = whatvalue.replace("numb(", "")
            numb = numb.replace(")", "")
            (varname) = int(numb)
        if ('"') in whatvalue:
            textstring = whatvalue.replace('"', "")
            (varname) = (textstring)
    elif ("print(") in terminal:
        textstring = terminal.replace("print(", "")
        textstring = textstring.replace(")", "")
        print (textstring)
    elif ("with ") in terminal:
        touse = terminal.replace("with ", "")
        if touse == ("Tkinter"):
            from tkinter import*
            print ("About Tkinter:")
            print ("Tkinter is a Graphical User Interface Module.")
            tkinterimported = True
    elif tkinterimported == True:
        if ("Tk(") in terminal:
            tktitle = terminal.replace("Tk(", "")
            tktitle = tktitle.replace(")", "")
            root = Tk()
            root.title(tktitle)
            root.mainloop()
    elif terminal == ("help"):
        print("print() - prints text of your choice into terminal")
        print("yourvarname: - makes new variable (default value is True)")
        print("varnamehere >> - set value on variable")
        print("with modulenamehere - imports module")
        print("Tk(Window Title) - ONLY FOR TKINTER MODULE, makes a Tkinter window")
    elif ("$$") in terminal:
        commenttext = terminal.replace("$$", "")
        print("Comment:",commenttext)
    elif terminal == ("credits"):
        print("Made by MemeProggrammer(GitHub) in python")
    else:
        print("unknown command")       



















        