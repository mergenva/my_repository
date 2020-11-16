# Пересекаются ли две прямые с данными уравнениями.
# Для решения задачи надо ссылаться на то, что множители x должны быть равны при двух параллельных прямых

import re
ur1 = "y =  -1x + 4"
ur2 = "y =x -12"
# char_eq = ur1.find("=")
# char_x = ur1.find("x")
# # Вариант-1 Безрегулярки
# k1 = int(ur1[ur1.find("=") + 1:ur1.find("x")])
# k2 = int(ur2[ur2.find("=") + 1:ur2.find("x")])
# print(k1)
# Вариант-2
"y =   -12x -12"
template = r"=\s*(-?\d+)x"
res = re.findall(template, ur1)
k1 = 1 if not res else int(res[0])
res = re.findall(template, ur2)
k2 = 1 if not res else int(res[0])
print("k1=", k1)
print("k2=", k2)
if res:
    k1 = 1
else:
    k1 = res[0]

if k1 != k2:
    print('Пересекаются')
else:
    print("Не пересекаются")
