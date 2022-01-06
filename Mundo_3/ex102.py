def fatorial(num=0, show=False):
    """
  -> Calcula o Fatorial de um número.
  :param num: O número a ser calculado.
  :param show: (Opcional) Mostrar ou não o desenvolvimento da conta.
  :return: O valor do Fatorial de um número num.
  """
    f = 1
    c = num
    if not show:
        while c > 0:
            f *= c
            c -= 1

    else:
        while c > 0:
            print(f'{c}', end='')
            print(' x ' if c > 1 else ' = ', end='')
            f *= c
            c -= 1
    return f


print(fatorial(5, True))
print(fatorial(5))
help(fatorial)
print(fatorial(6, True))
print(fatorial(6))
