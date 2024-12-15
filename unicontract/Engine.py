from antlr4.error.ErrorListener import ErrorListener
from antlr4 import *
from unicontract.grammar.UniContractLexer import *
from unicontract.grammar.UniContractGrammar import *
from unicontract.elements.ElementBuilder import *

class Source:
    def __init__(self):
        self.fileName: str = None
        self.content: str = None

    @staticmethod
    def CreateFromText(content, fileName="internal string"):
        source = Source()
        source.content = content
        source.fileName = fileName
        return source

    @staticmethod
    def CreateFromFile(fileName):
        source = Source()
        source.fileName = fileName
        with open(fileName, 'r') as file:
            source.content = file.read()
        return source


class Session:
    def __init__(self, source:Source):
        self.source: Source = source
        self.syntaxTree: UniContractGrammar.ContractContext = []
        self.diagnostics: List[Diagnostic] = []
        self.contract: contract = None

    def HasDiagnostic(self):
        if (len(self.diagnostics) > 0):
            return True
        return False

    def HasAnyError(self):
        for msg in self.diagnostics:
            if(msg.severity == Diagnostic.Severity.Error):
                return True
        return False

    def HasAnyWarning(self):
        for msg in self.diagnostics:
            if(msg.severity == Diagnostic.Severity.Warning):
                return True
        return False

    def PrintDiagnostics(self):
        for msg in self.diagnostics:
            print(f"{msg.toText()}\n")

    def ClearDiagnostics(self):
        self.diagnostics.clear()

    def ReportDiagnostic(self, message, severity, fileName="", line=0, column=0 ):
        diagnostic: Diagnostic = Diagnostic()
        diagnostic.severity = severity
        diagnostic.fileName = fileName
        diagnostic.line = line
        diagnostic.column = column
        diagnostic.message = message
        self.diagnostics.append(diagnostic)


class Engine:

    def Build(self, session: Session):
        self.__create_syntax_tree(session)
        self.__create_element_tree(session)

        return session.contract

    def __create_syntax_tree(self, session: Session):
            lexer = UniContractLexer(InputStream(session.source.content))
            grammar = UniContractGrammar(CommonTokenStream(lexer))

            error_listener = Engine.__syntaxErrorListener__(session.source.fileName, session)
            grammar.removeErrorListeners()
            grammar.addErrorListener(error_listener)

            session.syntaxTree = grammar.contract()

    def __create_element_tree(self, session: Session):
        visitor = ElementBuilder()
        visitor.fileName = session.source.fileName
        session.contract = visitor.visit(session.syntaxTree)
    
    class __syntaxErrorListener__(ErrorListener):
        def __init__(self, fileName, session: Session):
            super(Engine.__syntaxErrorListener__, self).__init__()
            self.fileName = fileName
            self.session = session

        def syntaxError(self, recognizer, offendingSymbol, line, column, message, e):
            self.session.ReportDiagnostic(message,Diagnostic.Severity.Error,self.fileName,line,column)

class Diagnostic:
    def __init__(self):
        self.severity: Diagnostic.Severity = Diagnostic.Severity.Message
        self.fileName: str = None
        self.line: int = None
        self.column: int = None
        self.message: int = None

    def toText(self):
        return f"{self.fileName}({self.line},{self.column}): {self.severity} :{self.message}\n"
    
    class Severity(Enum):
        Message = 1,
        Warning = 2,
        Error = 3,
        
