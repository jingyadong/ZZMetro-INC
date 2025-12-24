#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Quick integrity checks for ZZMetro-INC repository.
Run:
  python scripts/validate_repo.py
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def must_exist(p: Path):
    if not p.exists():
        raise FileNotFoundError(str(p))

def main():
    must_exist(ROOT/"data/processed/events_labeled.csv")
    must_exist(ROOT/"data/processed/samples_labeled.csv")
    must_exist(ROOT/"data/processed/station_metadata_final.csv")
    must_exist(ROOT/"data/processed/line_stations.csv")
    must_exist(ROOT/"data/processed/adjacency_edges.csv")
    must_exist(ROOT/"data/processed/panels/station_hourly_panel_2022_2025_AC.csv.gz")
    must_exist(ROOT/"data/processed/panels/station_hourly_panel_2022_2025_AC_weather.csv.gz")

    ev = pd.read_csv(ROOT/"data/processed/events_labeled.csv")
    sm = pd.read_csv(ROOT/"data/processed/samples_labeled.csv")
    st = pd.read_csv(ROOT/"data/processed/station_metadata_final.csv")
    ln = pd.read_csv(ROOT/"data/processed/line_stations.csv")
    adj = pd.read_csv(ROOT/"data/processed/adjacency_edges.csv")

    # Basic sanity
    assert ev.shape[0] > 0 and sm.shape[0] > 0
    assert "station_id" in st.columns
    assert {"u_station_id","v_station_id"}.issubset(set(adj.columns))
    # Coverage check for adjacency stations
    st_ids = set(st["station_id"].astype(str).unique())
    adj_ids = set(adj["u_station_id"].astype(str).unique()) | set(adj["v_station_id"].astype(str).unique())
    missing = sorted(list(adj_ids - st_ids))
    if missing:
        print("[WARN] adjacency has station_ids not in station_metadata_final.csv:", missing[:10], "...")
    else:
        print("[OK] adjacency station_ids covered by station_metadata.")

    print("[OK] repo validation finished.")

if __name__ == "__main__":
    main()
