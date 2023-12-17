# Obteniendo bits aletorios o pseudo-aleatorios en Unix

def random_bytes(n, true_random=False):
    """ Retorna n bytes aleatorios usando /dev/urandom """
    source = '/dev/random' if true_random else '/dev/urandom'
    with open(source, 'rb') as file:
        return file.read(n)
    
# imprimiendo 2MB bytes aleatorios
print(random_bytes(2048 * 1024, True).hex())

