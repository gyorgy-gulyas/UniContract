# Generated from ./unicontract/grammar/UniContractGrammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,40,293,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,
        1,0,1,1,1,1,1,1,1,2,5,2,59,8,2,10,2,12,2,62,9,2,1,2,5,2,65,8,2,10,
        2,12,2,68,9,2,1,2,1,2,1,2,1,2,5,2,74,8,2,10,2,12,2,77,9,2,1,2,1,
        2,1,3,1,3,3,3,83,8,3,1,4,5,4,86,8,4,10,4,12,4,89,9,4,1,4,5,4,92,
        8,4,10,4,12,4,95,9,4,1,4,1,4,1,4,3,4,100,8,4,1,4,1,4,5,4,104,8,4,
        10,4,12,4,107,9,4,1,4,1,4,1,5,1,5,1,5,3,5,114,8,5,1,6,5,6,117,8,
        6,10,6,12,6,120,9,6,1,6,5,6,123,8,6,10,6,12,6,126,9,6,1,6,3,6,129,
        8,6,1,6,1,6,1,6,1,6,1,6,1,7,5,7,137,8,7,10,7,12,7,140,9,7,1,7,5,
        7,143,8,7,10,7,12,7,146,9,7,1,7,3,7,149,8,7,1,7,1,7,1,7,1,7,3,7,
        155,8,7,1,7,1,7,5,7,159,8,7,10,7,12,7,162,9,7,1,7,1,7,1,7,3,7,167,
        8,7,1,8,5,8,170,8,8,10,8,12,8,173,9,8,1,8,5,8,176,8,8,10,8,12,8,
        179,9,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,189,8,9,1,10,1,10,1,
        11,1,11,1,11,1,11,1,11,3,11,198,8,11,1,12,1,12,1,12,1,12,1,12,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,5,14,220,8,14,10,14,12,14,223,9,14,1,14,1,14,3,14,227,8,
        14,1,15,1,15,1,15,1,15,3,15,233,8,15,1,16,1,16,1,16,5,16,238,8,16,
        10,16,12,16,241,9,16,1,17,1,17,1,17,1,17,5,17,247,8,17,10,17,12,
        17,250,9,17,1,18,5,18,253,8,18,10,18,12,18,256,9,18,1,18,5,18,259,
        8,18,10,18,12,18,262,9,18,1,18,1,18,1,18,1,18,3,18,268,8,18,1,18,
        1,18,5,18,272,8,18,10,18,12,18,275,9,18,1,18,1,18,1,19,5,19,280,
        8,19,10,19,12,19,283,9,19,1,19,5,19,286,8,19,10,19,12,19,289,9,19,
        1,19,1,19,1,19,0,0,20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,0,1,1,0,16,24,312,0,43,1,0,0,0,2,54,1,0,0,0,4,60,1,0,
        0,0,6,82,1,0,0,0,8,87,1,0,0,0,10,113,1,0,0,0,12,118,1,0,0,0,14,138,
        1,0,0,0,16,171,1,0,0,0,18,188,1,0,0,0,20,190,1,0,0,0,22,197,1,0,
        0,0,24,199,1,0,0,0,26,204,1,0,0,0,28,226,1,0,0,0,30,232,1,0,0,0,
        32,234,1,0,0,0,34,242,1,0,0,0,36,254,1,0,0,0,38,281,1,0,0,0,40,42,
        3,2,1,0,41,40,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,
        44,49,1,0,0,0,45,43,1,0,0,0,46,48,3,4,2,0,47,46,1,0,0,0,48,51,1,
        0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,51,49,1,0,0,0,52,
        53,5,0,0,1,53,1,1,0,0,0,54,55,5,12,0,0,55,56,3,32,16,0,56,3,1,0,
        0,0,57,59,5,38,0,0,58,57,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,
        61,1,0,0,0,61,66,1,0,0,0,62,60,1,0,0,0,63,65,3,28,14,0,64,63,1,0,
        0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,69,1,0,0,0,68,66,
        1,0,0,0,69,70,5,14,0,0,70,71,3,32,16,0,71,75,5,6,0,0,72,74,3,6,3,
        0,73,72,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,78,
        1,0,0,0,77,75,1,0,0,0,78,79,5,7,0,0,79,5,1,0,0,0,80,83,3,8,4,0,81,
        83,3,36,18,0,82,80,1,0,0,0,82,81,1,0,0,0,83,7,1,0,0,0,84,86,5,38,
        0,0,85,84,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,93,
        1,0,0,0,89,87,1,0,0,0,90,92,3,28,14,0,91,90,1,0,0,0,92,95,1,0,0,
        0,93,91,1,0,0,0,93,94,1,0,0,0,94,96,1,0,0,0,95,93,1,0,0,0,96,97,
        5,13,0,0,97,99,5,36,0,0,98,100,3,34,17,0,99,98,1,0,0,0,99,100,1,
        0,0,0,100,101,1,0,0,0,101,105,5,6,0,0,102,104,3,10,5,0,103,102,1,
        0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,108,1,
        0,0,0,107,105,1,0,0,0,108,109,5,7,0,0,109,9,1,0,0,0,110,114,3,14,
        7,0,111,114,3,12,6,0,112,114,3,36,18,0,113,110,1,0,0,0,113,111,1,
        0,0,0,113,112,1,0,0,0,114,11,1,0,0,0,115,117,5,38,0,0,116,115,1,
        0,0,0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,124,1,
        0,0,0,120,118,1,0,0,0,121,123,3,28,14,0,122,121,1,0,0,0,123,126,
        1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,128,1,0,0,0,126,124,
        1,0,0,0,127,129,5,31,0,0,128,127,1,0,0,0,128,129,1,0,0,0,129,130,
        1,0,0,0,130,131,5,29,0,0,131,132,5,36,0,0,132,133,5,3,0,0,133,134,
        3,18,9,0,134,13,1,0,0,0,135,137,5,38,0,0,136,135,1,0,0,0,137,140,
        1,0,0,0,138,136,1,0,0,0,138,139,1,0,0,0,139,144,1,0,0,0,140,138,
        1,0,0,0,141,143,3,28,14,0,142,141,1,0,0,0,143,146,1,0,0,0,144,142,
        1,0,0,0,144,145,1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,147,149,
        5,32,0,0,148,147,1,0,0,0,148,149,1,0,0,0,149,150,1,0,0,0,150,151,
        5,30,0,0,151,152,5,36,0,0,152,154,5,4,0,0,153,155,3,16,8,0,154,153,
        1,0,0,0,154,155,1,0,0,0,155,160,1,0,0,0,156,157,5,2,0,0,157,159,
        3,16,8,0,158,156,1,0,0,0,159,162,1,0,0,0,160,158,1,0,0,0,160,161,
        1,0,0,0,161,163,1,0,0,0,162,160,1,0,0,0,163,166,5,5,0,0,164,165,
        5,11,0,0,165,167,3,18,9,0,166,164,1,0,0,0,166,167,1,0,0,0,167,15,
        1,0,0,0,168,170,5,38,0,0,169,168,1,0,0,0,170,173,1,0,0,0,171,169,
        1,0,0,0,171,172,1,0,0,0,172,177,1,0,0,0,173,171,1,0,0,0,174,176,
        3,28,14,0,175,174,1,0,0,0,176,179,1,0,0,0,177,175,1,0,0,0,177,178,
        1,0,0,0,178,180,1,0,0,0,179,177,1,0,0,0,180,181,5,36,0,0,181,182,
        5,3,0,0,182,183,3,18,9,0,183,17,1,0,0,0,184,189,3,20,10,0,185,189,
        3,22,11,0,186,189,3,24,12,0,187,189,3,26,13,0,188,184,1,0,0,0,188,
        185,1,0,0,0,188,186,1,0,0,0,188,187,1,0,0,0,189,19,1,0,0,0,190,191,
        7,0,0,0,191,21,1,0,0,0,192,198,3,32,16,0,193,194,5,28,0,0,194,195,
        5,8,0,0,195,196,5,35,0,0,196,198,5,9,0,0,197,192,1,0,0,0,197,193,
        1,0,0,0,198,23,1,0,0,0,199,200,5,25,0,0,200,201,5,8,0,0,201,202,
        3,18,9,0,202,203,5,9,0,0,203,25,1,0,0,0,204,205,5,26,0,0,205,206,
        5,8,0,0,206,207,3,18,9,0,207,208,5,2,0,0,208,209,3,18,9,0,209,210,
        5,9,0,0,210,27,1,0,0,0,211,212,5,10,0,0,212,227,5,36,0,0,213,214,
        5,10,0,0,214,215,5,36,0,0,215,216,5,4,0,0,216,221,3,30,15,0,217,
        218,5,2,0,0,218,220,3,30,15,0,219,217,1,0,0,0,220,223,1,0,0,0,221,
        219,1,0,0,0,221,222,1,0,0,0,222,224,1,0,0,0,223,221,1,0,0,0,224,
        225,5,5,0,0,225,227,1,0,0,0,226,211,1,0,0,0,226,213,1,0,0,0,227,
        29,1,0,0,0,228,233,3,32,16,0,229,233,5,33,0,0,230,233,5,34,0,0,231,
        233,5,35,0,0,232,228,1,0,0,0,232,229,1,0,0,0,232,230,1,0,0,0,232,
        231,1,0,0,0,233,31,1,0,0,0,234,239,5,36,0,0,235,236,5,1,0,0,236,
        238,5,36,0,0,237,235,1,0,0,0,238,241,1,0,0,0,239,237,1,0,0,0,239,
        240,1,0,0,0,240,33,1,0,0,0,241,239,1,0,0,0,242,243,5,27,0,0,243,
        248,3,32,16,0,244,245,5,2,0,0,245,247,3,32,16,0,246,244,1,0,0,0,
        247,250,1,0,0,0,248,246,1,0,0,0,248,249,1,0,0,0,249,35,1,0,0,0,250,
        248,1,0,0,0,251,253,5,38,0,0,252,251,1,0,0,0,253,256,1,0,0,0,254,
        252,1,0,0,0,254,255,1,0,0,0,255,260,1,0,0,0,256,254,1,0,0,0,257,
        259,3,28,14,0,258,257,1,0,0,0,259,262,1,0,0,0,260,258,1,0,0,0,260,
        261,1,0,0,0,261,263,1,0,0,0,262,260,1,0,0,0,263,264,5,15,0,0,264,
        265,5,36,0,0,265,267,5,6,0,0,266,268,3,38,19,0,267,266,1,0,0,0,267,
        268,1,0,0,0,268,273,1,0,0,0,269,270,5,2,0,0,270,272,3,38,19,0,271,
        269,1,0,0,0,272,275,1,0,0,0,273,271,1,0,0,0,273,274,1,0,0,0,274,
        276,1,0,0,0,275,273,1,0,0,0,276,277,5,7,0,0,277,37,1,0,0,0,278,280,
        5,38,0,0,279,278,1,0,0,0,280,283,1,0,0,0,281,279,1,0,0,0,281,282,
        1,0,0,0,282,287,1,0,0,0,283,281,1,0,0,0,284,286,3,28,14,0,285,284,
        1,0,0,0,286,289,1,0,0,0,287,285,1,0,0,0,287,288,1,0,0,0,288,290,
        1,0,0,0,289,287,1,0,0,0,290,291,5,36,0,0,291,39,1,0,0,0,35,43,49,
        60,66,75,82,87,93,99,105,113,118,124,128,138,144,148,154,160,166,
        171,177,188,197,221,226,232,239,248,254,260,267,273,281,287
    ]

