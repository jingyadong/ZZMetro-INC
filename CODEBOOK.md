# CODEBOOK(Field Dictionary)

## 1) data/processed/events_labeled.csv(Event level)
-Doc_id: Unique ID of the event
-Source Domain: Source Domain
-Source_url: Original text link (traceability)
-Title: Title (Public Truncable)
-Pseudo label/label-name: Class 5 event labels
-Severity: Severity (0-3)
-Event_published.at: Announcement release time (ISO)
-Event_ts_hour: hourly time slice (used for panel aggregation)

## 2) data/processed/samples_labeled.csv(Evidence level/sample level)
-Sample_id: Unique ID of evidence
-Doc_id: Event ID to which it belongs
-Evidence text: Evidence fragments (publicly recommended truncation/desensitization)
-Sample_ts_hour: hours corresponding to evidence
-Sample_ppublish_time_comf/time_comfact: time extraction/alignment confidence level
-Multi_1evel_1abel_ *: Multi level exception labels (local/global/disposal, etc., according to your definition)

## 3) data/processed/panels/*.csv.gz(Station x Hour Panel)
Primary key: station_id+ts'hour
-Station_id: Site ID
-Ts_ hour: hourly time slot (local time zone)
-Event_comunt: The number of events on this station for that hour (T1)
-Risk_level: Risk level (T2)
-Hitl_trigger: whether to trigger manual (T3)
-Severity_max: maximum severity
-Time_ confidence: aggregation of time confidence
-Wx_ *: Weather characteristics (temperature/humidity/precipitation/wind speed/air pressure/cloud cover/weather code)

## 4) data/processed/adjacency_edges.csv(Adjacent Edge Table)
-Line: Line name
-U_station_id/v_station_id: Adjacent site ID
-U_Sq/V_Seq: Station sequence in the line
- edge_type：track_adjacent
-Is_undirected: 1 (undirected)
-Weight: 1.0 (expandable to distance/runtime, etc.)
