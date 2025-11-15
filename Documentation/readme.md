Manual de Usuario
Cuentos de mentes estrelladas

---

 Bienvenido

**Cuentos de mentes estrelladas** es una aventura narrativa que te sumerge en historias de suspenso, terror psicológico y fantasía oscura. Cada nivel presenta microcuentos únicos con una estética melancólica inspirada en Edgar Allan Poe, Tim Burton y obras como Limbo y Habromania.

Prepárate para adentrarte en mundos llenos de oscuridad, donde cada decisión cuenta y cada sombra esconde un secreto.

---

 Requisitos del Sistema

 Requisitos Mínimos
- **Sistema Operativo:** Windows 7/8/10/11, macOS 10.12+, o Linux
- **Procesador:** Intel Core i3 o equivalente
- **Memoria RAM:** 4 GB
- **Espacio en Disco:** 500 MB libres
- **Python:** Versión 3.7 o superior
- **Tarjeta Gráfica:** Compatible con OpenGL 2.0

---

Instalación

 Paso 1: Instalar Python
1. Descarga Python desde [python.org](https://www.python.org/downloads/)
2. Durante la instalación, **marca la casilla "Add Python to PATH"**
3. Completa la instalación siguiendo el asistente

Paso 2: Instalar Dependencias
Abre una terminal o símbolo del sistema y ejecuta:

```bash
pip install pygame
```

También se requiere `pyautogui` para la detección automática de resolución:

```bash
pip install pyautogui
```

### Paso 3: Verificar Instalación
Para verificar que todo está correctamente instalado:

```bash
python --version
pip list
```

Paso 4: Ejecutar el Juego
1. Descarga o extrae todos los archivos del juego en una carpeta
2. Abre una terminal en la carpeta del juego
3. Ejecuta:

```bash
python main.py
```

---

🎮 Controles del Juego

En el Menú Principal
- **↑ / ↓** o **W / S:** Navegar por las opciones
- **ENTER** o **SPACE:** Seleccionar opción
- **ESC:** Salir del juego

Durante el Juego
| Acción | Teclas |
|--------|--------|
| **Mover a la izquierda** | A o ← |
| **Mover a la derecha** | D o → |
| **Saltar** | SPACE |
| **Correr** | Mantener SHIFT + dirección |
| **Atacar** | X o J |
| **Interactuar con personajes** | E |
| **Pausar** | ESC |

Durante los Diálogos
- **ENTER** o **SPACE:** Avanzar el diálogo
- **ESC:** Cerrar diálogo rápidamente (si es posible)

> **Nota:** Los controles de movimiento se desactivan automáticamente durante los diálogos para evitar interrupciones. Usa la tecla **E** para iniciar conversaciones con personajes.

---

Historia: El Caza Sombras

La Leyenda

En lo profundo del bosque habita una criatura tenebrosa conocida como **El Caza Sombras**. Este ente devora por completo a los cazadores que se atreven a entrar en su territorio, sin dejar rastro alguno... ni siquiera una sombra.

Las autoridades del pueblo han ofrecido una jugosa recompensa a quien logre traer la cabeza del Caza Sombras. ¿Serás tú quien libere al bosque de esta maldición?

Tu Personaje: Jaime

Eres **Jaime**, el único leñador que queda en el pueblo. Hace meses que no puedes conseguir madera de los mejores árboles. Furioso y desesperado por alimentar a tu familia, decides enfrentar al Caza Sombras y reclamar el bosque... o morir en el intento.

El Enemigo: El Caza Sombras

Antes de convertirse en esta criatura, el Caza Sombras era un cazador del bosque que convirtió su labor en un hobby macabro, matando animales por pura diversión. Su caza irresponsable lo llevó a un castigo terrible: ahora posee una apariencia de esqueleto animal, siempre cubierto por ramas y hojas a modo de túnica, condenado eternamente a devorar a su siguiente reemplazo.

Personajes de Apoyo

**El Cantinero:** En la cantina del pueblo, este sabio personaje te ofrecerá consejos valiosos y misiones preparatorias para que tengas mejores posibilidades contra el Caza Sombras.

---

Mecánicas del Juego

Exploración
- Recorre diversos escenarios llenos de melancolía y oscuridad
- Descubre secretos ocultos en cada rincón
- La exploración es guiada por diálogos con NPCs
- Usa el sistema de plataformas para alcanzar zonas elevadas

Sistema de Combate
- **Ataque básico:** Presiona X o J para atacar enemigos
- **Esquiva:** Usa el movimiento y saltos para evitar ataques
- **Estrategia:** Cada enemigo tiene patrones de ataque únicos
- **Barra de vida:** Cuida tu salud, visible en la parte superior de la pantalla

Sistema de Diálogos
- Los diálogos aparecen al interaccionar con personajes (tecla E)
- Efecto de escritura progresiva para mayor inmersión
- Los diálogos contienen pistas importantes para tu aventura
- Durante un diálogo, el juego pausa otras acciones

Interacciones con Objetos
- Acércate a objetos brillantes o destacados
- Presiona **E** para interactuar
- Algunos objetos revelan fragmentos de la historia
- Otros pueden ayudarte en tu misión

Sistema de Física
- **Gravedad realista:** Tu personaje cae naturalmente
- **Colisiones:** Interactúa con plataformas y obstáculos
- **Salto:** Presiona SPACE para saltar
- **Carrera:** Mantén SHIFT mientras te mueves para correr y ganar velocidad
- **Impulso:** Corre antes de saltar para alcanzar plataformas lejanas

Prompts de Salto
- Indicadores visuales te mostrarán dónde puedes saltar
- Aparecen en zonas clave para avanzar en el nivel
- Sigue estas guías para no quedarte atascado

---

 Progresión del Juego

Estructura de Niveles
El juego está diseñado para presentar **cinco historias únicas** (actualmente en desarrollo). Cada historia es un microcuento independiente con sus propios personajes, enemigos y desafíos.

Objetivos Principales
1. **Resolver la historia:** Avanza en la narrativa completando objetivos
2. **Combatir enemigos:** Derrota criaturas oscuras que bloquean tu camino
3. **Recolectar microcuentos:** Descubre fragmentos de historias ocultas
4. **Completar mini-misiones:** Recibe encargos del Cantinero y otros NPCs

Sistema de Colección (Próximamente)
- **Skins desbloqueables:** Consigue nuevas apariencias para Jaime
- **Álbum de figuras:** Completa colecciones de enemigos y personajes
- **Microcuentos:** Recopila todas las historias del juego

---

Características del Juego

Estilo Visual
- **Estética 2D con falso 3D:** Uso de técnicas parallax para crear profundidad
- **Paleta oscura y melancólica:** Colores tenues que evocan terror psicológico
- **Animaciones frame by frame:** Movimientos fluidos y detallados
- **Iluminación cinematográfica:** Atmósfera tenebrosa y envolvente

Ambientación
- Bosques densos y misteriosos
- Casas abandonadas y tétricas
- Ambiente de novela negra
- Inspiración en obras de Edgar Allan Poe y Tim Burton

Temas Narrativos
El juego explora temas profundos:
- **Las consecuencias** de nuestros actos
- **La redención** ante errores del pasado
- **El dolor** como motor de transformación

---

Consejos y Estrategias

Para Principiantes
1. **Habla con todos:** El Cantinero y otros NPCs te darán información valiosa
2. **Explora cada rincón:** Los secretos están en los lugares menos obvios
3. **Practica el combate:** Aprende los patrones de ataque de los enemigos
4. **Lee con atención:** Los diálogos contienen pistas cruciales

Técnicas Avanzadas
1. **Domina el timing de salto:** Mantén presionado para alcanzar plataformas altas
2. **Usa el entorno:** Algunas áreas ofrecen ventaja táctica contra enemigos
3. **Administra tu salud:** No seas imprudente, retrocede si es necesario
4. **Experimenta:** Intenta interactuar con todo lo que veas

Contra el Caza Sombras
1. **Prepárate bien:** Completa todas las misiones del Cantinero primero
2. **Estudia sus movimientos:** Observa sus patrones de ataque
3. **Mantén la distancia:** Es una criatura poderosa en combate cercano
4. **Usa el escenario:** El bosque puede ser tu aliado si lo conoces bien

---

 Características Implementadas

✅ Sistema de movimiento y física del jugador  
✅ Sistema de plataformas y colisiones  
✅ Sistema de enemigos con IA básica  
✅ Sistema de diálogos interactivos con efecto de escritura  
✅ Menú principal con animaciones  
✅ Sistema de niveles y carga de mapas  
✅ Sistema de cámara que sigue al jugador  
✅ Barra de vida visible  
✅ Efecto parallax para profundidad visual  
✅ Prompts de salto en zonas específicas  

---

Próximas Características

Estas funciones estarán disponibles en futuras actualizaciones:

🔲 Sistema de animaciones completo con sprites  
🔲 Sistema de guardado y carga de partidas  
🔲 Inventario y objetos coleccionables  
🔲 Skins desbloqueables para Jaime  
🔲 Efectos de sonido y música ambiental  
🔲 Historias adicionales (hasta 5 niveles completos)  
🔲 Sistema de misiones del Cantinero  
🔲 Ataques especiales del Caza Sombras  
🔲 Partículas y efectos visuales mejorados  
🔲 Modo historia completo con cinemáticas  

---

Información Técnica

Motor y Herramientas
- **Motor del juego:** Pygame (Python)
- **Diseño de personajes:** Krita, Blender
- **Arte y animación:** 2D, frame by frame
- **Técnica visual:** Falso 3D con parallax


 Inspiraciones Artísticas

Este juego rinde homenaje a grandes obras y artistas:

- **Habromania:** Mecánicas de juego y diseño de niveles
- **Limbo:** Estética visual y atmósfera opresiva
- **Tim Burton:** Diseño de personajes y ambientación gótica
- **Edgar Allan Poe:** Narrativa, tono y temáticas oscuras

---


---

 ¡Disfruta la Aventura!

El bosque aguarda. Las sombras susurran. Tu destino te espera.

**¿Estás listo para enfrentar al Caza Sombras y liberar al pueblo de su maldición?**

Buena suerte, valiente leñador. Que tu hacha sea filosa y tu corazón valiente.

---

*"En cada sombra habita una historia. En cada historia, una verdad oscura."*