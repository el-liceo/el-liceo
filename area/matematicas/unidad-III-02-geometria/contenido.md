# Contenido · Unidad 03 · Geometría Analítica

---

## Sesión 1 · ¿Dónde estás?

### Motivación

Imagina que le describes a alguien por teléfono dónde estás en una ciudad que no conoce. Puedes decir "estoy cerca del parque" — impreciso. O puedes decir "calle 3, número 47" — exacto. Las coordenadas son eso: un sistema de direcciones para cualquier punto del plano.

### Concepto central

El **plano cartesiano** es una cuadrícula formada por dos rectas perpendiculares:
- El **eje X** (horizontal), llamado eje de abscisas
- El **eje Y** (vertical), llamado eje de ordenadas
- Su intersección es el **origen**, el punto (0, 0)

Todo punto del plano queda definido por un par ordenado **(x, y)**:
- `x` indica cuánto nos desplazamos horizontalmente desde el origen
- `y` indica cuánto nos desplazamos verticalmente

> **Importante:** el orden importa. (3, 5) y (5, 3) son puntos distintos.

### Los cuatro cuadrantes

```
         Y
         |
   II    |    I
(-,+)    |  (+,+)
         |
---------+--------  X
         |
  III    |   IV
 (-,-)   |  (+,-)
         |
```

### Actividad de aula

**"El mapa del aula"**

1. Definir el origen como la esquina de la pizarra
2. Cada alumno mide su posición en metros y la anota como (x, y)
3. En grupo, se construye un mapa del aula en papel cuadriculado
4. Preguntas: ¿quién está más lejos de la pizarra? ¿cómo lo sabes?

*Esta actividad prepara intuitivamente el concepto de distancia.*

---

## Sesión 2 · La distancia como medida de separación

### Motivación

Ya sabemos situar puntos. Ahora: ¿cómo medimos la distancia entre ellos sin una regla?

### Derivación de la fórmula

Dados dos puntos **A = (x₁, y₁)** y **B = (x₂, y₂)**, podemos construir un triángulo rectángulo:

```
B = (x₂, y₂)
|  ↖
|    \   ← esta es la distancia que buscamos
|     \
C------A
(x₂,y₁)  (x₁,y₁)
```

- El cateto horizontal mide: |x₂ − x₁|
- El cateto vertical mide: |y₂ − y₁|

Aplicando el teorema de Pitágoras:

$$d(A,B) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

> **Por qué elevamos al cuadrado:** para eliminar el problema del valor absoluto. Un número al cuadrado siempre es positivo, así que no importa si la diferencia es positiva o negativa.

### Ejemplos resueltos

**Ejemplo 1.** A = (1, 2), B = (4, 6)

```
d = √((4−1)² + (6−2)²)
  = √(3² + 4²)
  = √(9 + 16)
  = √25
  = 5
```

*Nota: este es el famoso triángulo 3-4-5, un caso especial que vale la pena reconocer.*

**Ejemplo 2.** A = (−2, 3), B = (1, −1)

```
d = √((1−(−2))² + (−1−3)²)
  = √(3² + (−4)²)
  = √(9 + 16)
  = 5
```

### Ejercicios

1. Calcula la distancia entre P(0, 0) y Q(5, 12). *[Respuesta: 13]*
2. Un punto A está en (2, 1). ¿Cuántos puntos con coordenadas enteras están a distancia exactamente 5 de A?
3. *(Reto)* Demuestra que el triángulo con vértices A(0,0), B(4,0), C(2,2√3) es equilátero.

---

## Sesión 3 · El punto medio

### Concepto

El **punto medio** M de un segmento AB es el punto que lo divide en dos partes iguales.

Si A = (x₁, y₁) y B = (x₂, y₂):

$$M = \left(\frac{x_1 + x_2}{2},\ \frac{y_1 + y_2}{2}\right)$$

**Intuición:** es simplemente la media aritmética de cada coordenada por separado.

### Aplicación real

**¿Dónde poner el punto de encuentro?**

Ana vive en (2, 5) y Bruno en (8, 1). Quedan en un punto equidistante de los dos. ¿Dónde?

```
M = ((2+8)/2, (5+1)/2) = (5, 3)
```

### Conexión con la distancia

Podemos verificar: ¿M está realmente a la misma distancia de A y de B?

```
d(A, M) = √((5−2)² + (3−5)²) = √(9+4) = √13
d(B, M) = √((5−8)² + (3−1)²) = √(9+4) = √13  ✓
```

### Ejercicios

1. Encuentra el punto medio de A(−3, 4) y B(7, −2).
2. El punto medio de AB es M(3, 1). Si A = (1, −1), ¿cuáles son las coordenadas de B?
3. *(Aplicación)* En un mapa, tu casa está en (0, 0) y tu colegio en (6, 8). ¿Cuánto mide el camino en línea recta si cada unidad es 100 metros?

---

## Sesión 4 · La recta como objeto algebraico

### Motivación

Una recta en geometría euclidea se define por dos puntos. En geometría analítica, una recta tiene una ecuación. Eso nos permite preguntar: "¿está este punto en esa recta?" con un simple cálculo.

### La ecuación de la recta

La forma más común es la **forma pendiente-ordenada al origen**:

$$y = mx + b$$

Donde:
- **m** es la **pendiente** (controla la inclinación)
- **b** es la **ordenada al origen** (dónde corta el eje Y)

### Qué significa cada parámetro

| m > 0 | La recta sube de izquierda a derecha |
| m < 0 | La recta baja de izquierda a derecha |
| m = 0 | La recta es horizontal |
| b | El punto (0, b) siempre está en la recta |

### Cómo encontrar la ecuación dada una recta

