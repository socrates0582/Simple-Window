import tkinter as tk

root = tk.Tk()
root.title("Socrates First Program")
root.geometry("300x150")

label = tk.Label(root, text="Pressing OK closes this program.", pady=20)
label.pack()

ok_button = tk.Button(root, text="OK", command=root.destroy, width=10)
ok_button.pack(pady=10)

root.mainloop()
