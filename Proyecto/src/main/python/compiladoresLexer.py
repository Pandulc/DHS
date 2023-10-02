# Generated from /home/gabriel/BaseCompiladores/src/main/python/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\32")
        buf.write("\u0095\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16")
        buf.write("\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\6\23a\n")
        buf.write("\23\r\23\16\23b\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\5\24n\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3")
        buf.write("\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\5\31\u0086\n\31\3\31\3\31\3\31\7")
        buf.write("\31\u008b\n\31\f\31\16\31\u008e\13\31\3\32\3\32\3\32\3")
        buf.write("\32\3\33\3\33\2\2\34\3\2\5\2\7\3\t\4\13\5\r\6\17\7\21")
        buf.write("\b\23\t\25\n\27\13\31\f\33\r\35\16\37\17!\20#\21%\22\'")
        buf.write("\23)\24+\25-\26/\27\61\30\63\31\65\32\3\2\5\4\2C\\c|\3")
        buf.write("\2\62;\5\2\13\f\17\17\"\"\2\u0098\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\3\67\3\2\2\2\59\3\2\2\2\7;\3\2\2\2\t=\3\2\2\2")
        buf.write("\13@\3\2\2\2\rC\3\2\2\2\17E\3\2\2\2\21G\3\2\2\2\23J\3")
        buf.write("\2\2\2\25M\3\2\2\2\27P\3\2\2\2\31S\3\2\2\2\33U\3\2\2\2")
        buf.write("\35W\3\2\2\2\37Y\3\2\2\2![\3\2\2\2#]\3\2\2\2%`\3\2\2\2")
        buf.write("\'m\3\2\2\2)o\3\2\2\2+u\3\2\2\2-x\3\2\2\2/|\3\2\2\2\61")
        buf.write("\u0085\3\2\2\2\63\u008f\3\2\2\2\65\u0093\3\2\2\2\678\t")
        buf.write("\2\2\28\4\3\2\2\29:\t\3\2\2:\6\3\2\2\2;<\7?\2\2<\b\3\2")
        buf.write("\2\2=>\7?\2\2>?\7?\2\2?\n\3\2\2\2@A\7#\2\2AB\7?\2\2B\f")
        buf.write("\3\2\2\2CD\7>\2\2D\16\3\2\2\2EF\7@\2\2F\20\3\2\2\2GH\7")
        buf.write(">\2\2HI\7?\2\2I\22\3\2\2\2JK\7@\2\2KL\7?\2\2L\24\3\2\2")
        buf.write("\2MN\7-\2\2NO\7-\2\2O\26\3\2\2\2PQ\7/\2\2QR\7/\2\2R\30")
        buf.write("\3\2\2\2ST\7*\2\2T\32\3\2\2\2UV\7+\2\2V\34\3\2\2\2WX\7")
        buf.write("}\2\2X\36\3\2\2\2YZ\7\177\2\2Z \3\2\2\2[\\\7=\2\2\\\"")
        buf.write("\3\2\2\2]^\7.\2\2^$\3\2\2\2_a\5\5\3\2`_\3\2\2\2ab\3\2")
        buf.write("\2\2b`\3\2\2\2bc\3\2\2\2c&\3\2\2\2de\7k\2\2ef\7p\2\2f")
        buf.write("n\7v\2\2gh\7f\2\2hi\7q\2\2ij\7w\2\2jk\7d\2\2kl\7n\2\2")
        buf.write("ln\7g\2\2md\3\2\2\2mg\3\2\2\2n(\3\2\2\2op\7y\2\2pq\7j")
        buf.write("\2\2qr\7k\2\2rs\7n\2\2st\7g\2\2t*\3\2\2\2uv\7k\2\2vw\7")
        buf.write("h\2\2w,\3\2\2\2xy\7h\2\2yz\7q\2\2z{\7t\2\2{.\3\2\2\2|")
        buf.write("}\7t\2\2}~\7g\2\2~\177\7v\2\2\177\u0080\7w\2\2\u0080\u0081")
        buf.write("\7t\2\2\u0081\u0082\7p\2\2\u0082\60\3\2\2\2\u0083\u0086")
        buf.write("\5\3\2\2\u0084\u0086\7a\2\2\u0085\u0083\3\2\2\2\u0085")
        buf.write("\u0084\3\2\2\2\u0086\u008c\3\2\2\2\u0087\u008b\5\3\2\2")
        buf.write("\u0088\u008b\5\5\3\2\u0089\u008b\7a\2\2\u008a\u0087\3")
        buf.write("\2\2\2\u008a\u0088\3\2\2\2\u008a\u0089\3\2\2\2\u008b\u008e")
        buf.write("\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d")
        buf.write("\62\3\2\2\2\u008e\u008c\3\2\2\2\u008f\u0090\t\4\2\2\u0090")
        buf.write("\u0091\3\2\2\2\u0091\u0092\b\32\2\2\u0092\64\3\2\2\2\u0093")
        buf.write("\u0094\13\2\2\2\u0094\66\3\2\2\2\b\2bm\u0085\u008a\u008c")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class compiladoresLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    EQ = 1
    EQQ = 2
    NE = 3
    LT = 4
    GT = 5
    LE = 6
    GE = 7
    PP = 8
    MM = 9
    PA = 10
    PC = 11
    LLA = 12
    LLC = 13
    PYC = 14
    COMA = 15
    NUMERO = 16
    TDATO = 17
    WHILE = 18
    IF = 19
    FOR = 20
    RETURN = 21
    ID = 22
    WS = 23
    OTRO = 24

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'++'", 
            "'--'", "'('", "')'", "'{'", "'}'", "';'", "','", "'while'", 
            "'if'", "'for'", "'return'" ]

    symbolicNames = [ "<INVALID>",
            "EQ", "EQQ", "NE", "LT", "GT", "LE", "GE", "PP", "MM", "PA", 
            "PC", "LLA", "LLC", "PYC", "COMA", "NUMERO", "TDATO", "WHILE", 
            "IF", "FOR", "RETURN", "ID", "WS", "OTRO" ]

    ruleNames = [ "LETRA", "DIGITO", "EQ", "EQQ", "NE", "LT", "GT", "LE", 
                  "GE", "PP", "MM", "PA", "PC", "LLA", "LLC", "PYC", "COMA", 
                  "NUMERO", "TDATO", "WHILE", "IF", "FOR", "RETURN", "ID", 
                  "WS", "OTRO" ]

    grammarFileName = "compiladores.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


