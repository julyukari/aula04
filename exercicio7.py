soma=0
num= int(input("digite a quantidade de numeros que você quer: "))
for x in range(num):
  nums= int(input("digite os numeros :"))
  soma=soma+nums
media=soma/num
print(f" a media é {media} ")
