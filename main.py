import src
import src.helpers as helpers
import src.preproc as preproc
import src.lex_gen as lex_gen

# import helpers
# import preproc
# import lex_gen

import os
def main():

    lex_rules = open('./preprox_out.txt', 'r').readlines()
    proc_rules = preproc.preproc.transfrom(lex_rules)
    # post_fix = [helpers.to_postfix(i) for i in proc_rules]
    nfa_super_node = lex_gen.gen_great_NFA(proc_rules)
    sym_table = lex_gen.gen_great_dfa(nfa_super_node, lex_gen.gen_elipson_table(nfa_super_node))
    import pprint
    pprint.pprint(sym_table)


if __name__ == '__main__':
    main()