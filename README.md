# 🔑 Generador Automático de Contraseñas Seguras

Este proyecto es el **Trabajo Integrador Final** desarrollado para el curso **Inicial de Python** dictado en **Tecno3F**. Consiste en una aplicación interactiva de consola que permite a los usuarios diseñar y generar contraseñas personalizadas según sus necesidades de seguridad, seleccionando diferentes tipos de caracteres y longitudes.

---

## 👥 Integrantes del Grupo
El desarrollo de este sistema fue realizado de forma colaborativa por:
* **Vanesa Veron**
* **Gabriela Ayala**
* **Paula Caviglia**

---

## 🚀 Características Principales

El programa ofrece una interfaz fluida en la terminal y cuenta con los siguientes módulos de control:
1.  **Menú de Selección de Seguridad:** Un panel interactivo que clasifica el tipo de contraseña deseada en cuatro categorías:
    * Solo letras (Seguridad básica).
    * Solo números (Ideal para PINs numéricos).
    * Letras y números (Seguridad intermedia).
    * Letras, números y caracteres especiales (Máxima seguridad).
2.  **Validación Robusta de Longitud:** El sistema solicita al usuario la cantidad de caracteres deseados y valida que sea un número entero estrictamente mayor a 0 utilizando controles lógicos avanzados, previniendo fallos en la aplicación si se ingresan textos de forma errónea.
3.  **Generación Aleatoria Dinámica:** Utiliza algoritmos de aleatoriedad para seleccionar de forma equitativa componentes del grupo de caracteres seleccionados, garantizando combinaciones únicas y seguras en cada ejecución.
4.  **Bucle de Continuidad Controlado:** Una vez generada la clave, el programa se frena de manera obligatoria para consultar si se desea generar otra contraseña o salir, evitando la sobreexposición repetitiva del menú principal en pantalla.

---

##  Conceptos de Python Aplicados

Para el diseño de este software, aplicamos los conocimientos clave adquiridos durante el cuatrimestre:
* **Librerías Nativas (`random` y `string`):** Uso de `random.choice` para la selección impredecible de caracteres y las constantes complejas de `string` (`ascii_letters`, `digits`, `punctuation`).
* **Bucles Anidados Estructurados:** Implementación de ciclos infinitos controlados (`while True`) combinados con banderas lógicas (`True/False`) para el control de la interfaz visual.
* **Comprensión de Listas y Métodos de Cadenas:** Uso del método `''.join()` estructurado sobre un generador dinámico para unificar de forma eficiente los caracteres seleccionados.
* **Filtrado Exclusivo de Datos:** Uso de `.strip()`, `.lower()` y `.isdigit()` para sanitizar las entradas ingresadas por teclado, logrando un programa limpio y libre de errores.

---

##  Instrucciones de Ejecución

Para correr este programa de forma local en tu computadora, asegurate de tener instalado **Python 3.x** y realizá los siguientes pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/PaulaXimena/trabajoIntegrador_Tecno3F.git](https://github.com/PaulaXimena/trabajoIntegrador_Tecno3F.git)
