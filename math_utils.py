def find_max_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
      return num1
    elif num2 > num3:
      return num2
    else:
      return num3

def find_mean(num1, num2, num3):
    a = (num1+num2+num3)/3
     return a

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    a = num1 - mean
    b = num2 - mean
    c = num3 - mean
    d = a**2 + b**2 + c**2
    std = (d/3)**1/2
     return (mean, std)
