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
        4,1,37,236,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,0,1,0,1,1,5,1,48,8,1,10,1,12,1,51,9,1,1,1,1,1,
        1,1,1,1,5,1,57,8,1,10,1,12,1,60,9,1,1,1,1,1,1,2,1,2,3,2,66,8,2,1,
        3,5,3,69,8,3,10,3,12,3,72,9,3,1,3,1,3,1,3,3,3,77,8,3,1,3,1,3,5,3,
        81,8,3,10,3,12,3,84,9,3,1,3,1,3,1,4,1,4,1,4,3,4,91,8,4,1,5,5,5,94,
        8,5,10,5,12,5,97,9,5,1,5,1,5,1,5,1,5,1,5,3,5,104,8,5,1,6,5,6,107,
        8,6,10,6,12,6,110,9,6,1,6,1,6,1,6,1,6,3,6,116,8,6,1,6,1,6,5,6,120,
        8,6,10,6,12,6,123,9,6,1,6,1,6,1,6,3,6,128,8,6,1,7,5,7,131,8,7,10,
        7,12,7,134,9,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,144,8,8,1,9,1,
        9,1,10,1,10,1,10,1,10,1,10,3,10,153,8,10,1,11,1,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,5,13,175,8,13,10,13,12,13,178,9,13,1,13,1,13,3,13,182,
        8,13,1,14,1,14,1,14,1,14,3,14,188,8,14,1,15,1,15,1,15,5,15,193,8,
        15,10,15,12,15,196,9,15,1,16,1,16,1,16,1,16,5,16,202,8,16,10,16,
        12,16,205,9,16,1,17,5,17,208,8,17,10,17,12,17,211,9,17,1,17,1,17,
        1,17,1,17,3,17,217,8,17,1,17,1,17,5,17,221,8,17,10,17,12,17,224,
        9,17,1,17,1,17,1,18,5,18,229,8,18,10,18,12,18,232,9,18,1,18,1,18,
        1,18,0,0,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        0,1,1,0,15,23,247,0,41,1,0,0,0,2,49,1,0,0,0,4,65,1,0,0,0,6,70,1,
        0,0,0,8,90,1,0,0,0,10,95,1,0,0,0,12,108,1,0,0,0,14,132,1,0,0,0,16,
        143,1,0,0,0,18,145,1,0,0,0,20,152,1,0,0,0,22,154,1,0,0,0,24,159,
        1,0,0,0,26,181,1,0,0,0,28,187,1,0,0,0,30,189,1,0,0,0,32,197,1,0,
        0,0,34,209,1,0,0,0,36,230,1,0,0,0,38,40,3,2,1,0,39,38,1,0,0,0,40,
        43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,
        0,44,45,5,0,0,1,45,1,1,0,0,0,46,48,3,26,13,0,47,46,1,0,0,0,48,51,
        1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,51,49,1,0,0,0,
        52,53,5,13,0,0,53,54,3,30,15,0,54,58,5,6,0,0,55,57,3,4,2,0,56,55,
        1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,61,1,0,0,0,
        60,58,1,0,0,0,61,62,5,7,0,0,62,3,1,0,0,0,63,66,3,6,3,0,64,66,3,34,
        17,0,65,63,1,0,0,0,65,64,1,0,0,0,66,5,1,0,0,0,67,69,3,26,13,0,68,
        67,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,73,1,0,0,
        0,72,70,1,0,0,0,73,74,5,12,0,0,74,76,5,34,0,0,75,77,3,32,16,0,76,
        75,1,0,0,0,76,77,1,0,0,0,77,78,1,0,0,0,78,82,5,6,0,0,79,81,3,8,4,
        0,80,79,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,85,
        1,0,0,0,84,82,1,0,0,0,85,86,5,7,0,0,86,7,1,0,0,0,87,91,3,12,6,0,
        88,91,3,10,5,0,89,91,3,34,17,0,90,87,1,0,0,0,90,88,1,0,0,0,90,89,
        1,0,0,0,91,9,1,0,0,0,92,94,3,26,13,0,93,92,1,0,0,0,94,97,1,0,0,0,
        95,93,1,0,0,0,95,96,1,0,0,0,96,98,1,0,0,0,97,95,1,0,0,0,98,99,5,
        28,0,0,99,100,5,34,0,0,100,101,5,3,0,0,101,103,3,16,8,0,102,104,
        5,30,0,0,103,102,1,0,0,0,103,104,1,0,0,0,104,11,1,0,0,0,105,107,
        3,26,13,0,106,105,1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,109,
        1,0,0,0,109,111,1,0,0,0,110,108,1,0,0,0,111,112,5,29,0,0,112,113,
        5,34,0,0,113,115,5,4,0,0,114,116,3,14,7,0,115,114,1,0,0,0,115,116,
        1,0,0,0,116,121,1,0,0,0,117,118,5,2,0,0,118,120,3,14,7,0,119,117,
        1,0,0,0,120,123,1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,124,
        1,0,0,0,123,121,1,0,0,0,124,127,5,5,0,0,125,126,5,11,0,0,126,128,
        3,16,8,0,127,125,1,0,0,0,127,128,1,0,0,0,128,13,1,0,0,0,129,131,
        3,26,13,0,130,129,1,0,0,0,131,134,1,0,0,0,132,130,1,0,0,0,132,133,
        1,0,0,0,133,135,1,0,0,0,134,132,1,0,0,0,135,136,5,34,0,0,136,137,
        5,3,0,0,137,138,3,16,8,0,138,15,1,0,0,0,139,144,3,18,9,0,140,144,
        3,20,10,0,141,144,3,22,11,0,142,144,3,24,12,0,143,139,1,0,0,0,143,
        140,1,0,0,0,143,141,1,0,0,0,143,142,1,0,0,0,144,17,1,0,0,0,145,146,
        7,0,0,0,146,19,1,0,0,0,147,153,3,30,15,0,148,149,5,27,0,0,149,150,
        5,8,0,0,150,151,5,33,0,0,151,153,5,9,0,0,152,147,1,0,0,0,152,148,
        1,0,0,0,153,21,1,0,0,0,154,155,5,24,0,0,155,156,5,8,0,0,156,157,
        3,16,8,0,157,158,5,9,0,0,158,23,1,0,0,0,159,160,5,25,0,0,160,161,
        5,8,0,0,161,162,3,16,8,0,162,163,5,2,0,0,163,164,3,16,8,0,164,165,
        5,9,0,0,165,25,1,0,0,0,166,167,5,10,0,0,167,182,5,34,0,0,168,169,
        5,10,0,0,169,170,5,34,0,0,170,171,5,4,0,0,171,176,3,28,14,0,172,
        173,5,2,0,0,173,175,3,28,14,0,174,172,1,0,0,0,175,178,1,0,0,0,176,
        174,1,0,0,0,176,177,1,0,0,0,177,179,1,0,0,0,178,176,1,0,0,0,179,
        180,5,5,0,0,180,182,1,0,0,0,181,166,1,0,0,0,181,168,1,0,0,0,182,
        27,1,0,0,0,183,188,3,30,15,0,184,188,5,31,0,0,185,188,5,32,0,0,186,
        188,5,33,0,0,187,183,1,0,0,0,187,184,1,0,0,0,187,185,1,0,0,0,187,
        186,1,0,0,0,188,29,1,0,0,0,189,194,5,34,0,0,190,191,5,1,0,0,191,
        193,5,34,0,0,192,190,1,0,0,0,193,196,1,0,0,0,194,192,1,0,0,0,194,
        195,1,0,0,0,195,31,1,0,0,0,196,194,1,0,0,0,197,198,5,26,0,0,198,
        203,3,30,15,0,199,200,5,2,0,0,200,202,3,30,15,0,201,199,1,0,0,0,
        202,205,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,33,1,0,0,0,205,
        203,1,0,0,0,206,208,3,26,13,0,207,206,1,0,0,0,208,211,1,0,0,0,209,
        207,1,0,0,0,209,210,1,0,0,0,210,212,1,0,0,0,211,209,1,0,0,0,212,
        213,5,14,0,0,213,214,5,34,0,0,214,216,5,6,0,0,215,217,3,36,18,0,
        216,215,1,0,0,0,216,217,1,0,0,0,217,222,1,0,0,0,218,219,5,2,0,0,
        219,221,3,36,18,0,220,218,1,0,0,0,221,224,1,0,0,0,222,220,1,0,0,
        0,222,223,1,0,0,0,223,225,1,0,0,0,224,222,1,0,0,0,225,226,5,7,0,
        0,226,35,1,0,0,0,227,229,3,26,13,0,228,227,1,0,0,0,229,232,1,0,0,
        0,230,228,1,0,0,0,230,231,1,0,0,0,231,233,1,0,0,0,232,230,1,0,0,
        0,233,234,5,34,0,0,234,37,1,0,0,0,26,41,49,58,65,70,76,82,90,95,
        103,108,115,121,127,132,143,152,176,181,187,194,203,209,216,222,
        230
    ]

