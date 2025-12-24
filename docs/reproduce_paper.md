# 论文复现（建议）

## 1) 训练表
- 含天气：`data/processed/panels/station_hourly_panel_2022_2025_AC_weather.csv.gz`
- 不含天气：`data/processed/panels/station_hourly_panel_2022_2025_AC.csv.gz`

## 2) 切分建议（避免时空泄漏）
- **时间切分优先**（推荐 rolling-origin / walk-forward）
  - train：最早 70%
  - calib：中间 10%（Conformal/校准）
  - test：最后 20%

## 3) 指标建议
- event_count：MAE / RMSE / Poisson deviance
- risk_level：Macro-F1 / Cohen’s kappa / Confusion matrix
- hitl_trigger：PR-AUC + 人工量曲线
- Conformal：coverage、平均集合大小、有效集合率
- EDL：ECE、拒识曲线（selective risk）
