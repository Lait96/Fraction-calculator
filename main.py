from CalcModule import FractionCalc


a = FractionCalc(*map(int, input().split()))
b = FractionCalc(*map(int, input().split()))


print(a / b)
