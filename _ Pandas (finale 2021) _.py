from api import *


# Fonction appelée au début de la partie
def partie_init():

    pass


# Fonction appelée à chaque tour
def jouer_tour():


    # Repérage des pandas
    global x_start, y_start
    x_start, y_start = position_panda(moi(), tour_info.id_panda_joue)


    # Cette fonction fait 1 case d'un chemin vers un objectif sur la carte
    def case_adj(x_chemin, y_chemin, x_obj, y_obj):

        # L'on regarde d'abord les directions ...
        gauche = x_obj > x_chemin
        droite = not(gauche)
        haut = y_obj > y_chemin
        bas = not(haut)

        # ... puis, on calcule les coordonnées de la destination en fonction des 4 cas possibles

        if gauche and haut:
            dest = (x_chemin - 1, y_chemin - x_chemin % 2)
            direc = direction.NORD_OUEST

        if gauche and bas:
            dest = (x_chemin - 1, y_chemin + x_chemin % 2)
            direc = direction.SUD_OUEST

        if droite and haut:
            dest = (x_chemin + 1, y_chemin - x_chemin % 2)
            direc = direction.NORD_EST

        if droite and bas:
            dest = (x_chemin + 1, y_chemin + x_chemin % 2)
            direc = direction.SUD_EST

        return (dest, direc)


    # Nous cherchons le bébé panda le plus proche
    def proche():

        # La carte est trop petite pour être à plus de 1000 cases
        dist_min = 1000

        # L'on passe toute la liste des bébés pandas alliés
        nb_bebes = len(liste_bebes()) // 2
        num_bebe = 0
        for beb in liste_bebes()[nb_bebes * moi():nb_bebes * (moi() + 1)]:

            # Prise des positions
            x_obj, y_obj = beb.bebe_pos
            x_chemin, y_chemin = (x_start, y_start)

            # Tant que nous ne sommes pas arrivés au bébé panda ...
            while (x_chemin, y_chemin) != (x_obj, y_obj):
                # ... s'en rapprocher
                x_chemin, y_chemin = case_adj(x_chemin, y_chemin, x_obj, y_obj)
                dist += 1

            # On garde l'information si la distance est minimale
            if dist < dist_min:
                dist_min = dist
                bebe_min = num_bebe

            num_bebe += 1

        return bebe_min


    # Ce sous-programme là permet de se déplacer (si possible) d'une case vers le bébé voulu
    def depl():

        # Coordonnées d'arrivée
        x_fin, y_fin = liste_bebes()[proche()].bebe_pos

        # Prochaine case
        dest, direc = case_adj(x_start, y_start, x_fin, y_fin)

        # Vérification de la possibilité de passage
        if type_case(dest) == case_type.PONT:

            # Calcul des hauteurs des cases
            ici = info_pont((x_start, y_start))
            devant = info_pont(dest)


            """
                Ici nous regardons si la case où l'on est
                est le début ou la fin d'un pont,
                pour ainsi prendre sa valeur ...
            """

            if ici.debut_pos == (x_start, y_start):
                ici_nb = ici.debut_val
            else:
                ici_nb = ici.fin_val

            # ... même chose pour la case de destination
            if devant.debut_pos == dest:
                devant_nb = devant.debut_val
            else:
                devant_nb = devant.fin_val

            # Cas où un pont permet le passage ou bien les terres sont à la même hauteur
            if ici == devant or ici_nb == devant_nb:

                deplacer(direc)

            # Nous gardons les infos sur la case pour construire un pont plus tard
            return (dest, direc)


    # Et pour finir, nous jouons enfin notre tour
    dest, direc = depl()
    poser(dest, direc, 1, 1)
    _ = depl()

    pass


# Fonction appelée à la fin de la partie
def partie_fin():

    pass
