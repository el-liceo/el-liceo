#!/usr/bin/env python3
"""
radar_update.py
Lee todos los evaluacion.yml del repositorio y genera
o actualiza el evaluacion-global.yml de cada unidad.

Uso:
    python scripts/radar_update.py
    python scripts/radar_update.py --unidad area-I-matematicas/unidad-03-geometria-analitica
"""

import argparse
import glob
import statistics
from datetime import datetime, timezone
from pathlib import Path

import yaml  # pip install pyyaml


def load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def save_yaml(path: Path, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)


def collect_session_records(unidad_path: Path) -> dict[str, list[dict]]:
    """
    Recorre todas las sesiones de una unidad y agrupa los registros por alumno.
    Devuelve: { "ana-garcia": [{"sesion": ..., "aprendido": ..., ...}, ...], ... }
    """
    alumnos: dict[str, list[dict]] = {}

    for eval_path in sorted(unidad_path.glob("sesiones/*/evaluacion.yml")):
        data = load_yaml(eval_path)
        sesion_id = eval_path.parent.name

        for reg in data.get("registros", []):
            alumno = reg.get("alumno")
            if not alumno:
                continue
            if alumno not in alumnos:
                alumnos[alumno] = []
            alumnos[alumno].append({
                "sesion": sesion_id,
                "fecha": reg.get("fecha"),
                "aprendido": reg.get("aprendido_de_pares"),
                "ensenado": reg.get("ensenado_a_pares"),
                "docente": reg.get("evaluacion_docente"),
            })

    return alumnos


def tendencia(scores: list[float]) -> str:
    if len(scores) < 3:
        return "insuficientes-datos"
    recent = scores[-3:]
    delta = recent[-1] - recent[0]
    avg = statistics.mean(scores)
    if delta > 1:
        return "mejorando"
    if delta < -1:
        return "empeorando"
    if avg >= 7.5:
        return "estable-alto"
    if avg >= 5:
        return "estable-medio"
    return "estable-bajo"


def build_global(unidad_path: Path, meta: dict) -> dict:
    sesiones_totales = meta.get("sesiones", 0)
    dimension = meta.get("dimension_radar", "desconocida")

    alumnos_data = collect_session_records(unidad_path)

    resumen_alumnos = []
    for alumno_id, registros in sorted(alumnos_data.items()):
        aprendidos = [r["aprendido"] for r in registros if r["aprendido"] is not None]
        ensenados  = [r["ensenado"]  for r in registros if r["ensenado"]  is not None]
        docentes   = [r["docente"]   for r in registros if r["docente"]   is not None]

        if not aprendidos:
            continue

        avg_ap = round(statistics.mean(aprendidos), 1)
        avg_en = round(statistics.mean(ensenados), 1) if ensenados else None
        avg_do = round(statistics.mean(docentes), 1)  if docentes  else None

        scores_all = aprendidos + (ensenados or []) + (docentes or [])
        score_dim  = round(statistics.mean(scores_all), 1)

        resumen_alumnos.append({
            "id": alumno_id,
            "sesiones_completadas": len(registros),
            "sesiones_totales": sesiones_totales,
            "promedios": {
                "aprendido_de_pares": avg_ap,
                "ensenado_a_pares":   avg_en,
                "evaluacion_docente": avg_do,
            },
            "score_dimension": score_dim,
            "tendencia": tendencia([r["docente"] for r in registros if r["docente"]]),
        })

    return {
        "unidad": str(unidad_path.relative_to(unidad_path.parent.parent)),
        "dimension_radar": dimension,
        "generado": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "alumnos": resumen_alumnos,
    }


def process_unidad(unidad_path: Path) -> None:
    meta_path = unidad_path / "meta.yml"
    if not meta_path.exists():
        print(f"  [skip] sin meta.yml: {unidad_path}")
        return

    meta = load_yaml(meta_path)
    global_data = build_global(unidad_path, meta)

    out_path = unidad_path / "evaluacion-global.yml"
    save_yaml(out_path, global_data)
    print(f"  [ok] {out_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Actualiza evaluacion-global.yml")
    parser.add_argument(
        "--unidad",
        help="Ruta relativa de una unidad concreta (opcional). "
             "Si no se especifica, procesa todas.",
    )
    parser.add_argument(
        "--repo",
        default=".",
        help="Raíz del repositorio (por defecto: directorio actual)",
    )
    args = parser.parse_args()

    repo = Path(args.repo).resolve()

    if args.unidad:
        targets = [repo / args.unidad]
    else:
        targets = [
            p.parent
            for p in repo.glob("area-*/unidad-*/meta.yml")
        ]

    print(f"Procesando {len(targets)} unidad(es)...")
    for unidad_path in sorted(targets):
        process_unidad(unidad_path)

    print("Listo.")


if __name__ == "__main__":
    main()
