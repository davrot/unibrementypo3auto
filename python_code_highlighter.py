from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatter import Formatter
import html
import argh


class NullFormatter(Formatter):
    def format(self, tokensource, outfile):
        for ttype, value in tokensource:
            escape_it: bool = True
            if str(ttype).startswith("Token.Literal.String"):
                start: str = '<strong class="text-danger">'
                end: str = "</strong>"

            elif str(ttype).startswith("Token.Comment"):
                start: str = '<strong class="text-muted">'
                end: str = "</strong>"

            elif str(ttype).startswith("Token.Operator"):
                start: str = '<strong class="text-info">'
                end: str = "</strong>"

            elif str(ttype).startswith("Token.Keyword"):
                start: str = '<strong class="text-success">'
                end: str = "</strong>"

            elif str(ttype).startswith("Token.Name.Builtin"):
                start: str = '<strong class="text-primary">'
                end: str = "</strong>"

            elif str(ttype).startswith("Token.Name"):
                start: str = '<strong class="text-warning">'
                end: str = "</strong>"

            elif str(ttype) == "Token.Text":
                if (len(value) == 1) and (value[0] == "\n"):
                    value = str("<br>")
                    start: str = ""
                    end: str = ""
                    escape_it = False
                else:
                    start: str = "<strong>"
                    end: str = "</strong>"

                all_space: bool = True
                for i in range(0, len(value)):
                    if value[0] != " ":
                        all_space = False
                        break

                if all_space is True:
                    replace_length: int = len(value)
                    escape_it = False

                    value = ""
                    for _ in range(0, replace_length):
                        value += str("&nbsp;")

            else:
                start: str = "<strong>"
                end: str = "</strong>"

            outfile.write(start)
            if escape_it is True:
                outfile.write(html.escape(value))
                outfile.write(str("&nbsp;"))
            else:
                outfile.write(value)
            outfile.write(end)


def main(filename: str):
    assert len(filename) > 0

    with open(filename, "r") as file:
        code = file.readlines()

    line_count: int = 0
    output: str = str("<pre>")
    for code_line in code:
        output += highlight(code_line, PythonLexer(), NullFormatter())
        line_count += 1

    output += str("</pre>")

    print(output)


if __name__ == "__main__":
    argh.dispatch_command(main)
