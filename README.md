# Harry Potter y la programación orientada a objetos

## Instalación

Necesitan pytest para correr los tests. Pueden instalarlo con requirements.txt

```bash
pip install -r requirements.txt
```

## Introducción

En el mundo de Harry Potter, el hechizo *Avada Kedavra*, mata al oponente. Sin embargo, mediante el uso de *Horrocruxes*, el hechizero divide parte de su alma y puede revivir mientras tenga alguno. Es decir, un hechizero puede revivir solo si tiene algún *Horrocrux* disponible.

## Consigna

Crear la clase `Mago` (en el archivo `harry.py`) que:

- Se inicialice con el nombre
- Tenga un método `crear_horrocruxes(numero)` que cree el número pasado por parámetro de *horrocruxes*. Para pensar: ¿Los *horrocruxes* deben ser guardados fuera o dentro de la clase mago?
- Tenga el método `morir()`. Si no tiene *horrocruxes*, morirá. Si tiene *horrocruxes*, restará un *horrocrux* de su total.
- Tenga el método `vivo()` que devuelva si está vivo o no.
- Tenga el método `avada_kedavra(mago enemigo)`, que mate al mago enemigo (usar el método morir del mago enemigo).

Luego, crear una serie de tests de unidad para la clase `Mago` en el archivo `harry_tests.py`. Algunas cosas a tener en cuenta:
- Testear el estado inicial del mago
- Tratar en lo posible de testear los métodos de forma independiente, pero algunos no se puede ( `avada_kedavra` con `vivo`)
- **NO** testeen `morir`. No porque no se deba hacer, si no porque lo vamos a considerar "privado", es decir, que no va a ser llamado por las instancias de forma directa si no por otros métodos.
- Concentrarse en situaciones, como por ejemplo `avada_kedavra` sin *horrocruxes*, `avada_kedavra` con *horrocruxes*, `avada_kedavra` suficientes veces como para acabar con los *horrocruxes*, etc.

Pueden trabajar la clase y los tests de forma independiente.

## Datos de color

J.K Rowling creó otras escuelas de magia además de Hogwarts. Sin embargo, se olvidó de algunas escuelas yanquis, como esta: https://www.youtube.com/watch?v=j-2ZxldMO-M.