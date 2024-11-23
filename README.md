# txt2musicxml
A simple tool to convert chords from text to musicxml. Musicxml files can be opened with most notation software (for example [MuseScore](https://musescore.org/), which is free and opensource).

## Install
use [pipx](https://github.com/pypa/pipx) to install
```shell
pipx install txt2musicxml
```

## Usage
pipe a string of chords into the cli
```shell
echo 'Cmaj7 A7 | Dm9 G7b913 |' | txt2musicxml
```
or redirect input/output from/to a file
```
txt2musicxml < path/to/Thriller.crd > path/to/Thriller.musicxml
```

## Syntax Example
Aguas de Marco - Elis Regina & Tom Jobim:
```crd
Bb/Ab | Bb/Ab |
Bb/Ab | Gm6 Cm7b5/Gb |
Bbmaj7/F E9b5 | Ebmaj9 Ab9 |
Bbmaj7 Bb7 | C7/E Ebm6 |
Bbmaj7/F Bb7 | C7/E Ebm6 |
```

- More info in [SYNTAX.md](./SYNTAX.md)
- More examples: [./examples/](./examples/)

## Developing Locally
### Dependencies
In order to change the grammer and regenerate lexer/parser/etc:
- [java](https://www.java.com/en/download/)
- [antlr](https://www.antlr.org/)

For other development:
- [python](https://www.python.org/) (3.13) 
    - I suggest using [pyenv](https://github.com/pyenv/pyenv) to manage multiple python versions on your machine
- [poetry](https://python-poetry.org/) - to manage virtual env
- [Make](https://www.gnu.org/software/make/) - to help run useful commands

### Updating and Debuging
Grammer is defined in `txt2musicxml/grammer/Chords.g4`.
To generate antlr python classes (Lexer, Parser, Visitor, Listener) from the grammer file, run:
```bash
antlr4 -Dlanguage=Python3 txt2musicxml/grammer/Chords.g4 -visitor
```
Those classes are direct dependecies of the application, they must exist for the main program to run.
