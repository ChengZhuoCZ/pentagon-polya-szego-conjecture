凸五边形：基态对数凹性与面积谱下界解析替换版（2026-10-12）

本版接续第五轮高振幅角点 PDE 版，保留前五轮全部成果。

本轮接入：
  Gaussian 边缘积分 + Dirichlet 热乘积极限 + 基态谱投影：在项目内证明凸多边形基态对数凹性，替代原 Brascamp–Lieb 外部引用。
  层集等周/余面积 + 十次正多项式：直接给面积谱预算 |R|lambda1(R)>289*pi/50，替代本项目 q 证明中的 Faber–Krahn 和第一 Bessel 零点步骤。
  显式 q 界加强为 q<5sqrt(2)/17<5/12；原下游 5/12 接口保持有效。

原 Bessel 级数界已是解析论证；本轮进一步移除当前 q 证明中的特殊函数零点。
其他章节 Bessel 核与级数仍保留。新谱阈值不声称强于尖锐 Faber–Krahn 常数。

本轮新增 5 引理、2 QMD，改写 2 旧节点。41 项有限精确检查通过，144 节点结构检查无错误、循环或不可达节点。
无限维极限与 PDE 步骤的适用条件见 checks/analytic-audit-round6.json；这是作者式核对，并非独立数学验证。
基础谱理论、Fourier、Sobolev、强极小值、Green/余面积等仍是明确保留的工具。

复算（Python 3 + SymPy）：
  python3 -I tools/check-ground-state-spectral-budget.py
对应 checks/ground-state-spectral-budget.json。
前三项入口分别为 gaussian-ground-state.qmd、area-spectral-budget.qmd 和 pressure-foundations.qmd。

完整范围与剩余基础见“替换范围与检查说明.txt”。
原稿见 archive/before-sixth-replacement；来源绑定见 checks/round6-source-map.json。
根主定理、statement-locks、AGENTS.md、backend=command 与 strict/strict/strict 配置不变。
结构检查仅在临时副本用 backend=none；未调用外部验证器，144 节点均为 unverified。
本轮不是整篇主定理独立审定或形式化证明。

书籍目录已同步补齐：纳入本轮两份新稿及第五轮的 finite-taylor-budget.qmd，62 份活动 QMD 均列入 Quarto 章节。旧章节配置保存在 archive/before-sixth-replacement/round5-_quarto.yml。
