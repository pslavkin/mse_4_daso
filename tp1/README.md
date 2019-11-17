#TP1 Desarrollo de Aplicaciones sobre sistemas operativos de propósito genera
----------------------------------------------------------------------------

Se implemento un programa en Python que lanza 3 tareas para enviar datos por UDP a 3 servicios 
uno en cada puerto, 10000, 10001 y 10002
Se logro implementar entre otras cosas:

### Threads
### Join
### Event
### try/except handlers para cerrar
### json 
### sockets udp
### modulos

Link al sistema corriendo:

<a href="https://asciinema.org/a/pZG9SiwhFqHqagaPAgCbMHA8f?speed=2" target="_blank"><img src="https://asciinema.org/a/pZG9SiwhFqHqagaPAgCbMHA8f.svg" /></a>

lanzar 3 instancias de PizarrService.py una en una terminal diferente para ver los resuptados
simultaneamente de la siguiente manera:

python3 PizarraService.py 10000
python3 PizarraService.py 10001
python3 PizarraService.py 10002

y en una cuarta consola lanzar parserservice.py

y para para oprimir C-c. Se mostraran mensajes de debug segun el nivel elegido



