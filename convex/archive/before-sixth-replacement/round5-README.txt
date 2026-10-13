凸五边形：高振幅比、相反角点及 PDE 解析替换版（2026-10-12）

本版接续第四轮共同相位/压力/校准版，保留前四轮全部成果。

本轮已直接接入：
  141 项旧正基条目改为 25 行连续 Taylor 余项估计和 q2 的短凸性论证。
  mathscr D 下界 0.007 → 0.0099，beta7 下界 0.00961664 → 0.0104，beta0 至 beta6>1/50 保持。
  统一角点引理改从 H01 弱方程出发，通过直边反射、调和提升、Poisson 核、幂次屏障及能量测试得到导数阶，最后积分推出 H2。
  两处多边形全域 H2 定理引用移除；逐边压力积分有限性改由法向导数连续有界直接得到。

本轮改写 5 个旧节点，新增 1 个引理。342 项精确检查通过，139 节点的结构检查无错误、循环或不可达节点。
范围：仍有有限有理余项运算，仍保留基态对数凹性、Faber–Krahn/Bessel 和其他基础 PDE 输入；不是整篇主定理独立审定或形式化证明。

复算（Python 3 + SymPy；可在任意目录执行）：
  python3 -I tools/check-high-ratio-corner-pde.py
输出应与 checks/high-ratio-corner-pde.json 一致。
该脚本从原有限定义重建多项式，再与旧表系数独立对照，并检查正文的 25 行常数。
前四轮脚本、记录和原稿均保留。

原始数学文件：archive/before-fifth-replacement（逐字归档，不进入证明图）。
本轮来源：checks/round5-source-map.json。
旧标签撤下：checks/withdrawn-stale-statuses-round5.json。
当前源码与成员哈希：checks/active-source-sha256.json、MEMBER_SHA256SUMS.txt。

根主定理、statement-locks、AGENTS.md 和 backend=command、strict/strict/strict 配置保持。
未调用外部验证器；结构检查仅在临时副本中切换 backend=none，139 个节点均为 unverified。
详见“替换范围与检查说明.txt”。
