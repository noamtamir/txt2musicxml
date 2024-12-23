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
		MEASURE_REPEAT=1, NOTE=2, ALTERATION=3, SUFFIX=4, SLASH=5, COLON=6, BARLINE=7, 
		NEWLINE=8, WHITESPACE=9;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"MEASURE_REPEAT", "NOTE", "ALTERATION", "SUFFIX", "SLASH", "COLON", "BARLINE", 
			"NEWLINE", "WHITESPACE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'%'", null, null, null, "'/'", "':'", "'|'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "MEASURE_REPEAT", "NOTE", "ALTERATION", "SUFFIX", "SLASH", "COLON", 
			"BARLINE", "NEWLINE", "WHITESPACE"
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
		"\u0004\u0000\tA\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0002\u0004\u0002\u0019\b\u0002\u000b\u0002\f\u0002\u001a"+
		"\u0001\u0002\u0004\u0002\u001e\b\u0002\u000b\u0002\f\u0002\u001f\u0003"+
		"\u0002\"\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003\'\b\u0003"+
		"\u0001\u0003\u0005\u0003*\b\u0003\n\u0003\f\u0003-\t\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0003\u00076\b\u0007\u0001\u0007\u0004\u00079\b\u0007\u000b\u0007\f\u0007"+
		":\u0001\b\u0004\b>\b\b\u000b\b\f\b?\u0000\u0000\t\u0001\u0001\u0003\u0002"+
		"\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0001"+
		"\u0000\u0004\u0001\u0000AG\f\u0000++--115799^^aaddmmooss\u00f8\u00f8\r"+
		"\u0000##+-09^^abddggijmmoossuu\u00f8\u00f8\u0002\u0000\t\t  H\u0000\u0001"+
		"\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005"+
		"\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001"+
		"\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000"+
		"\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000"+
		"\u0000\u0000\u0001\u0013\u0001\u0000\u0000\u0000\u0003\u0015\u0001\u0000"+
		"\u0000\u0000\u0005!\u0001\u0000\u0000\u0000\u0007&\u0001\u0000\u0000\u0000"+
		"\t.\u0001\u0000\u0000\u0000\u000b0\u0001\u0000\u0000\u0000\r2\u0001\u0000"+
		"\u0000\u0000\u000f8\u0001\u0000\u0000\u0000\u0011=\u0001\u0000\u0000\u0000"+
		"\u0013\u0014\u0005%\u0000\u0000\u0014\u0002\u0001\u0000\u0000\u0000\u0015"+
		"\u0016\u0007\u0000\u0000\u0000\u0016\u0004\u0001\u0000\u0000\u0000\u0017"+
		"\u0019\u0005b\u0000\u0000\u0018\u0017\u0001\u0000\u0000\u0000\u0019\u001a"+
		"\u0001\u0000\u0000\u0000\u001a\u0018\u0001\u0000\u0000\u0000\u001a\u001b"+
		"\u0001\u0000\u0000\u0000\u001b\"\u0001\u0000\u0000\u0000\u001c\u001e\u0005"+
		"#\u0000\u0000\u001d\u001c\u0001\u0000\u0000\u0000\u001e\u001f\u0001\u0000"+
		"\u0000\u0000\u001f\u001d\u0001\u0000\u0000\u0000\u001f \u0001\u0000\u0000"+
		"\u0000 \"\u0001\u0000\u0000\u0000!\u0018\u0001\u0000\u0000\u0000!\u001d"+
		"\u0001\u0000\u0000\u0000\"\u0006\u0001\u0000\u0000\u0000#\'\u0007\u0001"+
		"\u0000\u0000$%\u0005#\u0000\u0000%\'\u00055\u0000\u0000&#\u0001\u0000"+
		"\u0000\u0000&$\u0001\u0000\u0000\u0000\'+\u0001\u0000\u0000\u0000(*\u0007"+
		"\u0002\u0000\u0000)(\u0001\u0000\u0000\u0000*-\u0001\u0000\u0000\u0000"+
		"+)\u0001\u0000\u0000\u0000+,\u0001\u0000\u0000\u0000,\b\u0001\u0000\u0000"+
		"\u0000-+\u0001\u0000\u0000\u0000./\u0005/\u0000\u0000/\n\u0001\u0000\u0000"+
		"\u000001\u0005:\u0000\u00001\f\u0001\u0000\u0000\u000023\u0005|\u0000"+
		"\u00003\u000e\u0001\u0000\u0000\u000046\u0005\r\u0000\u000054\u0001\u0000"+
		"\u0000\u000056\u0001\u0000\u0000\u000067\u0001\u0000\u0000\u000079\u0005"+
		"\n\u0000\u000085\u0001\u0000\u0000\u00009:\u0001\u0000\u0000\u0000:8\u0001"+
		"\u0000\u0000\u0000:;\u0001\u0000\u0000\u0000;\u0010\u0001\u0000\u0000"+
		"\u0000<>\u0007\u0003\u0000\u0000=<\u0001\u0000\u0000\u0000>?\u0001\u0000"+
		"\u0000\u0000?=\u0001\u0000\u0000\u0000?@\u0001\u0000\u0000\u0000@\u0012"+
		"\u0001\u0000\u0000\u0000\t\u0000\u001a\u001f!&+5:?\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}