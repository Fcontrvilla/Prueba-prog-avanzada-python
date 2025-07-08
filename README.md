# Prueba-prog-avanzada-python



 +crear la arquitectura de clases básica que permite instanciar una campaña


 De la clase Anuncio:
● Al crear, o al querer modificar el alto o el ancho de un anuncio ya creado, debe
consultar si el valor que se quiere asignar es mayor a cero. De ser así, se asigna el
valor ingresado. De no ser así, se asigna 1.
● Para esta etapa no se le solicita implementar las reglas de los atributos url_archivo
ni url_clic, pero sí debe definir sus getter y setter con la lógica básica de
asignación de un nuevo valor al atributo correspondiente.
Al querer modificar el sub_tipo de algún anuncio ya creado, se debe validar que se
esté ingresando un subtipo dentro de los permitidos en el tipo de la instancia actual.
Los subtipos permitidos para las instancias de cada clase corresponden a los
elementos de la tupla definida en el atributo de clase SUB_TIPOS respectivo. En caso
de no cumplirse esta condición al momento de querer cambiar el valor del atributo
sub_tipo, se debe lanzar una excepción SubTipoInvalidoException.
● El método mostrar_formatos es un método estático que muestra en pantalla los
formatos y sus subtipos asociados disponibles para crear anuncios. Ejemplo:
FORMATO 1:

- Subtipo 1
- Subtipo 2
Para ello debe referenciar los atributos de clase respectivos que contienen la
información requerida (relación de colaboración señalada en el diagrama).

De la clase Video:
● Cada instancia de Video creada solo puede tener ancho igual a 1 y alto igual a 1.
Estos valores no se pueden modificar.
● Al crear, o al querer modificar el atributo duracion de una instancia de Video ya
creada, debe consultar si el valor que se quiere asignar es mayor a cero. De ser así, se
asigna el valor ingresado. De no ser así, se asigna 5.
● El método comprimir_anuncio implementado debe mostrar por pantalla el mensaje:
"COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN".
● El método redimensionar_anuncio implementado debe mostrar por pantalla el
mensaje: "RECORTE DE VIDEO NO IMPLEMENTADO AÚN".

De la clase Display:
● El método comprimir_anuncio implementado debe mostrar por pantalla el mensaje:
"COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN".
● El método redimensionar_anuncio implementado debe mostrar por pantalla el
mensaje: "REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN".

De la clase Social:
● El método comprimir_anuncio implementado debe mostrar por pantalla el mensaje:
"COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN".
El método redimensionar_anuncio implementado debe mostrar por pantalla el
mensaje: "REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO
IMPLEMENTADO AÚN".

De la clase Campaña:
● Se debe incluir en el constructor de la clase Campaña los parámetros y la lógica
necesaria para instanciar dentro de él los anuncios a incorporar en el atributo que
almacena el listado de anuncios. Como sugerencia, puede usar en el constructor un
parámetro que sea una estructura de datos que contenga la información necesaria
para crear cada instancia de Anuncio (por ejemplo, una tupla con diccionarios).
Opcionalmente, puede refactorizar esta lógica específica en un método privado.
● Al querer modificar el nombre de una campaña ya creada, se debe validar que el nuevo
nombre no supere los 250 caracteres. De ser así, se debe lanzar una excepción
LargoExcedidoException.
● Para esta etapa no se le solicita implementar las reglas de los atributos fecha_inicio
ni fecha_termino, pero sí debe definir sus setter con la lógica básica de asignación
de un nuevo valor al atributo correspondiente.
● Para esta etapa se le solicita solamente crear el método getter para el atributo
anuncios, sin crear su setter.
● El método sobrecargado __str__ dentro de la clase Campaña debe retornar una
cadena de texto que informe el nombre de la campaña de la instancia actual, y la
cantidad de anuncios por cada tipo. Ejemplo de retorno en una instancia específica:

Nombre de la campaña: Campaña 1
Anuncios: 1 Video, 2 Display, 0 Social

Se le solicita además crear un pequeño script demo.py que permita modificar los valores de
los atributos de una campaña ya creada. Para ello, cree directamente en este archivo una
instancia de Campaña (debe tener solo 1 anuncio de tipo Video), y luego solicite mediante
input un nuevo nombre de la campaña y un nuevo sub_tipo para el anuncio. Envuelva ambas
asignaciones en un bloque try/except, y en caso de que se produzca una excepción, añada
su mensaje en un archivo error.log.
