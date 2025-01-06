grammar Chords;

sheet: line+ EOF;
line: NEWLINE? bar+;
bar:
	((WHITESPACE? (TIME_SIGNATURE WHITESPACE)? chord_or_slash (WHITESPACE chord_or_slash)* WHITESPACE?) | (WHITESPACE? MEASURE_REPEAT WHITESPACE?)) right_barlines; // WHITESPACE? timeSignature? 
chord_or_slash: chord | slash;
chord: root | root suffix | root bass | root suffix bass;
slash: SLASH;
root: note alteration?;
bass: SLASH note alteration?;
note: NOTE;
alteration: ALTERATION;
suffix: SUFFIX;
right_barlines: BARLINE | DOUBLE_BARLINE | REPEAT_BARLINE;
MEASURE_REPEAT: '%';
NOTE: [A-G];
ALTERATION: 'b'+ | '#'+;
TIME_SIGNATURE: [0-9]+ '/' [0-9]+;
SUFFIX: ([15679^admosø+\-] | '#5') [0-9abdgijmosuø^#+,\-]*;
SLASH: '/';
REPEAT_BARLINE: ':||';
DOUBLE_BARLINE: '||';
BARLINE: '|';
NEWLINE: ('\r'? '\n')+;
WHITESPACE: [ \t]+;