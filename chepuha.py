import re


text = """Жирафы любят таскать
 различные __СУЩЕСТВИТЕЛЬНОЕ ВО МНОЖЕСТВЕННОМ ЧИСЛЕ__
 целый день напролет. Жирафы
 также славятся тем, что поедают
 прекрасные __СУЩЕСТВИТЕЛЬНОЕ ВО МНОЖЕСТВЕННОМ ЧИСЛЕ__, но
 после этого у них часто
 болит __ЧАСТЬ_ТЕЛА__. Если же
 жирафы находят __ЧИСЛО__
 __СУЩЕСТВИТЕЛЬНОЕ ВО МНОЖЕСТВЕННОМ ЧИСЛЕ__, у
 них моментально отваливается __ЧАСТЬ ТЕЛА__.
"""


def mad_libs(mls):
    """
    :param mls: В строках
    пользовательский ввод
    должен быть окружен двойными
    подчеркиваниями. Подчеркивания
    нельзя вставлять в подсказку:
    __подсказка_подсказка__ (нельзя);
    __подсказка__ (можно).
    """
    hints = re.findall("__.*?__",
                      mls)
    if hints is not None:
        for word in hints:
            q = "Введите {}"\
                   .format(word)
            new = input(q)
            mls = mls.replace(word,
                              new)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("ошибка ввода")

mad_libs(text)
