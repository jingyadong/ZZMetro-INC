# DATASET CARD — ZZMetro-INC

## Overview
ZZMetro-INC focuses on the identification and collaborative handling of sudden/abnormal events in urban rail transit, providing event level supervision signals, evidence level multi-level labels, station route diagram structures, and station x hour risk panels, and supporting research on trustworthy prediction (Confocal/EDL) and human-machine collaboration (HITL).

## Applicable tasks
- Event classification (5 categories)
- Site x hour risk prediction (count/level/trigger manual)
- Trustworthy prediction: Conform prediction set (APS, etc.)/EDL uncertainty
- Human machine collaboration: Low confidence sample/spatiotemporal fragment triage to manual review (HITL)

## Data source and processing
- The event comes from public announcements/news, and can be traced back to `source_url` 
- Sites/routes are structurally extracted from public site/route pages (`station_metadata_final.csv`、`line_stations.csv`)
- The weather is sourced from the Open Meteo Historical Hour API (see `data/external/weather/*.source.json`)

## Deviation and Limitations
- The time field may be the proxy or rule extraction result of the announcement release time, which may have deviations;
- The site link contains weak tags (interval_infered/line_depagated), which are not recommended as accurate positioning truth values;
- Coverage is affected by public information and does not represent full internal records of operations.

## Ethics and Risk
- Does not include passenger personal information;
- Not recommended for individual identification or discriminatory purposes;
- If used for real operational decision-making assistance, it needs to be linked with operational rules/security mechanisms and strictly verified.
