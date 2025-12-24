# CODEBOOK（字段字典）

## 1) data/processed/events_labeled.csv（事件级）
- doc_id：事件唯一 ID
- source_domain：来源域名
- source_url：原文链接（追溯）
- title：标题（公开可截断）
- pseudo_label / label_name：5 类事件标签
- severity：严重度（0-3）
- event_published_at：公告发布时间（ISO）
- event_ts_hour：小时级时间片（用于面板聚合）

## 2) data/processed/samples_labeled.csv（证据级/样本级）
- sample_id：证据唯一 ID
- doc_id：所属事件 ID
- evidence_text：证据片段（公开建议截断/脱敏）
- sample_ts_hour：证据对应小时
- sample_publish_time_conf / time_confidence：时间抽取/对齐置信度
- multi_level_label_*：多级异常标签（局部/整体/处置等，按你的定义）

## 3) data/processed/panels/*.csv.gz（站点×小时面板）
主键：station_id + ts_hour
- station_id：站点 ID
- ts_hour：小时级时间片（本地时区）
- event_count：该站该小时事件数（T1）
- risk_level：风险等级（T2）
- hitl_trigger：是否触发人工（T3）
- severity_max：最大严重度
- time_confidence：时间置信度聚合
- wx_*：天气特征（温度/湿度/降水/风速/气压/云量/天气码）

## 4) data/processed/adjacency_edges.csv（邻接边表）
- line：线路名
- u_station_id / v_station_id：相邻站点 ID
- u_seq / v_seq：在线路中的站序
- edge_type：track_adjacent
- is_undirected：1（无向）
- weight：1.0（可扩展为距离/运行时长等）
