// Generated from /Users/noamtamir/coding/txt2musicxml/txt2musicxml/grammer/Chords.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ChordsParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		MEASURE_REPEAT=1, REHEARSAL=2, NOTE=3, ALTERATION=4, TIME_SIGNATURE=5, 
		SUFFIX=6, SLASH=7, REPEAT_BARLINE=8, DOUBLE_BARLINE=9, BARLINE=10, NEWLINE=11, 
		WHITESPACE=12;
	public static final int
		RULE_sheet = 0, RULE_line = 1, RULE_bar = 2, RULE_chord_or_slash = 3, 
		RULE_chord = 4, RULE_slash = 5, RULE_root = 6, RULE_bass = 7, RULE_note = 8, 
		RULE_alteration = 9, RULE_suffix = 10, RULE_right_barlines = 11;
	private static String[] makeRuleNames() {
		return new String[] {
			"sheet", "line", "bar", "chord_or_slash", "chord", "slash", "root", "bass", 
			"note", "alteration", "suffix", "right_barlines"
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

	@Override
	public String getGrammarFileName() { return "Chords.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ChordsParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SheetContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(ChordsParser.EOF, 0); }
		public List<LineContext> line() {
			return getRuleContexts(LineContext.class);
		}
		public LineContext line(int i) {
			return getRuleContext(LineContext.class,i);
		}
		public SheetContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sheet; }
	}

	public final SheetContext sheet() throws RecognitionException {
		SheetContext _localctx = new SheetContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_sheet);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(25); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(24);
				line();
				}
				}
				setState(27); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 6334L) != 0) );
			setState(29);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LineContext extends ParserRuleContext {
		public TerminalNode NEWLINE() { return getToken(ChordsParser.NEWLINE, 0); }
		public List<BarContext> bar() {
			return getRuleContexts(BarContext.class);
		}
		public BarContext bar(int i) {
			return getRuleContext(BarContext.class,i);
		}
		public LineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_line; }
	}

	public final LineContext line() throws RecognitionException {
		LineContext _localctx = new LineContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_line);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NEWLINE) {
				{
				setState(31);
				match(NEWLINE);
				}
			}

			setState(35); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(34);
					bar();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(37); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BarContext extends ParserRuleContext {
		public Right_barlinesContext right_barlines() {
			return getRuleContext(Right_barlinesContext.class,0);
		}
		public List<Chord_or_slashContext> chord_or_slash() {
			return getRuleContexts(Chord_or_slashContext.class);
		}
		public Chord_or_slashContext chord_or_slash(int i) {
			return getRuleContext(Chord_or_slashContext.class,i);
		}
		public TerminalNode MEASURE_REPEAT() { return getToken(ChordsParser.MEASURE_REPEAT, 0); }
		public List<TerminalNode> WHITESPACE() { return getTokens(ChordsParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(ChordsParser.WHITESPACE, i);
		}
		public TerminalNode REHEARSAL() { return getToken(ChordsParser.REHEARSAL, 0); }
		public AlterationContext alteration() {
			return getRuleContext(AlterationContext.class,0);
		}
		public TerminalNode TIME_SIGNATURE() { return getToken(ChordsParser.TIME_SIGNATURE, 0); }
		public BarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bar; }
	}

	public final BarContext bar() throws RecognitionException {
		BarContext _localctx = new BarContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_bar);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(73);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				{
				setState(40);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WHITESPACE) {
					{
					setState(39);
					match(WHITESPACE);
					}
				}

				setState(44);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==REHEARSAL) {
					{
					setState(42);
					match(REHEARSAL);
					setState(43);
					match(WHITESPACE);
					}
				}

				setState(49);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ALTERATION) {
					{
					setState(46);
					alteration();
					setState(47);
					match(WHITESPACE);
					}
				}

				setState(53);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==TIME_SIGNATURE) {
					{
					setState(51);
					match(TIME_SIGNATURE);
					setState(52);
					match(WHITESPACE);
					}
				}

				setState(55);
				chord_or_slash();
				setState(60);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(56);
						match(WHITESPACE);
						setState(57);
						chord_or_slash();
						}
						} 
					}
					setState(62);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
				}
				setState(64);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WHITESPACE) {
					{
					setState(63);
					match(WHITESPACE);
					}
				}

				}
				}
				break;
			case 2:
				{
				{
				setState(67);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WHITESPACE) {
					{
					setState(66);
					match(WHITESPACE);
					}
				}

				setState(69);
				match(MEASURE_REPEAT);
				setState(71);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WHITESPACE) {
					{
					setState(70);
					match(WHITESPACE);
					}
				}

				}
				}
				break;
			}
			setState(75);
			right_barlines();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Chord_or_slashContext extends ParserRuleContext {
		public ChordContext chord() {
			return getRuleContext(ChordContext.class,0);
		}
		public SlashContext slash() {
			return getRuleContext(SlashContext.class,0);
		}
		public Chord_or_slashContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_chord_or_slash; }
	}

	public final Chord_or_slashContext chord_or_slash() throws RecognitionException {
		Chord_or_slashContext _localctx = new Chord_or_slashContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_chord_or_slash);
		try {
			setState(79);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOTE:
				enterOuterAlt(_localctx, 1);
				{
				setState(77);
				chord();
				}
				break;
			case SLASH:
				enterOuterAlt(_localctx, 2);
				{
				setState(78);
				slash();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ChordContext extends ParserRuleContext {
		public RootContext root() {
			return getRuleContext(RootContext.class,0);
		}
		public SuffixContext suffix() {
			return getRuleContext(SuffixContext.class,0);
		}
		public BassContext bass() {
			return getRuleContext(BassContext.class,0);
		}
		public ChordContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_chord; }
	}

	public final ChordContext chord() throws RecognitionException {
		ChordContext _localctx = new ChordContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_chord);
		try {
			setState(92);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(81);
				root();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(82);
				root();
				setState(83);
				suffix();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(85);
				root();
				setState(86);
				bass();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(88);
				root();
				setState(89);
				suffix();
				setState(90);
				bass();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SlashContext extends ParserRuleContext {
		public TerminalNode SLASH() { return getToken(ChordsParser.SLASH, 0); }
		public SlashContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_slash; }
	}

	public final SlashContext slash() throws RecognitionException {
		SlashContext _localctx = new SlashContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_slash);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			match(SLASH);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RootContext extends ParserRuleContext {
		public NoteContext note() {
			return getRuleContext(NoteContext.class,0);
		}
		public AlterationContext alteration() {
			return getRuleContext(AlterationContext.class,0);
		}
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_root);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			note();
			setState(98);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ALTERATION) {
				{
				setState(97);
				alteration();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BassContext extends ParserRuleContext {
		public TerminalNode SLASH() { return getToken(ChordsParser.SLASH, 0); }
		public NoteContext note() {
			return getRuleContext(NoteContext.class,0);
		}
		public AlterationContext alteration() {
			return getRuleContext(AlterationContext.class,0);
		}
		public BassContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bass; }
	}

	public final BassContext bass() throws RecognitionException {
		BassContext _localctx = new BassContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_bass);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(100);
			match(SLASH);
			setState(101);
			note();
			setState(103);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ALTERATION) {
				{
				setState(102);
				alteration();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NoteContext extends ParserRuleContext {
		public TerminalNode NOTE() { return getToken(ChordsParser.NOTE, 0); }
		public NoteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_note; }
	}

	public final NoteContext note() throws RecognitionException {
		NoteContext _localctx = new NoteContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_note);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			match(NOTE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AlterationContext extends ParserRuleContext {
		public TerminalNode ALTERATION() { return getToken(ChordsParser.ALTERATION, 0); }
		public AlterationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_alteration; }
	}

	public final AlterationContext alteration() throws RecognitionException {
		AlterationContext _localctx = new AlterationContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_alteration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			match(ALTERATION);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SuffixContext extends ParserRuleContext {
		public TerminalNode SUFFIX() { return getToken(ChordsParser.SUFFIX, 0); }
		public SuffixContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_suffix; }
	}

	public final SuffixContext suffix() throws RecognitionException {
		SuffixContext _localctx = new SuffixContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_suffix);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			match(SUFFIX);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Right_barlinesContext extends ParserRuleContext {
		public TerminalNode BARLINE() { return getToken(ChordsParser.BARLINE, 0); }
		public TerminalNode DOUBLE_BARLINE() { return getToken(ChordsParser.DOUBLE_BARLINE, 0); }
		public TerminalNode REPEAT_BARLINE() { return getToken(ChordsParser.REPEAT_BARLINE, 0); }
		public Right_barlinesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_right_barlines; }
	}

	public final Right_barlinesContext right_barlines() throws RecognitionException {
		Right_barlinesContext _localctx = new Right_barlinesContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_right_barlines);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1792L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\fr\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0001"+
		"\u0000\u0004\u0000\u001a\b\u0000\u000b\u0000\f\u0000\u001b\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0003\u0001!\b\u0001\u0001\u0001\u0004\u0001"+
		"$\b\u0001\u000b\u0001\f\u0001%\u0001\u0002\u0003\u0002)\b\u0002\u0001"+
		"\u0002\u0001\u0002\u0003\u0002-\b\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0003\u00022\b\u0002\u0001\u0002\u0001\u0002\u0003\u00026\b\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u0002;\b\u0002\n\u0002\f\u0002"+
		">\t\u0002\u0001\u0002\u0003\u0002A\b\u0002\u0001\u0002\u0003\u0002D\b"+
		"\u0002\u0001\u0002\u0001\u0002\u0003\u0002H\b\u0002\u0003\u0002J\b\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0003\u0003P\b\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004"+
		"]\b\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0003\u0006"+
		"c\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007h\b\u0007\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0000\u0000\f\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0000\u0001\u0001\u0000\b\nw\u0000\u0019\u0001\u0000\u0000\u0000"+
		"\u0002 \u0001\u0000\u0000\u0000\u0004I\u0001\u0000\u0000\u0000\u0006O"+
		"\u0001\u0000\u0000\u0000\b\\\u0001\u0000\u0000\u0000\n^\u0001\u0000\u0000"+
		"\u0000\f`\u0001\u0000\u0000\u0000\u000ed\u0001\u0000\u0000\u0000\u0010"+
		"i\u0001\u0000\u0000\u0000\u0012k\u0001\u0000\u0000\u0000\u0014m\u0001"+
		"\u0000\u0000\u0000\u0016o\u0001\u0000\u0000\u0000\u0018\u001a\u0003\u0002"+
		"\u0001\u0000\u0019\u0018\u0001\u0000\u0000\u0000\u001a\u001b\u0001\u0000"+
		"\u0000\u0000\u001b\u0019\u0001\u0000\u0000\u0000\u001b\u001c\u0001\u0000"+
		"\u0000\u0000\u001c\u001d\u0001\u0000\u0000\u0000\u001d\u001e\u0005\u0000"+
		"\u0000\u0001\u001e\u0001\u0001\u0000\u0000\u0000\u001f!\u0005\u000b\u0000"+
		"\u0000 \u001f\u0001\u0000\u0000\u0000 !\u0001\u0000\u0000\u0000!#\u0001"+
		"\u0000\u0000\u0000\"$\u0003\u0004\u0002\u0000#\"\u0001\u0000\u0000\u0000"+
		"$%\u0001\u0000\u0000\u0000%#\u0001\u0000\u0000\u0000%&\u0001\u0000\u0000"+
		"\u0000&\u0003\u0001\u0000\u0000\u0000\')\u0005\f\u0000\u0000(\'\u0001"+
		"\u0000\u0000\u0000()\u0001\u0000\u0000\u0000),\u0001\u0000\u0000\u0000"+
		"*+\u0005\u0002\u0000\u0000+-\u0005\f\u0000\u0000,*\u0001\u0000\u0000\u0000"+
		",-\u0001\u0000\u0000\u0000-1\u0001\u0000\u0000\u0000./\u0003\u0012\t\u0000"+
		"/0\u0005\f\u0000\u000002\u0001\u0000\u0000\u00001.\u0001\u0000\u0000\u0000"+
		"12\u0001\u0000\u0000\u000025\u0001\u0000\u0000\u000034\u0005\u0005\u0000"+
		"\u000046\u0005\f\u0000\u000053\u0001\u0000\u0000\u000056\u0001\u0000\u0000"+
		"\u000067\u0001\u0000\u0000\u00007<\u0003\u0006\u0003\u000089\u0005\f\u0000"+
		"\u00009;\u0003\u0006\u0003\u0000:8\u0001\u0000\u0000\u0000;>\u0001\u0000"+
		"\u0000\u0000<:\u0001\u0000\u0000\u0000<=\u0001\u0000\u0000\u0000=@\u0001"+
		"\u0000\u0000\u0000><\u0001\u0000\u0000\u0000?A\u0005\f\u0000\u0000@?\u0001"+
		"\u0000\u0000\u0000@A\u0001\u0000\u0000\u0000AJ\u0001\u0000\u0000\u0000"+
		"BD\u0005\f\u0000\u0000CB\u0001\u0000\u0000\u0000CD\u0001\u0000\u0000\u0000"+
		"DE\u0001\u0000\u0000\u0000EG\u0005\u0001\u0000\u0000FH\u0005\f\u0000\u0000"+
		"GF\u0001\u0000\u0000\u0000GH\u0001\u0000\u0000\u0000HJ\u0001\u0000\u0000"+
		"\u0000I(\u0001\u0000\u0000\u0000IC\u0001\u0000\u0000\u0000JK\u0001\u0000"+
		"\u0000\u0000KL\u0003\u0016\u000b\u0000L\u0005\u0001\u0000\u0000\u0000"+
		"MP\u0003\b\u0004\u0000NP\u0003\n\u0005\u0000OM\u0001\u0000\u0000\u0000"+
		"ON\u0001\u0000\u0000\u0000P\u0007\u0001\u0000\u0000\u0000Q]\u0003\f\u0006"+
		"\u0000RS\u0003\f\u0006\u0000ST\u0003\u0014\n\u0000T]\u0001\u0000\u0000"+
		"\u0000UV\u0003\f\u0006\u0000VW\u0003\u000e\u0007\u0000W]\u0001\u0000\u0000"+
		"\u0000XY\u0003\f\u0006\u0000YZ\u0003\u0014\n\u0000Z[\u0003\u000e\u0007"+
		"\u0000[]\u0001\u0000\u0000\u0000\\Q\u0001\u0000\u0000\u0000\\R\u0001\u0000"+
		"\u0000\u0000\\U\u0001\u0000\u0000\u0000\\X\u0001\u0000\u0000\u0000]\t"+
		"\u0001\u0000\u0000\u0000^_\u0005\u0007\u0000\u0000_\u000b\u0001\u0000"+
		"\u0000\u0000`b\u0003\u0010\b\u0000ac\u0003\u0012\t\u0000ba\u0001\u0000"+
		"\u0000\u0000bc\u0001\u0000\u0000\u0000c\r\u0001\u0000\u0000\u0000de\u0005"+
		"\u0007\u0000\u0000eg\u0003\u0010\b\u0000fh\u0003\u0012\t\u0000gf\u0001"+
		"\u0000\u0000\u0000gh\u0001\u0000\u0000\u0000h\u000f\u0001\u0000\u0000"+
		"\u0000ij\u0005\u0003\u0000\u0000j\u0011\u0001\u0000\u0000\u0000kl\u0005"+
		"\u0004\u0000\u0000l\u0013\u0001\u0000\u0000\u0000mn\u0005\u0006\u0000"+
		"\u0000n\u0015\u0001\u0000\u0000\u0000op\u0007\u0000\u0000\u0000p\u0017"+
		"\u0001\u0000\u0000\u0000\u0010\u001b %(,15<@CGIO\\bg";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}