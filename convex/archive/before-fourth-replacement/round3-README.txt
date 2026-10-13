凸五边形：同源熵、几何归约与谱桥解析替换版（2026-10-12）

本包接续“凸五边形-双核与精细均值解析替换-QMD项目-20261012.zip”。本轮改写 10 个旧节点，新增 3 个共享引理；此前双核、均值、二十三系数和实际自旋替换均保留。

本轮承重改动：
  workspace/analytic-replacements-1012/entropy-identities.qmd：完整平方根熵与倒数预算的两个准确平方恒等式，供五处旧证明共同使用；保留最优尺度、退化情形和负号信用。
  workspace/true-pressure-terminal-migration-1011/uniform-source.qmd：均匀源预算加强为 (1-q)D0-qL0 >= (3/200)s²，覆盖 s>=2t 及 t=0。
  workspace/true-pressure-terminal-migration-1011/geometry-interface.qmd：以强凸性完成平方和直接正下界代替振幅上界中的两条 Sturm 链，结论仍为 t<27/50。
  workspace/analytic-replacements-1012/spectral-normalization.qmd：保持面积与双振幅关联，得到连续分母上界。
  workspace/ps-pressure-spectral-bridge-audit-1011.qmd：无严格出口域的谱形状系数从 1/200000 加强为 1/75000；global-gluing 已同步。
  十分之一/五分之一条带的重复五根展开改为引用同一准确矩公式。

当前检查与边界：
  checks/entropy-geometry-spectral.json：本轮 73 项精确恒等式和有理支付检查；随包脚本重放逐字一致。
  checks/mechanical-inspection.json：135 节点、57 份 QMD 的语法及依赖图检查，0 结构错误、0 循环、0 不可达节点。
  全部 135 节点在 backend=none 的机械检查中仍记为 unverified。图检查不验证数学真伪。
  共同相位/振幅联合支付、压力基础链、混合面积、谱上桥和参考校准仍保留；本版不是整篇主定理重新审定或形式化证明。
  根目标和原验证配置逐字保持；未启动外部验证器。受影响节点的旧 verified 标签撤下记录见 checks/withdrawn-stale-statuses-round3.json。

历史与来源：
  archive/before-third-replacement：本轮前八份数学原稿及上一版说明，均逐字保存；checks/round3-source-map.json 绑定其来源与 SHA256。
  archive/before-second-replacement、replaced-kernel-chain、original-actual-spin、source-supplements 保留前两轮档案及用户数学来源。
  SOURCE_BINDINGS_1012.json 保留前两轮补充包来源绑定；本轮没有引入新的外部补充包。
  所有历史 QMD 使用 .qmd.txt 后缀，不进入活动图。
  checks/round1-*、round2-* 是历史版结构及源码记录；其余前两轮数学检查保留，不宣称本轮再次审定全部证明。
  checks/change-manifest.json 和 active-source-sha256.json 对应当前版；根目录 MEMBER_SHA256SUMS.txt 覆盖除自身外全部文件。

本轮复算命令（项目根目录，Python 3 + SymPy）：
  python3 -I tools/check-entropy-geometry-spectral.py
输出应与 checks/entropy-geometry-spectral.json 一致。

此前检查脚本仍可使用：
  python3 -I tools/check-kernel-payment.py
  python3 -I tools/check-moment-packets.py
  python3 -I tools/check-packet-symbols.py
  python3 -I tools/check-fine-envelope-joins.py
  python3 -I tools/check-supporting-identities.py
  python3 -I tools/check-nine-constants.py
前两项只需 Python 3 标准库；其余需要 SymPy。对应检查范围见随包第二轮历史说明。

原 backend=command、strict/strict/strict 配置保留。只需结构检查时，请另作临时副本，仅在该副本将 backend 改为 none，再运行 qmd-prover inspect project --graph。
完整替换域、常数、数量和仍保留内容见“替换范围与检查说明.txt”。
