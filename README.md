# ZZMetro-INC：郑州地铁特情事件与协同处置时空风险数据集（Station×Hour）

ZZMetro-INC 是一个面向城市轨道交通“特情识别—风险预测—可信决策—人机协同处置（HITL）”的多表时空数据集，覆盖 **事件级监督信号**、**证据级多级标签**、**站点—线路—邻接图结构** 与 **站点×小时风险面板（含天气外生变量）**，可直接支撑 TITS 体量研究与可复现实验：

> **事件分类（5类） → 站点×小时风险预测 → 可信预测（EDL + Conformal） → 低置信分诊至人工（HITL）**

## 数据规模概览
- 事件（events）：872
- 证据样本（samples）：3160
- 站点（stations）：231
- 线路（lines）：13
- 邻接边（adjacency_edges）：272
- 时间范围：2010-05-26T00:00:00 ~ 2025-12-19T14:00:00

## 仓库结构（推荐开源方式）
```
ZZMetro-INC/
  data/
    raw/manifests/                       # 原始来源清单（URL/时间/ID），不含全文
      events_manifest.csv
    processed/
      events_labeled.csv                 # 事件级（监督信号主表）
      samples_labeled.csv                # 证据级（多级标签/时间置信）
      station_metadata_final.csv         # 站点元信息
      line_stations.csv                  # 线路-站序
      adjacency_edges.csv                # 站点邻接边表（本仓库补全）
      links/                             # 站点/线路链接与空间范围
        event_station_link_explicit.csv
        event_station_link_interval_inferred.csv
        event_station_link_expanded.csv
        event_line_link.csv
        event_spatial_scope.csv
      panels/                            # 站点×小时面板（训练主输入）
        station_hourly_panel_2022_2025_AC.csv.gz
        station_hourly_panel_2022_2025_AC_weather.csv.gz
    external/weather/                    # 天气外生变量（Open-Meteo）
      weather_hourly_zhengzhou.csv
      weather_hourly_zhengzhou.source.json
  docs/
    task_definition.md
    reproduce_paper.md
  CODEBOOK.md                            # 字段字典（强烈建议公开）
  DATASET_CARD.md                        # 数据集卡片（动机/限制/偏差/伦理）
  CITATION.cff
  LICENSE
  sha256sums.txt
```

## 核心文件（训练/论文最常用）
- **最终训练表（不含天气）**：`data/processed/panels/station_hourly_panel_2022_2025_AC.csv.gz`
- **最终训练表（含天气）**：`data/processed/panels/station_hourly_panel_2022_2025_AC_weather.csv.gz`
- **图结构**：`line_stations.csv` + `adjacency_edges.csv`

## 推荐任务（与你的论文一致）
- **T1：event_count**（站点×小时事件计数）
- **T2：risk_level**（风险等级）
- **T3：hitl_trigger**（是否触发人工介入）

> 任务口径与建议指标见：`docs/task_definition.md`

## 合规与版权（重要）
本仓库默认发布 **结构化标注与派生特征**。原始公告/新闻全文可能受来源站点版权/条款约束；本仓库以 `source_url` 做可追溯引用，复现者可按各站点条款在本地抓取与使用。

## 引用
请见 `CITATION.cff`（GitHub 可直接识别）。
