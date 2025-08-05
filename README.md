# nistcli

`nistcli` es una herramienta de línea de comandos escrita en Python que permite buscar vulnerabilidades (CVEs) en la base de datos del [National Vulnerability Database (NVD)](https://nvd.nist.gov/) del NIST.

Puedes buscar por fabricante, producto y versión, y obtener los resultados (inglés o español) en la terminal o en un informe HTML.

## Instalación

Instalar `nistcli` con `pipx`en linux:

```bash
pipx ensurepath && source ~/.bashrc
pipx install git+https://github.com/siriil/nistcli.git
```

## Uso

A continuación se muestra la ayuda del script:

```
usage: nistcli.py [-h] -vr <VENDOR> -p <PRODUCT> -vp <VERSION PRODUCT>
                  -lg <es,en> [-oSTD] [-oHTML [OHTML]]

Lookup CVEs in NIST NVD

options:
  -h, --help            show this help message and exit
  -vr <VENDOR>          Vendor
  -p <PRODUCT>          Product
  -vp <VERSION PRODUCT>
                        Version
  -lg <es,en>           Language ['es', 'en']
  -oSTD                 Output in STDOUT
  -oHTML [OHTML]        Output in HTML
```

## Ejemplos

### Búsqueda en la terminal

Aquí puedes ver un ejemplo de cómo se ve la salida en la terminal:

![Captura de pantalla de la terminal](URL)

### Informe HTML

Y aquí una captura del informe HTML generado:

![Captura de pantalla del informe HTML](URL)
