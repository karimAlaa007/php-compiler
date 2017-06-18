import tkinter
from tkinter import *
from tkinter.scrolledtext import *
import tkinter.filedialog as file_dialog
import tkinter.messagebox as pop_up
import ply.ply.lex as lex
import ply.ply.yacc as yacc



tokens = (
   'START_CODE',            # <?php
   'CLASS',                 # class
   'OPEN_CURLY_BRACE' ,     # {
   'CLOSE_CURLY_BRACE' ,    # }
   'OPEN_BRACE',            # (
   'CLOSE_BRACE',           # )
   'VARIABLE',              # $ letter and digit
   'EQUALS',                # =
   'SEMICOLON',             # ;
   'FUNCTION',              # function
   'PRINT',                 # print                                                                                                                                                                                 # print
   "SINGLE_QUOTE",          # '
   "DOUBLE_QUOTE",          # "
   'COMMA',                 # ,
   'DOT',                   # .
   'PLUS',                  # +
   'MINUS',                 # -
   'TIMES',                 # *
   'DIVIDE',                # /
   'CONST',                 # 2534
   'END_CODE',              # ?>
   'IDENTIFIER',            # letter and digit
   'RETURN',                # return
   'NEW',                   # new
   'TRUE',                  # true
   'FALSE',                 #last
   'ARROW',                 #->
)


t_START_CODE         = r'[<][?]php'
t_VARIABLE           = r'[$][a-zA-Z_][a-zA-Z_0-9]*'
t_OPEN_CURLY_BRACE   = r'\{'
t_CLOSE_CURLY_BRACE  = r'\}'
t_OPEN_BRACE         = r'\('
t_CLOSE_BRACE        = r'\)'
t_EQUALS             = r'\='
t_SEMICOLON          = r';'
t_SINGLE_QUOTE       = r'\''
t_DOUBLE_QUOTE       = r'"'
t_COMMA              = r','
t_DOT                = r'\.'
t_PLUS               = r'\+'
t_MINUS              = r'-'
t_TIMES              = r'\*'
t_DIVIDE             = r'/'
t_CONST              = r'[0-9]+'
t_END_CODE           = r'\?>'
t_IDENTIFIER         = r'[a-zA-Z_][a-zA-Z_0-9]*'

def t_CLASS(t):
    r'\bclass\b'
    return t
def t_FUNCTION(t):
    r'\bfunction\b'
    return t
def t_PRINT(t):
    r'\bprint\b'
    return t
def t_RETURN(t):
    r'\breturn\b'
    return t
def t_NEW(t):
    r'\bnew\b'
    return t
def t_TRUE(t):
    r'\btrue\b'
    return t
def t_FALSE(t):
    r'\bfalse\b'
    return t
def t_ARROW(t):
    r'\->\b'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore  = ' \t'


def t_error(t):
    if t.lexer.lineno <= len( main_text.get(1.0, tk.END).split("\n")):
        pop_up.showerror("Lexer Error", "Unexpected Token at '" + t.value[0] + "' in line " + str(t.lexer.lineno))
    t.lexer.skip(1)




#########################################################################################################################################
#########################################################################################################################################
#########################################################################################################################################

def p_start_code(p):
    '''StartCode : START_CODE InternalCode END_CODE
                 | '''
def p_create_class(p):
    '''InternalCode : CLASS IDENTIFIER OPEN_CURLY_BRACE ClassCode CLOSE_CURLY_BRACE InternalCode
                    | VARIABLE EQUALS NEW IDENTIFIER OPEN_BRACE parameter CLOSE_BRACE SEMICOLON InternalCode
                    | dec_var InternalCode
                    | dec_fun InternalCode
                    | VARIABLE EQUALS expr SEMICOLON InternalCode
                    | CallRetFun InternalCode
                    | print InternalCode
                    | CallClassFun InternalCode
                    | '''
    pass
def p_callclassfun(p):
    '''CallClassFun : VARIABLE EQUALS VARIABLE ARROW IDENTIFIER OPEN_BRACE parameter CLOSE_BRACE SEMICOLON
                    | VARIABLE ARROW IDENTIFIER OPEN_BRACE parameter CLOSE_BRACE SEMICOLON'''
    pass
