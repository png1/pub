import csv
import json
import string


#############################
## heuristic/'scoring' Method -- also see: {heuristic_method}
#############################
class EmailAddr(object):
  ## !! NOTE: in order of *increasing* score
  Domains = '''
  @_STAFF_
  @_XSEED_
  ~~OTHER~~
  @_ROSLI_
  @_ALIAS_
  '''.split()

  @staticmethod
  def getScore(s):
    if len(s.strip()) == 0:  return -1 # -1 if s is BLANK
    _sc = [idx  for idx, emDom in enumerate(EmailAddr.Domains)  if emDom in s]
    return _sc[0]  if len(_sc) > 0  else EmailAddr.Domains.index('~~OTHER~~')

  @staticmethod
  def getEmail_MAX(listEmails):
    return max(
      [{'email':em, 'score': EmailAddr.getScore(em)}  for em in listEmails],
      key=lambda x: x['score']
    )['email']

  @staticmethod
  def getEmail_UPDATE(email_OLD, email_NEW):
    # i.e. don't update if BLANK!
    return email_NEW  if EmailAddr.getScore(email_NEW) >= 0  else email_OLD


## normalise Strings; then compare them 
#######################################
## // from: RECON script

# http://stackoverflow.com/questions/16474848/python-compare-strings-ignore-special-characters
#
# !! "translate() takes exactly one argument (2 given)"
#     .encode() ~ http://stackoverflow.com/questions/11692199/string-translate-with-unicode-data-in-python
def str_NORM(s, needUpper=False):
  # ORIG: (None, string.punctuation + string.whitespace)
  s2 = s.encode('utf-8').translate(None, string.whitespace)
  return s2.upper() if needUpper else s2.lower()
## **strCmpNORM
def strCmpNORM(s1, s2):
  return str_NORM(s1) == str_NORM(s2)


## get_OC() and get_UX()
########################
## // from: UPDATE script
def get_OC(empNUM, needMultiple=False):
  res = [oc for oc in OC if oc['Employee Number'] == str(empNUM)] # both are 'str' types
  if not needMultiple:
    if len(res) == 0:  return {}
    return res[0]
  else: # SORT by *multiple* keys: fun_finCostCentre, ...
    return sorted(res, key=lambda x: (x['fun_finCostCentre'],x['fun_finAccCode'],x['fun_finGrantNum']))

def get_UX(empNUM):
  res = [ux for ux in UX if ux['empNum'] == str(empNUM)]
  if len(res) == 0:  return {}
  return res[0]

  
## load INPUT files
###################
RECS = json.loads(open('_recs.json','r').read())  # 'empNUM'  'uun'  'email'
OC = ...                                          # 'Employee Number'  'Uun'  'Email Address'
UX = ...                                          # 'empNum'  'UUN'  'email'


################
## build Results
################
Results = []
for r in RECS:
  oc = get_OC(r['empNUM'])
  ux = get_UX(r['empNUM'])
  email_REC = r['email']
  email_OC = oc['Email Address']  if 'Email Address' in oc  else ''
  email_UX = ux['email']  if 'email' in ux  else ''
  
  email_MAX = EmailAddr.getEmail_MAX([email_OC, email_UX]) ## part of {heuristic_method}

  MAXscore = EmailAddr.getScore(email_MAX) ## part of {heuristic_method}
  RECscore = EmailAddr.getScore(email_REC) ## part of {heuristic_method}

  Results.append({
    'pnID': r['pnID'],
    'uun': r['uun'],
    'empNUM': r['empNUM'],

    'firstname': r['firstname'],
    'surname': r['surname'],

    'email_REC': email_REC,
    'email_OC': email_OC,
    'email_UX': email_UX,

    'email_MAX': email_MAX,
    'MAXscore__EQ__RECscore': 'Y'  if MAXscore == RECscore  else '',
    'MAXscore__LT__RECscore': 'Y'  if MAXscore < RECscore  else '',

    'email_DIFF': 'Y'  if not strCmpNORM(email_REC, email_MAX)  else '',

    'email_UPDATE': EmailAddr.getEmail_UPDATE(email_REC, email_MAX) ## part of {heuristic_method}
  })

Results = sorted(Results, key=lambda r: (r['surname'].upper(), r['firstname'].upper()))


## output Results to JSON file
##############################
with open('EmailAddr.json','w') as f:
  f.write( json.dumps(Results) )


## output Results to CSV file
#############################

FIELDS = '''
pnID
uun
empNUM
firstname
surname
email_REC
email_OC
email_UX
email_MAX
MAXscore__EQ__RECscore
MAXscore__LT__RECscore
email_DIFF
email_UPDATE
'''.split()

## !! NOTE: BINARY 'b' mode ~ http://stackoverflow.com/questions/3191528/csv-in-python-adding-an-extra-carriage-return
with open('EmailAddr.csv','wb') as f:
  dw = csv.DictWriter(
    f,
    fieldnames = FIELDS
  )
  dw.writeheader()
  dw.writerows( Results )
