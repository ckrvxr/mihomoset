# Mihomo Rules

This project retrieves the hosts file from the source at 6 AM in Beijing time every day to convert to the binary rule file for mihomo (mrs, yaml).

### Example:

Typically, only one needs to be selected. StevenBlack is used here.

```yaml
rule-providers:
  stevenblack:
    type: http
    behavior: domain
    format: mrs
    interval: 43200
    url: "https://testingcf.jsdelivr.net/gh/Ckrvxr/Mihomo-Rules@release/StevenBlack.mrs"
```

```yaml
rules:
  - 'RULE-SET,stevenblack,REJECT'
```

### CDN Links:

* StevenBlack:  https://testingcf.jsdelivr.net/gh/Ckrvxr/Mihomo-Rules@release/StevenBlack.mrs
* anti-AD :  https://testingcf.jsdelivr.net/gh/Ckrvxr/Mihomo-Rules@release/anti-AD.mrs

### Mihomo Party Override Rules

[Mihomo-Party.yaml](https://github.com/Ckrvxr/Mihomo-Rules/blob/main/Source/Override/Mihomo-Party.yaml)

### Subconverter Override Rules

```
https://url.v1.mk/sub?config=https://github.com/Ckrvxr/Mihomo-Rules/raw/refs/heads/main/Source/Override/Subconverter.yaml&clash.doh=true&target=clash&udp=true&url=YOURURL
```

### Special Thanks To

- https://github.com/MetaCubeX/mihomo
- https://github.com/privacy-protection-tools/anti-AD
- https://github.com/StevenBlack/hosts
- https://github.com/tindy2013/subconverter
- https://github.com/zsokami/ACL4SSR
- https://github.com/youshandefeiyang/sub-web-modify
- https://github.com/LoopDns/Fuck-you-MIUI/
