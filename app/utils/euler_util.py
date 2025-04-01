
def metodo_euler(f, x0, y0, xf, n):
    h = (xf - x0) / n
    x, y = x0, y0
    resultados = []

    for i in range(n + 1):
        resultados.append({"x": x, "y": y})
        y = y + h * f(x, y)
        x = x + h

    return resultados