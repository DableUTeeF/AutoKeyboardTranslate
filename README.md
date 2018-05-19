# AutoKeyboardTranslate
Thai Kedmani <-> En-US\
Add path to this directory then `chmod +x translate.py`
# Run
`translate.py -l {l} -m {m} -w {w}`

     l -> ['t', 'e', 'en', 'th']
          Input language. 
          Return thai if input 'e' or 'en', english if input 'th' or 't'.
     m -> [1, 0]
          Numpad mode.
          Will return something like "`1`" if input maybe numpad key.
     w -> Input word.
     