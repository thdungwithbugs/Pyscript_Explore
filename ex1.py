import math
print([math.sqrt(i) for i in range(5)])

def BMI(cao, nang):
    return nang / (cao ** 2)
    
def phanloai(bmi):
    if bmi < 18.5:
        return "gầy"
    elif bmi < 24.9:
        return "bth"
    elif bmi < 29.9:
        return "hoi beo"
    elif bmi < 34.9:
        return "beo phi cap do 1"
    elif bmi < 39.9:
        return "beo phi cap do 2"
    else:
        return "beo phi cap do 3"
    
def nguyco(bmi):
    if bmi < 18.5:
        return "thấp"
    elif bmi < 24.9:
        return "trung bình"
    elif bmi < 29.9:
        return "cao"
    elif bmi < 34.9:
        return "cao"
    elif bmi < 39.9:
        return "rat cao"
    else:
        return "nguy hiem"
    
chieucao = float(input("nhap chieu cao (m):"))
cannang = float(input("nhap can nang (kg):"))
bmi = BMI(chieucao, cannang)
print("chi so BMI cua ban la:", bmi)
print("phan loai:", phanloai(bmi))
print("nguy co:", nguyco(bmi))        