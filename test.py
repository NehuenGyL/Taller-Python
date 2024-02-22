import unittest
import prueba as pb

class TestEjercicio01(unittest.TestCase):
    def test_funcion_01(self):
        # Caso de prueba 1: Suma de números positivos
        num1_pos = 5
        num2_pos = 10
        resultado_pos = pb.funcion_01(num1_pos, num2_pos)
        resultado_esperado_pos = 15
        self.assertEqual(resultado_pos, resultado_esperado_pos)

        # Caso de prueba 2: Suma de números negativos
        num1_neg = -3
        num2_neg = -7
        resultado_neg = pb.funcion_01(num1_neg, num2_neg)
        resultado_esperado_neg = -10
        self.assertEqual(resultado_neg, resultado_esperado_neg)

        # Caso de prueba 3: Suma entre positivos y negativos
        num1_mix = 8
        num2_mix = -4
        resultado_mix = pb.funcion_01(num1_mix, num2_mix)
        resultado_esperado_mix = 4
        self.assertEqual(resultado_mix, resultado_esperado_mix)

        # Caso de prueba 4: Suma de un entero y un flotante
        num_entero = 5
        num_float = 3.5
        resultado_float = pb.funcion_01(num_entero, num_float)
        resultado_esperado_float = 8.5
        self.assertEqual(resultado_float, resultado_esperado_float)

if __name__ == '__main__':
    resultado_test = unittest.main(argv=[''], verbosity=2, exit=False)

    hc_tests = resultado_test.result.testsRun
    hc_fallas = len(resultado_test.result.failures)
    hc_errores = len(resultado_test.result.errors) + hc_fallas  # Sumar las fallas como errores
    hc_ok = hc_tests - hc_errores

    archivo_test = open('resultado_test.csv', 'w')
    archivo_test.write('Total_Tests,Errores,Correctos\n')
    archivo_test.write(str(hc_tests) + ',' + str(hc_errores) + ',' + str(hc_ok) + '\n')
    archivo_test.close()

    print('Resumen')
    print('Total Correctos:', str(hc_ok))
    print('Total Errores:', str(hc_errores))
