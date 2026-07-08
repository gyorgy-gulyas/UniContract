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
        4,1,43,265,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,5,0,50,8,0,10,0,12,0,53,
        9,0,1,0,1,0,1,1,5,1,58,8,1,10,1,12,1,61,9,1,1,1,1,1,1,1,1,2,5,2,
        67,8,2,10,2,12,2,70,9,2,1,2,1,2,1,2,1,2,5,2,76,8,2,10,2,12,2,79,
        9,2,1,2,1,2,1,3,1,3,3,3,85,8,3,1,4,5,4,88,8,4,10,4,12,4,91,9,4,1,
        4,1,4,1,4,3,4,96,8,4,1,4,5,4,99,8,4,10,4,12,4,102,9,4,1,4,1,4,5,
        4,106,8,4,10,4,12,4,109,9,4,1,4,1,4,1,5,1,5,1,5,3,5,116,8,5,1,6,
        5,6,119,8,6,10,6,12,6,122,9,6,1,6,3,6,125,8,6,1,6,1,6,1,6,1,6,1,
        6,1,7,5,7,133,8,7,10,7,12,7,136,9,7,1,7,3,7,139,8,7,1,7,1,7,1,7,
        3,7,144,8,7,1,7,1,7,3,7,148,8,7,1,7,1,7,5,7,152,8,7,10,7,12,7,155,
        9,7,1,7,1,7,1,7,3,7,160,8,7,1,8,5,8,163,8,8,10,8,12,8,166,9,8,1,
        8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,177,8,9,1,10,1,10,1,11,1,11,
        3,11,183,8,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,5,15,203,8,15,10,15,12,15,
        206,9,15,1,16,1,16,1,16,1,16,5,16,212,8,16,10,16,12,16,215,9,16,
        1,17,5,17,218,8,17,10,17,12,17,221,9,17,1,17,1,17,1,17,1,17,3,17,
        227,8,17,1,17,1,17,5,17,231,8,17,10,17,12,17,234,9,17,1,17,1,17,
        1,18,5,18,239,8,18,10,18,12,18,242,9,18,1,18,1,18,1,19,1,19,1,19,
        1,19,5,19,250,8,19,10,19,12,19,253,9,19,1,19,1,19,1,20,1,20,1,20,
        3,20,260,8,20,1,20,3,20,263,8,20,1,20,0,0,21,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,0,1,1,0,17,27,278,0,45,1,
        0,0,0,2,59,1,0,0,0,4,68,1,0,0,0,6,84,1,0,0,0,8,89,1,0,0,0,10,115,
        1,0,0,0,12,120,1,0,0,0,14,134,1,0,0,0,16,164,1,0,0,0,18,176,1,0,
        0,0,20,178,1,0,0,0,22,180,1,0,0,0,24,184,1,0,0,0,26,189,1,0,0,0,
        28,196,1,0,0,0,30,199,1,0,0,0,32,207,1,0,0,0,34,219,1,0,0,0,36,240,
        1,0,0,0,38,245,1,0,0,0,40,256,1,0,0,0,42,44,3,2,1,0,43,42,1,0,0,
        0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,51,1,0,0,0,47,45,
        1,0,0,0,48,50,3,4,2,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,
        51,52,1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,5,0,0,1,55,1,1,0,
        0,0,56,58,5,41,0,0,57,56,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,
        60,1,0,0,0,60,62,1,0,0,0,61,59,1,0,0,0,62,63,5,13,0,0,63,64,3,30,
        15,0,64,3,1,0,0,0,65,67,5,41,0,0,66,65,1,0,0,0,67,70,1,0,0,0,68,
        66,1,0,0,0,68,69,1,0,0,0,69,71,1,0,0,0,70,68,1,0,0,0,71,72,5,15,
        0,0,72,73,3,30,15,0,73,77,5,6,0,0,74,76,3,6,3,0,75,74,1,0,0,0,76,
        79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,0,79,77,1,0,0,
        0,80,81,5,7,0,0,81,5,1,0,0,0,82,85,3,8,4,0,83,85,3,34,17,0,84,82,
        1,0,0,0,84,83,1,0,0,0,85,7,1,0,0,0,86,88,5,41,0,0,87,86,1,0,0,0,
        88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,92,1,0,0,0,91,89,1,
        0,0,0,92,93,5,14,0,0,93,95,5,39,0,0,94,96,3,38,19,0,95,94,1,0,0,
        0,95,96,1,0,0,0,96,100,1,0,0,0,97,99,3,32,16,0,98,97,1,0,0,0,99,
        102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,103,1,0,0,0,102,100,
        1,0,0,0,103,107,5,6,0,0,104,106,3,10,5,0,105,104,1,0,0,0,106,109,
        1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,110,1,0,0,0,109,107,
        1,0,0,0,110,111,5,7,0,0,111,9,1,0,0,0,112,116,3,14,7,0,113,116,3,
        12,6,0,114,116,3,34,17,0,115,112,1,0,0,0,115,113,1,0,0,0,115,114,
        1,0,0,0,116,11,1,0,0,0,117,119,5,41,0,0,118,117,1,0,0,0,119,122,
        1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,124,1,0,0,0,122,120,
        1,0,0,0,123,125,5,35,0,0,124,123,1,0,0,0,124,125,1,0,0,0,125,126,
        1,0,0,0,126,127,5,33,0,0,127,128,5,39,0,0,128,129,5,3,0,0,129,130,
        3,18,9,0,130,13,1,0,0,0,131,133,5,41,0,0,132,131,1,0,0,0,133,136,
        1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,138,1,0,0,0,136,134,
        1,0,0,0,137,139,5,36,0,0,138,137,1,0,0,0,138,139,1,0,0,0,139,140,
        1,0,0,0,140,141,5,34,0,0,141,143,5,39,0,0,142,144,3,38,19,0,143,
        142,1,0,0,0,143,144,1,0,0,0,144,145,1,0,0,0,145,147,5,4,0,0,146,
        148,3,16,8,0,147,146,1,0,0,0,147,148,1,0,0,0,148,153,1,0,0,0,149,
        150,5,2,0,0,150,152,3,16,8,0,151,149,1,0,0,0,152,155,1,0,0,0,153,
        151,1,0,0,0,153,154,1,0,0,0,154,156,1,0,0,0,155,153,1,0,0,0,156,
        159,5,5,0,0,157,158,5,10,0,0,158,160,3,18,9,0,159,157,1,0,0,0,159,
        160,1,0,0,0,160,15,1,0,0,0,161,163,5,41,0,0,162,161,1,0,0,0,163,
        166,1,0,0,0,164,162,1,0,0,0,164,165,1,0,0,0,165,167,1,0,0,0,166,
        164,1,0,0,0,167,168,5,39,0,0,168,169,5,3,0,0,169,170,3,18,9,0,170,
        17,1,0,0,0,171,177,3,20,10,0,172,177,3,22,11,0,173,177,3,24,12,0,
        174,177,3,26,13,0,175,177,3,28,14,0,176,171,1,0,0,0,176,172,1,0,
        0,0,176,173,1,0,0,0,176,174,1,0,0,0,176,175,1,0,0,0,177,19,1,0,0,
        0,178,179,7,0,0,0,179,21,1,0,0,0,180,182,3,30,15,0,181,183,3,38,
        19,0,182,181,1,0,0,0,182,183,1,0,0,0,183,23,1,0,0,0,184,185,5,28,
        0,0,185,186,5,8,0,0,186,187,3,18,9,0,187,188,5,9,0,0,188,25,1,0,
        0,0,189,190,5,29,0,0,190,191,5,8,0,0,191,192,3,18,9,0,192,193,5,
        2,0,0,193,194,3,18,9,0,194,195,5,9,0,0,195,27,1,0,0,0,196,197,5,
        30,0,0,197,198,3,38,19,0,198,29,1,0,0,0,199,204,5,39,0,0,200,201,
        5,1,0,0,201,203,5,39,0,0,202,200,1,0,0,0,203,206,1,0,0,0,204,202,
        1,0,0,0,204,205,1,0,0,0,205,31,1,0,0,0,206,204,1,0,0,0,207,208,5,
        31,0,0,208,213,3,22,11,0,209,210,5,2,0,0,210,212,3,22,11,0,211,209,
        1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,33,1,
        0,0,0,215,213,1,0,0,0,216,218,5,41,0,0,217,216,1,0,0,0,218,221,1,
        0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,220,222,1,0,0,0,221,219,1,
        0,0,0,222,223,5,16,0,0,223,224,5,39,0,0,224,226,5,6,0,0,225,227,
        3,36,18,0,226,225,1,0,0,0,226,227,1,0,0,0,227,232,1,0,0,0,228,229,
        5,2,0,0,229,231,3,36,18,0,230,228,1,0,0,0,231,234,1,0,0,0,232,230,
        1,0,0,0,232,233,1,0,0,0,233,235,1,0,0,0,234,232,1,0,0,0,235,236,
        5,7,0,0,236,35,1,0,0,0,237,239,5,41,0,0,238,237,1,0,0,0,239,242,
        1,0,0,0,240,238,1,0,0,0,240,241,1,0,0,0,241,243,1,0,0,0,242,240,
        1,0,0,0,243,244,5,39,0,0,244,37,1,0,0,0,245,246,5,11,0,0,246,251,
        3,40,20,0,247,248,5,2,0,0,248,250,3,40,20,0,249,247,1,0,0,0,250,
        253,1,0,0,0,251,249,1,0,0,0,251,252,1,0,0,0,252,254,1,0,0,0,253,
        251,1,0,0,0,254,255,5,12,0,0,255,39,1,0,0,0,256,259,5,39,0,0,257,
        258,5,37,0,0,258,260,3,30,15,0,259,257,1,0,0,0,259,260,1,0,0,0,260,
        262,1,0,0,0,261,263,5,38,0,0,262,261,1,0,0,0,262,263,1,0,0,0,263,
        41,1,0,0,0,31,45,51,59,68,77,84,89,95,100,107,115,120,124,134,138,
        143,147,153,159,164,176,182,204,213,219,226,232,240,251,259,262
    ]

