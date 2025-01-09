grammar FrontMatter;

front_matter: title_author EOF;
title_author: title '-' author;
title: ANY_STRING;
author: ANY_STRING;
ANY_STRING: ~[\r\n\-]+;
// NEWLINE: ('\r'? '\n')+;
// WHITESPACE: [ \t]+;