# API Specs



Datos que recibe:
    - poblacion (número de arreglos de 1's y 0's
    - numKdeElitismo (número de arreglos de 1's y 0's cuyo valor de la función sea mayor que pasan)
    - cantidadGeneraciones (número de veces que el proceso se va a llevar a cabo)
    - umbral1 (Primer umbral de 1's y 0's paara generar los primeros arreglos de 1's y 0's) 
    - umbralX (Umbral para determinar si hay crucamiento o no)
    - umbralM (número que en caso de ser excedido por números aleatorios hara que mute o no cada uno de los elementos de un arreglo de 1's y 0's determinado) 
´´´
GET /poblacion/numKdeElitismo/cantidadGeneraciones/umbralL/umbralX/umbralM
´´´

- Regresar el más alto valor de  f(x,y) de la última generación con sus x y y respectivos
- Regresar los f(x,y) de toda la población de la última generación y de la primera
