import pandas as pd
from tabulate import tabulate

def f(x):
    return x**2 - 120*x + 100
def bisection(f, xl, xu, error):
    if f(xl) * f(xu) > 0:
        return "No hay raíces en el intervalo"

    iterations = 0
    xr_ant = 0
    data = []

    while (xu - xl) / 2 > error:
        xr = (xl + xu) / 2

        if xr_ant is None:
            error_absoluto = 0
        else:
            error_absoluto = abs(xr - xr_ant)


        data.append([iterations, xu, xl, xr, f(xu), f(xl), f(xr), f(xl) * f(xr), error_absoluto])

        if f(xr) == 0:
            xr_ant = xr
            iterations += 1
            break

        if f(xr) * f(xl) < 0:
            xu = xr
        else:
            xl = xr

        xr_ant = xr
        iterations += 1

    columns = ["Iteración", "xu", "xl", "xr", "f(xu)", "f(xl)", "f(xr)", "f(xl)f(xr)", "Error absoluto"]
    dataframe = pd.DataFrame(data, columns=columns)
    print(tabulate(dataframe, headers='keys', tablefmt='psql', showindex=False, numalign="center", stralign="center"))

    return xr, iterations


xl = 0
xu = 2
error = 0.01

raiz, num_iteraciones = bisection(f, xl, xu, error)

print("Raíz aproximada:", raiz)
print("Número de iteraciones:", num_iteraciones)

