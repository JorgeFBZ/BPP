# Actividad 1:
import pandas as pd
from statistics import mean
import plotly.express as px
# Clases errores 

class Error(Exception):
    pass
class Comprobar_num_meses(Error):
    pass
class Columna_vacia(Error):
    pass

def resultados_mes(mes):
    gasto_mes=0
    ingresos_mes = 0
    for dato in mes:
        #print (type(dato),dato)
        if dato < 0:
            gasto_mes += dato
        else:
            ingresos_mes+=dato
    return gasto_mes, ingresos_mes

def gasto_ahorro_max(df):
    gastos=[]
    ingresos=[]
    ahorros= []
    meses = df.columns.tolist()
    for mes in df:
        gasto, ingreso = resultados_mes(df[mes])
        gastos.append(gasto)
        ingresos.append(ingreso)
        ahorros.append(ingreso+gasto)

    print (f"Gasto máximo: {max(gastos)} en el mes {meses[gastos.index(max(gastos))]}")
    print (f"Ingreso máximo: {max(ingresos)} en el mes {meses[ingresos.index(max(ingresos))]}")
    print (f"Ahorro máximo: {max(ahorros)} en el mes {meses[ahorros.index(max(ahorros))]}")
    return gastos, ingresos, ahorros




try:
    archivo = r"Leccion 1\finanzas2020[1].csv"
    data = pd.read_csv(archivo, sep="\t")
    datos_ok = pd.DataFrame()
    meses = data.columns.tolist()
    # Comprobar numero de meses:
    if len(meses) != 12:
        raise Comprobar_num_meses
    # Comprobación de datos
    for columna in data:
        check=len(data.columns)
        if check ==0:
            raise Columna_vacia 
        datos=[]
        for dato in data[columna]:
            if type(dato)==str:
                try:
                    # Borra las ''
                    d =int(dato.replace("'",""))
                    datos.append(d)
                except ValueError:
                    #Cambia el dato erroneo por 0
                    print (f"Eliminado -> {dato}")
                    datos.append(0)

            else:
                datos.append(dato)
        
        datos_ok[columna]=datos

    # 1- ¿Qué mes se ha gastado más?
    # 2- ¿Qué mes se ha ahorrado más?
    gastos, ingresos, ahorro =gasto_ahorro_max(datos_ok)
    # 3- ¿Cuál es la media de gastos al año?
    print (f"Media de gastos anual: {mean(gastos)}")
    # 4- ¿Cuál ha sido el gasto total a lo largo del año?
    # 5- ¿Cuáles han sido los ingresos totales a lo largo del año?
    print (f"Gasto total anual: {sum(gastos)}")
    print (f"Ingreso total anual: {sum(ingresos)}")

    # 6- Realice una gráfica de la evolución de ingresos a lo largo del año.
    df=pd.DataFrame()
    df["Mes"]= meses
    df["Gastos"]=gastos
    df["Ingresos"]= ingresos
    df["Ahorro"]= ahorro
    fig = px.bar(df,x="Mes", y=["Gastos","Ingresos", "Ahorro"])
    fig.show()


except Comprobar_num_meses:
    print ("ERROR -> Los datos introducidos no contienen 12 meses")
except Columna_vacia:
    print ("ERROR -> Hay una columna vacía en los datos")
except IOError:
    print ("ERROR -> El archivo no existe")


