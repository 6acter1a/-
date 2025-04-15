import tkinter as tk
from tkinter import messagebox
from chemical_reaction import ReactionSimulator
def calculate_reaction():
    try:
        order = int(order_var.get())
        a0 = float(entry_a0.get())
        at = float(entry_at.get())
        time = float(entry_time.get())
        if a0 <= 0 or at <= 0 or time <= 0:
            raise ValueError
        simulator = ReactionSimulator(order, a0, at, time)
        rate = simulator.calculate_rate()
        if rate is None:
            result_label.config(text="입력값이 유효하지 않습니다.")
        else:
            result_label.config(text=f"계산된 반응 속도: {rate}")
    except ValueError:
        messagebox.showerror("입력 오류", "유효한 숫자를 모두 입력했는지 확인하세요.")
# GUI
root = tk.Tk()
root.title("반응 속도 계산기")
tk.Label(root, text="반응 차수 (0, 1, 2):").grid(row=0, column=0, sticky="e")
order_var = tk.StringVar(value="1")
tk.OptionMenu(root, order_var, "0", "1", "2").grid(row=0, column=1)
tk.Label(root, text="[A]₀ (초기 농도):").grid(row=1, column=0, sticky="e")
entry_a0 = tk.Entry(root)
entry_a0.grid(row=1, column=1)
tk.Label(root, text="[A]ₜ (시간 t 후 농도):").grid(row=2, column=0, sticky="e")
entry_at = tk.Entry(root)
entry_at.grid(row=2, column=1)
tk.Label(root, text="시간 t (초):").grid(row=3, column=0, sticky="e")
entry_time = tk.Entry(root)
entry_time.grid(row=3, column=1)
tk.Button(root, text="계산하기", command=calculate_reaction).grid(row=4, column=0, columnspan=2, pady=10)
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)
root.mainloop()