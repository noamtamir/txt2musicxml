// Generated from /Users/noamtamir/coding/txt2musicxml/txt2musicxml/grammer/Chords.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class ChordsLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		MEASURE_REPEAT=1, REHEARSAL=2, NOTE=3, ALTERATION=4, TIME_SIGNATURE=5, 
		SUFFIX=6, SLASH=7, REPEAT_BARLINE=8, DOUBLE_BARLINE=9, BARLINE=10, NEWLINE=11, 
		WHITESPACE=12;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"MEASURE_REPEAT", "REHEARSAL", "NOTE", "ALTERATION", "TIME_SIGNATURE", 
			"SUFFIX", "SLASH", "REPEAT_BARLINE", "DOUBLE_BARLINE", "BARLINE", "NEWLINE", 
			"WHITESPACE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'%'", null, null, null, null, null, "'/'", "':||'", "'||'", "'|'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "MEASURE_REPEAT", "REHEARSAL", "NOTE", "ALTERATION", "TIME_SIGNATURE", 
			"SUFFIX", "SLASH", "REPEAT_BARLINE", "DOUBLE_BARLINE", "BARLINE", "NEWLINE", 
			"WHITESPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public ChordsLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Chords.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\f_\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0004\u0001"+
		"\u001e\b\u0001\u000b\u0001\f\u0001\u001f\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0004\u0003\'\b\u0003\u000b\u0003\f\u0003"+
		"(\u0001\u0003\u0004\u0003,\b\u0003\u000b\u0003\f\u0003-\u0003\u00030\b"+
		"\u0003\u0001\u0004\u0004\u00043\b\u0004\u000b\u0004\f\u00044\u0001\u0004"+
		"\u0001\u0004\u0004\u00049\b\u0004\u000b\u0004\f\u0004:\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0003\u0005@\b\u0005\u0001\u0005\u0005\u0005C\b\u0005"+
		"\n\u0005\f\u0005F\t\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001"+
		"\n\u0003\nT\b\n\u0001\n\u0004\nW\b\n\u000b\n\f\nX\u0001\u000b\u0004\u000b"+
		"\\\b\u000b\u000b\u000b\f\u000b]\u0000\u0000\f\u0001\u0001\u0003\u0002"+
		"\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013"+
		"\n\u0015\u000b\u0017\f\u0001\u0000\u0006\u0004\u0000  09AZaz\u0001\u0000"+
		"AG\u0001\u000009\f\u0000++--115799^^aaddmmooss\u00f8\u00f8\r\u0000##+"+
		"-09^^abddggijmmoossuu\u00f8\u00f8\u0002\u0000\t\t  i\u0000\u0001\u0001"+
		"\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001"+
		"\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000"+
		"\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000"+
		"\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000"+
		"\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000"+
		"\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0001\u0019\u0001\u0000\u0000"+
		"\u0000\u0003\u001b\u0001\u0000\u0000\u0000\u0005#\u0001\u0000\u0000\u0000"+
		"\u0007/\u0001\u0000\u0000\u0000\t2\u0001\u0000\u0000\u0000\u000b?\u0001"+
		"\u0000\u0000\u0000\rG\u0001\u0000\u0000\u0000\u000fI\u0001\u0000\u0000"+
		"\u0000\u0011M\u0001\u0000\u0000\u0000\u0013P\u0001\u0000\u0000\u0000\u0015"+
		"V\u0001\u0000\u0000\u0000\u0017[\u0001\u0000\u0000\u0000\u0019\u001a\u0005"+
		"%\u0000\u0000\u001a\u0002\u0001\u0000\u0000\u0000\u001b\u001d\u0005[\u0000"+
		"\u0000\u001c\u001e\u0007\u0000\u0000\u0000\u001d\u001c\u0001\u0000\u0000"+
		"\u0000\u001e\u001f\u0001\u0000\u0000\u0000\u001f\u001d\u0001\u0000\u0000"+
		"\u0000\u001f \u0001\u0000\u0000\u0000 !\u0001\u0000\u0000\u0000!\"\u0005"+
		"]\u0000\u0000\"\u0004\u0001\u0000\u0000\u0000#$\u0007\u0001\u0000\u0000"+
		"$\u0006\u0001\u0000\u0000\u0000%\'\u0005b\u0000\u0000&%\u0001\u0000\u0000"+
		"\u0000\'(\u0001\u0000\u0000\u0000(&\u0001\u0000\u0000\u0000()\u0001\u0000"+
		"\u0000\u0000)0\u0001\u0000\u0000\u0000*,\u0005#\u0000\u0000+*\u0001\u0000"+
		"\u0000\u0000,-\u0001\u0000\u0000\u0000-+\u0001\u0000\u0000\u0000-.\u0001"+
		"\u0000\u0000\u0000.0\u0001\u0000\u0000\u0000/&\u0001\u0000\u0000\u0000"+
		"/+\u0001\u0000\u0000\u00000\b\u0001\u0000\u0000\u000013\u0007\u0002\u0000"+
		"\u000021\u0001\u0000\u0000\u000034\u0001\u0000\u0000\u000042\u0001\u0000"+
		"\u0000\u000045\u0001\u0000\u0000\u000056\u0001\u0000\u0000\u000068\u0005"+
		"/\u0000\u000079\u0007\u0002\u0000\u000087\u0001\u0000\u0000\u00009:\u0001"+
		"\u0000\u0000\u0000:8\u0001\u0000\u0000\u0000:;\u0001\u0000\u0000\u0000"+
		";\n\u0001\u0000\u0000\u0000<@\u0007\u0003\u0000\u0000=>\u0005#\u0000\u0000"+
		">@\u00055\u0000\u0000?<\u0001\u0000\u0000\u0000?=\u0001\u0000\u0000\u0000"+
		"@D\u0001\u0000\u0000\u0000AC\u0007\u0004\u0000\u0000BA\u0001\u0000\u0000"+
		"\u0000CF\u0001\u0000\u0000\u0000DB\u0001\u0000\u0000\u0000DE\u0001\u0000"+
		"\u0000\u0000E\f\u0001\u0000\u0000\u0000FD\u0001\u0000\u0000\u0000GH\u0005"+
		"/\u0000\u0000H\u000e\u0001\u0000\u0000\u0000IJ\u0005:\u0000\u0000JK\u0005"+
		"|\u0000\u0000KL\u0005|\u0000\u0000L\u0010\u0001\u0000\u0000\u0000MN\u0005"+
		"|\u0000\u0000NO\u0005|\u0000\u0000O\u0012\u0001\u0000\u0000\u0000PQ\u0005"+
		"|\u0000\u0000Q\u0014\u0001\u0000\u0000\u0000RT\u0005\r\u0000\u0000SR\u0001"+
		"\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000TU\u0001\u0000\u0000\u0000"+
		"UW\u0005\n\u0000\u0000VS\u0001\u0000\u0000\u0000WX\u0001\u0000\u0000\u0000"+
		"XV\u0001\u0000\u0000\u0000XY\u0001\u0000\u0000\u0000Y\u0016\u0001\u0000"+
		"\u0000\u0000Z\\\u0007\u0005\u0000\u0000[Z\u0001\u0000\u0000\u0000\\]\u0001"+
		"\u0000\u0000\u0000][\u0001\u0000\u0000\u0000]^\u0001\u0000\u0000\u0000"+
		"^\u0018\u0001\u0000\u0000\u0000\f\u0000\u001f(-/4:?DSX]\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}