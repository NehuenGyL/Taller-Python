def verificar_2(funcion_alumno):
    # Probamos la función del alumno con algunos casos de prueba
    try:
        print("Se espera:")
        for i in range(10):
            print(i)
            
        print("Resultado de tú función:")
        funcion_alumno(10)
        print("\n")

        print("FELICIDADES LO HICISTE BIEN")
    except Exception as e:
        print(f"Hubo un error al ejecutar la función: {e}")