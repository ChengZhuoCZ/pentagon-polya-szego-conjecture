凸五边形：共同相位、压力基础链与谱校准解析替换版（2026-10-12）

本版接续第三轮“熵几何谱桥解析替换”项目，前面三轮的双核、均值、实际自旋、同源熵、几何振幅和谱余量成果均保留。

本轮直接接入的改动：
  phase-short-payments.qmd：用连续 Taylor 和完成平方替换 50 项判别式正基长表及 9 项成本正基表。U>1/4，Ds>0.003，Dl 下界由 0.00012 加强至 0.0018。
  corner-barrier.qmd：以一个初等幂次屏障统一三处凸角控制，保留导数阶、切角谱代价和 Hadamard 的角弧消失；切角不再使用 Bessel 角点函数。
  pressure-foundations.qmd：新增完整作用量非负缺口，集中证明候选压力的唯一极小性与边界值；弱对偶明确保留奇异质量；压力像改用紧致性和连通性。
  正五边形校准节点 ID 保持、移动到 pressure-foundations.qmd。五重对称、支撑变分和真实压力缺口直接给准确校准，不再在该步骤使用谱 Brunn–Minkowski 不等式。

范围和检查：
  实质改写 9 个旧节点，新增 3 个引理、2 份 QMD；138 个活动节点全部在根目标依赖闭包内，结构检查无错误、循环或不可达节点。
  checks/phase-pressure-calibration.json：103 项精确检查通过，包含与归档原判别式的 50 项逐项恒等验证。
  有限 Taylor 的集中余项仍包含明确的有理比较，不声称整个共同相位预算已无需系数估计。
  高振幅比及其余相位长表、基态对数凹性、经典 PDE 正则性、压力存在基础和 q<5/12 的 Faber–Krahn/Bessel 界仍保留。
  本轮是局部解析替换及接口核对，不是整篇主定理重新审定或形式化证明。机械检查中的 138 节点仍记为 unverified。

复算（项目根目录，Python 3 + SymPy）：
  python3 -I tools/check-phase-pressure-calibration.py
该脚本读取随包归档的原长表，只作独立对应核对；新多项式从原有限定义重建。输出应与 checks/phase-pressure-calibration.json 一致。
前面三轮的检查脚本及记录均保留，复算命令见对应历史说明。

历史和状态：
  archive/before-fourth-replacement：本轮前四份数学原稿及第三轮 README/index/范围说明，逐字保留。
  checks/round4-source-map.json：本轮来源与 SHA256；此前 SOURCE_BINDINGS_1012.json 仍保留补充包绑定。
  checks/withdrawn-stale-statuses-round4.json：本轮受影响节点的旧标签撤下记录。
  checks/round1-*、round2-*、round3-* 是历史结构/源码记录，不是本轮对全项目重新验证的结果。
  checks/change-manifest.json、active-source-sha256.json 对应当前版；MEMBER_SHA256SUMS.txt 覆盖除自身外全部成员。

根主定理、statement-locks 和原 backend=command、strict/strict/strict 配置逐字保留。本轮未调用外部验证器。
只需结构检查时，请另作临时副本，仅在该副本中将 backend 改为 none，再运行 qmd-prover inspect project --graph。
完整推导范围和未替换部分见“替换范围与检查说明.txt”。
