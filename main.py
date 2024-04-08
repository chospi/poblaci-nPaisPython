import matplotlib.pyplot as plt

#Se descarga la libreria y se pone alias de plt


#creamos funcion para generar grafica
def generate(labels, values):
 
  fig,ax = plt.subplots() #son dos valores que nos da la librería, fig es como la figura y ax se refire a las coordenadas donde  vamos a empezar a graficar
  ax.bar(labels,values)
  plt.show()

def generate_pie(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis("equal")#Necesario para que el grafico sea circular y centrada
  plt.show()

def population_by_country(data, country):
  result = list(filter(lambda i: i["Country/Territory"] == country, data))
  population_country = {k:v for k,v in result[0].items() if k.endswith("Population")}
  labels = population_country.keys()
  #Para traer los valores de la clave en #entero y no salga en string
  values = [int(values) for values in population_country.values()]
  return labels, values

def read_csv(path):
  with open(path, "r") as csvfile: #Abrir y cerrar el archivo, con solo lectura
    reader = csv.reader(csvfile, delimiter=",")
    """
    Aca llamamos el modulo CSV y le decimos que lea el archivo que tenemos que hemos llamado csvfile
    """
    header = next(reader)#Leemos la primera linea del archivo y la guardamos en header
    data = [] #Creamos una lista vacia para llenarla de diccionarios
    for row in reader:#Iteracion para leer fila por fila
      #print("****"*5)ME indique cada row que escriba
      iterable = zip(header, row)#Unzip para unir los dos arrays en tuplas, el header y el row
      #Creamos un diccionario con dict comprehension
      country_dic = {key:value for key, value in iterable}
      data.append(country_dic)#Agregamos el diccionario a la lista
    return data  

