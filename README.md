# 五边形 Pólya–Szegő 猜想：凸与非凸情形

*The Pólya–Szegő Conjecture for Pentagons*

## 作者

**程卓**  
School of Mathematics and Statistics, HNP-LAMA, Central South University, Changsha, Hunan 410083, P. R. China  
*Email address*: [zhuo@outlook.cz](mailto:zhuo@outlook.cz)

**杨航**  
School of Mathematics, Hunan University, Changsha, P.R. China  
*Email address*: [hangyang0925@gmail.com](mailto:hangyang0925@gmail.com)

## 首次归档时间

**2026 年 10 月 13 日 18:26:51（北京时间，UTC+08:00）**，即 **2026-10-13 10:26:51 UTC**。

上述时间为 GitHub 服务器记录的[首次归档 Release](https://github.com/ChengZhuoCZ/pentagon-polya-szego-conjecture/releases/tag/archive-2026-10-13) 发布时间（`published_at`），对应标签 `archive-2026-10-13`。首次归档提交为 [`39e646aafd6945d122dfd582d7255e794399002d`](https://github.com/ChengZhuoCZ/pentagon-polya-szego-conjecture/commit/39e646aafd6945d122dfd582d7255e794399002d)。此时间记录的是版本归档时间，不将其等同于源文件标注的完成日期或首次公开时间。

本仓库由 GitHub 账户 **ChengZhuoCZ** 归档，包含两个独立的 QMD 源项目。

## 研究问题

在面积固定的简单五边形中，哪一种形状使第一 Dirichlet 特征值最小？本项目研究的核心命题是：**正五边形应当实现这个最小值**。

设 $\Omega\subset\mathbb R^2$ 为多边形内部区域，其第一 Dirichlet 特征值定义为

$$
\lambda_1(\Omega)
=\inf_{0\ne u\in H_0^1(\Omega)}
\frac{\int_\Omega |\nabla u|^2\,dx}
     {\int_\Omega |u|^2\,dx}.
$$

这里 $H_0^1(\Omega)$ 表示在边界上取零值的 Sobolev 函数空间。从振动的角度看，$\lambda_1$ 对应边缘固定、材料与张力均匀的薄膜的基频平方（相差一个由物理参数决定的常数因子）。因此，这个问题也可以理解为：在面积相同的五边形鼓膜中，正五边形是否具有最低的基频？

固定面积这一条件不可省略：将区域放大 $t$ 倍后，面积变为原来的 $t^2$ 倍，而特征值变为原来的 $t^{-2}$ 倍。等价地，可以研究尺度不变的量 $|\Omega|\lambda_1(\Omega)$。

## 两个项目如何衔接

设 $A>0$，记 $R_A$ 为面积等于 $A$ 的正五边形。两个子项目分别处理以下环节；下述内容介绍源项目的目标陈述，本次整理未对其证明作新的独立认证。

### 非凸部分：排除非凸极小者

[`nonconvex/goals.qmd`](nonconvex/goals.qmd) 的目标是：对每一个面积为 $A$ 的非凸简单至多五边形 $P$，构造同面积的简单至多五边形 $Q$，使

$$
\lambda_1(Q)<\lambda_1(P).
$$

“简单”指边界不自交；“有效边”排除把一条直边人为细分所增加的边数。源项目还要求：若竞争类限定为恰好五条有效边，竞争者 $Q$ 也可取为恰好五条有效边。这将说明：这些竞争类中的全局极小者，**若存在，必为凸多边形**。该陈述本身并不直接断言竞争者 $Q$ 就是正五边形。

### 凸部分：与正五边形比较

[`convex/goals.qmd`](convex/goals.qmd) 的目标是：对每一个面积为 $A$ 的有界开凸五边形 $P$，证明

$$
\lambda_1(P)\geq\lambda_1(R_A).
$$

这给出凸五边形类中的正五边形极小性。源目标没有单独陈述等号情形的唯一性，因此这里也不额外宣称唯一性。

### 整体问题

非凸部分负责说明非凸形状不能成为全局最优形状，凸部分负责建立正五边形的谱比较。要把两个结论衔接为整个简单五边形类中的极小性结论，还须核对极小者的存在性、退化到较少有效边时的处理，以及两个项目竞争类的兼容性；仅有“非凸形状存在更优竞争者”并不自动完成这些环节。

## 文件导航

| 目录 | 内容 | QMD 文件数 |
|---|---|---:|
| `nonconvex/` | 非凸五边形，英文解析 R4 版 | 18 |
| `convex/` | 凸五边形，强极值 Hilbert 积分分布解析替换版 | 70 |
| `archives/` | 两份未经修改的原始 ZIP 压缩包 | — |

各子项目原始文件逐字节保留，目录内部结构保持不变。阅读各自的 `index.qmd`、`goals.qmd`、`workspace/` 及原有 README；渲染配置见各自 `_quarto.yml`。两个项目应分别在各自目录中使用 Quarto。本次归档未重新审核数学证明或重新编译文稿。

## 版本与时间证据

- 原始压缩包名称标注日期为 **2026-10-12**；这属于源材料中的日期标注，不是独立可信时间戳。
- `PROVENANCE.json` 记录原始包的 SHA-256、版本与本次整理时间。
- `SHA256SUMS` 记录本次归档文件的 SHA-256，可通过 `shasum -a 256 -c SHA256SUMS` 验证。
- GitHub 私有仓库中的首次提交与归档 Release 保存本次上传的版本；Release 附件同时保留原始包和校验清单。以后公开时，应保留此仓库、提交、标签和 Release，而不是删除后重新建库。
- Git 提交的作者时间、提交时间和本地文件日期均可被修改，不能单独用来证明完成时间。GitHub 的服务器创建记录提供平台侧时间线，但不等同于独立公证、作者身份认证或对数学成果优先权的保证。
- 本仓库的整理说明不将 2026-10-12 宣称为已经独立验证的完成日期；作者署名以源文稿为准。

## 完整性检查

在仓库根目录运行：

```sh
shasum -a 256 -c SHA256SUMS
```

未来修改应新增提交和版本，保留初始归档记录。未添加开源许可证。