**A partir de dos puntos** A(x₁, y₁) y B(x₂, y₂):

1. Calcula la pendiente: `m = (y₂ − y₁) / (x₂ − x₁)`
2. Sustituye uno de los puntos en `y = mx + b` para encontrar `b`

**Ejemplo.** A(1, 3) y B(3, 7):

```
m = (7−3) / (3−1) = 4/2 = 2

Sustituimos A: 3 = 2·1 + b → b = 1

Ecuación: y = 2x + 1
```

Verificamos con B: y = 2·3 + 1 = 7 ✓

---

## Sesión 5 · Pendiente: la inclinación como número

### Intuición física

La pendiente de una carretera se expresa como porcentaje: una rampa del 10% sube 1 metro por cada 10 metros horizontales. En matemáticas, la pendiente es exactamente esa razón:

$$m = \frac{\text{variación vertical}}{\text{variación horizontal}} = \frac{\Delta y}{\Delta x}$$

### Propiedades importantes

**Rectas paralelas** tienen la misma pendiente: `m₁ = m₂`

**Rectas perpendiculares** tienen pendientes cuyo producto es −1:

$$m_1 \cdot m_2 = -1 \quad \Leftrightarrow \quad m_2 = -\frac{1}{m_1}$$

> **Por qué −1/m:** Si una recta "sube 2 por cada 1 a la derecha" (m=2), la perpendicular debe "bajar 1 por cada 2 a la derecha" (m=−½). Los catetos del triángulo se intercambian y uno se invierte.

### Ejercicio de exploración

Dibuja en papel cuadriculado las rectas:
- `y = 2x`
- `y = 2x + 3`
- `y = −½x`

¿Cuáles son paralelas? ¿Cuáles son perpendiculares?

---

## Sesión 6 · Rectas paralelas y perpendiculares

### Determinación de la relación entre dos rectas

Dadas dos rectas, hay tres posibilidades:

| Situación | Condición | Número de intersecciones |
|-----------|-----------|--------------------------|
| Paralelas (no coincidentes) | `m₁ = m₂`, `b₁ ≠ b₂` | 0 |
| Coincidentes | `m₁ = m₂`, `b₁ = b₂` | infinitas |
| Secantes | `m₁ ≠ m₂` | exactamente 1 |
| Perpendiculares (caso especial de secantes) | `m₁ · m₂ = −1` | exactamente 1, en ángulo recto |

### Encontrar el punto de intersección

Para encontrar dónde se cortan dos rectas, igualamos sus ecuaciones:

```
r₁: y = 2x + 1
r₂: y = −x + 7

2x + 1 = −x + 7
3x = 6
x = 2  →  y = 2·2 + 1 = 5

Intersección: (2, 5)
```

### Problema integrador

Un arquitecto diseña dos calles en una ciudad nueva:
- Calle A pasa por (0, 1) y (2, 5)
- Calle B pasa por (0, 7) y (3, 1)

¿Se cruzan? ¿Dónde? ¿Son perpendiculares?

---

## Sesión 7 · Proyecto — Mapear el aula o el barrio

### Descripción

En grupos de 2-3, los alumnos eligen un espacio real (el aula, el patio, un tramo del barrio) y crean un mapa en coordenadas que responda a preguntas reales.

### Fases del proyecto

**Fase 1 — Toma de datos** (fuera del aula o en el aula)
- Definir origen y escala
- Medir posiciones de al menos 8 puntos relevantes
- Registrar coordenadas

**Fase 2 — Análisis**
Responder al menos 3 de estas preguntas usando las herramientas de la unidad:
- ¿Cuál es el punto más alejado del origen?
- ¿Hay elementos alineados? ¿Puedes encontrar su ecuación?
- ¿Cuál es el punto equidistante de dos elementos?
- ¿Hay elementos paralelos o perpendiculares?

**Fase 3 — Presentación**
- Mapa dibujado con precisión (a escala)
- Documento con los cálculos realizados
- Reflexión: ¿qué fue difícil? ¿qué descubriste?

### Criterios de evaluación del proyecto

| Criterio | Peso |
|----------|------|
| Precisión de las coordenadas | 25% |
| Corrección de los cálculos | 35% |
| Claridad de la presentación | 20% |
| Profundidad de la reflexión | 20% |

---

## Sesión 8 · Exposición y evaluación entre pares

### Formato

- Cada grupo presenta su proyecto en 5 minutos
- 3 minutos de preguntas del resto de la clase
- Evaluación entre pares completada por cada alumno al escuchar

### Guía de evaluación entre pares

Cada alumno evalúa a los grupos que escucha (no al propio):

```yaml
grupo_evaluado: ""
evaluador: ""
fecha: ""

criterios:
  claridad_explicacion:    # 1-10
  solidez_matematica:      # 1-10
  creatividad_del_proyecto: # 1-10

comentario_positivo: ""    # algo que aprendiste de este grupo
sugerencia_mejora: ""      # algo que podría hacerse mejor
```

---

## Conexiones con otras áreas

- **Física:** el plano cartesiano es la base de la cinemática (posición, velocidad, aceleración)
- **Geografía:** los sistemas de coordenadas geográficas (latitud/longitud) son análogos
- **Arte:** la perspectiva geométrica usa proyecciones equivalentes
- **Tecnología:** los píxeles de una pantalla son un plano cartesiano discreto

---

## Para ir más lejos

- **Circunferencia analítica:** `(x − a)² + (y − b)² = r²`
- **Lugar geométrico:** ¿qué figura forman todos los puntos equidistantes de dos puntos dados?
- **Transformaciones:** traslaciones, rotaciones y reflexiones como operaciones sobre coordenadas
- **Introducción a vectores:** un segmento AB como el par (x₂−x₁, y₂−y₁)
