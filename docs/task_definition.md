# 任务定义（TITS 导向）

本数据集围绕“事件分类 → 站点×小时风险预测 → 可信预测 → 人机协同处置”设计，推荐以 **站点×小时** 为主任务单位。

## 标签
- **T1：event_count**：站点×小时事件计数（回归/计数）
- **T2：risk_level**：站点×小时风险等级（分类）
- **T3：hitl_trigger**：是否触发人工介入（分类）

## 建议风险等级口径（可解释、稳）
（若你已有更严格口径，可在论文中替换为你的定义）
- risk=0：event_count=0
- risk=1：event_count>0 且 severity_max<=1 且 event_count==1
- risk=2：severity_max==2 或 event_count>=2
- risk=3：severity_max==3 或 event_count>=3

## 可信预测 + HITL
- **Conformal（APS）**：输出 prediction set，用 coverage / set size 评估；set size > 1 作为“不确定”的天然触发器。
- **EDL 不确定性**：输出证据/不确定性指标，做拒识曲线（risk–uncertainty）或 selective prediction 曲线。
- **HITL 分诊**：将低置信（或 set size>1）样本送人工，比较“覆盖率—人工量—误报漏报”权衡曲线。
