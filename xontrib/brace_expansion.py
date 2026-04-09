"""
Implements simple brace expansion:

```console
@ echo a{d,c,b}e
ade ace abe
```

Nested expansion is not supported:

```console
@ echo /usr/{ucb/{ex,edit},lib/{ex?.?*,how_ex}}
SyntaxError: Unmatched "}" at line 1, column 16
```

See also:
* https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html
"""
from xonsh.events import events


def _expand_line(line):
    # Skip lines that don't contain brace expansion patterns
    if "{" not in line or "}" not in line:
        return line

    # Preserve leading whitespace
    stripped = line.lstrip()
    indent = line[: len(line) - len(stripped)]

    parts = stripped.split()
    expanded_parts = []

    for part in parts:
        if "{" in part and "}" in part:
            prefix, _, rest = part.partition("{")
            options, _, postfix = rest.partition("}")
            expanded_parts.extend(
                prefix + option + postfix for option in options.split(",")
            )
        else:
            expanded_parts.append(part)

    return indent + " ".join(expanded_parts)


@events.on_transform_command
def expand_braces(cmd, **_):
    lines = cmd.split("\n")
    return "\n".join(_expand_line(line) for line in lines)
