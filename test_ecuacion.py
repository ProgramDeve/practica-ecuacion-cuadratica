# test_ecuacion.py
import unittest
from ecuacion import resolver_ecuacion


class TestEcuacion(unittest.TestCase):

    # ============================================================
    # 1) Dos soluciones reales distintas (D > 0)
    # ============================================================
    def test_dos_soluciones_reales(self):
        # x^2 - 5x + 6 = 0  →  x = 2 y x = 3
        res = resolver_ecuacion(1, -5, 6)
        self.assertEqual(res["tipo"], "dos_soluciones")
        self.assertAlmostEqual(res["soluciones"][0], 3.0)
        self.assertAlmostEqual(res["soluciones"][1], 2.0)

    # ============================================================
    # 2) Una solución real (D = 0, raíz doble)
    # ============================================================
    def test_una_solucion(self):
        # x^2 - 4x + 4 = 0  →  x = 2 (doble)
        res = resolver_ecuacion(1, -4, 4)
        self.assertEqual(res["tipo"], "una_solucion")
        self.assertAlmostEqual(res["soluciones"][0], 2.0)

    # ============================================================
    # 3) Sin solución real (D < 0)
    # ============================================================
    def test_sin_solucion_real(self):
        # x^2 + x + 1 = 0  →  sin raíces reales
        res = resolver_ecuacion(1, 1, 1)
        self.assertEqual(res["tipo"], "sin_solucion_real")
        self.assertEqual(res["soluciones"], [])

    # ============================================================
    # 4) Ecuación lineal (a = 0, b ≠ 0)
    # ============================================================
    def test_ecuacion_lineal(self):
        # 2x + 4 = 0  →  x = -2
        res = resolver_ecuacion(0, 2, 4)
        self.assertEqual(res["tipo"], "lineal")
        self.assertAlmostEqual(res["soluciones"][0], -2.0)

    # ============================================================
    # 5) Coeficientes inválidos (a = 0 y b = 0) → ValueError
    # ============================================================
    def test_coeficientes_invalidos(self):
        with self.assertRaises(ValueError):
            resolver_ecuacion(0, 0, 5)

    # ============================================================
    # 6) Múltiples casos con subTest
    # ============================================================
    def test_multiples_casos_con_subTest(self):
        casos = [
            # (a, b, c, tipo_esperado)
            (1, -5, 6, "dos_soluciones"),
            (1, -4, 4, "una_solucion"),
            (1, 1, 1, "sin_solucion_real"),
            (0, 3, 9, "lineal"),
            (1, 0, -4, "dos_soluciones"),
        ]
        for a, b, c, tipo_esp in casos:
            with self.subTest(a=a, b=b, c=c):
                res = resolver_ecuacion(a, b, c)
                self.assertEqual(res["tipo"], tipo_esp)

    # ============================================================
    # RETO — 3 pruebas nuevas
    # ============================================================

    # Reto 1: Coeficientes grandes
    def test_coeficientes_grandes(self):
        # 1000000x^2 + 1000000x + 1000000 = 0 → sin solución real
        res = resolver_ecuacion(1000000, 1000000, 1000000)
        self.assertEqual(res["tipo"], "sin_solucion_real")

    # Reto 2: Precisión decimal con places=10
    def test_precision_decimal(self):
        # x^2 - 2 = 0  →  x = ±√2 ≈ ±1.4142135624
        res = resolver_ecuacion(1, 0, -2)
        self.assertAlmostEqual(res["soluciones"][0], 1.4142135624, places=10)
        self.assertAlmostEqual(res["soluciones"][1], -1.4142135624, places=10)

    # Reto 3: Todos cero → ValueError
    def test_todos_cero(self):
        with self.assertRaises(ValueError):
            resolver_ecuacion(0, 0, 0)


if __name__ == '__main__':
    unittest.main()