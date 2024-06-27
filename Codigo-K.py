print("Hola 😊,¿cómo estás?¡Qué interesante que quieras sabe los significados de estas palabras Kichwa!")
print("Te presento mi diccionario Kichwa")
    
Kichwa_dict = {
            "CARI": "Hombre",
            "WARMI": "Mujer",
            "WAWA": "Niño o niña",
            "RUCU": "Anciano",
            "MARCA": "Region",
            "USHANA": "Poder",
            "SUMA SUMAQ": "Belleza",
            }
for i in range(5):            
    Word = input("¿Que palabra en Kichwa te gustaria conocer su significado? Por favor escribela en mayusculas.")
    if Word in Kichwa_dict.keys():
        print(Kichwa_dict[Word])
    else:
        print("Esta palabra nose encuentra en el diccionario")
