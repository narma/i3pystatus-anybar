# i3pystatus-anybar
[AnyBar](https://github.com/tonsky/anybar) like the widget for i3pystatus
<img src="assets/screenshot.png?raw=true" />

# Install
`pip install i3pystatus_anybar`

# Usage
In your config:
```python
from i3pystatus_anybar import anybar_append

#...

anybar_append(status, port=1740)
anybar_append(status, port=1741)
```
