# Off-Pc

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

- `Pc-Off.py` → Código fuente principal.
- `config.json` → Archivo con configuraciones personalizadas.
- `icono-OffPc.ico` → Ícono de la aplicación.

También se incluye un archivo `.rar` con dos versiones compiladas de la aplicación:

### 🔧 Versión en Directorio

Una carpeta con todos los archivos necesarios para ejecutar la app (`Off-Pc.exe`, DLLs, íconos, etc.). Ejecuta el `.exe` dentro de la carpeta.

### 🗃️ Versión Un Solo Archivo

Un único archivo ejecutable `Off-Pc.exe`. Puedes ejecutarlo directamente, pero puede tardar unos segundos en abrir por primera vez.
