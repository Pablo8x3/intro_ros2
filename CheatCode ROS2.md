# CheatCode ROS2

Para ver este archivo con formato en VS Code, pulsad `Ctrl+Mayús+V`.

Oolap, os dejo por aquí comandos y buenas prácticas para tenerlos a mano mientras trabajáis. No hace falta memorizarlos todos, con la repetición se os van a quedar jsjsj.

**Supongo: ROS 2 Jazzy, Ubuntu y Bash.** Se presupone que Jazzy está instalado mediante paquetes (tutorial de ros2.docs); si usáis otra instalación o intérprete, algunas rutas y scripts cambiarán. Esta guía no sustituye los pasos de instalación.

Todos los comandos se escriben en la terminal. Podéis usar la de Ubuntu o instalar Terminator, que permite dividir la ventana en paneles. Cada panel es una sesión con su propia carpeta y entorno.

Cada entrada incluye su utilidad, los argumentos y opciones más habituales y un ejemplo. Los ejemplos son independientes salvo que se indique lo contrario; no ejecutéis el documento entero como un script.

## Navegar y trabajar con archivos

### cd: cambiar de carpeta

`cd` viene de **C**hange **D**irectory. Cada terminal tiene su propia carpeta de trabajo.

**Argumentos y opciones**

- `ruta`: carpeta de destino.
- `..`: carpeta superior; `~` o sin argumento: tu carpeta personal.
- `-`: volver a la carpeta en la que estabas antes.

**Ejemplo**

```bash
cd ~/ros2_ws/src
cd ..
cd ~
cd -
```

`cd ~/` también lleva a tu carpeta personal. Cambiar de carpeta en una terminal no cambia la de las demás.

### ls: listar archivos y carpetas

`ls` viene de **list**. Muestra el contenido de la carpeta actual o de la ruta indicada.

**Argumentos y opciones**

- `-l`: formato detallado, con permisos y tamaños.
- `-a`: incluir archivos ocultos, cuyos nombres empiezan por punto.
- `-h`: tamaños legibles al combinarlo con `-l`.

**Ejemplo**

```bash
ls
ls -lah ~/ros2_ws
```

Las opciones cortas se pueden agrupar: `-lah` equivale a `-l -a -h`. `la` puede existir como alias (un atajo configurado), pero no está disponible en todos los equipos: usa `ls -a` como referencia.

### mkdir: crear un directorio (carpeta)

`mkdir` viene de **M**a**K**e **DIR**ectory.

**Argumentos y opciones**

- `nombre_o_ruta`: carpeta que quieres crear.
- `-p`: crear también los directorios intermedios que falten y aceptar que el directorio de destino ya exista.

**Ejemplo**

```bash
mkdir -p ~/ros2_ws/src
```

Sin `-p`, intentar crear una carpeta que ya existe da un error. `-p` no soluciona errores de permisos ni permite que un archivo ocupe el lugar de una carpeta.

### touch: crear un archivo vacío

Si el archivo no existe, lo crea vacío; si existe, actualiza sus fechas de acceso y modificación sin vaciarlo.

**Argumentos y opciones**

- `archivo`: nombre o ruta del archivo; puedes indicar varios.

**Ejemplo**

```bash
touch notas.txt
touch seguidor.py
touch codigo.cpp
```

### cp: copiar archivos o carpetas

`cp` viene de **copy**. Conserva el original y crea una copia en el destino.

**Argumentos y opciones**

- `origen destino`: qué copiar y dónde.
- `-r`: copiar una carpeta y su contenido.
- `-i`: preguntar antes de sobrescribir un archivo existente.

**Ejemplo**

```bash
cp -i notas.txt notas_copia.txt
cp -ri mi_paquete/ mi_paquete_copia/
```

Sustituye los nombres por archivos o carpetas que existan. Copiar una carpeta dentro de otra ya existente puede añadir un nivel de carpeta al destino.

### mv: mover o renombrar

`mv` viene de **move**. Si cambias el nombre dentro de la misma carpeta, estás renombrando.

**Argumentos y opciones**

- `origen destino`: archivo o carpeta que mover y su destino.
- `-i`: preguntar antes de sobrescribir.

**Ejemplo**

```bash
mv -i notas.txt apuntes.txt
mv -i apuntes.txt ~/ros2_ws/
```

