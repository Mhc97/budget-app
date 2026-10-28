## Débogage : un exemple concret

Les tests échouaient avec un TypeError. J'ai lu la dernière ligne
de l'erreur ("Did you mean 'autoflush'?"), trouvé les deux options
mal écrites dans sessionmaker, corrigé la ligne 14 de database.py,
puis relancé pytest : 3 tests passent.

<video controls src="debug-sessionmaker-muet.mp4" title="Title"></video>
