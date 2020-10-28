from tkinter import *
from tkinter import filedialog
import pandas as pd
import errno


root = Tk()
root.geometry("800x600")
root.title("Final Attendance")

def takeAttendance():
    filePaths = filedialog.askopenfiles(title="Select files",filetypes=[("Text Files" , " *.txt " )]) # gives all files as a list

    files = [filePaths[x].name for x in range(0,len(filePaths))]  # only keeps the path of the file

    data = []
    for name in files:
        try:
            with open (name,encoding='utf-8-sig') as f:
                content = f.readlines()
                content = [l.rstrip("\n") for l in content]
                content = [x.strip() for x in content]

                for cont in content:
                    if len(cont) > 3:
                        data.append(cont)
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise

    finalList = list(set(data))

    names = Listbox(root,height=100,width=300)
    names.pack(pady=50)

    df = pd.DataFrame(finalList,columns=["Name"])
    df.to_csv("NameList.csv",index=False,encoding="utf-8")

    for x in range(0,len(finalList)):
        names.insert(END ,str(x+1) + ") " + finalList[x] + "\n")

btn = Button(root,text="Find The final list",command=takeAttendance,height=5).pack()

root.mainloop()
