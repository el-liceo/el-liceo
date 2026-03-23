# el-liceo

**Plan de estudios abierto y colaborativo para la ciudadanía del siglo XXI.**

Este repositorio contiene el currículo completo de El Liceo:
unidades didácticas, sesiones, ejercicios, recursos y registros de evaluación.
Todo el contenido es de acceso libre bajo licencia CC-BY-SA 4.0.

---

## Estructura del repositorio

```
el-liceo/
├── curriculo/                  ← plan de estudios base (meta-documento)
├── area-I-matematicas/
│   └── unidad-03-geometria-analitica/
│       ├── README.md           ← descripción legible de la unidad
│       ├── meta.yml            ← metadatos estructurados
│       ├── evaluacion-global.yml  ← generado por scripts/radar_update.py
│       ├── sesiones/
│       │   ├── s01-introduccion/
│       │   │   ├── guia-docente.md   ← para el profesor
│       │   │   ├── ejercicios.md     ← para el alumno
│       │   │   └── evaluacion.yml    ← registros de los tres ejes
│       │   └── s02-distancia/ ...
│       └── recursos/
│           ├── imagenes/
│           ├── datos/
│           ├── plantillas/
│           └── referencias/
├── area-II-lengua/ ...
├── scripts/
│   └── radar_update.py         ← genera evaluacion-global.yml desde las sesiones
└── .github/
    ├── CODEOWNERS
    └── pull_request_template.md
```

---

## Cómo contribuir

1. Haz fork del repositorio
2. Crea una rama con nombre descriptivo: `feat/area-I-unidad-04-algebra`
3. Añade o modifica contenido siguiendo la estructura de carpetas
4. Abre un Pull Request usando la plantilla
5. El PR necesita aprobación de N profesores del área (quorum definido por área en CODEOWNERS)

### Qué puede aportar cualquier profesor

- **Nueva sesión** en una unidad existente
- **Nuevos ejercicios** para una sesión (fichero `ejercicios.md`)
- **Corrección de errores** conceptuales o pedagógicos
- **Nuevos recursos** en la carpeta `recursos/`
- **Nueva unidad** completa (requiere quorum más amplio)

---

## Sistema de evaluación

Cada sesión tiene un `evaluacion.yml` con registros de tres ejes:

```yaml
- alumno: nombre-alumno
  fecha: "2025-03-03"
  aprendido_de_pares: 8    # 1–10
  ensenado_a_pares: 6      # 1–10
  evaluacion_docente: 7    # 1–10
  nota: "observación opcional"
```

El script `scripts/radar_update.py` agrega estos registros por unidad
y genera `evaluacion-global.yml`, que alimenta el radar de formación del alumno.

```bash
# Actualizar todas las unidades
python scripts/radar_update.py

# Actualizar solo una unidad
python scripts/radar_update.py --unidad area-I-matematicas/unidad-03-geometria-analitica
```

---

## Licencia

Todo el contenido de este repositorio está bajo licencia
[CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
Puedes usar, adaptar y redistribuir libremente citando la fuente
y manteniendo la misma licencia.
