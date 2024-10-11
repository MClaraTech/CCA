#1. Crie um autômato finito determinístico (AFD) que reconheça a linguagem sobre o alfabeto {0, 1}, onde todas as strings terminam com "1".

def afd_com_1(s):
    return s.endswith('1')

#2. Implemente um AFD que reconheça strings com número par de '0's sobre o alfabeto {0, 1}.

def afd_par_zeros(s):
    count = s.count('0')
    return count % 2 == 0

#3. Construa um AFD que reconheça a linguagem de strings que contenham exatamente dois '1's sobre o alfabeto {0, 1}.

def afd_dois_1s(s):
    return s.count('1') == 2

#4. Desenvolva um AFD que aceite strings com pelo menos um '0'.

def afd_um_zero(s):
    return '0' in s

#5. Implemente em Python um AFD que aceite qualquer string binária que comece e termine com o mesmo caractere.

def afd_comTer_mesmo_caractere(s):
    return len(s) > 0 and s[0] == s[-1]

#6. Construa um autômato finito não-determinístico (AFN) que aceite strings que contenham pelo menos um '0' sobre o alfabeto {0, 1}.

def afn_um_zero(s):
    return '0' in s

#7. Implemente um AFN que reconheça strings que comecem com '01' e terminem com '10'.

def afn_com_01_ter_10(s):
    return s.startswith('01') and s.endswith('10')

#8. Desenvolva um AFN que aceite strings onde o número de '0's é divisível por 3.

def afn_zeros_div_por_tres(s):
    return s.count('0') % 3 == 0

#9. Construa um AFD em Python que reconheça strings contendo a sequência "101".

def afd_sequencia_101(s):
    return '101' in s

#10. Implemente um AFN que aceite qualquer string que tenha pelo menos um '0' seguido de pelo menos um '1'.

def afn_0_seg_de_1(s):
    return '01' in s

#11. Construa um AFD para uma linguagem sobre o alfabeto {a, b}, que reconheça strings com um número ímpar de 'a's.

def afd_impar_as(s):
    return s.count('a') % 2 != 0

#12. Implemente um AFN que reconheça strings binárias contendo a substring '110'.

def afn_sub_110(s):
    return '110' in s

#13. Desenvolva um AFD que reconheça strings binárias onde o número de '1's seja maior que o número de '0's.

def afd_maior_1s_que_0s(s):
    return s.count('1') > s.count('0')

#14. Crie um AFN que aceite strings binárias onde as substrings "11" e "00" não aparecem.

def afn_nao_11_e_nao_00(s):
    return '11' not in s and '00' not in s

#15. Implemente um AFN que reconheça a linguagem de todas as strings sobre {a, b} com comprimento par.

def afn_comp_par(s):
    return len(s) % 2 == 0

#16. Construa um AFD para reconhecer strings sobre {0, 1} onde os '0's aparecem em blocos consecutivos.

def afd_bloc_consec_zeros(s):
    zeros_blocks = [block for block in s.split('1') if block]
    return all('0' in block for block in zeros_blocks)

#17. Implemente em Python a conversão de um AFN para um AFD para um autômato que reconhece strings terminadas em '01'.

def afn_para_afd_term_em_01(s):
    return s.endswith('01')

#18. Desenvolva um AFD que reconheça a linguagem de strings sobre {0, 1} com número ímpar de '0's e '1's.

def afd_impar_zeros_e_um(s):
    return s.count('0') % 2 != 0 and s.count('1') % 2 != 0

#19. Construa um AFN que reconheça a linguagem de todas as strings binárias que contenham a substring '010'.

def afn_contem_010(s):
    return '010' in s

#20. Implemente um AFD para strings sobre {a, b} onde a sequência 'ab' aparece exatamente uma vez.

def afd_uma_vez_ab(s):
    return s.count('ab') == 1

#21. Implemente um AFN que aceite todas as strings sobre {a, b} que tenham um 'a' após cada 'b'.

def afn_a_ap_b(s):
    return all('a' in s[i+1:] for i in range(len(s)) if s[i] == 'b')

#22. Desenvolva um AFD que reconheça uma linguagem onde a diferença entre o número de 'a's e 'b's seja múltipla de 3.

def afd_difer_multi_de_3(s):
    return (s.count('a') - s.count('b')) % 3 == 0

#23. Construa um AFN que aceite qualquer string que contenha a sequência "101" ou "110" sobre {0, 1}.

def afn_sequencia_101_ou_110(s):
    return '101' in s or '110' in s

#24. Implemente um AFD que aceite strings sobre {0, 1} onde a sequência "010" aparece pelo menos duas vezes.

def afd_010_2_vezes(s):
    return s.count('010') >= 2

#25. Crie um AFN que reconheça strings sobre {a, b} onde todas as ocorrências de 'a' aparecem antes de todas as ocorrências de 'b'.

def afn_as_ant_de_bs(s):
    return 'ba' not in s


