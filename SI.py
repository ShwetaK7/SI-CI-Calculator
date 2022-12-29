P = input("\n Enter the principal amount: ")
T = input("\n Enter Number of Years: ")
R = input("\n Enter the rate: ")
#Process
Si = (int(P) * float(T) * float(R) ) /100
Ci = int(P) * (((1 + float(R)/100) ** int(T)) - 1)

AmountSI = int(P) + int(Si)
AmountCI = int(P) + int(Ci)
#Output
print("\n _________________________________Output_______________________________________")
print("\n Simple Interest = ",Si)
print("\n Compound Interest = ",Ci)
print("\n Amount For Simple Interest = ", AmountSI)
print("\n Amount For Compound Interest = ", AmountCI)


print("\n ________________________________________________________________________________")