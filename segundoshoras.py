



segundo = int(input().strip())
hora = int(segundo // 3600)
res = segundo % 3600
minuto = int( res // 60)
seg = int( res % 60)
print(f'{hora}:{minuto}:{seg}')


              
           



