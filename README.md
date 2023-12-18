# CF Crypto

Ejercicios y ejemplos de criptografía para clase de ciencias computacionales, usando Python.

## Obteniendo números aleatorios

En `random_bits` puedes ver algunos ejemplos de uso de la librería `random` de Python y también la librería `secrets`.

## Hashes

En la carpeta `hashes` puedes ver ejemplos usando la librería `hashlib` de Python. Sólo usamos `md5` y `sha256`, te invito a experimentar con diferentes valores para que entiendas cómo se comportan.

Algunas preguntas:

- ¿Cuántos bits de salida tiene cada función?
- ¿Por qué es irrecuperable la información de entrada?

Si tienes curiosidad, puedes investigar sobre las **construcciones de esponja** que es lo más novedoso en funciones hash criptográficas.

## Ejemplo urandom

En el archivo ejemplo_urandom.txt, puedes encontrar un ejemplo de datos extraídos de `/dev/urandom`. Son 2MB. Están formateados en hexadecimal, por lo que cada byte se representa con dos caracteres. Por ejemplo, el byte `0x0A` se representa como `0A`.

## Ejercicios

- Investiga cómo usar AES-256 en tu lenguaje de programación
- Investiga cómo usar RSA en tu lenguaje de programación

En la biblioteca más popular de Python, está dentro de un sub-paquete que se llama `hazmat`, que es una contracción de `hazardous materials` (materiales peligrosos). Pregunta: **¿Por qué se consideraría que usar AES-256 directamente es peligroso?**.


## Lecturas extra

En los siguientes artículos puedes leer sobre los temas que vimos en clase:

- [Matemáticas para criptografía](https://blog.thedojo.mx/2021/12/25/matematicas-para-criptografia.html)
- [Criptografía básica para programadores: ¿Qué es la criptografía?](https://blog.thedojo.mx/2019/11/12/criptografia-basica-para-programadores-que-es-la-criptografia.html)
- [Recursos para aprender criptografía en 2022](https://blog.thedojo.mx/2021/12/08/recursos-para-aprender-criptografia-en-2021.html)
- [Cifrados de Bloque](https://blog.thedojo.mx/2020/12/03/tipos-de-algoritmos-criptograficos.html)
- [Cifrados de Flujo](https://blog.thedojo.mx/2021/12/12/tipos-de-algoritmos-criptograficos-cifrados-de-flujo.html)
- [¿Qué es un hash?](https://blog.thedojo.mx/2021/12/02/algoritmos-criptograficos-que-es-un-hash.html)
- [Las tres garantía de seguridad de un hash](https://blog.thedojo.mx/2023/08/28/las-tres-garantias-de-seguridad-de-un-hash.html)
- [Hashes seguros para alamcenar passwords](https://blog.thedojo.mx/2021/12/03/algoritmos-criptograficos-hashes-seguros-para-alamcenar-passwords.html)
- [Criptografía VS computación cuántica](https://blog.thedojo.mx/2021/12/11/criptografia-vs-computacion-cuantica.html)
- [Problemas difíciles de la computación y su relación con la criptografía: Problemas NP](https://blog.thedojo.mx/2023/02/03/problemas-dificiles-de-la-computacion-y-su-relacion-con-la-criptografia.html)
- [Crea hashes resistentes a balas con Keccak](https://blog.thedojo.mx/2022/10/12/crea-hashes-resistentes-a-balas-con-keccak-tambien-llamado-sha-3.html)
- [Máquinas de Turing no Deterministas y problemas NP](https://blog.thedojo.mx/2023/02/08/maquinas-de-turing-no-deterministas-y-problemas-np.html)
- [Generadores de números aleatorios y su importancia](https://blog.thedojo.mx/2021/12/07/generadores-de-numeros-aleatorios-y-su-importancia-para-el-desarrollo.html)
- [Criptografía para desarrolladores: códigos de autenticación de mensajes](https://blog.thedojo.mx/2021/12/30/criptografia-para-desarrolladores-codigos-de-autenticacion-de-mensajes.html)
