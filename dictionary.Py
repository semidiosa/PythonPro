meme_dict = {
            "LOL": "una respuesta a algo gracioso",
            "CRINGE": "algo raro o embarazoso",
            "ROLF": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "AGGRO": "ponerse agresivo/enojado",
            "CREEPY": "aterrador, siniestro"
            }
            
word = input("Escribe una palabra que no entiendas") 

if word in meme_dict:
    print(meme_dict[word])
    
else:
    print("Oooops, parece que la palabra no esta en nuestro dictionario")
