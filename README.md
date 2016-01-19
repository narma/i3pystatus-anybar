# i3pystatus-anybar

# This repo is not maintained, because this functionality was merged to [i3pystatus master](https://github.com/enkore/i3pystatus/pull/224)



[AnyBar](https://github.com/tonsky/anybar)-like widget for i3pystatus
<img src="assets/screenshot.png?raw=true" />

# Install
`pip install i3pystatus_anybar`

# Usage
In your config:
```python
from i3pystatus_anybar import AnyBar

#...
status.register(AnyBar(port=1470))
status.register(AnyBar(port=1472))
```
