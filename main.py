# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re
# tentativa 1

species_names = ['Panthera leo','Felix catus','Homo sapiens','Homo habilis']
novos_nomes = (f'\x1B[3m {species_names} \x1B[0m')
print(novos_nomes)   #convertendo array inteiro para itálico

# --------------------------------------------------------------------------------------------------------------------#
# tentativa 2
texto = 'Panthera leo'

for item in species_names:
    if texto == item:
        item = (f'\x1B[3m {item} \x1B[0m')
        print(item) #imprimindo apenas um item

# após isso, varrer o array buscando pelas similaridades do que a gestora digitou.


#---------------------------------------------------------------------------------------------------------------------#
# tentativa 3

banco = ["Panthera leo"]
array = ["O nome científico do leão é Panthera leo"]

banco = ";".join(banco)
banco = banco.split()


array = ";".join(array)
array = array.split()

print(banco)
print(array)

x =0
for item in banco:
    for i in array:
        if item == i:
            array = " ".join(array)
            array = array.replace(i, (f'\x1B[3m {i} \x1B[0m'))
            print(array)


####________________________________________________nova_tentativa_________________________________________________#####

genero = ['Arabdopsis','Australopitechus','Canis','Homo','Listeria','Bacillus','Zea','Gorilla']
especie =['thaliana','afarensis','lupus','sapiens','monocytogens','cereus','mays','gorilla']

text = ['O nome da especie estudada é Arabdopsis thaliana , o lobo se chama Canis lupus , o humano se chama Homo sapiens , o gorila se chama Gorilla gorilla , a Listeria monocytogens é um microrganismo. Bacillus cereus é utilizado em lacteos. O milho se chama Zea mays . Australopitechus afarensis é um ancestral da espécie humana.']

text = ",".join(text)
text = text.split()
print(text)

for palavra in text:
    for gen in genero:
        if palavra == gen:
            x = text.index(palavra)
            text[x] = (f'\x1B[3m{palavra}\x1B[0m')
        ##print(text)

for subs in text:
    for spp in especie:
        if subs == spp:
            y = text.index(subs)
            text[y] = (f'\x1B[3m{subs}\x1B[0m')
            texto_final = " ".join(text)
            texto_final = texto_final.replace(",", " ,")
            texto_final = texto_final.replace(" . ", ". ")
            texto_final = texto_final.replace(" .", ". ")

print(texto_final)







































