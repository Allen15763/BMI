# BMI計算
height = input('請輸入身高_cm: ')
weight = input('請輸入體重_kg: ')
height = float(height) / 100
weight = float(weight)
BMI = weight / (height ** 2)
if BMI < 18.5:
	print('你的BMI是:', round(BMI, 2), '過輕')
elif BMI >= 18.5 and BMI < 24:
	print('你的BMI是:', round(BMI, 2), 'Normal')
elif BMI >= 24 and BMI < 27:
	print('你的BMI是:', round(BMI, 2), '稍重')
elif BMI >= 27 and BMI < 30:
	print('你的BMI是:', round(BMI, 2), '輕度肥胖')
elif BMI >= 30 and BMI < 35:
	print('你的BMI是:', round(BMI, 2), '中度肥胖')
else:
	print('你的BMI是:', round(BMI, 2), '重度肥胖')