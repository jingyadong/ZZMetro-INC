# ZZMetro-INC (Zhengzhou Metro Incidents dataset)：A Spatiotemporal Risk Dataset for Metro Special Incidents and Collaborative Disposal (Station×Hour)

ZZMetro-INC is a multi-table spatiotemporal dataset for urban rail transit "Incident Recognition——Risk Prediction——Trustworthy Decision-making—Human-in-the-Loop Collaborative Response (HITL)", covering **incident-level supervisory signals**, **evidence-level multi-tier labels**, **station–line–adjacency graph structure**, and **station×hour risk panel (with weather exogenous variables)**, directly supporting research and reproducible experiments:

> **Incident Classification (5 classes) → Station×Hour Risk Prediction → Trustworthy Prediction (EDL + Conformal) → Low-Confidence Triage to Human (HITL)**

##Overview of Data Scale
-Events: 872
-Evidence samples: 3160
-Stations: 231
-Lines: 13
-Adjacent edges: 272
-Time range: 2010-05-26T00:00:00~2025-12-31T23:59:59

## Warehouse structure
```
ZZMetro-INC/
  data/
    raw/manifests/                       # Original Source List (URL/Time/ID)
      events_manifest.csv
    processed/
      events_labeled.csv                 # Event level (supervisory signal master table)
      samples_labeled.csv                # Evidence level (multi-level labels/time confidence)
      station_metadata_final.csv         # Site metadata
      line_stations.csv                  # Line Station Sequence
      adjacency_edges.csv                # Site adjacency edge table
      links/                             # Site/route links and spatial scope
        event_station_link_explicit.csv
        event_station_link_interval_inferred.csv
        event_station_link_expanded.csv
        event_line_link.csv
        event_spatial_scope.csv
      panels/                            # Station x Hour Panel (Training Main Input)
        station_hourly_panel_2022_2025_AC.csv.gz
        station_hourly_panel_2022_2025_AC_weather.csv.gz
    external/weather/                    # External weather variables (Open Meteo)
      weather_hourly_zhengzhou.csv
      weather_hourly_zhengzhou.source.json
  docs/
    task_definition.md
    reproduce_paper.md
  CODEBOOK.md                            # Field dictionary
  DATASET_CARD.md                        # Dataset Card (Motivation/Limitations/Bias/Ethics)
  CITATION.cff
  LICENSE
  sha256sums.txt
```

## Core document
- **Final training table (excluding weather)**：`data/processed/panels/station_hourly_panel_2022_2025_AC.csv.gz`
- **Final training schedule (including weather)**：`data/processed/panels/station_hourly_panel_2022_2025_AC_weather.csv.gz`
- **Graph structure**：`line_stations.csv` + `adjacency_edges.csv`

## Recommended tasks
- **T1：event_count**(Station x Hour Event Count)
- **T2：risk_level**(Risk level)
- **T3：hitl_trigger**(Whether to trigger manual intervention)

> Task caliber and suggested indicators can be found in：`docs/task_definition.md`

##  Compliance and Copyright
This repository defaults to publishing **structured annotations and derived features**. The original announcement/news full text may be subject to copyright/terms constraints of the source site; This repository uses' source_url 'as a traceable reference, and reproductors can retrieve and use it locally according to the terms of each site.
