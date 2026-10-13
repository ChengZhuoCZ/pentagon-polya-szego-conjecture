# 五边形 Pólya–Szegő 猜想：凸与非凸情形

# The Pólya–Szegő Conjecture for Pentagons: Convex and Nonconvex Cases

[中文介绍](#chinese) · [English overview](#english)

## 作者 / Authors

**程卓 / Zhuo Cheng**  
School of Mathematics and Statistics, HNP-LAMA, Central South University, Changsha, Hunan 410083, P. R. China  
*邮箱 / Email address*: [zhuo@outlook.cz](mailto:zhuo@outlook.cz)

**杨航 / Hang Yang**  
School of Mathematics, Hunan University, Changsha, P.R. China  
*邮箱 / Email address*: [hangyang0925@gmail.com](mailto:hangyang0925@gmail.com)

## 首次归档时间 / Initial archive timestamp

**2026 年 10 月 13 日 18:26:51（北京时间，UTC+08:00）**  
**13 October 2026, 18:26:51 China Standard Time (UTC+08:00)**  
**UTC: 2026-10-13 10:26:51**

上述时间为 GitHub 服务器记录的[首次归档 Release](https://github.com/ChengZhuoCZ/pentagon-polya-szego-conjecture/releases/tag/archive-2026-10-13) 发布时间（`published_at`），对应标签 `archive-2026-10-13`。首次归档提交为 [`39e646aafd6945d122dfd582d7255e794399002d`](https://github.com/ChengZhuoCZ/pentagon-polya-szego-conjecture/commit/39e646aafd6945d122dfd582d7255e794399002d)。此时间记录的是版本归档时间，不将其等同于源文件标注的完成日期或首次公开时间。

This is the GitHub server-recorded publication time (`published_at`) of the [initial archive release](https://github.com/ChengZhuoCZ/pentagon-polya-szego-conjecture/releases/tag/archive-2026-10-13), tagged `archive-2026-10-13`. The initial archive commit is [`39e646aafd6945d122dfd582d7255e794399002d`](https://github.com/ChengZhuoCZ/pentagon-polya-szego-conjecture/commit/39e646aafd6945d122dfd582d7255e794399002d). It records the archiving of this version, rather than independently establishing the completion date stated in the source files or the date of first public disclosure.

**独立时间戳加固：2026 年 10 月 13 日 19:00:06（北京时间）/ 11:00:06 UTC。** 已取得 FreeTSA RFC 3161 签名凭证并通过验证，关联原始压缩包、作者信息及完整 Git 历史快照。仅向服务提交摘要；本次独立时间戳与上述首次 GitHub 归档时间分别记录。[凭证与复核方法](evidence/timestamp-20261013/README.md)。

**Independent timestamp: 13 October 2026, 11:00:06 UTC / 19:00:06 China Standard Time.** A FreeTSA RFC 3161 signed receipt has been obtained and verified, binding the original archives, author information, and a complete Git history snapshot. Only a digest request was submitted to the service. This new attestation is distinct from the initial GitHub archive timestamp above. [Evidence and verification instructions](evidence/timestamp-20261013/README.md).

本仓库由 GitHub 账户 **ChengZhuoCZ** 归档，包含两个独立的 QMD 源项目。  
Archived by GitHub account **ChengZhuoCZ**, this repository contains two independent QMD source projects.

<a id="chinese"></a>

## 中文介绍

### 研究问题

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

### 两个项目如何衔接

设 $A>0$，记 $R_A$ 为面积等于 $A$ 的正五边形。两个子项目分别处理以下环节；下述内容介绍源项目的目标陈述，本次整理未对其证明作新的独立认证。

#### 非凸部分：排除非凸极小者

[`nonconvex/goals.qmd`](nonconvex/goals.qmd) 的目标是：对每一个面积为 $A$ 的非凸简单至多五边形 $P$，构造同面积的简单至多五边形 $Q$，使

$$
\lambda_1(Q)<\lambda_1(P).
$$

“简单”指边界不自交；“有效边”排除把一条直边人为细分所增加的边数。源项目还要求：若竞争类限定为恰好五条有效边，竞争者 $Q$ 也可取为恰好五条有效边。这将说明：这些竞争类中的全局极小者，**若存在，必为凸多边形**。该陈述本身并不直接断言竞争者 $Q$ 就是正五边形。

#### 凸部分：与正五边形比较

[`convex/goals.qmd`](convex/goals.qmd) 的目标是：对每一个面积为 $A$ 的有界开凸五边形 $P$，证明

$$
\lambda_1(P)\geq\lambda_1(R_A).
$$

这给出凸五边形类中的正五边形极小性。源目标没有单独陈述等号情形的唯一性，因此这里也不额外宣称唯一性。

#### 整体问题

非凸部分负责说明非凸形状不能成为全局最优形状，凸部分负责建立正五边形的谱比较。要把两个结论衔接为整个简单五边形类中的极小性结论，还须核对极小者的存在性、退化到较少有效边时的处理，以及两个项目竞争类的兼容性；仅有“非凸形状存在更优竞争者”并不自动完成这些环节。

### 论文 PDF

以下为另行提供的两份论文稿，保留原始 PDF 内容，仅规范文件名。文件名日期 `20261013` 表示加入本仓库的日期，不代表首次完成时间。这两份 PDF 在首次归档和独立时间戳之后新增，不属于原时间戳覆盖的文件；其版本来源与 SHA-256 见 [`papers/manifest.json`](papers/manifest.json)。

- [Convexity and attainment in the five-sided Dirichlet problem](papers/Convexity-and-Attainment-in-the-Five-Sided-Dirichlet-Problem-20261013.pdf)：非凸排除、凸性与极小值达到的综合稿。
- [A pressure comparison for the first Dirichlet eigenvalue of convex pentagons](papers/Pressure-Comparison-for-the-First-Dirichlet-Eigenvalue-of-Convex-Pentagons-20261013.pdf)：凸五边形第一 Dirichlet 特征值的压力比较稿。

### 文件导航

| 目录 | 内容 | QMD 文件数 |
|---|---|---:|
| `nonconvex/` | 非凸五边形，英文解析 R4 版 | 18 |
| `convex/` | 凸五边形，强极值 Hilbert 积分分布解析替换版 | 70 |
| `archives/` | 两份未经修改的原始 ZIP 压缩包 | — |

各子项目原始文件逐字节保留，目录内部结构保持不变。阅读各自的 `index.qmd`、`goals.qmd`、`workspace/` 及原有 README；渲染配置见各自 `_quarto.yml`。两个项目应分别在各自目录中使用 Quarto。本次归档未重新审核数学证明或重新编译文稿。

### 版本与时间证据

- 原始压缩包名称标注日期为 **2026-10-12**；这属于源材料中的日期标注，不是独立可信时间戳。
- `PROVENANCE.json` 记录原始包的 SHA-256、版本与本次整理时间。
- `SHA256SUMS` 记录归档内容与说明文件的 SHA-256；README 修改后会同步更新校验清单，首次 Release 则保留原始清单。可通过 `shasum -a 256 -c SHA256SUMS` 验证。
- GitHub 私有仓库中的首次提交与归档 Release 保存本次上传的版本；Release 附件同时保留原始包和校验清单。以后公开时，应保留此仓库、提交、标签和 Release，而不是删除后重新建库。
- Git 提交的作者时间、提交时间和本地文件日期均可被修改，不能单独用来证明完成时间。GitHub 的服务器创建记录提供平台侧时间线，但不等同于独立公证、作者身份认证或对数学成果优先权的保证。
- 本仓库的整理说明不将 2026-10-12 宣称为已经独立验证的完成日期；作者署名以源文稿为准。

### 完整性检查

在仓库根目录运行：

```sh
shasum -a 256 -c SHA256SUMS
```

未来修改应新增提交和版本，保留初始归档记录。未添加开源许可证。

<a id="english"></a>

## English overview

### Research question

Among simple pentagons of a prescribed area, which shape minimizes the first Dirichlet eigenvalue? The central conjecture studied here is that **the regular pentagon attains this minimum**.

For a polygonal domain $\Omega\subset\mathbb R^2$, the first Dirichlet eigenvalue is

$$
\lambda_1(\Omega)
=\inf_{0\ne u\in H_0^1(\Omega)}
\frac{\int_\Omega |\nabla u|^2\,dx}
     {\int_\Omega |u|^2\,dx}.
$$

Here $H_0^1(\Omega)$ is the Sobolev space with zero boundary trace. For a membrane with fixed edges and uniform density and tension, $\lambda_1$ is proportional to the square of its fundamental frequency. The question can therefore be interpreted as asking whether a regular pentagonal drum has the lowest fundamental frequency among pentagonal drums of equal area.

The area constraint is essential: dilation by a factor $t$ multiplies area by $t^2$ and the eigenvalue by $t^{-2}$. Equivalently, one may study the scale-invariant quantity $|\Omega|\lambda_1(\Omega)$.

### How the two projects fit together

Let $A>0$, and let $R_A$ denote a regular pentagon of area $A$. The two projects address the following steps. These descriptions summarize the goal statements in the sources; preparing this archive did not provide a new independent verification of their proofs.

#### Nonconvex case: excluding nonconvex minimizers

The goal in [`nonconvex/goals.qmd`](nonconvex/goals.qmd) is to construct, for every nonconvex simple polygon $P$ of area $A$ with at most five effective sides, a simple polygon $Q$ of the same area with at most five effective sides such that

$$
\lambda_1(Q)<\lambda_1(P).
$$

“Simple” means that the boundary does not intersect itself. Counting effective sides excludes artificial subdivisions of a straight side. The source statement also requires that, when the admissible class consists of polygons with exactly five effective sides, $Q$ may be chosen with exactly five effective sides. This would imply that every global minimizer in either class, **if one exists, must be convex**. The statement does not itself assert that $Q$ is regular.

#### Convex case: comparison with the regular pentagon

The goal in [`convex/goals.qmd`](convex/goals.qmd) is to prove that every bounded open convex pentagon $P$ of area $A$ satisfies

$$
\lambda_1(P)\geq\lambda_1(R_A).
$$

This establishes the minimality of the regular pentagon within the convex pentagon class. The source goal does not separately assert uniqueness in the equality case, and no additional uniqueness claim is made here.

#### The full problem

The nonconvex project seeks to exclude nonconvex shapes as global minimizers, while the convex project seeks to establish the spectral comparison with the regular pentagon. Combining these statements into a global minimality result for all simple pentagons also requires checking the existence of minimizers, possible degeneration to fewer effective sides, and compatibility of the admissible classes. The existence of a better competitor for each nonconvex polygon does not by itself settle these issues.

### Manuscript PDFs

These two separately supplied manuscripts retain their original PDF bytes under descriptive filenames. The suffix `20261013` records the date they were added to this repository, not their original completion date. They were added after the initial archive and independent timestamp, which do not cover these new PDFs. Source versions and SHA-256 hashes are recorded in [`papers/manifest.json`](papers/manifest.json).

- [Convexity and attainment in the five-sided Dirichlet problem](papers/Convexity-and-Attainment-in-the-Five-Sided-Dirichlet-Problem-20261013.pdf): a synthesis manuscript on nonconvex exclusion, convexity, and attainment.
- [A pressure comparison for the first Dirichlet eigenvalue of convex pentagons](papers/Pressure-Comparison-for-the-First-Dirichlet-Eigenvalue-of-Convex-Pentagons-20261013.pdf): a pressure-comparison manuscript for the first Dirichlet eigenvalue of convex pentagons.

### Repository guide

| Directory | Contents | QMD files |
|---|---|---:|
| `nonconvex/` | Nonconvex pentagons, English analytic edition R4 | 18 |
| `convex/` | Convex pentagons, analytic replacements involving strong extrema, Hilbert spaces, integrals, and distributions | 70 |
| `archives/` | Two unmodified original ZIP archives | — |

The original files in each source project are preserved byte for byte, with their internal directory structure unchanged. Start with each project's `index.qmd`, `goals.qmd`, `workspace/`, and original README. Rendering settings are in the respective `_quarto.yml` files; use Quarto separately from each project directory. This archiving work did not re-audit the mathematical proofs or rebuild the manuscripts.

### Versions and timestamp evidence

- The original archive filenames carry the date **2026-10-12**. This is a date stated in the source materials, not an independently trusted timestamp.
- `PROVENANCE.json` records the original archive hashes, versions, and initial packaging time.
- `SHA256SUMS` records SHA-256 hashes of the tracked archive contents and documentation. It is updated when the README changes; the initial release retains its original checksum file.
- The initial commit and archive release preserve the first uploaded version. Release attachments retain the original ZIP files and checksum manifest. When making the repository public, preserve this repository, its commits, tags, and release instead of recreating it.
- Git author and committer dates and local file dates can be modified and do not independently prove a completion date. GitHub server records provide a platform-side timeline, but are not independent notarization, identity certification, or a guarantee of research priority.
- This repository does not claim that **2026-10-12** is an independently verified completion date. Authorship of the manuscripts follows their source texts.

### Integrity check

Run the following from the repository root:

```sh
shasum -a 256 -c SHA256SUMS
```

Future changes should be recorded in new commits and versions while preserving the initial archive. No open-source license has been added.
