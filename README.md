# investmentmap-opendata-downloader

Este repositorio facilita la descarga centralizada de datos abiertos de las plataformas abiertas y públicas de InvestmentMap del BID.

## Acerca de MapaInversiones

MapaInversiones es una iniciativa del Banco Interamericano de Desarrollo (BID) que promueve la transparencia en el gasto, las inversiones y las contrataciones públicas en América Latina y el Caribe. Esto se logra a través de plataformas digitales que integran y visualizan datos públicos de manera accesible y comprensible.

## Descripción del Repositorio

Este repositorio se enfoca en la centralización y automatización del proceso de descarga de datos abiertos de las plataformas InvestmentMap del BID. Se utiliza un archivo JSON que contiene los enlaces de descarga, el código ISO2 del país, la URL de descarga, el nombre del conjunto de datos y un diccionario de datos asociado.

## Funcionamiento del Script

El script Python incluido en este repositorio lee el archivo JSON y descarga los archivos de datos de las plataformas InvestmentMap del BID. Esto permite un manejo más eficiente de los datos para su posterior análisis y uso.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas colaborar en este proyecto, siéntete libre de enviar solicitudes de extracción con mejoras, correcciones de errores o nuevas características que consideres útiles.

## Dependencias

Asegúrate de tener instalada la biblioteca `requests` en tu entorno de Python. Puedes instalarla utilizando el siguiente comando:

```
pip install requests
```

## Países Incluidos

El script está configurado para trabajar con los siguientes países que forman parte de la iniciativa MapaInversiones del BID:

- Paraguay (PY)
- Argentina (AR)
- Jamaica (JM)
- República Dominicana (DO)
- Perú (PE)
- Costa Rica (CR)
- Colombia (CO)
- Honduras (HN)
- Panamá (PA)

## Nota Importante

Este proyecto se encuentra en desarrollo activo. Si encuentras algún problema o tienes sugerencias para mejorar, no dudes en abrir un problema en el repositorio o contactar a los mantenedores del proyecto.

Para obtener más información sobre MapaInversiones, visita [este enlace](https://www.iadb.org/es/quienes-somos/tematicas/reforma-modernizacion-del-estado/mapainversiones).

# Disclaimer y Licencia

Este repositorio sirve exclusivamente como un recolector de datasets abiertos sobre las plataformas públicas y abiertas de MapaInversiones del Banco Interamericano de Desarrollo (BID). Su único objetivo es facilitar la descarga centralizada de estos datos para promover la transparencia y accesibilidad de la información pública.

Este proyecto no tiene ningún otro objetivo más allá de este y no está asociado con ninguna actividad comercial o de lucro. No se hace responsable de cualquier uso indebido de los datos recolectados.

Este repositorio está bajo una licencia MIT, lo que significa que puedes usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender copias del software, siempre y cuando se reconozca adecuadamente la autoría del software original en todas las copias o partes sustanciales del software. Sin embargo, es importante recordar que este es un resumen y no reemplaza los términos legales de la licencia MIT. Para más detalles sobre la licencia, por favor consulta el archivo LICENSE en este repositorio..

---
*Última actualización: Abril 2024*
