parser grammar UniContractGrammar;
options { 
    tokenVocab=UniContractLexer; 
    caseInsensitive = true;
}

contract
    : namespace* EOF
    ;

namespace
    : decorator* 'namespace' qualifiedName '{' namespace_elements* '}'
    ;

namespace_elements
    : interface
    | enum
    ;
   
interface
    : decorator* 'interface' IDENTIFIER inherits? '{' interface_element* '}'
    ;

    interface_element
        : interface_method
        | interface_property
        | enum
        ;
        
        interface_property
            : decorator* 'property' IDENTIFIER ':' type 'readonly'?
            ;

   
        interface_method
            : decorator* 'method' IDENTIFIER '(' (interface_method_param? (',' interface_method_param)*) ')' ('=>' type )?
            ;

        interface_method_param
            : decorator* IDENTIFIER ':' type
            ;

type
    : primitive_type
    | reference_type
    | list_type
    | map_type
    ;
    
    primitive_type
        : 'integer'
        | 'number'
        | 'float'
        | 'date'
        | 'time'
        | 'dateTime'
        | 'string'
        | 'boolean'
        | 'bytes'
        ;

    reference_type
        : qualifiedName
        | 'external' '[' STRING_LITERAL ']'
        ;

    list_type
        : 'list' '[' type ']'
        ;

    map_type
        : 'map' '[' type ',' type ']'
        ;
        
decorator
    : '@' IDENTIFIER
    | '@' IDENTIFIER '(' decorator_param (',' decorator_param)* ')' ;
    
    decorator_param
        : qualifiedName
        | INTEGER_CONSTANS
        | NUMBER_CONSTANS 
        | STRING_LITERAL
        ;

qualifiedName 
    : IDENTIFIER ('.' IDENTIFIER)* 
    ;

inherits
    : 'inherits' qualifiedName (',' qualifiedName)*
    ;

enum
    : decorator* 'enum' IDENTIFIER '{' enum_element? (',' enum_element)* '}'
    ;

    enum_element
        : decorator* IDENTIFIER
        ;