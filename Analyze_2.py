import string
import Analyze_1
import globalValues

# i%3 row / i%2 keyword / i%1 type
FOLLOW_declaration_list = ['if', 'while', 'for', 'read', 'write', '{', '}', ';', 'ID', 'NUM']
FIRST_statement_list = ['if', 'while', 'for', 'read', 'write', '{', ';', 'ID', 'NUM']
FIRST_bool_expr_1 = [">", "<", ">=", "<=", "==", "!="]  # fllow(C)
FIRST_expr = ['ID', 'NUM', '(']


# @name-def nt
def name_find(new_name):
    flag = 0
    for (name, addr) in globalValues.data.items():
        if name == new_name:
            flag = 1
            print
            '[-]Error of id ,plead renew \'' + new_name + ' \'in Line' + str(globalValues.row)
            break
    if flag == 0:
        globalValues.data[new_name] = globalValues.addr
        globalValues.addr += 1


def name_lookup(new_name):
    flag = 0
    for (name, addr) in globalValues.data.items():
        if name == new_name:
            flag = 1
            break
    if flag == 0:
        return 0
    else:
        return 1


def GET_next_word():
    globalValues.i += 3
    if globalValues.i >= len(globalValues.Got_char) and globalValues.Got_char[globalValues.i] != '}':
        globalValues.file_new.write('      STOP \n')
        exit()


def program():
    if (cmp(globalValues.Got_char[globalValues.i], '{')):
        print
        "[-]Error : lack of '{' in Line " + str(globalValues.Got_char[globalValues.i - 1])
    else:
        GET_next_word()
    declaration_list()
    statement_list()
    print
    "[+]Finished at the word " + globalValues.Got_char[globalValues.i] + "in Line " + globalValues.Got_char[
        globalValues.i - 1]
    if cmp(globalValues.Got_char[globalValues.i], '}'):
        print
        "[-]Error : lack of '}' in Line " + str(globalValues.Got_char[globalValues.i - 1])
    else:
        GET_next_word()
    globalValues.file_new.write('      STOP \n')


# first<declaration_list><statement>='{'


def declaration_list():
    if cmp(globalValues.Got_char[(globalValues.i + 1)], 'int') == 0:
        declaration_stat()
        declaration_list()
    elif globalValues.Got_char[globalValues.i + 1] in FOLLOW_declaration_list:
        return


# <declaration_list>→<declaration_stat><declaration_list> | ε


def statement_list():
    if globalValues.Got_char[globalValues.i + 1] in FIRST_statement_list:
        statement()
        statement_list()
    elif globalValues.Got_char[globalValues.i] == '}':
        return


# <statement_list>→<statement><statement_list>| ε


def declaration_stat():
    if cmp(globalValues.Got_char[(globalValues.i + 1)], 'int') == 0:
        GET_next_word()
    if cmp(globalValues.Got_char[(globalValues.i + 1)], 'ID') == 0:
        name_find(globalValues.Got_char[(globalValues.i)])
        GET_next_word()
    else:
        print
        "[-]Error : 'ID' Defiend error in Line " + str(globalValues.Got_char[globalValues.i - 1])
        while globalValues.Got_char[globalValues.i + 1] != ';':
            GET_next_word()
    if cmp(globalValues.Got_char[(globalValues.i + 1)], ';') == 0:
        GET_next_word()
    else:
        print
        "[-]Error : lack of ';' in Line " + str(globalValues.Got_char[globalValues.i - 1])  # last char_row
        return


# <declaration_stat>→int ID; *****************************************************************************add vartablep!


def statement():
    if cmp(globalValues.Got_char[globalValues.i + 1], 'if') == 0:
        GET_next_word()
        if_stat()
    elif cmp(globalValues.Got_char[globalValues.i + 1], 'while') == 0:
        GET_next_word()
        while_stat()
    elif cmp(globalValues.Got_char[globalValues.i + 1], 'for') == 0:
        GET_next_word()
        for_stat()
    elif cmp(globalValues.Got_char[globalValues.i + 1], 'read') == 0:
        GET_next_word()
        read_stat()
    elif cmp(globalValues.Got_char[globalValues.i + 1], 'write') == 0:
        GET_next_word()
        write_stat()
    elif cmp(globalValues.Got_char[globalValues.i + 1], '{') == 0:
        GET_next_word()
        compound_stat()
    elif globalValues.Got_char[globalValues.i + 1] in FIRST_expr or globalValues.Got_char[globalValues.i + 1] == ';':
        expression_stat()


def if_stat():
    if globalValues.Got_char[globalValues.i + 1] == '(':
        GET_next_word()
    else:
        print
        "[-]Error : Lack of '(' in Line " + globalValues.Got_char[i - 1]
    expression()
    if globalValues.Got_char[globalValues.i + 1] == ')':
        GET_next_word()
    else:
        print
        "[-]Error : Lack of ')' in Line " + globalValues.Got_char[i - 1]
    label1 = globalValues.labelp + 1
    globalValues.labelp += 1
    globalValues.file_new.write('BRF LABEL%s\n' % label1)
    statement()
    label2 = globalValues.labelp + 1
    globalValues.labelp += 1
    globalValues.file_new.write('BR LABEL%s\n' % label2)
    globalValues.file_new.write('LABEL%s:\n' % label1)
    if cmp(globalValues.Got_char[globalValues.i + 1], 'else') == 0:
        GET_next_word()
        statement()
    globalValues.file_new.write('LABEL%s:\n' % label2)


