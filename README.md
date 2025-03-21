# bisslog-core

Es una librería auxiliar para la capa de negocio o dominio del servicio, que permite tener un 
lenguaje común para operaciones a la hora de interactuar con componentes externos que
hacen parte de la infraestructura de la misma. Es decir, las reglas de negocio no van a cambiar 
si el arquitecto decidió cambiar el sistema de mensajería, a este no le importa. 
El punto esencial de esta librería es que el dominio no debe cambiar porque algún adaptador cambió.

Es el nucleo de la capa de negocio de los programas en python para estructurar proyectos en base al dominio




## Tests

To Run test with coverage
~~~commandline
coverage run --source=bisslog_core -m pytest tests/
~~~


To generate report
~~~commandline
coverage html && open htmlcov/index.html
~~~