import wikipedia
import tkinter as tk


def search(event):
    content = search_box.get()
    if not content:
        T.delete("1.0", tk.END)
        T.insert(tk.END, "Write a search word")
        return
    result = wikipedia.summary(content, sentences=2, auto_suggest=False)
    print(content)
    T.delete("1.0", tk.END)
    T.insert(tk.END, result)


window = tk.Tk()
window.geometry("700x300")
search_box = tk.Entry(window)
search_box.place(x=0, y=0)
search_box.bind('<Return>', search)
T = tk.Text(window)
label = tk.Label(text="Search Wikipedia: ")
label.pack()
search_box.pack()
T.pack()
T.mainloop()