# <if_stat> → if (<expression>) <statement >| if (<expression>) <statement >else < statement >


def while_stat():
    label1 = globalValues.labelp + 1
    globalValues.labelp += 1
    globalValues.file_new.write('LABEL%s:\n' % label1)
    if globalValues.Got_char[globalValues.i + 1] == '(':
        GET_next_word()
    else:
        print
        "[-]Error : Lack of '(' in Line " + globalValues.Got_char[i - 1]
    expression()
    if globalValues.Got_char[globalValues.i + 1] == ')':
        GET_next_word()
    else:
        print
        "[-]Error : Lack of ')' in Line " + globalValues.Got_char[i - 1]
    label2 = globalValues.labelp + 1
    globalValues.labelp += 1
    globalValues.file_new.write('BRF LABEL%d\n' % label2)
    statement()
    globalValues.file_new.write('BR LABEL%s\n' % label1)
    globalValues.file_new.write('LABEL%s:\n' % label2)


# <while_stat> → while (<expression>) < statement >


def for_stat():
    if globalValues.Got_char[globalValues.i + 1] == '(':
        GET_next_word()
    else:
        print
        "[-]Error : Lack of '(' in Line " + globalValues.Got_char[globalValues.i - 1]
    expression()
    globalValues.file_new.write('      POP\n')
    if globalValues.Got_char[globalValues.i + 1] == ';':
        GET_next_word()
    else:
        print
        "[-]Error : Lack of ';' in Line " + globalValues.Got_char[globalValues.i - 1]
    label1 = globalValues.labelp + 1
    globalValues.labelp += 1
    globalValues.file_new.write('LABEL%s:\n' % label1)
    expression()
    label2 = globalValues.labelp + 1
    globalValues.labelp += 1
    globalValues.file_new.write('      BRF LABEL%s\n' % label2)
    label3 = globalValues.labelp + 1
    globalValues.labelp += 1
    globalValues.file_new.write('      BR LABEL%s\n' % label3)
    if globalValues.Got_char[globalValues.i + 1] == ';':
        GET_next_word()
    else:
        print
        "[-]Error : Lack of ';' in Line " + globalValues.Got_char[globalValues.i - 1]
    label4 = globalValues.labelp + 1
    globalValues.labelp += 1
    globalValues.file_new.write('LABEL%s:\n' % label4)
    expression()
    globalValues.file_new.write('      POP\n')
    globalValues.file_new.write('      BR LABEL%s\n' % label1)
    if globalValues.Got_char[globalValues.i + 1] == ')':
        GET_next_word()
    else:
        print
        "[-]Error : Lack of ')' in Line " + globalValues.Got_char[globalValues.i - 1]
    globalValues.file_new.write('LABEL%s:\n' % label3)
    statement()
    globalValues.file_new.write('      BR LABEL%s\n' % label4)
    globalValues.file_new.write('LABEL%s:\n' % label2)


# <for_stat> → for (<expression>;<expression>;<expression>)<statement>


def read_stat():
    if globalValues.Got_char[globalValues.i + 1] == 'ID':
        GET_next_word()
    else:
        print
        "[-]Error : Lack of 'ID' in Line " + globalValues.Got_char[globalValues.i - 1]
    globalValues.file_new.write('      IN      \n')
    globalValues.file_new.write('      STO %s\n' % globalValues.data[globalValues.Got_char[globalValues.i - 3]])
    globalValues.file_new.write('      POP\n')
    if globalValues.Got_char[globalValues.i + 1] == ';':
        GET_next_word()
    else:
        print
        "[-]Error : Lack of ';' in Line " + globalValues.Got_char[globalValues.i - 1]


# <read_stat> →read ID;


def write_stat():
    expression()
    if globalValues.Got_char[globalValues.i + 1] != ';':
        print
        "[-]Error : Lack of ';' in Line " + globalValues.Got_char[globalValues.i - 1]
    globalValues.file_new.write('      OUT\n')


# <write_stat> →write <expression>;


def compound_stat():
    statement_list()
    if (globalValues.Got_char[globalValues.i + 1] == '}'):
        GET_next_word()
    else:
        print
        "[-]Error : Lack of '}' in Line of " + globalValues.Got_char[globalValues.i - 1]


# <compound_stat> →{<statement_list>}


def expression_stat():
    if globalValues.Got_char[globalValues.i + 1] == ';':
        GET_next_word()
    else:
        expression()
        globalValues.file_new.write('      POP\n')
        if globalValues.Got_char[globalValues.i + 1] == ';':
            GET_next_word()
        else:
            print
            "[-]Error : Lack of ';' in Line " + globalValues.Got_char[globalValues.i - 1]


