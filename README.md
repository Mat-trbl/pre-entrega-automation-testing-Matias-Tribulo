# 🧪 Proyecto de Automatización de Pruebas: SauceDemo

En este proyecto se realizo una **automatización de pruebas** para el sitio web **SauceDemo** (https://www.saucedemo.com/), utilizando **Selenium WebDriver** y **Python**.

## 🎯 Propósito del Proyecto

El objetivo principal es automatizar los flujos de navegacion web dentro de la página **SauceDemo** y **garantizar** que las funcionalidaes y elemento del sitio web se comporten como se espera mediante pruebas automatizadas.

***

## 🛠️ Tecnologías Utilizadas

Las siguientes tecnologías y librerías son fundamentales para el desarrollo y la ejecución de las pruebas:

* **Python**: Lenguaje de programación principal.
* **pytest**: Framework de testing para la gestión y ejecución de pruebas.
* **pytest-html**: Plugin para generar reportes de prueba en formato HTML.
* **Selenium WebDriver**: Herramienta para la automatización de navegadores web.

***

## ⚙️ Instalación y Configuración

Sigue estos pasos para configurar el entorno y ejecutar las pruebas:

1.  **Requisito de Python:** Asegúrate de tener **Python 3.7 o superior** instalado.
2.  **WebDriver:** Descarga el **WebDriver** correspondiente a tu navegador (se utilizo firefox para este proyecto) .
3.  **Clonar el Repositorio:**
    git clone https://github.com/Mat-trbl/pre-entrega-automation-testing-Matias-Tribulo.git
4.  **Instalar Dependencias:** Instala las librerías necesarias mediante `pip`:
    ```bash
    pip install selenium pytest pytest-html
    ```
***

## ✅ Casos de Prueba

Los siguientes casos de prueba están implementados en el archivo `tests/test_saucedemo.py`:

* **`test_login`**: Carga las credenciales para loguearse y verifica el acceso correcto a la página de inventario después de un inicio de sesión exitoso.
* **`test_catalogo`**: Comprueba la correcta visualización de productos y la accesibilidad del menú principal.
* **`test_carrito`**: Valida que la funcionalidad, de **agregar un producto al carrito**, funcione correctamente.

***

## ▶️ Ejecución de Pruebas

### Ejecución Estándar

Para ejecutar todas las pruebas en el archivo `test_saucedemo.py`:

pytest -v
***
### Ejecución Estándar y reporte

Para ejecutar las pruebas y generar un reporte detallado en formato HTML dentro del directorio reporte/:

pytest tests/test_saucedemo.py -v --html=./reporte/reporte.html
