import functions

def run(path):
  data = read_csv("./app/data.csv")
  country = input("¿Que pais quiere ver la población?")
  labels, values = population_by_country(data,country)
  generate(labels,values)

if __name__ == "__main__":
  run("./app/data.csv")
  
