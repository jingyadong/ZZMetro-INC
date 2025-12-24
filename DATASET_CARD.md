# DATASET CARD — ZZMetro-INC

## 概述
ZZMetro-INC 面向城市轨道交通突发/异常事件识别与协同处置研究，提供事件级监督信号、证据级多级标签、站点-线路图结构与站点×小时风险面板，并支持可信预测（Conformal/EDL）与人机协同（HITL）研究。

## 适用任务
- 事件分类（5 类）
- 站点×小时风险预测（计数/等级/触发人工）
- 可信预测：Conformal prediction set（APS 等）/ EDL 不确定性
- 人机协同：低置信样本/时空片段分诊至人工审核（HITL）

## 数据来源与处理
- 事件来自公开公告/新闻，`source_url` 可追溯
- 站点/线路由公开站点/线路页面结构化抽取（`station_metadata_final.csv`、`line_stations.csv`）
- 天气来自 Open-Meteo 历史小时 API（见 `data/external/weather/*.source.json`）

## 偏差与限制
- 时间字段可能为公告发布时间的代理或规则抽取结果，存在偏差；
- 站点链接含弱标签（interval_inferred / line_propagated），不建议当作精确定位真值；
- 覆盖受公开信息影响，不代表运营内部全量记录。

## 伦理与风险
- 不包含乘客个人信息；
- 不建议用于个体识别或歧视性用途；
- 若用于真实运营辅助决策，需要与运营规则/安全机制联动并严格验证。
