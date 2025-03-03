# Override Rules

Override Rules for Mihomo, With Anti-Anti-Fraud.

### Mihomo Party Override Rules

[MihomoParty.yaml](https://github.com/Ckrvxr/MihomoRules/blob/main/Source/Override/MihomoParty.yaml)

### Subconverter Override Rules (Only Mihomo)

```
https://api.sublink.dev/sub?config=https://github.com/Ckrvxr/MihomoRules/raw/refs/heads/main/Source/Override/Subconverter.yaml&target=clash&udp=true&url=YOURURL
```
# Generated Rules

This project also retrieves the hosts file from the source at 6 AM in Beijing time every day to convert to the binary rule file for mihomo (mrs, yaml).

### Example:

Typically, only one needs to be selected. StevenBlack is used here.

```yaml
rule-providers:
  stevenblack:
    type: http
    behavior: domain
    format: mrs
    interval: 43200
    url: "https://testingcf.jsdelivr.net/gh/Ckrvxr/MihomoRules@release/StevenBlack.mrs"
```

```yaml
rules:
  - 'RULE-SET,stevenblack,REJECT'
```

### CDN Links:

* StevenBlack:  https://testingcf.jsdelivr.net/gh/Ckrvxr/MihomoRules@release/StevenBlack.mrs
* anti-AD :  https://testingcf.jsdelivr.net/gh/Ckrvxr/MihomoRules@release/anti-AD.mrs

### Special Thanks To

- https://github.com/MetaCubeX/mihomo
- https://github.com/privacy-protection-tools/anti-AD
- https://github.com/StevenBlack/hosts
- https://github.com/tindy2013/subconverter
- https://github.com/zsokami/ACL4SSR
- https://github.com/youshandefeiyang/sub-web-modify
- https://github.com/LoopDns/Fuck-you-MIUI/
