import sys
import os
import re
import logging
import src.helpers as helpers
logging.basicConfig(level=logging.INFO)
class preproc():
    def transfrom(lex_lines): #pylint: disable=E0213
        logging.info("Started prep proc")
        sym_table = {}
        out = []
        for i in lex_lines: #pylint: disable=E1133
            if re.search(r'=',i) is not None:
                temp = i.split('=')
                if(sym_table.get(temp[0]) is not None):
                    logging.error('two equivalent regular def')
                    return None
                temp[0] = temp[0].strip()
                temp[1] = temp[1].strip()
                sym_table[temp[0]] = temp[1]
                logging.debug('added in sym table '+temp[0]+ ' '+sym_table[temp[0]])
        logging.info('started translation')
        for line in lex_lines: #pylint: disable=E1133
            # line = line[0:-1]
            out.append(helpers.replace_all(line,sym_table))
        logging.info(out)
        logging.info('ended translation')

        return out 

if (__name__ == "__main__"):
    import os
    print(os.getcwd())
    x =preproc.transfrom(open('src/preproc_input.txt','r').readlines())
    open('src/preprox_out.txt', 'w+').writelines(x)