import random

# Generando números aleatorios no criptográficos
# 
print(random.randint(1, 100))

# Generando números aleatorios criptográficos - seguros para usarse en criptografía

import secrets

print(secrets.randbelow(100))

