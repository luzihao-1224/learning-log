# day1.py —— 你的第一个 Python 脚本
# 目标：跑通它，感受变量、输入、字典、循环、求和

name = input("你叫什么名字？")
hours = float(input("今天打算学几小时？"))
print(f"{name}，今天投入 {hours} 小时")

# 顺便感受一下：为什么这里用 dict 而不是三个独立的变量？
plan = {"看语法": 1.5, "动手写代码": 1.5, "刷题": 0.5}
for task, h in plan.items():
    print(f"  {task}: {h} 小时")

print(f"计划合计 {sum(plan.values())} 小时")
