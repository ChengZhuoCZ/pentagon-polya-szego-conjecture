凸五边形：强极值、Hilbert、积分与分布基础解析替换版（2026-10-12）

接续第七轮，新增 7 个引理、4 份 QMD，实质改写 17 个旧节点、10 份旧数学文件。

指数环带屏障直接覆盖严格 Hessian、开边法向导数和角压缩中的极值原理。
Hilbert 投影、Riesz、Parseval、弱子列和强制二次极小问题均在项目内展开。
L2/H1/H01 完备性、积分收敛、欧氏 Fubini、卷积及局部弱微分接口也已展开并接入。

保留实数及集合基础、Lebesgue 测度构造/正则性、经典光滑换元、Green/散度、规则层集余面积。
前七轮常数预算和 q<5sqrt(2)/17<5/12 保持。

36 项本轮有限检查通过；第七轮 44 项和第六轮 41 项历史复算逐字一致。
157 节点、70 QMD，结构检查无错误、循环或不可达；全部 QMD 已列入 Quarto 书目。
这是作者式推导与结构/有限代数检查，不是整篇证明独立审定或形式化验证。
交付配置仍为 command、strict/strict/strict；结构只在副本用 none 检查，未调用外部验证器。

完整范围见“替换范围与检查说明.txt”。
复算：python3 -I tools/check-extrema-hilbert-integrals.py（需要 SymPy）。
接口核对见 checks/analytic-audit-round8.json；原稿见 archive/before-eighth-replacement。
历史记录按轮次保留，不视作本轮对未改内容的重新审定。
