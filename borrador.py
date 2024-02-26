import unittest
import prueba as pb
import io
import sys
import unittest.mock

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


class TestEjercicio02(unittest.TestCase):
    def test_funcion_02(self):
        # Redirigiendo la entrada estándar
        with unittest.mock.patch('builtins.input', return_value='5'):
            with io.StringIO() as mock_stdout:
                sys.stdout = mock_stdout
                pb.funcion_02()
                output = mock_stdout.getvalue()
                self.assertEqual(output.strip(), "0\n1\n2\n3\n4\n5")


class TestEjercicio03(unittest.TestCase):
    def test_funcion_03(self):
        # Caso de prueba 1: Número par
        with unittest.mock.patch('builtins.input', return_value='6'):
            with io.StringIO() as mock_stdout:
                sys.stdout = mock_stdout
                pb.funcion_03()
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, "El número 6 es par.")

        # Caso de prueba 2: Número impar
        with unittest.mock.patch('builtins.input', return_value='9'):
            with io.StringIO() as mock_stdout:
                sys.stdout = mock_stdout
                pb.funcion_03()
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, "El número 9 es impar.")


class TestEjercicio04(unittest.TestCase):
    def test_funcion_04(self):
        nombre_usuario = "Pepito"
        expected_saludo = f"Hola, {nombre_usuario}, ¿cómo estás?"

        with io.StringIO() as mock_stdout:
            sys.stdout = mock_stdout
            mensaje_saludo = pb.funcion_04(nombre_usuario)
            output = mock_stdout.getvalue().strip()

            # Verificar que el nombre del usuario esté en el saludo
            self.assertIn(nombre_usuario, mensaje_saludo)

        # Restablecer el flujo de salida estándar
        sys.stdout = sys.__stdout__

        # Verificar que el saludo generado coincida con el esperado
        self.assertEqual(expected_saludo, mensaje_saludo)


class TestEjercicio05(unittest.TestCase):
    def test_funcion_05(self):
        # Redirigiendo la entrada estándar
        with unittest.mock.patch('builtins.input', return_value='5'):
            with io.StringIO() as mock_stdout:
                sys.stdout = mock_stdout
                pb.funcion_05()
                output = mock_stdout.getvalue().strip()
                expected_output = "Tabla de multiplicar del 5:\n5 x 1 = 5\n5 x 2 = 10\n5 x 3 = 15\n5 x 4 = 20\n5 x 5 = 25"
                self.assertEqual(output, expected_output)


class TestEjercicio06(unittest.TestCase):
    def test_funcion_06(self):
        # Redirigiendo la entrada estándar
        with unittest.mock.patch('builtins.input', return_value='15'):
            with io.StringIO() as mock_stdout:
                sys.stdout = mock_stdout
                pb.funcion_06()
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, "Eres un adolescente")


if __name__ == '__main__':
    resultado_test = unittest.main(argv=[''], verbosity=2, exit=False)

    hc_tests = resultado_test.result.testsRun
    hc_fallas = len(resultado_test.result.failures)
    hc_errores = len(resultado_test.result.errors) + hc_fallas  # Sumar las fallas como errores
    hc_ok = hc_tests - hc_errores

    with open('resultado_test.csv', 'w') as archivo_test:
        archivo_test.write('Total_Tests,Errores,Correctos\n')
        archivo_test.write(f"{hc_tests},{hc_errores},{hc_ok}\n")

    print('Resumen')
    print('Total Correctos:', hc_ok)
    print('Total Errores:', hc_errores)
