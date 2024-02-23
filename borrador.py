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
    def test_imprimir_numeros(self):
        # Redirigiendo la entrada estándar
        with unittest.mock.patch('builtins.input', return_value='5'):
            with io.StringIO() as mock_stdout:
                sys.stdout = mock_stdout
                pb.imprimir_numeros()
                output = mock_stdout.getvalue()
                self.assertEqual(output.strip(), "0\n1\n2\n3\n4\n5")




class TestEjercicio03(unittest.TestCase):
    def test_verificar_par_o_impar(self):
        # Caso de prueba 1: Número par
        with unittest.mock.patch('builtins.input', return_value='6'):
            with io.StringIO() as mock_stdout:
                sys.stdout = mock_stdout
                pb.verificar_par_o_impar()
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, "El número 6 es par.")

        # Caso de prueba 2: Número impar
        with unittest.mock.patch('builtins.input', return_value='9'):
            with io.StringIO() as mock_stdout:
                sys.stdout = mock_stdout
                pb.verificar_par_o_impar()
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, "El número 9 es impar.")



class TestEjercicio04(unittest.TestCase):
    def test_saludar(self):
        nombre_usuario = "Juan"
        expected_saludo = "Hola, Juan, ¿cómo estás?"
        
        with io.StringIO() as mock_stdout:
            sys.stdout = mock_stdout
            pb.saludar(nombre_usuario)
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, expected_saludo)



class TestEjercicio05(unittest.TestCase):
    def test_tabla_de_multiplicar(self):
        # Redirigiendo la entrada estándar
        with unittest.mock.patch('builtins.input', return_value='3'):
            with io.StringIO() as mock_stdout:
                sys.stdout = mock_stdout
                pb.tabla_de_multiplicar()
                output = mock_stdout.getvalue().strip()
                expected_output = "Tabla de multiplicar del 3:\n3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15"
                self.assertEqual(output, expected_output)


class TestEjercicio06(unittest.TestCase):
    def test_clasificar_edades(self):
        # Caso de prueba 1: Edad menor a 5 años
        with io.StringIO() as mock_stdout:
            sys.stdout = mock_stdout
            pb.clasificar_edades(3)
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Eres un bebé")

        # Caso de prueba 2: Edad entre 5 y 12 años
        with io.StringIO() as mock_stdout:
            sys.stdout = mock_stdout
            pb.clasificar_edades(10)
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Eres un niño")

        # Caso de prueba 3: Edad entre 13 y 19 años
        with io.StringIO() as mock_stdout:
            sys.stdout = mock_stdout
            pb.clasificar_edades(16)
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Eres un adolescente")

        # Caso de prueba 4: Edad igual o mayor a 20 años
        with io.StringIO() as mock_stdout:
            sys.stdout = mock_stdout
            pb.clasificar_edades(25)
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Eres un adulto")


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