class UniContractGrammar ( Parser ):

    grammarFileName = "UniContractGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "','", "':'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "'@'", "'=>'", "'import'", "'interface'", 
                     "'namespace'", "'enum'", "'integer'", "'number'", "'float'", 
                     "'date'", "'time'", "'dateTime'", "'string'", "'boolean'", 
                     "'bytes'", "'list'", "'map'", "'inherits'", "'external'", 
                     "'property'", "'method'", "'readonly'", "'async'" ]

    symbolicNames = [ "<INVALID>", "DOT", "COMMA", "SEMI", "LPAREN", "RPAREN", 
                      "LCURLY", "RCURLY", "LBARCKET", "RBRACKET", "AT", 
                      "ARROW", "IMPORT", "INTERFACE", "NAMESPACE", "ENUM", 
                      "INTEGER", "NUMBER", "FLOAT", "DATE", "TIME", "DATETIME", 
                      "STRING", "BOOLEAN", "BYTES", "LIST", "MAP", "INHERITS", 
                      "EXTERNAL", "PROPERTY", "METHOD", "READONLY", "ASYNC", 
                      "INTEGER_CONSTANS", "NUMBER_CONSTANS", "STRING_LITERAL", 
                      "IDENTIFIER", "WS", "DOCUMENT_LINE", "LINE_COMMENT", 
                      "BLOCK_COMMENT" ]

    RULE_contract = 0
    RULE_import_rule = 1
    RULE_namespace = 2
    RULE_namespace_elements = 3
    RULE_interface = 4
    RULE_interface_element = 5
    RULE_interface_property = 6
    RULE_interface_method = 7
    RULE_interface_method_param = 8
    RULE_type = 9
    RULE_primitive_type = 10
    RULE_reference_type = 11
    RULE_list_type = 12
    RULE_map_type = 13
    RULE_decorator = 14
    RULE_decorator_param = 15
    RULE_qualifiedName = 16
    RULE_inherits = 17
    RULE_enum = 18
    RULE_enum_element = 19

    ruleNames =  [ "contract", "import_rule", "namespace", "namespace_elements", 
                   "interface", "interface_element", "interface_property", 
                   "interface_method", "interface_method_param", "type", 
                   "primitive_type", "reference_type", "list_type", "map_type", 
                   "decorator", "decorator_param", "qualifiedName", "inherits", 
                   "enum", "enum_element" ]

    EOF = Token.EOF
    DOT=1
    COMMA=2
    SEMI=3
    LPAREN=4
    RPAREN=5
    LCURLY=6
    RCURLY=7
    LBARCKET=8
    RBRACKET=9
    AT=10
    ARROW=11
    IMPORT=12
    INTERFACE=13
    NAMESPACE=14
    ENUM=15
    INTEGER=16
    NUMBER=17
    FLOAT=18
    DATE=19
    TIME=20
    DATETIME=21
    STRING=22
    BOOLEAN=23
    BYTES=24
    LIST=25
    MAP=26
    INHERITS=27
    EXTERNAL=28
    PROPERTY=29
    METHOD=30
    READONLY=31
    ASYNC=32
    INTEGER_CONSTANS=33
    NUMBER_CONSTANS=34
    STRING_LITERAL=35
    IDENTIFIER=36
    WS=37
    DOCUMENT_LINE=38
    LINE_COMMENT=39
    BLOCK_COMMENT=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ContractContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(UniContractGrammar.EOF, 0)

        def import_rule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UniContractGrammar.Import_ruleContext)
            else:
                return self.getTypedRuleContext(UniContractGrammar.Import_ruleContext,i)


        def namespace(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UniContractGrammar.NamespaceContext)
            else:
                return self.getTypedRuleContext(UniContractGrammar.NamespaceContext,i)


        def getRuleIndex(self):
            return UniContractGrammar.RULE_contract

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContract" ):
                listener.enterContract(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContract" ):
                listener.exitContract(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContract" ):
                return visitor.visitContract(self)
            else:
                return visitor.visitChildren(self)




    def contract(self):

        localctx = UniContractGrammar.ContractContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_contract)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 40
                self.import_rule()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274877924352) != 0):
                self.state = 46
                self.namespace()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(UniContractGrammar.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_ruleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(UniContractGrammar.IMPORT, 0)

        def qualifiedName(self):
            return self.getTypedRuleContext(UniContractGrammar.QualifiedNameContext,0)


        def getRuleIndex(self):
            return UniContractGrammar.RULE_import_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_rule" ):
                listener.enterImport_rule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_rule" ):
                listener.exitImport_rule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_rule" ):
                return visitor.visitImport_rule(self)
            else:
                return visitor.visitChildren(self)




    def import_rule(self):

        localctx = UniContractGrammar.Import_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_import_rule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(UniContractGrammar.IMPORT)
            self.state = 55
            self.qualifiedName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamespaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAMESPACE(self):
            return self.getToken(UniContractGrammar.NAMESPACE, 0)

        def qualifiedName(self):
            return self.getTypedRuleContext(UniContractGrammar.QualifiedNameContext,0)


        def LCURLY(self):
            return self.getToken(UniContractGrammar.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(UniContractGrammar.RCURLY, 0)

        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(UniContractGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(UniContractGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UniContractGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(UniContractGrammar.DecoratorContext,i)


        def namespace_elements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UniContractGrammar.Namespace_elementsContext)
            else:
                return self.getTypedRuleContext(UniContractGrammar.Namespace_elementsContext,i)


        def getRuleIndex(self):
            return UniContractGrammar.RULE_namespace

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespace" ):
                listener.enterNamespace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespace" ):
                listener.exitNamespace(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamespace" ):
                return visitor.visitNamespace(self)
            else:
                return visitor.visitChildren(self)




    def namespace(self):

        localctx = UniContractGrammar.NamespaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_namespace)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 57
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 63
                self.decorator()
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
            self.match(UniContractGrammar.NAMESPACE)
            self.state = 70
            self.qualifiedName()
            self.state = 71
            self.match(UniContractGrammar.LCURLY)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274877948928) != 0):
                self.state = 72
                self.namespace_elements()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(UniContractGrammar.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Namespace_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface(self):
            return self.getTypedRuleContext(UniContractGrammar.InterfaceContext,0)


        def enum(self):
            return self.getTypedRuleContext(UniContractGrammar.EnumContext,0)


        def getRuleIndex(self):
            return UniContractGrammar.RULE_namespace_elements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespace_elements" ):
                listener.enterNamespace_elements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespace_elements" ):
                listener.exitNamespace_elements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamespace_elements" ):
                return visitor.visitNamespace_elements(self)
            else:
                return visitor.visitChildren(self)




    def namespace_elements(self):

        localctx = UniContractGrammar.Namespace_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_namespace_elements)
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.interface()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.enum()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERFACE(self):
            return self.getToken(UniContractGrammar.INTERFACE, 0)

        def IDENTIFIER(self):
            return self.getToken(UniContractGrammar.IDENTIFIER, 0)

        def LCURLY(self):
            return self.getToken(UniContractGrammar.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(UniContractGrammar.RCURLY, 0)

        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(UniContractGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(UniContractGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UniContractGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(UniContractGrammar.DecoratorContext,i)


        def inherits(self):
            return self.getTypedRuleContext(UniContractGrammar.InheritsContext,0)


        def interface_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UniContractGrammar.Interface_elementContext)
            else:
                return self.getTypedRuleContext(UniContractGrammar.Interface_elementContext,i)


        def getRuleIndex(self):
            return UniContractGrammar.RULE_interface

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface" ):
                listener.enterInterface(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface" ):
                listener.exitInterface(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface" ):
                return visitor.visitInterface(self)
            else:
                return visitor.visitChildren(self)




    def interface(self):

        localctx = UniContractGrammar.InterfaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_interface)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 84
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 90
                self.decorator()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self.match(UniContractGrammar.INTERFACE)
            self.state = 97
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 98
                self.inherits()


            self.state = 101
            self.match(UniContractGrammar.LCURLY)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 282931004416) != 0):
                self.state = 102
                self.interface_element()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
            self.match(UniContractGrammar.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method(self):
            return self.getTypedRuleContext(UniContractGrammar.Interface_methodContext,0)


        def interface_property(self):
            return self.getTypedRuleContext(UniContractGrammar.Interface_propertyContext,0)


        def enum(self):
            return self.getTypedRuleContext(UniContractGrammar.EnumContext,0)


        def getRuleIndex(self):
            return UniContractGrammar.RULE_interface_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_element" ):
                listener.enterInterface_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_element" ):
                listener.exitInterface_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_element" ):
                return visitor.visitInterface_element(self)
            else:
                return visitor.visitChildren(self)




    def interface_element(self):

        localctx = UniContractGrammar.Interface_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_interface_element)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.interface_method()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.interface_property()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                self.enum()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_propertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTY(self):
            return self.getToken(UniContractGrammar.PROPERTY, 0)

        def IDENTIFIER(self):
            return self.getToken(UniContractGrammar.IDENTIFIER, 0)

        def SEMI(self):
            return self.getToken(UniContractGrammar.SEMI, 0)

        def type_(self):
            return self.getTypedRuleContext(UniContractGrammar.TypeContext,0)


        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(UniContractGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(UniContractGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UniContractGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(UniContractGrammar.DecoratorContext,i)


        def READONLY(self):
            return self.getToken(UniContractGrammar.READONLY, 0)

        def getRuleIndex(self):
            return UniContractGrammar.RULE_interface_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_property" ):
                listener.enterInterface_property(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_property" ):
                listener.exitInterface_property(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_property" ):
                return visitor.visitInterface_property(self)
            else:
                return visitor.visitChildren(self)




    def interface_property(self):

        localctx = UniContractGrammar.Interface_propertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_interface_property)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 115
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 121
                self.decorator()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 127
                self.match(UniContractGrammar.READONLY)


            self.state = 130
            self.match(UniContractGrammar.PROPERTY)
            self.state = 131
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 132
            self.match(UniContractGrammar.SEMI)
            self.state = 133
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def METHOD(self):
            return self.getToken(UniContractGrammar.METHOD, 0)

        def IDENTIFIER(self):
            return self.getToken(UniContractGrammar.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(UniContractGrammar.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(UniContractGrammar.RPAREN, 0)

        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(UniContractGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(UniContractGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UniContractGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(UniContractGrammar.DecoratorContext,i)


        def ASYNC(self):
            return self.getToken(UniContractGrammar.ASYNC, 0)

        def ARROW(self):
            return self.getToken(UniContractGrammar.ARROW, 0)

        def type_(self):
            return self.getTypedRuleContext(UniContractGrammar.TypeContext,0)


        def interface_method_param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UniContractGrammar.Interface_method_paramContext)
            else:
                return self.getTypedRuleContext(UniContractGrammar.Interface_method_paramContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(UniContractGrammar.COMMA)
            else:
                return self.getToken(UniContractGrammar.COMMA, i)

        def getRuleIndex(self):
            return UniContractGrammar.RULE_interface_method

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_method" ):
                listener.enterInterface_method(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_method" ):
                listener.exitInterface_method(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method" ):
                return visitor.visitInterface_method(self)
            else:
                return visitor.visitChildren(self)




    def interface_method(self):

        localctx = UniContractGrammar.Interface_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_interface_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 135
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 141
                self.decorator()
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 147
                self.match(UniContractGrammar.ASYNC)


            self.state = 150
            self.match(UniContractGrammar.METHOD)
            self.state = 151
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 152
            self.match(UniContractGrammar.LPAREN)

            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 343597384704) != 0):
                self.state = 153
                self.interface_method_param()


            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 156
                self.match(UniContractGrammar.COMMA)
                self.state = 157
                self.interface_method_param()
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 163
            self.match(UniContractGrammar.RPAREN)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 164
                self.match(UniContractGrammar.ARROW)
                self.state = 165
                self.type_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_method_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(UniContractGrammar.IDENTIFIER, 0)

        def SEMI(self):
            return self.getToken(UniContractGrammar.SEMI, 0)

        def type_(self):
            return self.getTypedRuleContext(UniContractGrammar.TypeContext,0)


        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(UniContractGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(UniContractGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UniContractGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(UniContractGrammar.DecoratorContext,i)


        def getRuleIndex(self):
            return UniContractGrammar.RULE_interface_method_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_method_param" ):
                listener.enterInterface_method_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_method_param" ):
                listener.exitInterface_method_param(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method_param" ):
                return visitor.visitInterface_method_param(self)
            else:
                return visitor.visitChildren(self)




    def interface_method_param(self):

        localctx = UniContractGrammar.Interface_method_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_interface_method_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 168
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 174
                self.decorator()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 180
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 181
            self.match(UniContractGrammar.SEMI)
            self.state = 182
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(UniContractGrammar.Primitive_typeContext,0)


        def reference_type(self):
            return self.getTypedRuleContext(UniContractGrammar.Reference_typeContext,0)


        def list_type(self):
            return self.getTypedRuleContext(UniContractGrammar.List_typeContext,0)


        def map_type(self):
            return self.getTypedRuleContext(UniContractGrammar.Map_typeContext,0)


        def getRuleIndex(self):
            return UniContractGrammar.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = UniContractGrammar.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_type)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 17, 18, 19, 20, 21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.primitive_type()
                pass
            elif token in [28, 36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.reference_type()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 186
                self.list_type()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 187
                self.map_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(UniContractGrammar.INTEGER, 0)

        def NUMBER(self):
            return self.getToken(UniContractGrammar.NUMBER, 0)

        def FLOAT(self):
            return self.getToken(UniContractGrammar.FLOAT, 0)

        def DATE(self):
            return self.getToken(UniContractGrammar.DATE, 0)

        def TIME(self):
            return self.getToken(UniContractGrammar.TIME, 0)

        def DATETIME(self):
            return self.getToken(UniContractGrammar.DATETIME, 0)

        def STRING(self):
            return self.getToken(UniContractGrammar.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(UniContractGrammar.BOOLEAN, 0)

        def BYTES(self):
            return self.getToken(UniContractGrammar.BYTES, 0)

        def getRuleIndex(self):
            return UniContractGrammar.RULE_primitive_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitive_type" ):
                listener.enterPrimitive_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitive_type" ):
                listener.exitPrimitive_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = UniContractGrammar.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33488896) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Reference_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qualifiedName(self):
            return self.getTypedRuleContext(UniContractGrammar.QualifiedNameContext,0)


        def EXTERNAL(self):
            return self.getToken(UniContractGrammar.EXTERNAL, 0)

        def LBARCKET(self):
            return self.getToken(UniContractGrammar.LBARCKET, 0)

        def STRING_LITERAL(self):
            return self.getToken(UniContractGrammar.STRING_LITERAL, 0)

        def RBRACKET(self):
            return self.getToken(UniContractGrammar.RBRACKET, 0)

        def getRuleIndex(self):
            return UniContractGrammar.RULE_reference_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReference_type" ):
                listener.enterReference_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReference_type" ):
                listener.exitReference_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReference_type" ):
                return visitor.visitReference_type(self)
            else:
                return visitor.visitChildren(self)




    def reference_type(self):

        localctx = UniContractGrammar.Reference_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_reference_type)
        try:
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.qualifiedName()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(UniContractGrammar.EXTERNAL)
                self.state = 194
                self.match(UniContractGrammar.LBARCKET)
                self.state = 195
                self.match(UniContractGrammar.STRING_LITERAL)
                self.state = 196
                self.match(UniContractGrammar.RBRACKET)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIST(self):
            return self.getToken(UniContractGrammar.LIST, 0)

        def LBARCKET(self):
            return self.getToken(UniContractGrammar.LBARCKET, 0)

        def type_(self):
            return self.getTypedRuleContext(UniContractGrammar.TypeContext,0)


        def RBRACKET(self):
            return self.getToken(UniContractGrammar.RBRACKET, 0)

        def getRuleIndex(self):
            return UniContractGrammar.RULE_list_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_type" ):
                listener.enterList_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_type" ):
                listener.exitList_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_type" ):
                return visitor.visitList_type(self)
            else:
                return visitor.visitChildren(self)




    def list_type(self):

        localctx = UniContractGrammar.List_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_list_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(UniContractGrammar.LIST)
            self.state = 200
            self.match(UniContractGrammar.LBARCKET)
            self.state = 201
            self.type_()
            self.state = 202
            self.match(UniContractGrammar.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Map_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAP(self):
            return self.getToken(UniContractGrammar.MAP, 0)

        def LBARCKET(self):
            return self.getToken(UniContractGrammar.LBARCKET, 0)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UniContractGrammar.TypeContext)
            else:
                return self.getTypedRuleContext(UniContractGrammar.TypeContext,i)


        def COMMA(self):
            return self.getToken(UniContractGrammar.COMMA, 0)

        def RBRACKET(self):
            return self.getToken(UniContractGrammar.RBRACKET, 0)

        def getRuleIndex(self):
            return UniContractGrammar.RULE_map_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMap_type" ):
                listener.enterMap_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMap_type" ):
                listener.exitMap_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMap_type" ):
                return visitor.visitMap_type(self)
            else:
                return visitor.visitChildren(self)




    def map_type(self):

        localctx = UniContractGrammar.Map_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_map_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(UniContractGrammar.MAP)
            self.state = 205
            self.match(UniContractGrammar.LBARCKET)
            self.state = 206
            self.type_()
            self.state = 207
            self.match(UniContractGrammar.COMMA)
            self.state = 208
            self.type_()
            self.state = 209
            self.match(UniContractGrammar.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecoratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(UniContractGrammar.AT, 0)

        def IDENTIFIER(self):
            return self.getToken(UniContractGrammar.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(UniContractGrammar.LPAREN, 0)

        def decorator_param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UniContractGrammar.Decorator_paramContext)
            else:
                return self.getTypedRuleContext(UniContractGrammar.Decorator_paramContext,i)


        def RPAREN(self):
            return self.getToken(UniContractGrammar.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(UniContractGrammar.COMMA)
            else:
                return self.getToken(UniContractGrammar.COMMA, i)

        def getRuleIndex(self):
            return UniContractGrammar.RULE_decorator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecorator" ):
                listener.enterDecorator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecorator" ):
                listener.exitDecorator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecorator" ):
                return visitor.visitDecorator(self)
            else:
                return visitor.visitChildren(self)




    def decorator(self):

        localctx = UniContractGrammar.DecoratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_decorator)
        self._la = 0 # Token type
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(UniContractGrammar.AT)
                self.state = 212
                self.match(UniContractGrammar.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.match(UniContractGrammar.AT)
                self.state = 214
                self.match(UniContractGrammar.IDENTIFIER)
                self.state = 215
                self.match(UniContractGrammar.LPAREN)
                self.state = 216
                self.decorator_param()
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 217
                    self.match(UniContractGrammar.COMMA)
                    self.state = 218
                    self.decorator_param()
                    self.state = 223
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 224
                self.match(UniContractGrammar.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decorator_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qualifiedName(self):
            return self.getTypedRuleContext(UniContractGrammar.QualifiedNameContext,0)


        def INTEGER_CONSTANS(self):
            return self.getToken(UniContractGrammar.INTEGER_CONSTANS, 0)

        def NUMBER_CONSTANS(self):
            return self.getToken(UniContractGrammar.NUMBER_CONSTANS, 0)

        def STRING_LITERAL(self):
            return self.getToken(UniContractGrammar.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return UniContractGrammar.RULE_decorator_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecorator_param" ):
                listener.enterDecorator_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecorator_param" ):
                listener.exitDecorator_param(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecorator_param" ):
                return visitor.visitDecorator_param(self)
            else:
                return visitor.visitChildren(self)




    def decorator_param(self):

        localctx = UniContractGrammar.Decorator_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_decorator_param)
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.qualifiedName()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.match(UniContractGrammar.INTEGER_CONSTANS)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 230
                self.match(UniContractGrammar.NUMBER_CONSTANS)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 4)
                self.state = 231
                self.match(UniContractGrammar.STRING_LITERAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QualifiedNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(UniContractGrammar.IDENTIFIER)
            else:
                return self.getToken(UniContractGrammar.IDENTIFIER, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(UniContractGrammar.DOT)
            else:
                return self.getToken(UniContractGrammar.DOT, i)

        def getRuleIndex(self):
            return UniContractGrammar.RULE_qualifiedName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualifiedName" ):
                listener.enterQualifiedName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualifiedName" ):
                listener.exitQualifiedName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQualifiedName" ):
                return visitor.visitQualifiedName(self)
            else:
                return visitor.visitChildren(self)




    def qualifiedName(self):

        localctx = UniContractGrammar.QualifiedNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_qualifiedName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 235
                self.match(UniContractGrammar.DOT)
                self.state = 236
                self.match(UniContractGrammar.IDENTIFIER)
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InheritsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INHERITS(self):
            return self.getToken(UniContractGrammar.INHERITS, 0)

        def qualifiedName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UniContractGrammar.QualifiedNameContext)
            else:
                return self.getTypedRuleContext(UniContractGrammar.QualifiedNameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(UniContractGrammar.COMMA)
            else:
                return self.getToken(UniContractGrammar.COMMA, i)

        def getRuleIndex(self):
            return UniContractGrammar.RULE_inherits

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInherits" ):
                listener.enterInherits(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInherits" ):
                listener.exitInherits(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInherits" ):
                return visitor.visitInherits(self)
            else:
                return visitor.visitChildren(self)




    def inherits(self):

        localctx = UniContractGrammar.InheritsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_inherits)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(UniContractGrammar.INHERITS)
            self.state = 243
            self.qualifiedName()
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 244
                self.match(UniContractGrammar.COMMA)
                self.state = 245
                self.qualifiedName()
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENUM(self):
            return self.getToken(UniContractGrammar.ENUM, 0)

        def IDENTIFIER(self):
            return self.getToken(UniContractGrammar.IDENTIFIER, 0)

        def LCURLY(self):
            return self.getToken(UniContractGrammar.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(UniContractGrammar.RCURLY, 0)

        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(UniContractGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(UniContractGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UniContractGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(UniContractGrammar.DecoratorContext,i)


        def enum_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UniContractGrammar.Enum_elementContext)
            else:
                return self.getTypedRuleContext(UniContractGrammar.Enum_elementContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(UniContractGrammar.COMMA)
            else:
                return self.getToken(UniContractGrammar.COMMA, i)

        def getRuleIndex(self):
            return UniContractGrammar.RULE_enum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnum" ):
                listener.enterEnum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnum" ):
                listener.exitEnum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnum" ):
                return visitor.visitEnum(self)
            else:
                return visitor.visitChildren(self)




    def enum(self):

        localctx = UniContractGrammar.EnumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_enum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 251
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 257
                self.decorator()
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 263
            self.match(UniContractGrammar.ENUM)
            self.state = 264
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 265
            self.match(UniContractGrammar.LCURLY)
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 343597384704) != 0):
                self.state = 266
                self.enum_element()


            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 269
                self.match(UniContractGrammar.COMMA)
                self.state = 270
                self.enum_element()
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 276
            self.match(UniContractGrammar.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Enum_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(UniContractGrammar.IDENTIFIER, 0)

        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(UniContractGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(UniContractGrammar.DOCUMENT_LINE, i)

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UniContractGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(UniContractGrammar.DecoratorContext,i)


        def getRuleIndex(self):
            return UniContractGrammar.RULE_enum_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnum_element" ):
                listener.enterEnum_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnum_element" ):
                listener.exitEnum_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnum_element" ):
                return visitor.visitEnum_element(self)
            else:
                return visitor.visitChildren(self)




    def enum_element(self):

        localctx = UniContractGrammar.Enum_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_enum_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 278
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 284
                self.decorator()
                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 290
            self.match(UniContractGrammar.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





