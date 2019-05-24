import xlrd
from fanti import Simplified2Traditional
from youdao import translateEnglish
from xlutils.copy import copy

workbook = xlrd.open_workbook(u'edit.xlsx')
wb = copy(workbook)
table= workbook.sheet_by_name('edit')
# rows = sheet2.row_values(3) # 获取第四行内容
cols1 = table.col_values(0) # 获取第二列内容
# cols2 = table.col_values(1) # 获取第二列内容
cols3 = table.col_values(2) # 获取第二列内容
# print(cols1)
# print(cols2)
# print(cols3)

for idx, val  in enumerate(cols3):
  if not val:
    en = translateEnglish(cols1[idx])
    gb = Simplified2Traditional(cols1[idx])
    print(idx, val, '----', en, '------', gb)
    # wb.write(idx, 2, en)
    # wb.write(idx, 3, gb)
    # wb.save('edit.xlsx')
#   print(col, '----------' ,Simplified2Traditional(col))