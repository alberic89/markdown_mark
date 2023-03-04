# markdown_mark

Extends the [Python Markdown](https://python-markdown.github.io/).
Adds the possibility to use `==something==` or `???something???` to create a span that looks like `<mark>something</mark>`

Install through pip:

```bash
pip install markdown_mark
```

To enable the markdown_mark package and use it in your markdown generation just add it like so:

```python
import markdown

result = markdown.markdown(textToRender, extensions=["markdown_mark",])
```
