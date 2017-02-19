import pilasengine

pilas =  pilasengine.iniciar()
mono = pilas.actores.Mono()
mono.decir("Hola Mundo cruel")


pilas.ejecutar()
