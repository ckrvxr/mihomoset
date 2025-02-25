# mihomoset

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
    url: "https://testingcf.jsdelivr.net/gh/ckrvxr/mihomoset@release/StevenBlack.mrs"

```

```yaml
rules:
  - 'RULE-SET,stevenblack,REJECT'
```

### CDN Links:

* StevenBlack:  https://testingcf.jsdelivr.net/gh/ckrvxr/mihomoset@release/StevenBlack.mrs
* anti-AD :  https://testingcf.jsdelivr.net/gh/ckrvxr/mihomoset@release/anti-AD.mrs

### Subconverter rules

```
https://api.sublink.dev/sub?config=https://raw.githubusercontent.com/ckrvxr/mihomoset/refs/heads/main/subconverter-rules.ini&target=clash&udp=true&url=YOURURL

```
### Special Thanks To

- https://github.com/MetaCubeX/mihomo
- https://github.com/privacy-protection-tools/anti-AD
- https://github.com/StevenBlack/hosts
- https://github.com/tindy2013/subconverter