def p_class_code_empty(p):
    '''ClassCode : dec_var ClassCode
                 | dec_fun ClassCode
                 | VARIABLE EQUALS expr SEMICOLON ClassCode
                 | CallRetFun ClassCode
                 | '''
    pass
def p_classcode_callfun(p):
    '''CallFun : IDENTIFIER OPEN_BRACE parameter CLOSE_BRACE SEMICOLON
               | CallRetFun'''
    pass
def p_classcode_callretfun(p):
    '''CallRetFun : VARIABLE EQUALS IDENTIFIER OPEN_BRACE parameter CLOSE_BRACE SEMICOLON'''
    pass
def p_classcode_decfunp(p):
    '''dec_fun : FUNCTION IDENTIFIER OPEN_BRACE parameter CLOSE_BRACE OPEN_CURLY_BRACE fun_code CLOSE_CURLY_BRACE'''
    pass
def p_classcode_multi_parameter(p):
    '''parameter : VARIABLE COMMA parameter
                 | VARIABLE
                 | '''
    pass
def p_classcode_funcodev(p):
    '''fun_code : dec_var fun_code
                | print fun_code
                | VARIABLE EQUALS expr SEMICOLON fun_code
                | CallFun fun_code
                | FunRet SEMICOLON
                | '''
    pass
def p_dec_var(p):
    '''dec_var :  VARIABLE EQUALS DOUBLE_QUOTE string DOUBLE_QUOTE SEMICOLON
               |  VARIABLE EQUALS CONST SEMICOLON'''
    pass
def p_classcode_print(p):
    '''print : PRINT SINGLE_QUOTE string SINGLE_QUOTE PrintData SEMICOLON
             | PRINT VARIABLE SEMICOLON'''
    pass
def p_classcode_printdata(p):
    '''PrintData : DOT SINGLE_QUOTE string SINGLE_QUOTE PrintData
                 | DOT VARIABLE PrintData
                 | '''
    pass
def p_classcode_string(p):
    '''string : IDENTIFIER string
              | '''
    pass
def p_classcode_exprplus(p):
    '''expr : expr PLUS term
            | expr MINUS term
            | term'''
    pass
def p_classcode_termtimes(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | factor'''
    pass
def p_classcode_factorid(p):
    '''factor : IDENTIFIER
              | CONST
              | VARIABLE'''
def p_funcode_return(p):
    '''FunRet : RETURN VARIABLE
              | RETURN SINGLE_QUOTE string SINGLE_QUOTE
              | RETURN TRUE
              | RETURN FALSE'''


def p_error(p):
    line_no = p.lineno - (len( main_text.get(1.0, tkinter.END).split("\n")) - 1)
    pop_up.showerror("Parser Error","Syntax error! unexpected token '" + p.value + "' in line " + str(line_no))





root = tkinter.Tk(className=" PHP Compiler - IDE")
main_text = ScrolledText(root, width=200, height=45)




def open_command():
    file = file_dialog.askopenfile(parent=root, mode='rb', title='Select a file')
    if file != None:
        contents = file.read()
        main_text.insert('1.0', contents)
        file.close()


def save_command():
    file = file_dialog.asksaveasfile(mode='w')
    if file != None:
        data = main_text.get('1.0', END) # END + '-1c'
        file.write(data)
        file.close()


def exit_command():
    if pop_up.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()


def about_command():
    label = pop_up.showinfo("About", "PHP Compiler Project Made By : Karim Alaa")


def new():
    main_text.delete('1.0',END)

def add_cover():
    data = '''<?php



?>'''
    main_text.insert(tkinter.INSERT, data)

def Run():
    data = main_text.get(1.0, tkinter.END)
    lexer = lex.lex(optimize=1)

    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break
            # print(tok)
    parser = yacc.yacc()

    result = parser.parse(data)
    pop_up.showinfo("Done", "Program Run With No More Error")




menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)

menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)


menu.add_command(label="Run", command=Run)
menu.add_command(label="Add PHP Cover", command=add_cover)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about_command)

main_text.pack()
root.mainloop()