El original deja de estar en la ruta anterior.

### rm: borrar archivos o carpetas

`rm` viene de **remove**. Lo que borra no pasa por la papelera.

**Argumentos y opciones**

- `ruta`: archivo o carpeta que borrar.
- `-i`: pedir confirmación por cada archivo.
- `-r`: borrar una carpeta y su contenido de forma recursiva.

**Ejemplo**

```bash
rm -i notas_copia.txt
rm -ri mi_paquete_copia/
```

Comprueba la ruta antes de confirmar. Empieza con nombres concretos y evita comodines cuando estés aprendiendo.

### find: buscar archivos y carpetas

Recorre una ruta y busca elementos que cumplan las condiciones indicadas.

**Argumentos y opciones**

- Primer argumento: carpeta desde la que buscar; `.` significa la actual.
- `-name`: buscar por nombre; `-iname` ignora mayúsculas y minúsculas.
- `-type f`: solo archivos; `-type d`: solo carpetas.

**Ejemplo**

```bash
find ~/ros2_ws/src -type f -name '*.py'
find . -type d -iname '*sensor*'
```

Las comillas evitan que Bash interprete `*` antes de que lo reciba `find`.

## Leer, editar y buscar texto

### cat: mostrar un archivo corto

`cat` viene de **concatenate**: también puede juntar el contenido de varios archivos en la salida.

**Argumentos y opciones**

- `archivo`: archivo de texto que leer.
- `-n`: mostrar los números de línea.

**Ejemplo**

```bash
cat -n notas.txt
```

Úsalo con texto; un archivo binario o muy largo puede llenar la terminal de contenido poco útil.

### nano: editar un archivo de texto

Abre un editor dentro de la terminal. Si el archivo no existe, se creará al guardarlo.

**Argumentos y opciones**

- `archivo`: nombre o ruta del archivo que editar.

**Ejemplo**

```bash
nano notas.txt
```

Guardar: `Ctrl+O` y después `Enter`. Salir: `Ctrl+X`. En la ayuda inferior, `^` significa `Ctrl`. La carpeta que contiene el archivo debe existir.

### grep: buscar texto

Su nombre viene de una orden histórica de ed, `g/re/p`: buscar una expresión regular y mostrar las líneas que coinciden.

**Argumentos y opciones**

- `patrón ruta`: texto o expresión que buscar y dónde.
- `-n`: mostrar números de línea; `-i`: ignorar mayúsculas.
- `-r`: buscar dentro de carpetas; `-F`: tratar el patrón como texto literal.

**Ejemplo**

```bash
grep -nF 'error' notas.txt
grep -rni 'sensor' ~/ros2_ws/src
```

Sin `-F`, algunos caracteres del patrón tienen significado especial. No encontrar coincidencias no significa que el comando esté roto.

### echo: mostrar texto o una variable

Es útil para escribir un mensaje o comprobar un valor del entorno.

**Argumentos y opciones**

- `texto`: contenido que mostrar.
- `$NOMBRE`: valor de una variable; las comillas dobles permiten expandirlo.

**Ejemplo**

```bash
echo 'Hola, ROS 2'
echo "$ROS_DISTRO"
echo "$HOME"
```

`HOME` guarda tu carpeta personal. `ROS_DISTRO` debería mostrar `jazzy` tras cargar su entorno; si está vacía, no se ha definido en esa terminal.

### man: consultar el manual

`man` viene de **manual**. Abre la documentación de un comando.

**Argumentos y opciones**

- `comando`: nombre del comando sobre el que necesitas ayuda.

**Ejemplo**

```bash
man mkdir
man chmod
```

Dentro del manual: `/palabra` busca, `n` avanza a la siguiente coincidencia y `q` sale. No todos los comandos tienen una página de manual; la guía completa incluye otras formas de consultar ayuda.

## Ubuntu y permisos

### sudo: ejecutar con permisos de otro usuario

Por defecto ejecuta la orden como administrador (`root`). Úsalo cuando la operación lo requiera, como instalar paquetes del sistema.

**Argumentos y opciones**

- `comando`: orden que necesita esos permisos.

**Ejemplo**

```bash
sudo apt update
```

Al escribir la contraseña puede que no veas ni letras ni asteriscos: es normal. Tus archivos del workspace deben poder gestionarse con tu usuario.