# <expression_stat> →< expression >;|;


def expression():
    if globalValues.Got_char[globalValues.i + 1] == 'ID':
        GET_next_word()
        if globalValues.Got_char[globalValues.i + 1] == '=':
            if name_lookup(globalValues.Got_char[globalValues.i - 3]) == 0:
                return
            tmp = globalValues.data[globalValues.Got_char[globalValues.i - 3]]
            GET_next_word()
            bool_expr()
            globalValues.file_new.write('      STO %s\n' % tmp)
        else:
            globalValues.i -= 3
            bool_expr()
    else:
        bool_expr()


# < expression > → ID=<bool_expr>|<bool_expr>


def bool_expr():
    if globalValues.Got_char[globalValues.i + 1] in FIRST_expr:
        additive_expr()
        additive_expr_E()


# <bool_expr> →<additive_expr>E


def additive_expr_E():
    if globalValues.Got_char[globalValues.i + 1] in FIRST_bool_expr_1:
        GET_next_word()
        additive_expr()
        if globalValues.Got_char[globalValues.i - 6] == '>':
            globalValues.file_new.write('      GT\n')
        if globalValues.Got_char[globalValues.i - 6] == '>=':
            globalValues.file_new.write('      GE\n')
        if globalValues.Got_char[globalValues.i - 6] == '<':
            globalValues.file_new.write('      LES\n')
        if globalValues.Got_char[globalValues.i - 6] == '<=':
            globalValues.file_new.write('      LE\n')
        if globalValues.Got_char[globalValues.i - 6] == '==':
            globalValues.file_new.write('      EQ\n')
        if globalValues.Got_char[globalValues.i - 6] == '!=':
            globalValues.file_new.write('      NOTEQ\n')
    elif globalValues.Got_char[globalValues.i + 1] == ';' or globalValues.Got_char[globalValues.i + 1] == ')':
        return


# E→ε|(>|<|>=|<=|==|!=)< additive_expr >
# fllow=


def term():
    if globalValues.Got_char[globalValues.i + 1] in FIRST_expr:
        factor()
        factor_D()
    # < term > →< factor >D ,


def additive_expr():
    if globalValues.Got_char[globalValues.i + 1] in FIRST_expr:
        term()
        term_C()
    else:
        print
        "[-]Error : There is an error of \'expression\' in Line " + globalValues.Got_char[globalValues.i - 1]


# < additive_expr> →< term >C


def term_C():
    if globalValues.Got_char[globalValues.i + 1] == '+' or globalValues.Got_char[globalValues.i + 1] == '-':
        if globalValues.Got_char[globalValues.i] == '+':
            globalValues.file_new.write('      ADD\n')
        else:
            globalValues.file_new.write('      SUB\n')
        GET_next_word()
        term()
        term_C()
    elif globalValues.Got_char[globalValues.i + 1] == ';' or globalValues.Got_char[globalValues.i + 1] == ')' or \
            globalValues.Got_char[globalValues.i + 1] in FIRST_bool_expr_1:
        return


# C →+<term>C|-<term>C|ε
# Follow(C)={;, ), (>|<|>=|<=|==|!=)}


def factor():
    if globalValues.Got_char[globalValues.i + 1] == '(':
        GET_next_word()
        expression()
        if globalValues.Got_char[globalValues.i + 1] == ')':
            GET_next_word()
        else:
            print
            "[-]Error : Lack of ')' in Line " + globalValues.Got_char[globalValues.i - 1]
    elif globalValues.Got_char[globalValues.i + 1] == 'ID' or globalValues.Got_char[globalValues.i + 1] == 'NUM':
        if globalValues.Got_char[globalValues.i + 1] == 'ID':
            globalValues.file_new.write('      LOAD %s\n' % globalValues.data[globalValues.Got_char[globalValues.i]])
        else:
            globalValues.file_new.write('      LOADI %s\n' % globalValues.Got_char[globalValues.i])
        GET_next_word()


# < factor > →(< expression >)|ID|NUM


def factor_D():
    if globalValues.Got_char[globalValues.i + 1] == '*' or globalValues.Got_char[globalValues.i + 1] == '/':
        if globalValues.Got_char[globalValues.i] == '*':
            globalValues.file_new.write('      MULT\n')
        else:
            globalValues.file_new.write('      DIV\n')
        GET_next_word()
        factor()
        factor_D()
    elif globalValues.Got_char[globalValues.i + 1] == ';' or globalValues.Got_char[globalValues.i + 1] == ')' or \
            globalValues.Got_char[globalValues.i + 1] in FIRST_bool_expr_1:
        return


# D →*<factor>D|/<factor>D|ε


def main():
    file = open("analyze_2.txt", 'r')
    fin = file.read()
    for x in fin:
        if x != ' ' and x != '\n':
            globalValues.Str += x
        else:
            globalValues.Got_char.append(globalValues.Str)
            globalValues.Str = ''
    globalValues.Got_char.append('')
    globalValues.Got_char.append('')
    globalValues.Got_char.append('')
    # prevent out of index
    program()


if __name__ == '__main__':
    main()