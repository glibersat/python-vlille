Python-Vlille
=============

Ce module permet d'accéder aux informations du système de vélos en
libre service (VLS) de Lille : le VLille ( http://vlille.fr )

Les informations suivantes sont accessibles pour chaque station :
  * Nom
  * Adresse
  * Position géographique (lat, long)
  * Nombre de vélos disponibles
  * Nombre d'attaches
  * État de la station (en maintenance, ...)
  * Les modes de paiement acceptés
  * La date de dernière mise à jour

Pour l'instant, les données sont quasiment identiques à celles du XML
brut, n'hésitez pas à soumettre des patchs pour rendre l'interface
plus pythonique.

Il n'y a plus qu'à montrer que l'on peut intelligemment exploiter les
données ouvertes :-)

Exemple de code
---------------

 v = Vlille()

 v.load_stations()

 print v.stations[0]

 <Station: Lille Metropole - LMCU RUE DU BALLON>

Licence
-------

GNU GPL v3 (voir le fichier COPYING)

Auteurs/Contributeurs
---------------------

Guillaume Libersat <glibersat@sigill.org>






