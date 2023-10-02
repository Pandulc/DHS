// Generated from /home/gabriel/DHS/Proyecto/src/main/python/compiladores.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class compiladoresLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		EQ=1, EQQ=2, NE=3, LT=4, GT=5, LE=6, GE=7, PP=8, MM=9, PA=10, PC=11, LLA=12, 
		LLC=13, PYC=14, COMA=15, NUMERO=16, TDATO=17, WHILE=18, IF=19, FOR=20, 
		RETURN=21, ID=22, WS=23, OTRO=24;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"LETRA", "DIGITO", "EQ", "EQQ", "NE", "LT", "GT", "LE", "GE", "PP", "MM", 
			"PA", "PC", "LLA", "LLC", "PYC", "COMA", "NUMERO", "TDATO", "WHILE", 
			"IF", "FOR", "RETURN", "ID", "WS", "OTRO"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'++'", "'--'", 
			"'('", "')'", "'{'", "'}'", "';'", "','", null, null, "'while'", "'if'", 
			"'for'", "'return'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "EQ", "EQQ", "NE", "LT", "GT", "LE", "GE", "PP", "MM", "PA", "PC", 
			"LLA", "LLC", "PYC", "COMA", "NUMERO", "TDATO", "WHILE", "IF", "FOR", 
			"RETURN", "ID", "WS", "OTRO"
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


	public compiladoresLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "compiladores.g4"; }

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
		"\u0004\u0000\u0018\u0093\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017"+
		"\u0002\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\u000b"+
		"\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001"+
		"\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0011\u0004\u0011_\b"+
		"\u0011\u000b\u0011\f\u0011`\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0003"+
		"\u0012l\b\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0003"+
		"\u0017\u0084\b\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0005\u0017\u0089"+
		"\b\u0017\n\u0017\f\u0017\u008c\t\u0017\u0001\u0018\u0001\u0018\u0001\u0018"+
		"\u0001\u0018\u0001\u0019\u0001\u0019\u0000\u0000\u001a\u0001\u0000\u0003"+
		"\u0000\u0005\u0001\u0007\u0002\t\u0003\u000b\u0004\r\u0005\u000f\u0006"+
		"\u0011\u0007\u0013\b\u0015\t\u0017\n\u0019\u000b\u001b\f\u001d\r\u001f"+
		"\u000e!\u000f#\u0010%\u0011\'\u0012)\u0013+\u0014-\u0015/\u00161\u0017"+
		"3\u0018\u0001\u0000\u0003\u0002\u0000AZaz\u0001\u000009\u0003\u0000\t"+
		"\n\r\r  \u0096\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000"+
		"\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000"+
		"\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000"+
		"\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000"+
		"\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000"+
		"\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000"+
		"\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000"+
		"\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%"+
		"\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001"+
		"\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000"+
		"\u0000\u0000/\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u0000"+
		"3\u0001\u0000\u0000\u0000\u00015\u0001\u0000\u0000\u0000\u00037\u0001"+
		"\u0000\u0000\u0000\u00059\u0001\u0000\u0000\u0000\u0007;\u0001\u0000\u0000"+
		"\u0000\t>\u0001\u0000\u0000\u0000\u000bA\u0001\u0000\u0000\u0000\rC\u0001"+
		"\u0000\u0000\u0000\u000fE\u0001\u0000\u0000\u0000\u0011H\u0001\u0000\u0000"+
		"\u0000\u0013K\u0001\u0000\u0000\u0000\u0015N\u0001\u0000\u0000\u0000\u0017"+
		"Q\u0001\u0000\u0000\u0000\u0019S\u0001\u0000\u0000\u0000\u001bU\u0001"+
		"\u0000\u0000\u0000\u001dW\u0001\u0000\u0000\u0000\u001fY\u0001\u0000\u0000"+
		"\u0000![\u0001\u0000\u0000\u0000#^\u0001\u0000\u0000\u0000%k\u0001\u0000"+
		"\u0000\u0000\'m\u0001\u0000\u0000\u0000)s\u0001\u0000\u0000\u0000+v\u0001"+
		"\u0000\u0000\u0000-z\u0001\u0000\u0000\u0000/\u0083\u0001\u0000\u0000"+
		"\u00001\u008d\u0001\u0000\u0000\u00003\u0091\u0001\u0000\u0000\u00005"+
		"6\u0007\u0000\u0000\u00006\u0002\u0001\u0000\u0000\u000078\u0007\u0001"+
		"\u0000\u00008\u0004\u0001\u0000\u0000\u00009:\u0005=\u0000\u0000:\u0006"+
		"\u0001\u0000\u0000\u0000;<\u0005=\u0000\u0000<=\u0005=\u0000\u0000=\b"+
		"\u0001\u0000\u0000\u0000>?\u0005!\u0000\u0000?@\u0005=\u0000\u0000@\n"+
		"\u0001\u0000\u0000\u0000AB\u0005<\u0000\u0000B\f\u0001\u0000\u0000\u0000"+
		"CD\u0005>\u0000\u0000D\u000e\u0001\u0000\u0000\u0000EF\u0005<\u0000\u0000"+
		"FG\u0005=\u0000\u0000G\u0010\u0001\u0000\u0000\u0000HI\u0005>\u0000\u0000"+
		"IJ\u0005=\u0000\u0000J\u0012\u0001\u0000\u0000\u0000KL\u0005+\u0000\u0000"+
		"LM\u0005+\u0000\u0000M\u0014\u0001\u0000\u0000\u0000NO\u0005-\u0000\u0000"+
		"OP\u0005-\u0000\u0000P\u0016\u0001\u0000\u0000\u0000QR\u0005(\u0000\u0000"+
		"R\u0018\u0001\u0000\u0000\u0000ST\u0005)\u0000\u0000T\u001a\u0001\u0000"+
		"\u0000\u0000UV\u0005{\u0000\u0000V\u001c\u0001\u0000\u0000\u0000WX\u0005"+
		"}\u0000\u0000X\u001e\u0001\u0000\u0000\u0000YZ\u0005;\u0000\u0000Z \u0001"+
		"\u0000\u0000\u0000[\\\u0005,\u0000\u0000\\\"\u0001\u0000\u0000\u0000]"+
		"_\u0003\u0003\u0001\u0000^]\u0001\u0000\u0000\u0000_`\u0001\u0000\u0000"+
		"\u0000`^\u0001\u0000\u0000\u0000`a\u0001\u0000\u0000\u0000a$\u0001\u0000"+
		"\u0000\u0000bc\u0005i\u0000\u0000cd\u0005n\u0000\u0000dl\u0005t\u0000"+
		"\u0000ef\u0005d\u0000\u0000fg\u0005o\u0000\u0000gh\u0005u\u0000\u0000"+
		"hi\u0005b\u0000\u0000ij\u0005l\u0000\u0000jl\u0005e\u0000\u0000kb\u0001"+
		"\u0000\u0000\u0000ke\u0001\u0000\u0000\u0000l&\u0001\u0000\u0000\u0000"+
		"mn\u0005w\u0000\u0000no\u0005h\u0000\u0000op\u0005i\u0000\u0000pq\u0005"+
		"l\u0000\u0000qr\u0005e\u0000\u0000r(\u0001\u0000\u0000\u0000st\u0005i"+
		"\u0000\u0000tu\u0005f\u0000\u0000u*\u0001\u0000\u0000\u0000vw\u0005f\u0000"+
		"\u0000wx\u0005o\u0000\u0000xy\u0005r\u0000\u0000y,\u0001\u0000\u0000\u0000"+
		"z{\u0005r\u0000\u0000{|\u0005e\u0000\u0000|}\u0005t\u0000\u0000}~\u0005"+
		"u\u0000\u0000~\u007f\u0005r\u0000\u0000\u007f\u0080\u0005n\u0000\u0000"+
		"\u0080.\u0001\u0000\u0000\u0000\u0081\u0084\u0003\u0001\u0000\u0000\u0082"+
		"\u0084\u0005_\u0000\u0000\u0083\u0081\u0001\u0000\u0000\u0000\u0083\u0082"+
		"\u0001\u0000\u0000\u0000\u0084\u008a\u0001\u0000\u0000\u0000\u0085\u0089"+
		"\u0003\u0001\u0000\u0000\u0086\u0089\u0003\u0003\u0001\u0000\u0087\u0089"+
		"\u0005_\u0000\u0000\u0088\u0085\u0001\u0000\u0000\u0000\u0088\u0086\u0001"+
		"\u0000\u0000\u0000\u0088\u0087\u0001\u0000\u0000\u0000\u0089\u008c\u0001"+
		"\u0000\u0000\u0000\u008a\u0088\u0001\u0000\u0000\u0000\u008a\u008b\u0001"+
		"\u0000\u0000\u0000\u008b0\u0001\u0000\u0000\u0000\u008c\u008a\u0001\u0000"+
		"\u0000\u0000\u008d\u008e\u0007\u0002\u0000\u0000\u008e\u008f\u0001\u0000"+
		"\u0000\u0000\u008f\u0090\u0006\u0018\u0000\u0000\u00902\u0001\u0000\u0000"+
		"\u0000\u0091\u0092\t\u0000\u0000\u0000\u00924\u0001\u0000\u0000\u0000"+
		"\u0006\u0000`k\u0083\u0088\u008a\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}