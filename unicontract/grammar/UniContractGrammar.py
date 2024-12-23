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
        4,1,38,225,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,5,0,38,8,0,10,0,12,0,
        41,9,0,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,1,0,1,1,5,1,52,8,1,10,
        1,12,1,55,9,1,1,1,1,1,1,1,1,2,5,2,61,8,2,10,2,12,2,64,9,2,1,2,1,
        2,1,2,1,2,5,2,70,8,2,10,2,12,2,73,9,2,1,2,1,2,1,3,1,3,3,3,79,8,3,
        1,4,5,4,82,8,4,10,4,12,4,85,9,4,1,4,1,4,1,4,3,4,90,8,4,1,4,1,4,5,
        4,94,8,4,10,4,12,4,97,9,4,1,4,1,4,1,5,1,5,1,5,3,5,104,8,5,1,6,5,
        6,107,8,6,10,6,12,6,110,9,6,1,6,3,6,113,8,6,1,6,1,6,1,6,1,6,1,6,
        1,7,5,7,121,8,7,10,7,12,7,124,9,7,1,7,3,7,127,8,7,1,7,1,7,1,7,1,
        7,3,7,133,8,7,1,7,1,7,5,7,137,8,7,10,7,12,7,140,9,7,1,7,1,7,1,7,
        3,7,145,8,7,1,8,5,8,148,8,8,10,8,12,8,151,9,8,1,8,1,8,1,8,1,8,1,
        9,1,9,1,9,1,9,3,9,161,8,9,1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,
        1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,5,14,182,
        8,14,10,14,12,14,185,9,14,1,15,1,15,1,15,1,15,5,15,191,8,15,10,15,
        12,15,194,9,15,1,16,5,16,197,8,16,10,16,12,16,200,9,16,1,16,1,16,
        1,16,1,16,3,16,206,8,16,1,16,1,16,5,16,210,8,16,10,16,12,16,213,
        9,16,1,16,1,16,1,17,5,17,218,8,17,10,17,12,17,221,9,17,1,17,1,17,
        1,17,0,0,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,1,
        1,0,16,25,234,0,39,1,0,0,0,2,53,1,0,0,0,4,62,1,0,0,0,6,78,1,0,0,
        0,8,83,1,0,0,0,10,103,1,0,0,0,12,108,1,0,0,0,14,122,1,0,0,0,16,149,
        1,0,0,0,18,160,1,0,0,0,20,162,1,0,0,0,22,164,1,0,0,0,24,166,1,0,
        0,0,26,171,1,0,0,0,28,178,1,0,0,0,30,186,1,0,0,0,32,198,1,0,0,0,
        34,219,1,0,0,0,36,38,3,2,1,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,
        0,0,0,39,40,1,0,0,0,40,45,1,0,0,0,41,39,1,0,0,0,42,44,3,4,2,0,43,
        42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,
        0,47,45,1,0,0,0,48,49,5,0,0,1,49,1,1,0,0,0,50,52,5,36,0,0,51,50,
        1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,
        55,53,1,0,0,0,56,57,5,12,0,0,57,58,3,28,14,0,58,3,1,0,0,0,59,61,
        5,36,0,0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,
        63,65,1,0,0,0,64,62,1,0,0,0,65,66,5,14,0,0,66,67,3,28,14,0,67,71,
        5,6,0,0,68,70,3,6,3,0,69,68,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,
        71,72,1,0,0,0,72,74,1,0,0,0,73,71,1,0,0,0,74,75,5,7,0,0,75,5,1,0,
        0,0,76,79,3,8,4,0,77,79,3,32,16,0,78,76,1,0,0,0,78,77,1,0,0,0,79,
        7,1,0,0,0,80,82,5,36,0,0,81,80,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,
        0,83,84,1,0,0,0,84,86,1,0,0,0,85,83,1,0,0,0,86,87,5,13,0,0,87,89,
        5,34,0,0,88,90,3,30,15,0,89,88,1,0,0,0,89,90,1,0,0,0,90,91,1,0,0,
        0,91,95,5,6,0,0,92,94,3,10,5,0,93,92,1,0,0,0,94,97,1,0,0,0,95,93,
        1,0,0,0,95,96,1,0,0,0,96,98,1,0,0,0,97,95,1,0,0,0,98,99,5,7,0,0,
        99,9,1,0,0,0,100,104,3,14,7,0,101,104,3,12,6,0,102,104,3,32,16,0,
        103,100,1,0,0,0,103,101,1,0,0,0,103,102,1,0,0,0,104,11,1,0,0,0,105,
        107,5,36,0,0,106,105,1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,
        109,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,111,113,5,32,0,0,112,
        111,1,0,0,0,112,113,1,0,0,0,113,114,1,0,0,0,114,115,5,30,0,0,115,
        116,5,34,0,0,116,117,5,3,0,0,117,118,3,18,9,0,118,13,1,0,0,0,119,
        121,5,36,0,0,120,119,1,0,0,0,121,124,1,0,0,0,122,120,1,0,0,0,122,
        123,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,125,127,5,33,0,0,126,
        125,1,0,0,0,126,127,1,0,0,0,127,128,1,0,0,0,128,129,5,31,0,0,129,
        130,5,34,0,0,130,132,5,4,0,0,131,133,3,16,8,0,132,131,1,0,0,0,132,
        133,1,0,0,0,133,138,1,0,0,0,134,135,5,2,0,0,135,137,3,16,8,0,136,
        134,1,0,0,0,137,140,1,0,0,0,138,136,1,0,0,0,138,139,1,0,0,0,139,
        141,1,0,0,0,140,138,1,0,0,0,141,144,5,5,0,0,142,143,5,11,0,0,143,
        145,3,18,9,0,144,142,1,0,0,0,144,145,1,0,0,0,145,15,1,0,0,0,146,
        148,5,36,0,0,147,146,1,0,0,0,148,151,1,0,0,0,149,147,1,0,0,0,149,
        150,1,0,0,0,150,152,1,0,0,0,151,149,1,0,0,0,152,153,5,34,0,0,153,
        154,5,3,0,0,154,155,3,18,9,0,155,17,1,0,0,0,156,161,3,20,10,0,157,
        161,3,22,11,0,158,161,3,24,12,0,159,161,3,26,13,0,160,156,1,0,0,
        0,160,157,1,0,0,0,160,158,1,0,0,0,160,159,1,0,0,0,161,19,1,0,0,0,
        162,163,7,0,0,0,163,21,1,0,0,0,164,165,3,28,14,0,165,23,1,0,0,0,
        166,167,5,26,0,0,167,168,5,8,0,0,168,169,3,18,9,0,169,170,5,9,0,
        0,170,25,1,0,0,0,171,172,5,27,0,0,172,173,5,8,0,0,173,174,3,18,9,
        0,174,175,5,2,0,0,175,176,3,18,9,0,176,177,5,9,0,0,177,27,1,0,0,
        0,178,183,5,34,0,0,179,180,5,1,0,0,180,182,5,34,0,0,181,179,1,0,
        0,0,182,185,1,0,0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,29,1,0,0,
        0,185,183,1,0,0,0,186,187,5,28,0,0,187,192,3,28,14,0,188,189,5,2,
        0,0,189,191,3,28,14,0,190,188,1,0,0,0,191,194,1,0,0,0,192,190,1,
        0,0,0,192,193,1,0,0,0,193,31,1,0,0,0,194,192,1,0,0,0,195,197,5,36,
        0,0,196,195,1,0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,198,199,1,0,
        0,0,199,201,1,0,0,0,200,198,1,0,0,0,201,202,5,15,0,0,202,203,5,34,
        0,0,203,205,5,6,0,0,204,206,3,34,17,0,205,204,1,0,0,0,205,206,1,
        0,0,0,206,211,1,0,0,0,207,208,5,2,0,0,208,210,3,34,17,0,209,207,
        1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,214,
        1,0,0,0,213,211,1,0,0,0,214,215,5,7,0,0,215,33,1,0,0,0,216,218,5,
        36,0,0,217,216,1,0,0,0,218,221,1,0,0,0,219,217,1,0,0,0,219,220,1,
        0,0,0,220,222,1,0,0,0,221,219,1,0,0,0,222,223,5,34,0,0,223,35,1,
        0,0,0,25,39,45,53,62,71,78,83,89,95,103,108,112,122,126,132,138,
        144,149,160,183,192,198,205,211,219
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
                     "'bytes'", "'stream'", "'list'", "'map'", "'inherits'", 
                     "'external'", "'property'", "'method'", "'readonly'", 
                     "'async'" ]

    symbolicNames = [ "<INVALID>", "DOT", "COMMA", "SEMI", "LPAREN", "RPAREN", 
                      "LCURLY", "RCURLY", "LBARCKET", "RBRACKET", "AT", 
                      "ARROW", "IMPORT", "INTERFACE", "NAMESPACE", "ENUM", 
                      "INTEGER", "NUMBER", "FLOAT", "DATE", "TIME", "DATETIME", 
                      "STRING", "BOOLEAN", "BYTES", "STREAM", "LIST", "MAP", 
                      "INHERITS", "EXTERNAL", "PROPERTY", "METHOD", "READONLY", 
                      "ASYNC", "IDENTIFIER", "WS", "DOCUMENT_LINE", "LINE_COMMENT", 
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
    RULE_qualifiedName = 14
    RULE_inherits = 15
    RULE_enum = 16
    RULE_enum_element = 17

    ruleNames =  [ "contract", "import_rule", "namespace", "namespace_elements", 
                   "interface", "interface_element", "interface_property", 
                   "interface_method", "interface_method_param", "type", 
                   "primitive_type", "reference_type", "list_type", "map_type", 
                   "qualifiedName", "inherits", "enum", "enum_element" ]

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
    STREAM=25
    LIST=26
    MAP=27
    INHERITS=28
    EXTERNAL=29
    PROPERTY=30
    METHOD=31
    READONLY=32
    ASYNC=33
    IDENTIFIER=34
    WS=35
    DOCUMENT_LINE=36
    LINE_COMMENT=37
    BLOCK_COMMENT=38

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
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 36
                    self.import_rule() 
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14 or _la==36:
                self.state = 42
                self.namespace()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
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


        def DOCUMENT_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(UniContractGrammar.DOCUMENT_LINE)
            else:
                return self.getToken(UniContractGrammar.DOCUMENT_LINE, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 50
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self.match(UniContractGrammar.IMPORT)
            self.state = 57
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
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 59
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.match(UniContractGrammar.NAMESPACE)
            self.state = 66
            self.qualifiedName()
            self.state = 67
            self.match(UniContractGrammar.LCURLY)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68719517696) != 0):
                self.state = 68
                self.namespace_elements()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
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
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.interface()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
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
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 80
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(UniContractGrammar.INTERFACE)
            self.state = 87
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 88
                self.inherits()


            self.state = 91
            self.match(UniContractGrammar.LCURLY)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 84825636864) != 0):
                self.state = 92
                self.interface_element()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
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
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.interface_method()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.interface_property()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 102
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
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 105
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 111
                self.match(UniContractGrammar.READONLY)


            self.state = 114
            self.match(UniContractGrammar.PROPERTY)
            self.state = 115
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 116
            self.match(UniContractGrammar.SEMI)
            self.state = 117
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
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 119
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 125
                self.match(UniContractGrammar.ASYNC)


            self.state = 128
            self.match(UniContractGrammar.METHOD)
            self.state = 129
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 130
            self.match(UniContractGrammar.LPAREN)

            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34 or _la==36:
                self.state = 131
                self.interface_method_param()


            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 134
                self.match(UniContractGrammar.COMMA)
                self.state = 135
                self.interface_method_param()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 141
            self.match(UniContractGrammar.RPAREN)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 142
                self.match(UniContractGrammar.ARROW)
                self.state = 143
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
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 146
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 152
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 153
            self.match(UniContractGrammar.SEMI)
            self.state = 154
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
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 17, 18, 19, 20, 21, 22, 23, 24, 25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.primitive_type()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.reference_type()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 158
                self.list_type()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 4)
                self.state = 159
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

        def STREAM(self):
            return self.getToken(UniContractGrammar.STREAM, 0)

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
            self.state = 162
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 67043328) != 0)):
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
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.qualifiedName()
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
            self.state = 166
            self.match(UniContractGrammar.LIST)
            self.state = 167
            self.match(UniContractGrammar.LBARCKET)
            self.state = 168
            self.type_()
            self.state = 169
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
            self.state = 171
            self.match(UniContractGrammar.MAP)
            self.state = 172
            self.match(UniContractGrammar.LBARCKET)
            self.state = 173
            self.type_()
            self.state = 174
            self.match(UniContractGrammar.COMMA)
            self.state = 175
            self.type_()
            self.state = 176
            self.match(UniContractGrammar.RBRACKET)
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
        self.enterRule(localctx, 28, self.RULE_qualifiedName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 179
                self.match(UniContractGrammar.DOT)
                self.state = 180
                self.match(UniContractGrammar.IDENTIFIER)
                self.state = 185
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
        self.enterRule(localctx, 30, self.RULE_inherits)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(UniContractGrammar.INHERITS)
            self.state = 187
            self.qualifiedName()
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 188
                self.match(UniContractGrammar.COMMA)
                self.state = 189
                self.qualifiedName()
                self.state = 194
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
        self.enterRule(localctx, 32, self.RULE_enum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 195
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 201
            self.match(UniContractGrammar.ENUM)
            self.state = 202
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 203
            self.match(UniContractGrammar.LCURLY)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34 or _la==36:
                self.state = 204
                self.enum_element()


            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 207
                self.match(UniContractGrammar.COMMA)
                self.state = 208
                self.enum_element()
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 214
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
        self.enterRule(localctx, 34, self.RULE_enum_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 216
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 222
            self.match(UniContractGrammar.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





