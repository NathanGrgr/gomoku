# Gomoku
Le Gomoku, du nom japonais ***gomoku narabe*** signifiant littéralement "alignement des cinq pions", est le nom japonais d'un jeu de plateau chinois, où il est nommé ***Wǔzi qí*** ("l'échiquier des 5") consistant à aligner 5 pions sur les intersections d'un plateau de ***jeu de go*** (ou ***wéiqí, 围棋***)

Il est également connu en France sous le nom de "**Darpion**"
```mermaid
timeline
    title Chronologie des variantes du Gomoku
    1800 : Gomoku : Jeu traditionnel où l'objectif est d'aligner cinq pions consécutifs sur un plateau de 15x15 sans restrictions.
    1900 : Renju : Variante du Gomoku avec des règles supplémentaires pour limiter l'avantage du joueur noir, jouant en premier, et souvent pratiquée en compétition.
    20ème siecle : Free-style Gomoku : Version plus libre du Renju sans restrictions pour le joueur noir, permettant une plus grande flexibilité dans le jeu.
    1990-20-- : Gomoku en ligne : Adaptation numérique du jeu, permettant aux joueurs de s'affronter sur Internet avec des fonctionnalités sociales et compétitives.
```
## Règles du jeu
Se jouant sur un plateau quadrillé virtuel de 15x15,le but sera d'aligner 5 pions sur l'une des intersections du plateau. les joueurs jouent chacun leur tour n'importe où sur le plateau, l'un avec les pions blanc et l'autre avec les pions noir
Si les deux joueurs placent tous leurs pions sans qu'aucun ne parvienne à réaliser un alignement, le jeu est déclaré nul, et ils recommencent. Une partie se dispute généralement en deux manches, afin que celui qui a commencé avec les noirs ait les blancs la seconde fois.
# Contenu du répertoire

|**Fichier**                                    |**Description**                                                  |     
|---                                            |:-:                                                              |
|gomoku/gomoku_avec_bot/gomoku_affichage.py     | Procedure concernant l'affichage de l'interface utilisateur     |  
|gomoku/gomoku_avec_bot/gomoku_fus_bot.py       | Programme  principal doté du bot                                |    
|gomoku/gomoku_sans_bot/gomoku_affichage.py     | Procedure concernant l'affichage de l'interface utilisateur     |      
|gomoku/gomoku_sans_bot/gomoku_fus.py           | Programme principal sans le bot                                 |


# Les bibliothèques utilisées 

|**Bibliothèque**  |**Description**                              |     
|---               |:-:                                          |
|Tkinter           | gestion d'interface utilisateur             |  
|Random            | permet de generer des positions aléatoires  |    
|Imagetk           | affichage d'image                           |      
|gomoku_affichage  |gère l'affichage de l'interface utilisateur  |


# Stratégies de base
Meme si le jeu semble simple, il existe des stratégies complexes que les joueurs peuvent utiliser tel que:
> Double menace : un coup qui crée deux alignements possibles de cinq pions.
>> Contrôle du centre : comme au go, le contrôle des intersections centrales offre souvent un avantage.
>>> Blocage de l'adversaire : une bonne défense consiste à bloquer les alignements de l'adversaire avant
qu'il ne parvienne à placer ses cinq pions.