### apt update: actualizar el catálogo de paquetes

Consulta los repositorios configurados y actualiza la información local sobre versiones disponibles.

**Argumentos y opciones**

- `update`: operación de actualización del catálogo; no instala las nuevas versiones.

**Ejemplo**

```bash
sudo apt update
```

### apt upgrade: actualizar programas instalados

Instala las actualizaciones disponibles que pueda resolver esta operación.

**Argumentos y opciones**

- `upgrade`: operación de actualización de los paquetes instalados.

**Ejemplo**

```bash
sudo apt update
sudo apt upgrade
```

Lee el resumen de cambios antes de confirmar. `update` renueva el catálogo; `upgrade` actualiza programas.

### apt install: instalar programas

Instala paquetes y las dependencias que necesiten.

**Argumentos y opciones**

- `paquete`: nombre del paquete; puedes indicar varios.

**Ejemplo**

```bash
sudo apt install terminator
sudo apt install ros-jazzy-turtlesim ros-jazzy-rqt-graph
```

Terminator es una terminal opcional que permite dividir la ventana en paneles. Los paquetes `ros-jazzy-*` requieren tener configurado el repositorio de ROS 2 Jazzy. Los ejemplos con turtlesim y rqt_graph requieren esos paquetes.

### apt remove: desinstalar programas

Elimina el paquete indicado, aunque puede conservar archivos de configuración del sistema.

**Argumentos y opciones**

- `paquete`: nombre del paquete que quieres desinstalar.

**Ejemplo**

```bash
sudo apt remove terminator
```

Es un ejemplo independiente: ejecútalo solo si quieres quitar Terminator. Revisa también qué dependencias propone eliminar.

### apt search: buscar paquetes disponibles

Busca nombres y descripciones en el catálogo local de paquetes.

**Argumentos y opciones**

- `texto`: término que buscar.

**Ejemplo**

```bash
apt search ros-jazzy-turtlesim
```

Consultar no requiere `sudo`.

### apt show: consultar información de un paquete

Muestra su descripción, versión, dependencias y otros datos.

**Argumentos y opciones**

- `paquete`: nombre del paquete que consultar.

**Ejemplo**

```bash
apt show ros-jazzy-turtlesim
```

Que aparezca en el catálogo no significa que esté instalado.

### chmod: cambiar permisos

`chmod` viene de **change mode**. Los permisos básicos son `r` (leer), `w` (escribir) y `x` (ejecutar; en carpetas, acceder/atravesar).

**Argumentos y opciones**

- `u`: propietario; `g`: grupo; `o`: resto; `a`: todos.
- `+`: añadir un permiso; `-`: quitarlo.
- `u+x`: añadir ejecución al propietario.

**Ejemplo**

```bash
chmod u+x script.sh
```

El archivo debe existir. Esto no ejecuta el script ni registra un nodo para `ros2 run`. Cambia únicamente los permisos necesarios; evita `777` como solución genérica.

## Cargar el entorno de ROS 2 Jazzy

### source: cargar ROS 2 Jazzy

`source` lee un script y ejecuta sus instrucciones en el Bash actual, de modo que sus cambios de entorno permanecen en esa terminal.

**Argumentos y opciones**

- `/opt/ros/jazzy/setup.bash`: ruta del script de configuración de Jazzy instalado mediante paquetes en Ubuntu.

**Ejemplo**

```bash
source /opt/ros/jazzy/setup.bash
```

Puedes ejecutarlo desde cualquier carpeta porque la ruta es absoluta. Debe existir una instalación de Jazzy; hacer `source` no instala ROS 2.

### source: cargar el workspace

Añade al entorno los paquetes instalados al compilar tu workspace.

**Argumentos y opciones**

- `~/ros2_ws/install/setup.bash`: ruta del script generado por colcon para este workspace.

