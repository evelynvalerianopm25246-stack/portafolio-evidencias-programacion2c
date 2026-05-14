"""
Trabajas en la organizacion de un evento de precios.
Tienes una lista de celebridades que entraran por la alfombra roja.
El orden es vital.
1. Crea una lista llamada invitados con los nombres:"Robert Downy Jr",
"Emma Stone" y "Cillian Murphy"
2. llegada de ultimo minuto. Agrega a "zendays" al final de la lista.
3. invitado VIP, "Steven Spleber" acaba de llegar y debe ir al principio de la lista.
4. cancelacion",."Emma Stone" avisa que no podria asistir.
5. seguridad. El ultimo de la lista se porto mal y debo ser retirado
6. Imprime la lista final y cuantos invitados quedan en total.
"""

#punto no.1
Invitados =["Robert Downy Jr","Emma Stone","Cillian Murphy"]
#punto no.2
Invitados.append("zendaya")
#punto no.3
Invitados.insert(0,"Steven Splelberg")
#punto no.4
#Invitados.pop(2)
Invitados.remove("Emma Stone")
#punto no.5
Invitados.pop(3) #Invitados.pop
