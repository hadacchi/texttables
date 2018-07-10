# texttables for multibyte japanese

This is a forked project.
This module cannot be installed by pip.

Original, notable `texttables` is [Taywee/texttables](https://github.com/Taywee/texttables).


This module accept multibyte unicode string in python 3.x.
This mechanism depends on `unicodedata.east_asian_width`.
This module assumes that width of multibyte characters is twice of ASCII characters.

# sample

this sample is convert data into markdown table string.

```python
import io
from texttables import Dialect
from texttables.dynamic import writer

# data
head = ['en','ja']
data = [['15000','100','300000'],     # data[0] is ascii ver.
        ['一万五千','百','三十万']]   # data[1] is japansese multibyte ver.

dialect = Dialect()
dialect.cell_delimiter=' | '

buf = io.StringIO()

with writer(buf, ['','>'], dialect=dialect) as wobj:
    wobj.writeheader(head)
    wobj.writerows([zipped for zipped in zip(data[0],data[1])])

print(buf.getvalue())
```

output should be following.
separater under table header should be inserted by you...

```
en     |       ja
15000  | 一万五千
100    |       百
300000 |   三十万
```