**Ejemplo**

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
```

Hazlo en la terminal de ejecución, después de compilar correctamente. Si estás en `~/ros2_ws`, el segundo comando también se escribe `source install/setup.bash`. Esa ruta relativa depende de la carpeta actual.

### Qué son los archivos `.bash` y por qué los cargamos

Bash es el intérprete que lee las órdenes de esta guía. La terminal es la ventana; Bash es el programa que interpreta lo que escribes en ella.

Un archivo `.bash` contiene instrucciones para Bash. La extensión ayuda a reconocerlo, pero no lo ejecuta por sí sola. Los `setup.bash` de ROS 2 preparan variables y rutas para que las herramientas encuentren paquetes, ejecutables y bibliotecas.

- `/opt/ros/jazzy/setup.bash`: entorno de la instalación base de Jazzy.
- `~/ros2_ws/install/setup.bash`: entorno del workspace y de los entornos base registrados al construirlo.
- `source` aplica las instrucciones en el Bash actual. Ejecutar `bash archivo.bash` crea otro Bash: los cambios de entorno de ese proceso no se conservan en la terminal que lo lanzó.

Por eso se referencia el archivo con su ruta: `source` necesita saber qué script leer. La carga afecta a esa terminal y a los programas que arranques desde ella; no configura las otras terminales ya abiertas.

### Dónde está `.bashrc` y para qué sirve

Está en tu carpeta personal: `~/.bashrc`, normalmente `/home/tu_usuario/.bashrc`. El punto inicial hace que sea un archivo oculto. No termina en `.bash`, pero también contiene instrucciones para Bash.

Bash lo lee al iniciar una sesión interactiva que no sea de login, como las terminales habituales de Ubuntu. Aquí puedes definir alias o cargar el entorno base de ROS 2 automáticamente.

**Ejemplo: abrirlo y editarlo**

```bash
nano ~/.bashrc
```

Añade esta línea al final, si no estaba ya:

```bash
source /opt/ros/jazzy/setup.bash
```

Guarda con `Ctrl+O`, pulsa `Enter` y sal con `Ctrl+X`. Abre otra terminal para aplicar la configuración. En una terminal existente puedes volver a leer el archivo:

```bash
source ~/.bashrc
```

Carga el workspace manualmente en las terminales de ejecución. Así evitas que todas las terminales, incluida la de compilación, arranquen con ese workspace cargado. Si ya tienes una línea que carga automáticamente `~/ros2_ws/install/setup.bash`, coméntala anteponiendo `#` si vas a seguir esta separación de terminales. Después abre una terminal nueva: comentar una línea no deshace lo que ya se había cargado.

No añadas cargas de otras distribuciones de ROS 2 a la misma configuración. Esta guía usa Jazzy.

## Construir y ejecutar ROS 2

### colcon build: compilar el workspace

Construye e instala los paquetes del workspace; en Python también prepara su instalación, aunque no haya compilación C++.

**Argumentos y opciones**

- `--symlink-install`: usar enlaces simbólicos donde se admita, para facilitar cambios en archivos que no necesitan compilarse.
- `--packages-select mi_paquete`: construir solo ese paquete; sus dependencias deben estar disponibles.
- `--packages-up-to mi_paquete`: construir ese paquete y las dependencias necesarias que estén en el workspace.

**Ejemplo**

```bash
# Terminal de compilación: Jazzy cargado, sin cargar este workspace
source /opt/ros/jazzy/setup.bash
cd ~/ros2_ws
colcon build --symlink-install
```

Se ejecuta desde la raíz del workspace, donde está `src`, sin `sudo`. Genera `build`, `install` y `log` al lado de `src`. `--symlink-install` no evita recompilar C++ ni todos los cambios de configuración.

### ros2 pkg create: crear un paquete

Crea la estructura inicial de un paquete dentro de `src`. `pkg` abrevia **package**.

**Argumentos y opciones**

- `nombre_paquete`: nombre nuevo, normalmente en minúsculas y con guiones bajos.
- `--build-type`: `ament_python` para Python o `ament_cmake` para C++.
- `--node-name`: generar un ejecutable inicial de ejemplo.
- `--dependencies`: dependencias del paquete; `--license`: licencia del proyecto.

**Ejemplo**

```bash
cd ~/ros2_ws/src
ros2 pkg create mi_paquete --build-type ament_python --node-name mi_nodo --license Apache-2.0 --dependencies rclpy
# Alternativa C++, con otro nombre:
ros2 pkg create mi_paquete_cpp --build-type ament_cmake --node-name mi_nodo_cpp --license Apache-2.0 --dependencies rclcpp
```

