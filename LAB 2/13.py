#Curency Notes
amount=int(input('Enter Amount: '))
Hrs=amount/100
print("Hundred Rs Notes: ",Hrs)
Frs=(amount%100)/50
print("Fifty Rs Notes: ",Frs)
Trs=(((amount%100)%50)/10)
print("Ten Rs Notes: ",Trs)

