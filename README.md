# Proyecto de Programacion I UCAB
# Primera entrega CMD
    Creacion de un juego que se ejecuta en la terminal, donde el objetivo principal es hacer
    que un robot llegue a su destino,evitando colisionar con minas que se encuntran
    en el mapa, y contra las paredes del mismo

    Se implementa un algoritmo que crea los mapas de forma aleatoria y otro que los verfica
    para que se creen de manera adecuada

    Se estrutura el codigo de manera modular y POO

* Utilizacion de matrices
    - Se crean segun los datos propocionados por el usuario
* Utilizacion de colores para mejor estética
* Detección de colisiones con la minas y las paredes
* Implementacion de guardado en un archivo Txt
    - Se actualiza en tiempo real 
* Se implemento una función que limpia la terminal


### Imports
* Random
* os
* getch


# Segunda entrega UX-UI
    Se implementa interfaz al juego de terminal, usando la libreria de pygame, donde se reutiliza 
    el mismo codigo de la version de cmd, se toma la creacion del mapa, las colisiones y los mivimientos

### Import
*Pygame