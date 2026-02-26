# csud_modules

Modules Python used at EPFL for the Turing course.

## Loading a module from Pyodide (WebTigerPython)

```python
import micropip
await micropip.install("https://raw.githubusercontent.com/donnerc/turing-modules/refs/heads/main/dist/turing-0.1.0-py3-none-any.whl")

from turing.nqueens import *
```