Carga Jazzy antes de usarlo. Son dos ejemplos independientes: no necesitas crear ambos. `Apache-2.0` es una licencia de ejemplo; usa la acordada para tu proyecto. Crear no equivale a compilar.

### ros2 run: ejecutar un programa de un paquete

Localiza un ejecutable instalado por un paquete y lo inicia.

**Argumentos y opciones**

- Primer argumento: nombre del paquete.
- Segundo argumento: nombre del ejecutable, que puede diferir del nombre del nodo.

**Ejemplo**

```bash
ros2 run mi_paquete mi_nodo
```

Este ejemplo usa el paquete Python de `ros2 pkg create`, después de compilarlo y cargar el workspace. Para probar la instalación de ROS 2 puedes usar `ros2 run turtlesim turtlesim_node`. Detén el proceso con `Ctrl+C`.

### ros2 launch: arrancar una configuración de nodos

Ejecuta un archivo launch, que puede iniciar varios nodos y configurar sus parámetros.

**Argumentos y opciones**

- Primer argumento: paquete que contiene el launch.
- Segundo argumento: nombre del archivo launch instalado.
- `nombre:=valor`: pasar un argumento declarado por ese launch.

**Ejemplo**

```bash
# Ejemplo disponible con turtlesim instalado
ros2 launch turtlesim multisim.launch.py
# Plantilla para vuestro proyecto, si dispone de ese launch y argumento:
# ros2 launch mi_paquete arranque.launch.py nombre_argumento:=valor
```

El ejemplo de turtlesim abre dos nodos en espacios de nombres distintos. `ros2 pkg create` no genera automáticamente un launch: para usar uno propio debes crearlo e instalarlo con el paquete. Los argumentos `nombre:=valor` deben estar declarados por el launch.

### ros2 topic list: listar tópicos

Muestra los canales de mensajes descubiertos por ROS 2 en el entorno actual.

**Argumentos y opciones**

- `-t`: mostrar también el tipo de mensaje de cada tópico.

**Ejemplo**

```bash
ros2 topic list
ros2 topic list -t
```

Para ver tópicos de ejemplo, mantén turtlesim ejecutándose en otra terminal con Jazzy cargado.

### ros2 topic echo: ver mensajes de un tópico

Se suscribe al tópico indicado y muestra los mensajes que recibe.

**Argumentos y opciones**

- `/nombre_topico`: nombre del tópico que quieres observar.
- `--once`: terminar después del primer mensaje recibido.

**Ejemplo**

```bash
ros2 topic echo /turtle1/pose
# Alternativa: recibir solo un mensaje
ros2 topic echo /turtle1/pose --once
```

Requiere turtlesim ejecutándose en otra terminal. Si no llega ningún mensaje, puede quedarse esperando; sal con `Ctrl+C`.

### rqt_graph: ver las conexiones entre nodos

Abre una herramienta gráfica que representa nodos, tópicos y sus conexiones.

**Argumentos y opciones**

- En `ros2 run rqt_graph rqt_graph`, el primer `rqt_graph` es el paquete y el segundo es el ejecutable.

**Ejemplo**

```bash
ros2 run rqt_graph rqt_graph
```

Requiere `ros-jazzy-rqt-graph` y un entorno gráfico. Arranca nodos para ver conexiones y usa el botón de refrescar si el dibujo no se actualiza.

## Atajos y conceptos de terminal

### Atajos que usaréis a diario

| Atajo | Para qué sirve |
| --- | --- |
| `Tab` | Completar nombres de archivos y comandos. En herramientas configuradas para ello, también opciones. |
| `Tab` dos veces | Mostrar posibles coincidencias cuando no hay una única opción. |
| `↑` / `↓` | Recorrer órdenes anteriores. |
| `Ctrl+R` | Buscar una orden en el historial; escribe una parte de ella. `Ctrl+R` sigue buscando, `Enter` ejecuta y `Ctrl+G` cancela. |
| `Ctrl+C` | Solicitar la interrupción del proceso en primer plano o cancelar la línea actual. |
| `Ctrl+L` | Limpiar la vista; no detiene procesos ni borra el historial. |
| `Ctrl+Shift+C` | Copiar el texto seleccionado en terminales como Terminator. |
| `Ctrl+Shift+V` | Pegar en esas terminales. Revisa el texto antes de ejecutarlo. |

