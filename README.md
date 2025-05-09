# Off-Pc 🕒🖥️

**Off-Pc** es una aplicación de escritorio para Windows que permite programar el apagado automático de tu computadora mediante un cronómetro configurable. Ideal para momentos en los que deseas dejar la PC encendida solo por un tiempo determinado.

## 🕒 Características principales

- Temporizador con horas, minutos y segundos.
- Al llegar a cero:
  - Se muestra un mensaje final grande: **"Adiós"**.
  - Pasados 5 segundos, se apaga la computadora automáticamente.
- Interfaz sencilla y centrada en la pantalla.
- Se puede personalizar:
  - Colores del fondo.
  - Color en estado crítico.
  - Tiempo de segundos críticos (mínimo: 25 segundos).

## ⚙️ Configuración

La configuración personalizada se guarda en un archivo llamado `config.json`. Puedes modificar los ajustes desde la propia aplicación, en el botón de **Ajustes**.

## 📁 Archivos incluidos

- `Off-Pc.py` → Código fuente principal.
- `config.json` → Archivo con configuraciones personalizadas.
- `icono-OffPc.ico` → Ícono de la aplicación.

También se incluye un archivo `.rar` con dos versiones compiladas de la aplicación:

### 🔧 Versión en Directorio

Una carpeta con todos los archivos necesarios para ejecutar la app (`Off-Pc.exe`, DLLs, íconos, etc.). Ejecuta el `.exe` dentro de la carpeta.

### 🗃️ Versión Un Solo Archivo

Un único archivo ejecutable `Off-Pc.exe`. Puedes ejecutarlo directamente, pero puede tardar unos segundos en abrir por primera vez.

## 💡 Michel.sr145

Esta aplicación nació de una necesidad personal: muchas veces dejaba la computadora encendida por tareas que no requerían supervisión, como descargas largas, actualizaciones o la reproducción de música o películas.

### 🛏️ Ejemplo real:

> Cuando estaba viendo una película a altas horas de la noche, y luego de un tiempo me quedaba dormido.
> Con **Off-Pc**, puedo definir un tiempo y olvidarme de si me duermo, Ya que alfinal la PC se apaga sola.

Así evitando dejar la computadora encendida sin necesidad, ahorrando energía y alargando la vida útil del equipo.

Busqué una solución liviana, sin instalaciones complicadas, y que además se pudiera personalizar visualmente. Así surgió **Off-Pc**, una herramienta práctica y directa para cualquiera que quiera cuidar su equipo sin complicaciones.
