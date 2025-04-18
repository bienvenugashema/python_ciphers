import random

import secrets

# Public area

g = 5

n = 4000#should be bigg in real world

#Alice

alice_key = secrets.randbelow(n)


#Bob

bob_key = secrets.randbelow(n)

#alice sharing key

a = pow(g,alice_key,n)

#bob sharing key

b = pow(g, bob_key, n)

#secrete alice

sec_alice = pow(b, alice_key, n)
sec_bob = pow(a, bob_key, n)

print(sec_alice)
print(sec_bob)