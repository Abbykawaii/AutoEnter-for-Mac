import tkinter as tk
import pyautogui as pg
import time

IsWorking = False

def start_auto_input():
    # 设置为开始打印
    global IsWorking
    IsWorking = True
    status_label.config(text="正在打印...")
    # 延迟 3 秒，方便切换到目标窗口
    root.after(3000, auto_type)

def auto_type():
    global IsWorking
    # 获取文本框内容，并按行分割成列表，保留每行的缩进
    text_to_type = text_box.get("1.0", "end-1c").splitlines()

    # 逐行输入文本框内容
    pg.write("\n")
    for line in text_to_type:
        if not IsWorking:  # 检查是否需要取消输入
            status_label.config(text="已取消输入")
            return
        # 去除行首多余空格，以确保 VS Code 不会额外增加缩进
        clean_line = line.lstrip()  # 去除行首空格
        pg.write(clean_line)   # 输入当前行内容
        pg.press('enter')  # 换行
        time.sleep(0.1)  # 控制每行输入的间隔

    status_label.config(text="已完成自动输入")

def stop_auto_input():
    global IsWorking
    IsWorking = False  # 设置为 False 以停止输入

# 创建 Tkinter 窗口
root = tk.Tk()
root.title("AutoEnter for Mac")

# 标签和输入框
label = tk.Label(root, text="请输入要输入的文本:")
label.pack(pady=10)

text_box = tk.Text(root, width=100, height=30)
text_box.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)
# 按钮触发自动输入
start_button = tk.Button(button_frame, text="开始", command=start_auto_input)
start_button.pack(side="left",padx=5)

#取消按钮
stop_button = tk.Button(button_frame,text="取消",command=stop_auto_input)
stop_button.pack(side="right",padx=5)

#状态
status_label = tk.Label(root, text="")  # 初始状态为空
status_label.pack(pady=10)

# 运行 Tkinter 窗口
root.mainloop()