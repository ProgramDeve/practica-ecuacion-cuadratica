# ecuacion.py
import math

def resolver_ecuacion(a, b, c):
    """
    Resuelve ax^2 + bx + c = 0.
    Retorna un diccionario con:
      - "tipo": "dos_soluciones", "una_solucion", "sin_solucion_real" o "lineal"
      - "soluciones": lista con las soluciones
    Lanza ValueError si a=0 y b=0.
    """
    # Caso no cuadrático
    if a == 0:
        if b == 0:
            raise ValueError(
                'No es una ecuacion valida: a y b no pueden ser ambos 0'
            )
        # Ecuación lineal: bx + c = 0  →  x = -c/b
        return {"tipo": "lineal", "soluciones": [-c / b]}

    # Discriminante
    disc = b ** 2 - 4 * a * c   # ✅ correcto

    if disc < 0:
        # Sin solución real (raíces complejas)
        return {"tipo": "sin_solucion_real", "soluciones": []}

    if disc == 0:
        # Una solución real (raíz doble)
        return {"tipo": "una_solucion", "soluciones": [-b / (2 * a)]}

    # Dos soluciones reales distintas
    raiz = math.sqrt(disc)
    x1 = (-b + raiz) / (2 * a)
    x2 = (-b - raiz) / (2 * a)
    return {"tipo": "dos_soluciones", "soluciones": [x1, x2]}