## convert CSV data-file to JSON data-file
! python csvutil.py csvjson -t -i 2 _DB_TABLE_.csv  >  _DB_TABLE_.json


import json
import re


## load JSON data-file into Python
Recs = json.loads( open('_DB_TABLE_.json', 'r').read() )
# len(Recs) == 403


## define/compile reg exps for BR tag, and for P tags that are 'blank'
rgex_BR = re.compile(r'<BR\s*/>', re.I)
rgex_PP = re.compile(r'<P>\s*(&NBSP;\s*)*\s*</P>', re.I)


## define list of fields
Fields = '''
description
furtherinfo
references
subjectarea
'''.strip().split()


## count number of BR tags
BR_counts = [len(rgex_BR.findall(r[fld]))  for r in Recs  for fld in Fields]
# sum(BR_counts) == 5190


## SPECIAL CASE: enclose 'subjectarea' values in P tags
## !! NOTE: 'u' (for *Unicode* chars in the JSON data)
## !! [In the APP, need to change 'subjectarea' from a *textarea* to *rich-text editor*]
for r in Recs:
  fld = 'subjectarea'
  r[fld] = u'<P>' + r[fld] + '</P>'


#######################################
## replace <BR/> tags by </P><P> ; etc.
#######################################
for r in Recs:
  for fld in Fields:
    val = rgex_BR.sub('</P><P>', r[fld])  # NOTE: MAIN objective!
    val = rgex_PP.sub('', val)            # some clean-up (determined empirically!)
    r[fld] = val.replace('\t', '')        # remove TAB chars


## build a 'template' from Fields
Fields_TMPL = ",\n".join([
  '`' + fld + '`' + '="{' + fld + '}"'  for fld in Fields
])

## generate SQL
## !! NOTE: 'u' (for *Unicode* chars in the JSON data)
SQL = "\n".join([
  (u'UPDATE _DB_TABLE_ SET ' + Fields_TMPL + ' WHERE id={id};').format(**r)
  for r in Recs
])


## write SQL to file
## !! NOTE: .encode() for *Unicode* chars
with open('_DB_TABLE_.SQL.txt', 'w') as f:
  f.write(SQL.encode('UTF-8'))
