import random
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import time

def shuffle_file_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    random.shuffle(lines)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)

def select_input_file():
    file_path = filedialog.askopenfilename(title="选择输入文件")
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)

def shuffle_action():
    input_file = input_entry.get()
    if not input_file:
        messagebox.showerror("错误", "请选择输入文件路径")
        return
    base_dir = os.path.dirname(input_file)
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    time_str = time.strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(base_dir, f"{base_name}_shuffled_{time_str}.txt")
    try:
        shuffle_file_lines(input_file, output_file)
        messagebox.showinfo("成功", f"文件已成功打乱并保存为：\n{output_file}")
    except Exception as e:
        messagebox.showerror("错误", f"处理文件时出错：{e}")

root = tk.Tk()
root.title("文本行随机打乱工具")

tk.Label(root, text="输入文件:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
input_entry = tk.Entry(root, width=40)
input_entry.grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="浏览", command=select_input_file).grid(row=0, column=2, padx=10, pady=5)

tk.Button(root, text="开始打乱", command=shuffle_action, width=20, bg="lightblue").grid(row=1, column=1, pady=15)

root.mainloop()