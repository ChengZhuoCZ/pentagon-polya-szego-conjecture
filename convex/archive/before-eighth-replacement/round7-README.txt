凸五边形：基础谱、Fourier 与 Sobolev 解析替换版（2026-10-12）

接续第六轮，新增 6 个引理、4 份 QMD，实质改写 11 个旧节点。

本轮接入：
  正紧算子极值构造 → Dirichlet 离散谱、正第一基态单性及长时间投影。
  高斯卷积能量恒等式 → 替换 Plancherel；对角分解与 Bernstein 逼近 → 替换一般谱演算。
  一维变分与周期 ODE → 替换等周步骤中的周期 Fourier，并给准确条带常数。
  向内伸缩、卷积及有限网格 → 凸域零延拓、Dirichlet 紧性。
  内缩多边形、Fatou 与凹性 → 压力边界可积性及散度公式。
  逐片积分和 H01 闭包 → 五扇能量换元；角积分权端点由一维原函数给出。

热乘积声明收窄到本项目全部实际调用所满足的有界开凸集。
一般 Dirichlet 谱引理覆盖有界连通开集，包括全部凸体内部。
保留 Hilbert/积分/分布基础、规则层集换元与严格 Hessian 的强极小值原理。
前六轮的常数预算和 q<5sqrt(2)/17<5/12 保持。

44 项本轮有限检查通过；第六轮 41 项复算记录逐字相同。
150 节点、66 QMD，结构检查无错误、循环或不可达；全部 QMD 已列入 Quarto 书目。
这是作者式推导与结构/有限代数检查，不是整篇证明独立审定或形式化验证。
交付配置保持 command、strict/strict/strict；结构仅在副本以 none 检查，未运行外部验证器。

完整范围见“替换范围与检查说明.txt”。
复算：python3 -I tools/check-spectral-sobolev-foundations.py（需要 SymPy）。
新证明及接口核对见 checks/analytic-audit-round7.json；原稿见 archive/before-seventh-replacement。
历史记录按轮次保存，不能当成本轮对未修改内容的重新审定。
