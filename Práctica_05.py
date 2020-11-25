import requests
from bs4 import BeautifulSoup as bs
import re

##Hice esto, pues para ver más rápido lo que este relacionado con el grupo que
##gusta y cuando no tengo tiempo de ponerme al día

print('En un momento nos mostrara los encabezados que tengan que ver con')
print('el grupo de kpop "TXT", además de proporcionarnos el link, por si')
print('la noticia nos interesa.')

##Una expresión regular para que coincida que solo nos proporcione lo que tenga
##que ver con el grupo
txt = re.compile(r'\bTXT\b', re.I)

##hacemos el requests a la pagina de lo más popular
response = requests.get('https://www.soompi.com/es/category/musica/popular')
soup = bs(response.content, 'html.parser')

lista = []

##por cada noticia vamos obteniendo el link
for i in soup.find_all('a'):
    lk = i.get('href')
    ##checamos si tiene que ver con txt
    si = txt.search(lk)
    if si != None:
        ##si es asi, metemos en una lista el titulo de la noticia y el link
        texto = i.get_text()
        lista.append(texto)
        lista.append('https://www.soompi.com/' + lk)

##eliminamos elementos repetidos
listita = set(lista)

##imprimimos cada noticia con su link
for inf in listita:
    print(inf)

    
    


        
