grammar Chords;

sheet: line+ EOF;
line: NEWLINE? bar+;
bar:
	WHITESPACE? chord (WHITESPACE chord)* WHITESPACE? BARLINE; // WHITESPACE? timeSignature? 
chord: root | root suffix | root bass | root suffix bass;
root: note alteration?;
bass: SLASH note alteration?;
note: NOTE;
alteration: ALTERATION;
// timeSignature: DIGITS COLON DIGITS;
suffix: SUFFIX;
NOTE: [A-G];
ALTERATION: 'b'+ | '#'+;
SUFFIX: ([15679^admosø+\-] | '#5') [0-9abdgijmosuø^#+,\-]*;
SLASH: '/';
COLON: ':';
BARLINE: '|';
NEWLINE: ('\r'? '\n')+;
WHITESPACE: [ \t]+;
// DIGITS: [0-9]+;