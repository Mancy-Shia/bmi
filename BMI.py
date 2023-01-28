height = input('輸入身高:')
weight = input('輸入體重:')
height = float(height)
weight = float(weight)
bmi = weight / ((height / 100) ** 2)
# 18.5 24 27 30  35 
if bmi < 18.5:
    print("體重過輕")
elif bmi >= 18.5 and bmi < 24:
    print("正常")
elif bmi >= 24 and bmi < 27:
    print("稍重")
elif bmi >= 27 and bmi < 30:
    print("輕度肥胖")
elif bmi >= 30 and bmi < 35:
    print("中度肥胖")
elif bmi >= 35:
    print("重度肥胖")

