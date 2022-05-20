
####________________________________________________Conversão automática de palavras para itálico_________________________________________________#####

## recebimento dos bancos

genero = ['Salmonela','Bacillus']   ## a célula de gêneros deve vir aqui
especie =['enterica','cereus']  ## a célula de epíteteto específico deve vir aqui

## recebimento do input

text = ['Salmonela enterica e Bacillus cereus group foram encontrados'] ## a célula do texto deve vir aqui

# tratamento do input
   #transformacao do array em string

text = ",".join(text)

   #conversao para array

text = text.split()

#print(text)

#tratamento dos generos, comparando os generos presentes no input de texto com os generos presentes no banco

for palavra in text:
    for gen in genero:
        if palavra == gen:
            x = text.index(palavra)
            text[x] = (f'\x1B[3m{palavra}\x1B[0m')
        ##print(text)

# tratamento das especies, comparando as especies presentes no input com as especies presentes no banco

for subs in text:
    for spp in especie:
        if subs == spp:
            y = text.index(subs)
            text[y] = (f'\x1B[3m{subs}\x1B[0m')
            texto_final = " ".join(text)    #aqui eu converto o código para string e afasto as pontuacoes
            texto_final = texto_final.replace(",", " ,")
            texto_final = texto_final.replace(".", " .")
            texto_final = texto_final.replace(";", " ;")
            texto_final=texto_final.split()

# tratamento das pontuacoes que poderiam estar juntas do texto e ocasionar problemas na conversao das palavras

for newspp in texto_final:
    for newItembank in especie:
        if newspp == newItembank:
            z = texto_final.index(newspp)
            texto_final[z]=(f'\x1B[3m{newspp}\x1B[0m')

texto_final = " ".join(texto_final)
texto_final = texto_final.replace(" ,", ",")
texto_final = texto_final.replace(" .", ". ")
texto_final = texto_final.replace(" ;", ";")

print(texto_final)






































