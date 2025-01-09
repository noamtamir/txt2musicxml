// Generated from /Users/noamtamir/coding/txt2musicxml/txt2musicxml/grammer/FrontMatter.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class FrontMatterParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, ANY_STRING=2;
	public static final int
		RULE_front_matter = 0, RULE_title_author = 1, RULE_title = 2, RULE_author = 3;
	private static String[] makeRuleNames() {
		return new String[] {
			"front_matter", "title_author", "title", "author"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'-'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, "ANY_STRING"
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
	public String getGrammarFileName() { return "FrontMatter.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public FrontMatterParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Front_matterContext extends ParserRuleContext {
		public Title_authorContext title_author() {
			return getRuleContext(Title_authorContext.class,0);
		}
		public TerminalNode EOF() { return getToken(FrontMatterParser.EOF, 0); }
		public Front_matterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_front_matter; }
	}

	public final Front_matterContext front_matter() throws RecognitionException {
		Front_matterContext _localctx = new Front_matterContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_front_matter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(8);
			title_author();
			setState(9);
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
	public static class Title_authorContext extends ParserRuleContext {
		public TitleContext title() {
			return getRuleContext(TitleContext.class,0);
		}
		public AuthorContext author() {
			return getRuleContext(AuthorContext.class,0);
		}
		public Title_authorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_title_author; }
	}

	public final Title_authorContext title_author() throws RecognitionException {
		Title_authorContext _localctx = new Title_authorContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_title_author);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(11);
			title();
			setState(12);
			match(T__0);
			setState(13);
			author();
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
	public static class TitleContext extends ParserRuleContext {
		public TerminalNode ANY_STRING() { return getToken(FrontMatterParser.ANY_STRING, 0); }
		public TitleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_title; }
	}

	public final TitleContext title() throws RecognitionException {
		TitleContext _localctx = new TitleContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_title);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(15);
			match(ANY_STRING);
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
	public static class AuthorContext extends ParserRuleContext {
		public TerminalNode ANY_STRING() { return getToken(FrontMatterParser.ANY_STRING, 0); }
		public AuthorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_author; }
	}

	public final AuthorContext author() throws RecognitionException {
		AuthorContext _localctx = new AuthorContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_author);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(17);
			match(ANY_STRING);
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
		"\u0004\u0001\u0002\u0014\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0000\u0000\u0004\u0000"+
		"\u0002\u0004\u0006\u0000\u0000\u000f\u0000\b\u0001\u0000\u0000\u0000\u0002"+
		"\u000b\u0001\u0000\u0000\u0000\u0004\u000f\u0001\u0000\u0000\u0000\u0006"+
		"\u0011\u0001\u0000\u0000\u0000\b\t\u0003\u0002\u0001\u0000\t\n\u0005\u0000"+
		"\u0000\u0001\n\u0001\u0001\u0000\u0000\u0000\u000b\f\u0003\u0004\u0002"+
		"\u0000\f\r\u0005\u0001\u0000\u0000\r\u000e\u0003\u0006\u0003\u0000\u000e"+
		"\u0003\u0001\u0000\u0000\u0000\u000f\u0010\u0005\u0002\u0000\u0000\u0010"+
		"\u0005\u0001\u0000\u0000\u0000\u0011\u0012\u0005\u0002\u0000\u0000\u0012"+
		"\u0007\u0001\u0000\u0000\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}