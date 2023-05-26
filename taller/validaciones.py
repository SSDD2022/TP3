import re
# Validaciones

def ValMail (mail):
    EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if mail and not re.match(EMAIL_REGEX, mail):
         return False
    return True
 
def ValCelular (celular):
    CEL_ARG_REGEX = r"(^(?:(?:00)?549?)?0?(?:11|[2368]\d)(?:(?=\d{0,2}15)\d{2})??\d{8}$)"
    if celular and not re.match(CEL_ARG_REGEX, celular):
         return False
    return True