Los atajos pueden variar según la aplicación de terminal. `Ctrl+C` dentro de la terminal suele interrumpir, no copiar.

### Rutas: `.`, `..`, `~`, `/` y `./`

| Notación | Significado | Ejemplo |
| --- | --- | --- |
| `.` | Carpeta actual. | `find . -name '*.py'` |
| `..` | Carpeta superior. | `cd ..` |
| `~` | Tu carpeta personal. | `cd ~/ros2_ws` |
| `/` al principio | Ruta absoluta, desde la raíz del sistema. | `cd /opt/ros/jazzy` |
| `./` | Ruta relativa que empieza explícitamente en la carpeta actual. | `./script.sh` |

Una ruta relativa, como `src/mi_paquete`, depende de dónde estés. Una absoluta, como `/opt/ros/jazzy/setup.bash`, no. `/src` significa una carpeta en la raíz del sistema; `~/ros2_ws/src` es el código de tu workspace.

### Nombres, espacios y comillas

Linux distingue mayúsculas y minúsculas: `Sensor.py` y `sensor.py` son nombres diferentes. Para proyectos y paquetes, usa nombres descriptivos y consistentes; los guiones bajos suelen simplificar el trabajo.

```bash
mkdir -p ~/ros2_ws
cd ~/ros2_ws
mkdir -p "mis apuntes"
cd "mis apuntes"
echo "$HOME"
echo '$HOME'
```

Las comillas agrupan nombres con espacios. Las dobles permiten sustituir variables: `"$HOME"` muestra su valor. Las simples conservan el texto literal: `'$HOME'` muestra `$HOME`. Deja `~` fuera de las comillas: `~/"mis apuntes"`, o usa `"$HOME/mis apuntes"`.

### Sintaxis de los ejemplos

- Una orden suele seguir la forma `comando opciones argumentos`.
- En `mkdir -p nombre_del_directorio`, `-p` es una opción y `nombre_del_directorio` es un argumento.
- Sustituye nombres como `mi_paquete`, `script.sh` o `notas.txt` por los tuyos. Algunos ejemplos requieren archivos ya existentes y son independientes entre sí.
- No escribas un `$` inicial como los que aparecen en algunos tutoriales: suele representar el prompt.
- Lo que empieza por `#` fuera de comillas es un comentario. En los ejemplos explica la orden y no se ejecuta.

### `|`, `>`, `>>` y `&&`: combinar órdenes

| Símbolo | Qué hace | Ejemplo |
| --- | --- | --- |
| `|` | Pasar la salida estándar de una orden a la entrada de otra. | `ls ~/ros2_ws/src | grep sensor` |
| `>` | Guardar la salida estándar en un archivo, sustituyendo su contenido anterior. | `echo 'Primera nota' > notas.txt` |
| `>>` | Añadir la salida al final de un archivo. | `echo 'Otra nota' >> notas.txt` |
| `&&` | Ejecutar la siguiente orden solo si la anterior termina correctamente. | `mkdir -p ~/ros2_ws/src && cd ~/ros2_ws` |

`>` vacía el archivo de destino antes de que se ejecute la orden: comprueba el nombre. Estas redirecciones no incluyen automáticamente los mensajes enviados a la salida de errores.

### Ejecutar scripts: `./script.sh` y `bash script.sh`

Un script agrupa órdenes en un archivo. Por ejemplo, guarda esto como `script.sh` con Nano:

```bash
#!/usr/bin/env bash
echo "Hola desde un script"
```

La primera línea, llamada *shebang*, indica qué intérprete usar al ejecutarlo directamente.

```bash
chmod u+x script.sh
./script.sh
# Alternativa: pasar el archivo como argumento a Bash
bash script.sh
```

`./script.sh` necesita permiso de ejecución y una primera línea adecuada. `bash script.sh` necesita que puedas leerlo y fuerza Bash como intérprete. Ambos ejemplos ejecutan el script en otro proceso; para configurar el entorno del Bash actual usamos `source`.

### Estructura de un workspace

```text
ros2_ws/
├── src/       # Código de tus paquetes
├── build/     # Archivos intermedios de construcción
├── install/   # Paquetes instalados y scripts de entorno
└── log/       # Registros de colcon
```

Al empezar, puedes tener únicamente `src`. Colcon genera las otras tres carpetas al construir. Edita tus fuentes y configuraciones dentro de `src`; mantén los archivos generados fuera del control de versiones.

