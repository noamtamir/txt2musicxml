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
		SUFFIX=6, SLASH=7, DOUBLE_SIDED_REPEAT_BARLINE=8, FORWARD_REPEAT_BARLINE=9, 
		REPEAT_BARLINE=10, DOUBLE_BARLINE=11, BARLINE=12, NEWLINE=13, WHITESPACE=14;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"MEASURE_REPEAT", "REHEARSAL", "NOTE", "ALTERATION", "TIME_SIGNATURE", 
			"SUFFIX", "SLASH", "DOUBLE_SIDED_REPEAT_BARLINE", "FORWARD_REPEAT_BARLINE", 
			"REPEAT_BARLINE", "DOUBLE_BARLINE", "BARLINE", "NEWLINE", "WHITESPACE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'%'", null, null, null, null, null, "'/'", "':||:'", "'||:'", 
			"':||'", "'||'", "'|'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "MEASURE_REPEAT", "REHEARSAL", "NOTE", "ALTERATION", "TIME_SIGNATURE", 
			"SUFFIX", "SLASH", "DOUBLE_SIDED_REPEAT_BARLINE", "FORWARD_REPEAT_BARLINE", 
			"REPEAT_BARLINE", "DOUBLE_BARLINE", "BARLINE", "NEWLINE", "WHITESPACE"
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
		"\u0004\u0000\u000el\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0004\u0001\"\b\u0001\u000b\u0001\f\u0001#\u0001\u0001"+
		"\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0004\u0003+\b\u0003"+
		"\u000b\u0003\f\u0003,\u0001\u0003\u0004\u00030\b\u0003\u000b\u0003\f\u0003"+
		"1\u0003\u00034\b\u0003\u0001\u0004\u0004\u00047\b\u0004\u000b\u0004\f"+
		"\u00048\u0001\u0004\u0001\u0004\u0004\u0004=\b\u0004\u000b\u0004\f\u0004"+
		">\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005D\b\u0005\u0001\u0005"+
		"\u0005\u0005G\b\u0005\n\u0005\f\u0005J\t\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\u000b\u0001\u000b\u0001\f\u0003\fa\b\f\u0001\f\u0004\fd\b\f\u000b"+
		"\f\f\fe\u0001\r\u0004\ri\b\r\u000b\r\f\rj\u0000\u0000\u000e\u0001\u0001"+
		"\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f"+
		"\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u0001\u0000"+
		"\u0006\u0004\u0000  09AZaz\u0001\u0000AG\u0001\u000009\f\u0000++--115"+
		"799^^aaddmmooss\u00f8\u00f8\r\u0000##+-09^^abddggijmmoossuu\u00f8\u00f8"+
		"\u0002\u0000\t\t  v\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001"+
		"\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001"+
		"\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000"+
		"\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000"+
		"\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000"+
		"\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000"+
		"\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000"+
		"\u0000\u0001\u001d\u0001\u0000\u0000\u0000\u0003\u001f\u0001\u0000\u0000"+
		"\u0000\u0005\'\u0001\u0000\u0000\u0000\u00073\u0001\u0000\u0000\u0000"+
		"\t6\u0001\u0000\u0000\u0000\u000bC\u0001\u0000\u0000\u0000\rK\u0001\u0000"+
		"\u0000\u0000\u000fM\u0001\u0000\u0000\u0000\u0011R\u0001\u0000\u0000\u0000"+
		"\u0013V\u0001\u0000\u0000\u0000\u0015Z\u0001\u0000\u0000\u0000\u0017]"+
		"\u0001\u0000\u0000\u0000\u0019c\u0001\u0000\u0000\u0000\u001bh\u0001\u0000"+
		"\u0000\u0000\u001d\u001e\u0005%\u0000\u0000\u001e\u0002\u0001\u0000\u0000"+
		"\u0000\u001f!\u0005[\u0000\u0000 \"\u0007\u0000\u0000\u0000! \u0001\u0000"+
		"\u0000\u0000\"#\u0001\u0000\u0000\u0000#!\u0001\u0000\u0000\u0000#$\u0001"+
		"\u0000\u0000\u0000$%\u0001\u0000\u0000\u0000%&\u0005]\u0000\u0000&\u0004"+
		"\u0001\u0000\u0000\u0000\'(\u0007\u0001\u0000\u0000(\u0006\u0001\u0000"+
		"\u0000\u0000)+\u0005b\u0000\u0000*)\u0001\u0000\u0000\u0000+,\u0001\u0000"+
		"\u0000\u0000,*\u0001\u0000\u0000\u0000,-\u0001\u0000\u0000\u0000-4\u0001"+
		"\u0000\u0000\u0000.0\u0005#\u0000\u0000/.\u0001\u0000\u0000\u000001\u0001"+
		"\u0000\u0000\u00001/\u0001\u0000\u0000\u000012\u0001\u0000\u0000\u0000"+
		"24\u0001\u0000\u0000\u00003*\u0001\u0000\u0000\u00003/\u0001\u0000\u0000"+
		"\u00004\b\u0001\u0000\u0000\u000057\u0007\u0002\u0000\u000065\u0001\u0000"+
		"\u0000\u000078\u0001\u0000\u0000\u000086\u0001\u0000\u0000\u000089\u0001"+
		"\u0000\u0000\u00009:\u0001\u0000\u0000\u0000:<\u0005/\u0000\u0000;=\u0007"+
		"\u0002\u0000\u0000<;\u0001\u0000\u0000\u0000=>\u0001\u0000\u0000\u0000"+
		"><\u0001\u0000\u0000\u0000>?\u0001\u0000\u0000\u0000?\n\u0001\u0000\u0000"+
		"\u0000@D\u0007\u0003\u0000\u0000AB\u0005#\u0000\u0000BD\u00055\u0000\u0000"+
		"C@\u0001\u0000\u0000\u0000CA\u0001\u0000\u0000\u0000DH\u0001\u0000\u0000"+
		"\u0000EG\u0007\u0004\u0000\u0000FE\u0001\u0000\u0000\u0000GJ\u0001\u0000"+
		"\u0000\u0000HF\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000\u0000I\f\u0001"+
		"\u0000\u0000\u0000JH\u0001\u0000\u0000\u0000KL\u0005/\u0000\u0000L\u000e"+
		"\u0001\u0000\u0000\u0000MN\u0005:\u0000\u0000NO\u0005|\u0000\u0000OP\u0005"+
		"|\u0000\u0000PQ\u0005:\u0000\u0000Q\u0010\u0001\u0000\u0000\u0000RS\u0005"+
		"|\u0000\u0000ST\u0005|\u0000\u0000TU\u0005:\u0000\u0000U\u0012\u0001\u0000"+
		"\u0000\u0000VW\u0005:\u0000\u0000WX\u0005|\u0000\u0000XY\u0005|\u0000"+
		"\u0000Y\u0014\u0001\u0000\u0000\u0000Z[\u0005|\u0000\u0000[\\\u0005|\u0000"+
		"\u0000\\\u0016\u0001\u0000\u0000\u0000]^\u0005|\u0000\u0000^\u0018\u0001"+
		"\u0000\u0000\u0000_a\u0005\r\u0000\u0000`_\u0001\u0000\u0000\u0000`a\u0001"+
		"\u0000\u0000\u0000ab\u0001\u0000\u0000\u0000bd\u0005\n\u0000\u0000c`\u0001"+
		"\u0000\u0000\u0000de\u0001\u0000\u0000\u0000ec\u0001\u0000\u0000\u0000"+
		"ef\u0001\u0000\u0000\u0000f\u001a\u0001\u0000\u0000\u0000gi\u0007\u0005"+
		"\u0000\u0000hg\u0001\u0000\u0000\u0000ij\u0001\u0000\u0000\u0000jh\u0001"+
		"\u0000\u0000\u0000jk\u0001\u0000\u0000\u0000k\u001c\u0001\u0000\u0000"+
		"\u0000\f\u0000#,138>CH`ej\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}