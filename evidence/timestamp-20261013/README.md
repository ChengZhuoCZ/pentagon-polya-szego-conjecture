# 独立时间戳凭证 / Independent timestamp evidence

**FreeTSA 签发时间 / Signed TSA time: 2026-10-13 11:00:06 UTC = 2026-10-13 19:00:06 北京时间 / China Standard Time.**

RFC 3161 响应序列号 / Response serial: `0x09278611`。摘要算法 / Digest: SHA-256。

## 证据范围 / Scope

`manifest.json` 记录两份原始 ZIP、初始 SHA256SUMS、来源记录、GitHub 元数据快照，以及包含全部历史的 `history.bundle` 的 SHA-256。作者、单位、邮箱也包含在此清单中。只有时间戳请求（摘要、随机 nonce 与协议字段）发送给 FreeTSA，没有上传论文、姓名、邮箱或原始文件。

The manifest binds both original ZIP archives, the initial checksum list, provenance records, GitHub metadata snapshots, and a complete Git history bundle through SHA-256. It also includes the authors, affiliations, and email addresses. Only the timestamp request (digest, random nonce, and protocol fields) was sent to FreeTSA; manuscripts, names, email addresses, and source files were not uploaded to that service.

该凭证在信任 FreeTSA 签发者与密码算法的前提下，证明对应内容不晚于签发时间已经存在。它不追溯认证 2026-10-12 的完成日期，不独立认证作者身份、成果优先权或证明正确性。原始 GitHub Release 时间 **2026-10-13 10:26:51 UTC** 保留为另一条平台记录。

Subject to trust in the FreeTSA issuer and cryptographic algorithms, this receipt attests that the committed content existed no later than the signed time. It does not retroactively certify completion on 2026-10-12, independently authenticate authorship or priority, or validate the mathematics. The original GitHub release time, **2026-10-13 10:26:51 UTC**, remains a separate platform record.

## 复核 / Verification

在具有完整历史的仓库克隆根目录运行（需要 Python 3 和支持 `ts` 的 OpenSSL）：

Run from a repository clone with full history (requires Python 3 and OpenSSL with `ts` support):

```sh
python3 evidence/timestamp-20261013/verify.py
```

脚本检查签名、请求 nonce、清单中的全部摘要及 Git bundle。README 与根目录 SHA256SUMS 后续会变化，因此检查使用清单指定的原始快照提交，而非当前工作区版本。

The script checks the signature, request nonce, every manifest digest, and the Git bundle. Since README and the root checksum list can change later, it verifies the commit named in the manifest, rather than their current working-tree versions.

只检查签名 / To check the signature alone:

```sh
openssl ts -verify \
  -data evidence/timestamp-20261013/manifest.json \
  -in evidence/timestamp-20261013/response.tsr \
  -CAfile evidence/timestamp-20261013/cacert.pem \
  -untrusted evidence/timestamp-20261013/tsa.crt
```

如果只有证据包，可从 bundle 恢复当时的仓库：

If only the evidence package remains, recover the archived repository from the bundle:

```sh
git clone history.bundle recovered-project
```

`response.tsr` 是签名凭证，`request.tsq` 是原始请求；`tsa.crt` 与 `cacert.pem` 为从 FreeTSA 官网取得的签发证书与根证书。验证使用该服务的根证书作为信任锚；这是第三方签名时间戳，不是区块链证明。长期保存时请保留所有文件，并在算法或证书信任条件改变前考虑续存证。

`response.tsr` is the signed receipt and `request.tsq` is the original request. The issuer and root certificates were retrieved from FreeTSA's official website. Verification trusts that service's root certificate. This is a third-party signed timestamp, not a blockchain proof. Preserve all files; consider renewed archival attestation before cryptographic algorithms or certificate trust conditions change.

[FreeTSA 官方说明 / Official documentation](https://www.freetsa.org/index_en.php)
