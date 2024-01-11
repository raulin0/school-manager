from validate_docbr import CPF


def is_valid_cpf(cpf_number):
    cpf = CPF()
    if cpf.validate(cpf_number):
        return True
    return False


def is_valid_name(name):
    if not name.isalpha():
        return True
    return False
