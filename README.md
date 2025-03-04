**MihomoRules** 是为 [Mihomo](https://github.com/MetaCubeX/mihomo) 打造的规则库，提供广告拦截与隐私防护、反反诈骗的功能。

---

## 🎛️ 覆写规则配置指南

### 选项一：MihomoParty 直装方案
```yaml
▸ 配置文件：MihomoParty.yaml
▸ 下载地址：
  https://github.com/Ckrvxr/MihomoRules/raw/main/Source/Override/MihomoParty.yaml
```
**操作步骤**
1. 下载配置文件
2. 打开 MihomoParty 控制台
3. 进入「覆写配置」界面上传文件
4. 启用「全局应用」开关

以下是 MihomoParty 覆写包含的主要功能表格：

| 功能名称              | 描述                                                                   |
|-----------------------|----------------------------------------------------------------------|
| applicationdesktop    | 使代理工具和P2P下载软件等不走代理                                         |
| anti-AD               | 拦截国内广告和遥测                                                   |
| StevenBlack           | 拦截全球广告、遥测和恶意网站                                         |
| anti-AD-EDNS          | 拦截用于加载广告的加密DNS                                             |
| AntiPCDN              | 拦截P2P2 CDN，用于加速流媒体访问                                      |
| category-games@cn     | 使支持国内访问的游戏下载走直连，以节省流量                             |

### 选项二：Subconverter 订阅转换方案
```bash
# 订阅转换模板URL（复制后替换YOURURL字段）
https://api.sublink.dev/sub?config=https://github.com/Ckrvxr/MihomoRules/raw/refs/heads/main/Source/Override/Subconverter.yaml&target=clash&udp=true&url=YOURURL
```
**参数说明表**

| 参数名 | 必需 | 示例值 | 功能说明 |
|---------|-----|---------|---------|
| config  | ✔️ | [Subconverter.yaml](https://...) | 规则模板地址 |
| target  | ✔️ | clash | 输出格式 |
| udp     |   | true | 启用UDP转发 |
| url     | ✔️ | 您的订阅链接 | 原始订阅地址 |

以下是 Mihomo 覆写包含的主要功能表格：

| 功能名称              | 描述                                                                 |
|-----------------------|----------------------------------------------------------------------|
| antiantifraud         | 强力拦截手机的反诈骗程序，包括自动上传应用列表。这是本项目收集和整理的规则，目前还不够完善，希望大家参与建设，提供一个没有反诈的世界。 |
| fuck-you-miui         | 强力拦截小米的遥测                                                   |
| applicationdesktop    | 使代理工具和P2P下载软件等不走代理                                     |
| anti-AD               | 拦截国内广告和遥测                                                   |
| StevenBlack           | 拦截全球广告、遥测和恶意网站                                         |
| anti-AD-EDNS          | 拦截用于加载广告的加密DNS                                             |
| AntiPCDN              | 拦截P2P2 CDN，用于加速流媒体访问。这是本项目收集和整理的规则，目前还不够完善，希望大家参与建设。 |
| category-games@cn     | 使支持国内访问的游戏下载走直连，以节省流量                             |

---

## 🚀 路由规则引擎

### 📦 可用规则集列表

| 规则集名称       | 主要规则                  | 更新频率 | CDN地址                                                                 |
|------------------|-------------------------|----------|-------------------------------------------------------------------------|
| `StevenBlack`    | 全球广告/恶意软件拦截     | 自动生成 | [jsDelivr链接](https://testingcf.jsdelivr.net/gh/...) |
| `anti-AD`        | 中文区广告拦截、隐私保护           | 自动生成 | [jsDelivr链接](https://testingcf.jsdelivr.net/gh/...) |

（完整列表在 Release 分支中）

### 🛠️ 集成示例
```yaml
# config.yaml 配置片段
rule-providers:
  anti-ad:
    type: http
    behavior: domain
    format: mrs
    interval: 43200  # 每12小时更新
    url: "https://cdn.jsdelivr.net/gh/Ckrvxr/MihomoRules@RELEASE/anti-AD.mrs"

  stevenblack:
    type: http
    behavior: domain
    format: mrs
    interval: 43200
    url: "https://cdn.jsdelivr.net/gh/Ckrvxr/MihomoRules@RELEASE/StevenBlack.mrs"

rules:
  - RULE-SET,anti-ad,REJECT
  - RULE-SET,stevenblack,REJECT
```

---

> 📌 本项目遵循 [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) 协议，使用规则即视为同意授权条款。
