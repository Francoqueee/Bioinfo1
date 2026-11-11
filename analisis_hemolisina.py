#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Automatización - TP Final Bioinformática 1
Autor: Franco Romero Pompar
Descripción: Automatiza la lectura de un archivo FASTA, calcula la longitud
             de la proteína e identifica motivos estructurales usando Regex.
"""

import re  # Importamos el módulo de expresiones regulares de Python

def analizar_secuencia(ruta_fasta):
    # Inicializamos variables para almacenar el encabezado y la secuencia
    header = ""
    sequence_lines = []

    # Abrimos y leemos el archivo FASTA línea por línea
    print(f"[*] Leyendo el archivo: {ruta_fasta}")
    with open(ruta_fasta, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                header = line[1:]  # Guardamos el encabezado sin el símbolo '>'
            else:
                sequence_lines.append(line)

    # Unimos todas las líneas de la secuencia en un único string continuo
    full_sequence = "".join(sequence_lines)

    # 1. Cálculo de métrica: Longitud de la secuencia
    longitud = len(full_sequence)
    print(f"\n--- RESULTADOS DEL ANÁLISIS ---")
    print(f"Secuencia ID: {header}")
    print(f"Longitud total (Aminoácidos): {longitud}")

    # 2. Búsqueda de motivos mediante Expresiones Regulares (Regex)
    # Patrón: Glicina (G) + 1 a 3 aminoácidos cualesquiera ([A-Z]{1,3}) + Glicina (G)
    patron = r"G[A-Z]{1,3}G"
    coincidencias = re.findall(patron, full_sequence)

    print(f"Motivos ricos en glicina detectados ({patron}):")
    for idx, motivo in enumerate(coincidencias, 1):
        print(f"  {idx}. {motivo}")

if __name__ == "__main__":
    # Ejecutamos la función apuntando al archivo local de la alfa-hemolisina
    archivo_input = "rcsb_pdb_9mbx.fasta"
    analizar_secuencia(archivo_input)