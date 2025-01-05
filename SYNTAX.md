# Syntax

## Quick start example
```crd
Bb/Ab | % |
Bb/Ab | Gm6 Cm7b5/Gb |
Bbmaj7/F E9b5 | Ebmaj9 Ab9 |
Bbmaj7 Bb7 | C7/E Ebm6 |
Bbmaj7/F Bb7 | C7/E Ebm6 |
```

## Chord
A chord is 1 block of text without whitespace that must at least have a root, in this format:
```
<root>[alteration][suffix][/bass][alteration]
```
Example:
```
Gbmaj7#5/Bb
```
- **Root**: A name of a note. An uppercase letter between A-G. Required for any chord. E.g. `C`
- **Alteration**: An accidental (sharp/flat), may optional come after a note (root/bass). E.g. `#`, `b`, `##` `bb`
- **Suffix**: Anything related to the type of the chord and/or tensions. E.g. `m`, `maj7`, `7#9`, `b9b13`, `9,13`
- **Bass**: Same as note, but must have a slash (/) before it and must come after a root (+ optional alteration and/or suffix ). No whitespace is allowed before or after the slash. E.g `/G`

## Bar
A bar consists of multiple chords seperated by whitespace, following a barline. It could also be a repeat bar, also followed by a bar line.
- Barline: `|`, `||`, `:||`
- Repate Bar: `%`
```
Gm6 Cm7b5/Gb | % |
```

## Rhythm
Chords occupy an equal of time in a bar if possible to fit into simple rhythms such as whole/half/quarter notes. If not possible, the later chords' rhythm is split to make them shorter. Examples:
```
Cmaj || -> 1 whole note
Cmaj7 Fmaj7 || -> 2 half notes
Cmaj7 G/B Am7 || -> 1 half note and 2 quarter notes
Cmaj7 G/B Am7 Am/G || -> 4 quarter notes
Cmaj7 G/B C/Bb Am7 Am/G || -> 3 quarter notes and 2 eighth notes
Cmaj7 G/B Am7 Am/G Fmaj7 C/E || -> 2 quarter notes and 4 eighth notes
```
### Slashes
To indicate rhythm more precisely you can use slashes `/`. A slash is a placeholder for a chord in the rhythm, without an acutal chord change. Make sure to have a space before and after, to avoid confusion with bass notes (i.e. `C / B |` is not the same as `C/B |`). Examples:
```
Cmaj7 / / Fmaj7 || -> The first chord has a duration of3 quraters, and the last just 1 quarter
Cmaj7 / Dm7 G7 || -> 1 half note and 2 quarter notes
Cmaj7 Dm7 C/E / || -> 2 quarter notes and 1 half note\
```


## Line
A line consists of multiple bars seperated by barlines, and ending with a barline.
- Barline: `|`, `||`, `:||`
```
Bb/Ab | Gm6 Cm7b5/Gb ||
```

## Sheet
A sheet consists of multiple lines separated by a newline (`\n`). Example at the top (quick start section).


## Supported suffixes
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| 5 | sus2 | sus4 | 6 | ^ | ^7 |
| maj7 | ^9 | maj9 | ^11 | maj11 | ^13 |
| maj13 | 7 | 7,9 | 9 | 11 | 13 |
| 7b5 | 7b9 | 7#9 | 7,13 | 7add13 | b9b13 |
| 7b9b13 | 9,13 | 7,9,13 | 7b9,13 | b9,13 | 9b5 |
| 7,9b5 | 7,9b13 | 9b13 | \+ | aug | #5 |
| +7 | aug7 | 7#5 | +maj7 | +M7 | augM7 |
| +9 | aug9 | 9#5 | +#11 | +9#11 | aug#11 |
| aug9#11 | 9#11#5 | \- | m | -6 | m6 |
| -7 | m7 | -9 | m9 | -11 | m11 |
| -13 | m13 | -^ | -^7 | -maj | -maj7 |
| mmaj | mmaj7 | m^ | m^7 | -^9 | m^9 |
| -maj9 | mmaj9 | -^#11 | m^#11 | -maj#11 | mmaj#11 |
| -^#11,13 | m^#11,13 | -maj#11,13 | mmaj#11,13 | dim | mb5 |
| -b5 | dim7 | o | o7 | m7b5 | -7b5 |
| ø | ø7 | ømaj7 | mmaj7b5 | -maj7b5 | -^7b5 |
| m^7b5 | ø^7 | | | | |

## More info
- [Grammer file](./txt2musicxml/grammer/Chords.g4) (antlr4)
- [More examples](./examples/)