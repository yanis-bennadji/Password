import re
import hashlib
while True :
    mdp = input("Veuillez entrer votre mot de passe avec les spécificités suivantes :" )
    if (len(mdp) <= 8):
        print("Le mot de passe est trop court.")
    
    elif not re.search("[a-z]", mdp):
        print("Le mot de passe ne contient pas de minuscule.")

    elif not re.search("[A-Z]", mdp):
        print("Le mot de passe ne contient pas de majuscule.")

    elif not re.search("[0-9]", mdp):
        print("Le mot de passe ne contient pas de chiffre.")

    elif not re.search("[!@#$%^&*]", mdp):
        print("Le mot de passe ne contient pas de caractère spéciale.")

    else:
        print("Le mot de passe est valide")
        break

mdp = mdp.encode()
crypt = hashlib.sha256(mdp)
mdp = crypt.hexdigest()
print("Voici votre mot de passe crypté :\n", mdp)