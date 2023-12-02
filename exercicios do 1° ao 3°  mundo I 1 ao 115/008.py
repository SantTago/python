
#------------------------como eu fiz ---------------------------------------------

#Exercício Python 8: Escreva um programa que leia 
# um valor em metros e o exiba convertido em centímetros e milímetros.

h = float(input('digite uma distancia em metros: '))
h1 = h *100
h2 = h1 *1000
print('{} Metro(os) \n{} centimetros \n{} milimitros '.format(h, h1, h2))

#------------------------como o professor fez ---------------------------------------------

media = float(input(' digite uma distancia: '))
cm = media *100
mm = media *1000
print('A media de {}M e corresponte a {}cm e {}mm '.format (media, cm, mm))
