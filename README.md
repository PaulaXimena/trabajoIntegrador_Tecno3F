# 🎫 Sistema de Gestión de Tickets (Ticketera)

Este proyecto es el **Trabajo Integrador Final** desarrollado para el curso **Inicial de Python** dictado en **Tecno3F**. Consiste en una aplicación de consola interactiva pensada para simular un centro de soporte técnico o atención al cliente, permitiendo dar de alta incidentes, generar códigos de seguimiento automáticos y consultar la información almacenada en tiempo real.

---

## 👥 Integrantes del Grupo
El desarrollo de este sistema fue realizado de forma colaborativa por:
* **Vanesa Veron**
* **Gabriela Ayala**
* **Paula Caviglia**

---

## 🚀 Características Principales

El programa cuenta con un flujo dinámico que simula un entorno real y cumple con los siguientes requerimientos:
1.  **Menú Principal Interactivo:** Un panel inicial con validación de entradas numéricas para navegar entre las opciones de administración y la salida segura del sistema.
2.  **Módulo de Alta de Tickets:** * Captura datos clave del usuario: *Nombre*, *Sector*, *Asunto* y detalle del *Problema*.
    * Genera de forma automática un **ID único de ticket** utilizando números aleatorios acotados (entre 1000 y 9999).
    * Cuenta con bucles de control internos para agilizar la carga consecutiva de tickets sin necesidad de recargar la aplicación o pasar obligatoriamente por el menú principal.
3.  **Módulo de Consulta (Leer Ticket):** * Permite ingresar un número de ticket y buscar de forma instantánea si el registro existe utilizando estructuras indexadas eficientes (Diccionarios).
    * Muestra los detalles completos del incidente o advierte de forma clara si el número ingresado no coincide con ningún registro activo.
4.  **Finalización de Sesión Protegida:** Un sistema que exige doble confirmación del usuario antes de cerrar de manera definitiva la ejecución en la terminal.

---

##  Conceptos de Python Aplicados

Para la estructura y lógica interna de este trabajo, implementamos y consolidamos las herramientas esenciales aprendidas a lo largo de la cursada:
* **Estructuras de Control de Flujo:** Uso intensivo de bucles infinitos controlados (`while True`) combinados con declaraciones `break` y `continue`.
* **Estructuras de Datos Estructuradas:** Colecciones dinámicas de tipo **Diccionario** (`dict`) para almacenar cada ticket de forma persistente en memoria asignando parejas de *clave-valor*.
* **Modularización mediante Funciones:** Bloques de código independientes (`def`) para el alta, lectura y maquetado visual del menú, facilitando un código limpio, legible y reutilizable.
* **Validación de Datos:** Uso de métodos embebidos como `.strip()` para limpiar entradas vacías y `.isdigit()` para asegurar la correcta conversión de tipos de datos de texto a enteros.

---

##  Instrucciones de Ejecución

Para correr este programa de forma local en tu computadora, asegurate de tener instalado **Python 3.x** y realizá los siguientes pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/PaulaXimena/trabajoIntegrador_Tecno3F.git](https://github.com/PaulaXimena/trabajoIntegrador_Tecno3F.git)
