#!/usr/bin/env python

import ply.lex as lex
import ply.yacc as yacc

import sys


class NotGreedyLexer:
    
    def __init__(self):
        self.lexer = lex.lex(module=self)
        
    tokens = ["KEYWORD", "CHAR"]
    
    
        #~ one char
    def t_CHAR(self, t):
        r"."
        return t
        
    #~ chaine of 7 chars
    def t_KEYWORD(self, t):
        r"KEYWORD"
        return t
    
    t_ignore = '\n'

    def t_error(self, t):
        print "ERROR"
        print "Illegal character '%s'" % t.value[0]
        t.lexer.skip(1)
        

    def tokenize(self, data):
        'Debug method!'
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if tok:
                yield tok
            else:
                break


class NotGreedyParser:
    
    def __init__(self):
        self.lexer = NotGreedyLexer()
        self.tokens = self.lexer.tokens
        self.parser = yacc.yacc(module=self,write_tables=0,debug=False)

    def parse(self,data):
        if data:
            return self.parser.parse(data,self.lexer.lexer,0,0,None)
        else:
            return []
    
    def p_statement_keyword(self, p):
        'statement : KEYWORD'
        print "It's the keyword"
    
    def p_statement_char(self, p):
        'statement : CHAR word'
        print "It's a word"
    
    def p_word(self, p):
        '''word : CHAR
                | CHAR word'''
        pass
    
    def p_error(self, p):
        print "ERROR"
        print "Syntax error at '%s'" % p.value
        exit(1)

if __name__ == "__main__":
    
    parser = NotGreedyParser()
    try:
        s = open("toparse")
    except EOFError:
        pass
    for line in s:
        print line
        parser.parse(line)
        
    

    
