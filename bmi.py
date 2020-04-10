#elif if else practice (bmi)
height = input('how tall are you ? ')
weight = input('how weight are you ? ')
height = int(height)
weight = int(weight)
height = height / 100 # to meter
BMI = weight / (height * height)

if BMI >= 35 :
	print('重度肥胖', BMI)
elif BMI >= 30 and BMI < 35 :
	print('中度肥胖', BMI)
elif BMI >= 27 and BMI < 30 :
	print('輕度肥胖', BMI)
elif BMI >= 24 and BMI < 27 :
	print('過重', BMI)
elif BMI >= 18.5 and BMI < 24 :
	print('normal', BMI)
elif BMI <18.5 :
	print('過輕', BMI)

