凸五边形：双核与精细均值解析替换版（2026-10-12）

本包接续“凸五边形-解析接口替换-QMD项目-20261012.zip”。原主定理声明和验证配置保持不变。

本轮新增的承重正文（workspace/analytic-replacements-1012）：
  u0-radial.qmd：第六标量 u0 的完整连续下界。
  finite-mass-kernels.qmd：六标量到完整双核的四行包围；真实积分权的有限质量；完整 Lorentz 比较。
  moment-packets.qmd：八个初等角矩；C/U 二十三系数的统一生成、明确有理包围与完整均值余项。
此外 bessel-core.qmd 导出原证明内已有的 f 配对和 f 全尾式；j-radial.qmd 导出原证明内已有的 H 二次包围。

原消费者 ID 保持：
  prp-ppcs-central-lorentz-closure-1011、prp-ppus-unit-lorentz-closure-1011 的证明已改用有限质量比较。
  lem-ppsm-ten-packets-1011、lem-ppusm-ten-packets-1011 的证明已改用八角矩统一生成。
  prp-ppsm-shared-phase-sharp-means-1011、prp-ppusm-shared-phase-sharp-means-1011 的强包络及共同相位信用继续承重。
上一轮 C/U 粗均值与实际自旋解析替换完整保留。

数学范围：
  新完整核比较针对同一含源权、同一任意复相位和可容许 W,V，包含全部径向与别名尾。
  U：0<=t<=27/50，0<=s<=5/8；C：0<=s<=t<=27/50。
  新比较不依赖实际 K/C；原实际自旋定理仍独立供给消费者斜率。
  主线已不需要旧 D_lambda/H_lambda 的整个圆盘逐点符号；这些更强、不同形式的旧声明只留档，不被新定理冒名替代。
  二十三个系数的表示方式已简化，七次相位字符及精细相位平方信用仍保留。活动节点的减少不代表整篇主定理已完成独立审定。

历史与来源：
  archive/original-actual-spin：上一轮退出的两份旧实际自旋原文。
  archive/before-second-replacement：本轮之前两份均值文件及两份 Lorentz 消费者的原文。
  archive/replaced-kernel-chain：本轮退出的 11 份完整双核链文件，以及 tensor-frontier 原稿。
  archive/source-supplements：用户补充包中用到的数学来源，SHA256 绑定见 SOURCE_BINDINGS_1012.json。
  八角矩共同生成、U 支扩至 5/8 的支付、以及有限质量主线接合为本轮在这些来源上整理推导的正文。
  所有历史 QMD 使用 .qmd.txt 后缀，保留原字节且不进入活动证明图。

当前检查：
  checks/kernel-payment.json：47 项精确有理比较。
  checks/moment-packets.json：56 项检查，使用正文已声明的十三位常数区间。
  checks/packet-symbols.json：31 项符号恒等式；直接从原含权核展开，保留符号源参数 kappa，并与八角矩包全部单项式比较。
  checks/fine-envelope-joins.json：31 项旧精细包络符号/合并/相位因子核对。
  checks/supporting-identities.json：上轮 91 项检查在当前工具目录重放，结果一致。
  checks/mechanical-inspection.json：本版 132 节点的结构检查（backend=none，仅临时副本）。
  checks/retired-kernel-chain.json：旧双核节点及文件退出清单。
  checks/withdrawn-stale-statuses-round2.json：本轮受影响的节点及撤下的旧状态。
  checks/round1-* 及 mean-replay、spin-replay 是上一轮历史记录，不是本版全部节点的验证结果。
  checks/change-manifest.json、active-source-sha256.json 对应本版；根目录 MEMBER_SHA256SUMS.txt 覆盖除自身外的所有文件。

可复算命令（在项目根目录；前两项只需 Python 3 标准库，其余需要 SymPy）：
  python3 -I tools/check-kernel-payment.py
  python3 -I tools/check-moment-packets.py
  python3 -I tools/check-packet-symbols.py
  python3 -I tools/check-fine-envelope-joins.py
  python3 -I tools/check-supporting-identities.py
  python3 -I tools/check-nine-constants.py
前五项输出分别与上述当前 JSON 记录一致；最后一项为此前九常数的独立精确检查。

原 backend=command、strict/strict/strict 验证配置保留。本次没有启动外部验证器。要只重放结构检查，请另作临时副本并仅在该副本中将 backend 改为 none，再运行 qmd-prover inspect project --graph。
有限精确检查验证公开公式和常数；连续不等式的论证写在正文中。机械图检查不验证数学真伪，本版不声称整篇主定理已重新审定或形式化证明。

详细替换数量、域和限制见“替换范围与检查说明.txt”。
