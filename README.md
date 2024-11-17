# Sopa de Letras

## Descripción del Proyecto
**Sopa de Letras** es un programa en Python que busca palabras dentro de una sopa de letras. El programa permite procesar una matriz de letras y buscar palabras en 8 direcciones (horizontal, vertical y diagonal). Al finalizar, genera un archivo JSON con los resultados indicando qué palabras fueron encontradas y cuáles no.

## Cómo Ejecutarlo

### Requisitos Previos
- **Python 3.8 o superior** debe estar instalado en tu computadora.

### Pasos para Ejecutar
1. Clona este repositorio en tu máquina:
   ```bash
   git clone https://github.com/tu-usuario/sopa-de-letras.git
   cd sopa-de-letras
2. Asegúrate de tener la siguiente estructura de carpetas:
sopa-de-letras/
├── SOPA/
│   └── sopa.txt
├── RESPUESTA/
└── main.py
Crea un archivo llamado sopa.txt dentro de la carpeta SOPA. Este archivo debe tener el siguiente formato:

yaml
Copiar código
ABCDE
FGHIJ
KLMNO
---
PALABRA1
PALABRA2
Primera parte: La sopa de letras como una cuadrícula (una fila por línea).
Separador: Una línea con ---.
Segunda parte: Lista de palabras a buscar.
Ejecuta el programa desde la terminal:

bash
python main.py
El programa generará un archivo resultados.json en la carpeta RESPUESTA con el reporte de búsqueda.

