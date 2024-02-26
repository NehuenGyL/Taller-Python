import unittest
import prueba as pb
from io import StringIO
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
        
    def test_funcion_02(self):
        # Caso de prueba para funcion_02

        # Crear un objeto StringIO para simular la entrada del usuario
        input_data = "5\n"  # Puedes ajustar este valor según el caso de prueba
        sys.stdin = StringIO(input_data)

        # Capturar la salida estándar para verificarla más tarde
        output_data = StringIO()
        sys.stdout = output_data

        # Llamar a la función
        pb.funcion_02()

        # Restaurar la entrada y salida estándar
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        # Verificar la salida esperada
        expected_output = "0\n1\n2\n3\n4\n5\n"
        # Ajustar la comparación para omitir el mensaje de entrada
        self.assertEqual(output_data.getvalue().lstrip('Ingrese un número: '), expected_output)

    def test_funcion_03(self):
        # Caso de prueba para funcion_03
        # Puedes ajustar el valor en input_data según el caso de prueba
        input_data = "7\n"
        sys.stdin = StringIO(input_data)

        # Capturar la salida estándar para verificarla más tarde
        output_data = StringIO()
        sys.stdout = output_data

        # Llamar a la función
        pb.funcion_03()

        # Restaurar la entrada y salida estándar
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        # Verificar la salida esperada
        expected_output = "El número 7 es impar.\n"
        # Ajustar la comparación para omitir el mensaje de entrada
        self.assertEqual(output_data.getvalue().lstrip('Ingrese un número: '), expected_output)

    def test_funcion_04(self):
        # Caso de prueba para funcion_04
        nombre = "Juan"
        resultado = pb.funcion_04(nombre)
        resultado_esperado = "Hola, Juan, ¿cómo estás?"
        self.assertEqual(resultado, resultado_esperado)

    def test_funcion_05(self):
        # Caso de prueba para funcion_05
        # Puedes ajustar el valor en input_data según el caso de prueba
        input_data = "3\n"
        sys.stdin = StringIO(input_data)

        # Capturar la salida estándar para verificarla más tarde
        output_data = StringIO()
        sys.stdout = output_data

        # Llamar a la función
        pb.funcion_05()

        # Restaurar la entrada y salida estándar
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        # Verificar la salida esperada
        expected_output = "Tabla de multiplicar del 3:\n3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15\n"
        # Ajustar la comparación para omitir el mensaje de entrada
        self.assertEqual(output_data.getvalue().lstrip('Ingrese un número: '), expected_output)

    def test_funcion_06(self):
        # Caso de prueba para funcion_06
        # Puedes ajustar el valor en input_data según el caso de prueba
        input_data = "18\n"
        sys.stdin = StringIO(input_data)

        # Capturar la salida estándar para verificarla más tarde
        output_data = StringIO()
        sys.stdout = output_data

        # Llamar a la función
        pb.funcion_06()

        # Restaurar la entrada y salida estándar
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        # Verificar la salida esperada
        expected_output = "Eres un adolescente\n"
        # Ajustar la comparación para omitir el mensaje de entrada
        self.assertEqual(output_data.getvalue().lstrip('Ingrese su edad: '), expected_output)




if __name__ == '__main__':
    resultado_test = unittest.main(argv=[''], verbosity=2, exit=False)

    hc_tests = resultado_test.result.testsRun
    hc_fallas = len(resultado_test.result.failures)
    hc_errores = len(resultado_test.result.errors) + hc_fallas  # Sumar las fallas como errores
    hc_ok = hc_tests - hc_errores

    archivo_test = open('resultado_test.csv', 'w')
    archivo_test.write('Total_Tests,Errores,Correctos\n')
    archivo_test.write(str(hc_tests) + ',' + str(hc_errores) + ',' + str(hc_ok) + '\n')

    print('Resumen')
    print('Total Correctos:', str(hc_ok))
    print('Total Errores:', str(hc_errores))

    archivo_test.close()  # Move the close statement here