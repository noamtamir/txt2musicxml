# txt2musicxml
A simple tool to convert chords from text to musicxml. Musicxml files can be opened with most notation software (for example [MuseScore](https://musescore.org/), which is free and open source).

## Install
use [pipx](https://github.com/pypa/pipx)
```shell
pipx install txt2musicxml
```

## Usage
pipe a string of chords into the cli
```shell
echo -n 'Cmaj7 A7 | Dm9 G7b9,13 |' | txt2musicxml
```
or redirect input/output from/to a file
```shell
txt2musicxml < path/to/Thriller.crd > path/to/Thriller.musicxml
```

## Syntax Example
Aguas de Marco - Elis Regina & Tom Jobim:
```crd
Bb/Ab | % |
Bb/Ab | Gm6 Cm7b5/Gb |
Bbmaj7/F E9b5 | Ebmaj9 Ab9 |
Bbmaj7 Bb7 | C7/E Ebm6 |
Bbmaj7/F Bb7 | C7/E Ebm6 :||
```

- More info in [SYNTAX.md](./SYNTAX.md)
- More examples: [./examples/](./examples/)

## Export to PDF (with MuseScore)
[Install MuseScore 3](https://musescore.org/en/download) and make sure to add `mscore` to your PATH. Not fully tested with v4. `%` doesn't work in v3.
```shell
TMPSUFFIX=.musicxml; mscore -o path/to/output.pdf =(txt2musicxml < path/to/input.crd)
```

## Developing Locally
### Dependencies
In order to change the grammer and regenerate lexer/parser/etc:
- [java](https://www.java.com/en/download/)
- [antlr](https://www.antlr.org/)

For other development:
- [python ^3.9](https://www.python.org/)
    - I suggest using [pyenv](https://github.com/pyenv/pyenv) to manage multiple python versions on your machine
- [poetry](https://python-poetry.org/) - to manage virtual env
- [Make](https://www.gnu.org/software/make/) - to help run useful commands

### Updating and Debugging
Grammer is defined in `txt2musicxml/grammer/Chords.g4`.
To generate antlr python classes (Lexer, Parser, Visitor, Listener) from the grammer file, run:
```bash
antlr4 -Dlanguage=Python3 txt2musicxml/grammer/Chords.g4 -visitor
```
Those classes are direct dependencies of the application, they must exist for the main program to run.

To use the built-in antlr GUI and debug your grammer, first compile those java classes, and then run the gui:
```bash
javac txt2musicxml/grammer/.antlr/Chords*.java
cd txt2musicxml/grammer/.antlr && grun Chords sheet -gui
```
Then enter some text and hit `^D` (on mac) to indicate EOF, and see the parse tree get generated!
> **_NOTE:_** `Chords` and `sheet` are names unique to the program (grammer name, root element), if you change the grammer file, the commands you run should change as well.