class UniContractGrammar ( Parser ):

    grammarFileName = "UniContractGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "','", "':'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "'@'", "'=>'", "'interface'", 
                     "'namespace'", "'enum'", "'integer'", "'number'", "'float'", 
                     "'date'", "'time'", "'dateTime'", "'string'", "'boolean'", 
                     "'bytes'", "'list'", "'map'", "'inherits'", "'external'", 
                     "'property'", "'method'", "'readonly'" ]

    symbolicNames = [ "<INVALID>", "DOT", "COMMA", "SEMI", "LPAREN", "RPAREN", 
                      "LCURLY", "RCURLY", "LBARCKET", "RBRACKET", "AT", 
                      "ARROW", "INTERFACE", "NAMESPACE", "ENUM", "INTEGER", 
                      "NUMBER", "FLOAT", "DATE", "TIME", "DATETIME", "STRING", 
                      "BOOLEAN", "BYTES", "LIST", "MAP", "INHERITS", "EXTERNAL", 
                      "PROPERTY", "METHOD", "READONLY", "INTEGER_CONSTANS", 
                      "NUMBER_CONSTANS", "STRING_LITERAL", "IDENTIFIER", 
                      "WS", "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_contract = 0
    RULE_namespace = 1
    RULE_namespace_elements = 2
    RULE_interface = 3
    RULE_interface_element = 4
    RULE_interface_property = 5
    RULE_interface_method = 6
    RULE_interface_method_param = 7
    RULE_type = 8
    RULE_primitive_type = 9
    RULE_reference_type = 10
    RULE_list_type = 11
    RULE_map_type = 12
    RULE_decorator = 13
    RULE_decorator_param = 14
    RULE_qualifiedName = 15
    RULE_inherits = 16
    RULE_enum = 17
    RULE_enum_element = 18

    ruleNames =  [ "contract", "namespace", "namespace_elements", "interface", 
                   "interface_element", "interface_property", "interface_method", 
                   "interface_method_param", "type", "primitive_type", "reference_type", 
                   "list_type", "map_type", "decorator", "decorator_param", 
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
    INTERFACE=12
    NAMESPACE=13
    ENUM=14
    INTEGER=15
    NUMBER=16
    FLOAT=17
    DATE=18
    TIME=19
    DATETIME=20
    STRING=21
    BOOLEAN=22
    BYTES=23
    LIST=24
    MAP=25
    INHERITS=26
    EXTERNAL=27
    PROPERTY=28
    METHOD=29
    READONLY=30
    INTEGER_CONSTANS=31
    NUMBER_CONSTANS=32
    STRING_LITERAL=33
    IDENTIFIER=34
    WS=35
    LINE_COMMENT=36
    BLOCK_COMMENT=37

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
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10 or _la==13:
                self.state = 38
                self.namespace()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(UniContractGrammar.EOF)
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
        self.enterRule(localctx, 2, self.RULE_namespace)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 46
                self.decorator()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(UniContractGrammar.NAMESPACE)
            self.state = 53
            self.qualifiedName()
            self.state = 54
            self.match(UniContractGrammar.LCURLY)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 21504) != 0):
                self.state = 55
                self.namespace_elements()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
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
        self.enterRule(localctx, 4, self.RULE_namespace_elements)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.interface()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
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
        self.enterRule(localctx, 6, self.RULE_interface)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 67
                self.decorator()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 73
            self.match(UniContractGrammar.INTERFACE)
            self.state = 74
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 75
                self.inherits()


            self.state = 78
            self.match(UniContractGrammar.LCURLY)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 805323776) != 0):
                self.state = 79
                self.interface_element()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
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
        self.enterRule(localctx, 8, self.RULE_interface_element)
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.interface_method()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.interface_property()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
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
        self.enterRule(localctx, 10, self.RULE_interface_property)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 92
                self.decorator()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.match(UniContractGrammar.PROPERTY)
            self.state = 99
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 100
            self.match(UniContractGrammar.SEMI)
            self.state = 101
            self.type_()
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 102
                self.match(UniContractGrammar.READONLY)


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

        def decorator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UniContractGrammar.DecoratorContext)
            else:
                return self.getTypedRuleContext(UniContractGrammar.DecoratorContext,i)


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
        self.enterRule(localctx, 12, self.RULE_interface_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 105
                self.decorator()
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 111
            self.match(UniContractGrammar.METHOD)
            self.state = 112
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 113
            self.match(UniContractGrammar.LPAREN)

            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10 or _la==34:
                self.state = 114
                self.interface_method_param()


            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 117
                self.match(UniContractGrammar.COMMA)
                self.state = 118
                self.interface_method_param()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self.match(UniContractGrammar.RPAREN)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 125
                self.match(UniContractGrammar.ARROW)
                self.state = 126
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
        self.enterRule(localctx, 14, self.RULE_interface_method_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 129
                self.decorator()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 135
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 136
            self.match(UniContractGrammar.SEMI)
            self.state = 137
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
        self.enterRule(localctx, 16, self.RULE_type)
        try:
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16, 17, 18, 19, 20, 21, 22, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.primitive_type()
                pass
            elif token in [27, 34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.reference_type()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.list_type()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
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
        self.enterRule(localctx, 18, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16744448) != 0)):
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
        self.enterRule(localctx, 20, self.RULE_reference_type)
        try:
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.qualifiedName()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.match(UniContractGrammar.EXTERNAL)
                self.state = 149
                self.match(UniContractGrammar.LBARCKET)
                self.state = 150
                self.match(UniContractGrammar.STRING_LITERAL)
                self.state = 151
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
        self.enterRule(localctx, 22, self.RULE_list_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(UniContractGrammar.LIST)
            self.state = 155
            self.match(UniContractGrammar.LBARCKET)
            self.state = 156
            self.type_()
            self.state = 157
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
        self.enterRule(localctx, 24, self.RULE_map_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(UniContractGrammar.MAP)
            self.state = 160
            self.match(UniContractGrammar.LBARCKET)
            self.state = 161
            self.type_()
            self.state = 162
            self.match(UniContractGrammar.COMMA)
            self.state = 163
            self.type_()
            self.state = 164
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
        self.enterRule(localctx, 26, self.RULE_decorator)
        self._la = 0 # Token type
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(UniContractGrammar.AT)
                self.state = 167
                self.match(UniContractGrammar.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(UniContractGrammar.AT)
                self.state = 169
                self.match(UniContractGrammar.IDENTIFIER)
                self.state = 170
                self.match(UniContractGrammar.LPAREN)
                self.state = 171
                self.decorator_param()
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 172
                    self.match(UniContractGrammar.COMMA)
                    self.state = 173
                    self.decorator_param()
                    self.state = 178
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 179
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
        self.enterRule(localctx, 28, self.RULE_decorator_param)
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.qualifiedName()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.match(UniContractGrammar.INTEGER_CONSTANS)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.match(UniContractGrammar.NUMBER_CONSTANS)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 4)
                self.state = 186
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
        self.enterRule(localctx, 30, self.RULE_qualifiedName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 190
                self.match(UniContractGrammar.DOT)
                self.state = 191
                self.match(UniContractGrammar.IDENTIFIER)
                self.state = 196
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
        self.enterRule(localctx, 32, self.RULE_inherits)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(UniContractGrammar.INHERITS)
            self.state = 198
            self.qualifiedName()
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 199
                self.match(UniContractGrammar.COMMA)
                self.state = 200
                self.qualifiedName()
                self.state = 205
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
        self.enterRule(localctx, 34, self.RULE_enum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 206
                self.decorator()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 212
            self.match(UniContractGrammar.ENUM)
            self.state = 213
            self.match(UniContractGrammar.IDENTIFIER)
            self.state = 214
            self.match(UniContractGrammar.LCURLY)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10 or _la==34:
                self.state = 215
                self.enum_element()


            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 218
                self.match(UniContractGrammar.COMMA)
                self.state = 219
                self.enum_element()
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 225
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
        self.enterRule(localctx, 36, self.RULE_enum_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 227
                self.decorator()
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 233
            self.match(UniContractGrammar.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





