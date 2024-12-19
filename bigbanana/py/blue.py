import tkinter as tk

def create_green_window():
    root = tk.Tk()
    root.title("大香蕉")
    root.configure(bg="blue")
    root.geometry("400x400")

    # 添加文字
    label = tk.Label(root, text="你的电脑被大香蕉控制了！", fg="black", bg="blue", font=("Arial", 16))
    label.pack()

    root.mainloop()

if __name__ == "__main__":
    create_green_window()