### `.gitignore`: excluir archivos generados de Git

Es un archivo de texto, llamado exactamente `.gitignore`, situado dentro de un repositorio Git. Si el repositorio está en la raíz del workspace, puedes editar `~/ros2_ws/.gitignore` y añadir:

```gitignore
/build/
/install/
/log/
```

Las barras iniciales hacen que estas reglas se apliquen en la raíz del repositorio. Si cada paquete de `src` es un repositorio distinto, ubica y adapta las reglas a la estructura real.

Esto evita que Git añada archivos nuevos que coincidan; no deja de seguir archivos que ya estuviesen versionados. Las órdenes para trabajar con Git están en la guía completa.

## Errores típicos

### Hacer `colcon build` dentro de `src`

Genera `build`, `install` y `log` dentro de `~/ros2_ws/src`, mezclando código con resultados de construcción. Vuelve a `~/ros2_ws` antes de compilar. Si ya ocurrió, revisa esas carpetas y elimina únicamente las generadas por esa compilación; no borres tu código.

### Olvidar cargar ROS 2 o el workspace

Si aparece `ros2: command not found`, comprueba que Jazzy está instalado y carga `/opt/ros/jazzy/setup.bash` en esa terminal. Si ROS 2 funciona pero no encuentra tu paquete, comprueba que se construyó correctamente y carga `~/ros2_ws/install/setup.bash` en la terminal de ejecución.

### Mezclar terminales de compilación y ejecución

Usa una terminal de compilación con Jazzy cargado y sin cargar el workspace que estás construyendo. Usa otra para cargar ese workspace y ejecutar sus programas. Si ya lo cargaste en la de compilación, abre una nueva y revisa que `.bashrc` no lo esté cargando automáticamente. Cambiar de carpeta no limpia el entorno.

### Usar `sudo` para compilar

`sudo colcon build` puede dejar archivos propiedad de `root` y cambiar el entorno usado durante la construcción. Compila con tu usuario. Si aparecen errores de permisos, revisa primero su causa en lugar de repetir la orden con `sudo`.

### Usar `chmod 777` para cualquier problema

Da lectura, escritura y ejecución a todos. Un problema puede deberse a la propiedad del archivo, a su ruta o a permisos de una carpeta. Revisa los permisos con `ls -l` y cambia solo los necesarios; para permitirte ejecutar tu script suele bastar `chmod u+x script.sh`.

### Confundir paquete, ejecutable, nodo y tópico

Un paquete agrupa código; un ejecutable es el programa que arrancas; un nodo es un participante de ROS 2 creado por ese programa; un tópico es un canal de mensajes. En `ros2 run turtlesim turtlesim_node`, `turtlesim` es el paquete y `turtlesim_node` es el ejecutable. Sus nombres no tienen por qué coincidir con el del nodo o el de un tópico.

### Editar archivos dentro de `build` o `install`

Tus cambios pueden perderse en la siguiente construcción. Edita el original en `src` y vuelve a construir cuando corresponda, aunque hayas encontrado una copia dentro de `install`.

### Subir `build`, `install` o `log` a Git

Son resultados generados, pueden ocupar mucho y contener rutas específicas de tu equipo. Guarda el código y la configuración necesarios para reconstruir el proyecto; usa `.gitignore` para excluir esos directorios. Si ya se subieron, añadir reglas no los retira automáticamente del seguimiento.

## Referencias

Las rutas y los ejemplos de ROS 2 de este documento corresponden a Jazzy. Para comprobar variantes y requisitos, consultad:

- [Entorno de ROS 2 Jazzy](https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Configuring-ROS2-Environment.html).
- [Workspace y separación de terminales](https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html).
- [Crear paquetes](https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html).
- [Tópicos y rqt_graph](https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html).
- [Lanzar varios nodos](https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Launching-Multiple-Nodes/Launching-Multiple-Nodes.html).
- [Opciones de construcción de colcon](https://colcon.readthedocs.io/en/released/reference/verb/build.html) y [selección de paquetes](https://colcon.readthedocs.io/en/released/reference/package-selection-arguments.html).
- [Terminal de Linux: guía de Ubuntu](https://ubuntu.com/tutorials/command-line-for-beginners).