class UniContractGrammar ( Parser ):

    grammarFileName = "UniContractGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "','", "':'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "'=>'", "'<'", "'>'", "'import'", 
                     "'interface'", "'namespace'", "'enum'", "'integer'", 
                     "'number'", "'float'", "'date'", "'time'", "'dateTime'", 
                     "'string'", "'boolean'", "'bytes'", "'stream'", "'any'", 
                     "'list'", "'map'", "'query'", "'inherits'", "'external'", 
                     "'property'", "'method'", "'readonly'", "'async'", 
                     "'constraint'", "'instantiable'" ]

    symbolicNames = [ "<INVALID>", "DOT", "COMMA", "SEMI", "LPAREN", "RPAREN", 
                      "LCURLY", "RCURLY", "LBARCKET", "RBRACKET", "ARROW", 
                      "LT", "GT", "IMPORT", "INTERFACE", "NAMESPACE", "ENUM", 
                      "INTEGER", "NUMBER", "FLOAT", "DATE", "TIME", "DATETIME", 
                      "STRING", "BOOLEAN", "BYTES", "STREAM", "ANY", "LIST", 
                      "MAP", "QUERY", "INHERITS", "EXTERNAL", "PROPERTY", 
                      "METHOD", "READONLY", "ASYNC", "CONSTRAINT", "INSTANTIABLE", 
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
    RULE_query_type = 14
    RULE_qualifiedName = 15
    RULE_inherits = 16
    RULE_enum = 17
    RULE_enum_element = 18
    RULE_generic = 19
    RULE_generic_type = 20

    ruleNames =  [ "contract", "import_rule", "namespace", "namespace_elements", 
                   "interface", "interface_element", "interface_property", 
                   "interface_method", "interface_method_param", "type", 
                   "primitive_type", "reference_type", "list_type", "map_type", 
                   "query_type", "qualifiedName", "inherits", "enum", "enum_element", 
                   "generic", "generic_type" ]

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
    ARROW=10
    LT=11
    GT=12
    IMPORT=13
    INTERFACE=14
    NAMESPACE=15
    ENUM=16
    INTEGER=17
    NUMBER=18
    FLOAT=19
    DATE=20
    TIME=21
    DATETIME=22
    STRING=23
    BOOLEAN=24
    BYTES=25
    STREAM=26
    ANY=27
    LIST=28
    MAP=29
    QUERY=30
    INHERITS=31
    EXTERNAL=32
    PROPERTY=33
    METHOD=34
    READONLY=35
    ASYNC=36
    CONSTRAINT=37
    INSTANTIABLE=38
    IDENTIFIER=39
    WS=40
    DOCUMENT_LINE=41
    LINE_COMMENT=42
    BLOCK_COMMENT=43

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
            self.state = 45
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 42
                    self.import_rule() 
                self.state = 47
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==41:
                self.state = 48
                self.namespace()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
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
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 56
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.match(UniContractGrammar.IMPORT)
            self.state = 63
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
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 65
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self.match(UniContractGrammar.NAMESPACE)
            self.state = 72
            self.qualifiedName()
            self.state = 73
            self.match(UniContractGrammar.LCURLY)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2199023337472) != 0):
                self.state = 74
                self.namespace_elements()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
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
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.interface()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
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

        def generic(self):
            return self.getTypedRuleContext(UniContractGrammar.GenericContext,0)


        def inherits(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UniContractGrammar.InheritsContext)
            else:
                return self.getTypedRuleContext(UniContractGrammar.InheritsContext,i)


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
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 86
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.match(UniContractGrammar.INTERFACE)
            self.state = 93
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 94
                self.generic()


            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 97
                self.inherits()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
            self.match(UniContractGrammar.LCURLY)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2327872339968) != 0):
                self.state = 104
                self.interface_element()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
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
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.interface_method()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.interface_property()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 114
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
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 117
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 123
                self.match(UniContractGrammar.READONLY)


            self.state = 126
            self.match(UniContractGrammar.PROPERTY)
            self.state = 127
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 128
            self.match(UniContractGrammar.SEMI)
            self.state = 129
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

        def generic(self):
            return self.getTypedRuleContext(UniContractGrammar.GenericContext,0)


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
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 131
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 137
                self.match(UniContractGrammar.ASYNC)


            self.state = 140
            self.match(UniContractGrammar.METHOD)
            self.state = 141
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 142
                self.generic()


            self.state = 145
            self.match(UniContractGrammar.LPAREN)

            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39 or _la==41:
                self.state = 146
                self.interface_method_param()


            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 149
                self.match(UniContractGrammar.COMMA)
                self.state = 150
                self.interface_method_param()
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 156
            self.match(UniContractGrammar.RPAREN)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 157
                self.match(UniContractGrammar.ARROW)
                self.state = 158
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
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 161
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 167
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 168
            self.match(UniContractGrammar.SEMI)
            self.state = 169
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


        def query_type(self):
            return self.getTypedRuleContext(UniContractGrammar.Query_typeContext,0)


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
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.primitive_type()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.reference_type()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.list_type()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 4)
                self.state = 174
                self.map_type()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 5)
                self.state = 175
                self.query_type()
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

        def ANY(self):
            return self.getToken(UniContractGrammar.ANY, 0)

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
            self.state = 178
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 268304384) != 0)):
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


        def generic(self):
            return self.getTypedRuleContext(UniContractGrammar.GenericContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.qualifiedName()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 181
                self.generic()


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
            self.state = 184
            self.match(UniContractGrammar.LIST)
            self.state = 185
            self.match(UniContractGrammar.LBARCKET)
            self.state = 186
            self.type_()
            self.state = 187
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
            self.state = 189
            self.match(UniContractGrammar.MAP)
            self.state = 190
            self.match(UniContractGrammar.LBARCKET)
            self.state = 191
            self.type_()
            self.state = 192
            self.match(UniContractGrammar.COMMA)
            self.state = 193
            self.type_()
            self.state = 194
            self.match(UniContractGrammar.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Query_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUERY(self):
            return self.getToken(UniContractGrammar.QUERY, 0)

        def generic(self):
            return self.getTypedRuleContext(UniContractGrammar.GenericContext,0)


        def getRuleIndex(self):
            return UniContractGrammar.RULE_query_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery_type" ):
                listener.enterQuery_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery_type" ):
                listener.exitQuery_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery_type" ):
                return visitor.visitQuery_type(self)
            else:
                return visitor.visitChildren(self)




    def query_type(self):

        localctx = UniContractGrammar.Query_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_query_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(UniContractGrammar.QUERY)
            self.state = 197
            self.generic()
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
        self.enterRule(localctx, 30, self.RULE_qualifiedName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 200
                self.match(UniContractGrammar.DOT)
                self.state = 201
                self.match(UniContractGrammar.IDENTIFIER)
                self.state = 206
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

        def reference_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UniContractGrammar.Reference_typeContext)
            else:
                return self.getTypedRuleContext(UniContractGrammar.Reference_typeContext,i)


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
        self.enterRule(localctx, 32, self.RULE_inherits)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(UniContractGrammar.INHERITS)
            self.state = 208
            self.reference_type()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 209
                self.match(UniContractGrammar.COMMA)
                self.state = 210
                self.reference_type()
                self.state = 215
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
        self.enterRule(localctx, 34, self.RULE_enum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 216
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 222
            self.match(UniContractGrammar.ENUM)
            self.state = 223
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 224
            self.match(UniContractGrammar.LCURLY)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39 or _la==41:
                self.state = 225
                self.enum_element()


            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 228
                self.match(UniContractGrammar.COMMA)
                self.state = 229
                self.enum_element()
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 235
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
        self.enterRule(localctx, 36, self.RULE_enum_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 237
                self.match(UniContractGrammar.DOCUMENT_LINE)
                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 243
            self.match(UniContractGrammar.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GenericContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(UniContractGrammar.LT, 0)

        def generic_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UniContractGrammar.Generic_typeContext)
            else:
                return self.getTypedRuleContext(UniContractGrammar.Generic_typeContext,i)


        def GT(self):
            return self.getToken(UniContractGrammar.GT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(UniContractGrammar.COMMA)
            else:
                return self.getToken(UniContractGrammar.COMMA, i)

        def getRuleIndex(self):
            return UniContractGrammar.RULE_generic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneric" ):
                listener.enterGeneric(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneric" ):
                listener.exitGeneric(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeneric" ):
                return visitor.visitGeneric(self)
            else:
                return visitor.visitChildren(self)




    def generic(self):

        localctx = UniContractGrammar.GenericContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_generic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(UniContractGrammar.LT)
            self.state = 246
            self.generic_type()
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 247
                self.match(UniContractGrammar.COMMA)
                self.state = 248
                self.generic_type()
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 254
            self.match(UniContractGrammar.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Generic_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(UniContractGrammar.IDENTIFIER, 0)

        def CONSTRAINT(self):
            return self.getToken(UniContractGrammar.CONSTRAINT, 0)

        def qualifiedName(self):
            return self.getTypedRuleContext(UniContractGrammar.QualifiedNameContext,0)


        def INSTANTIABLE(self):
            return self.getToken(UniContractGrammar.INSTANTIABLE, 0)

        def getRuleIndex(self):
            return UniContractGrammar.RULE_generic_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneric_type" ):
                listener.enterGeneric_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneric_type" ):
                listener.exitGeneric_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeneric_type" ):
                return visitor.visitGeneric_type(self)
            else:
                return visitor.visitChildren(self)




    def generic_type(self):

        localctx = UniContractGrammar.Generic_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_generic_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 257
                self.match(UniContractGrammar.CONSTRAINT)
                self.state = 258
                self.qualifiedName()


            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 261
                self.match(UniContractGrammar.INSTANTIABLE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





