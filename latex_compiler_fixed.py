#!/usr/bin/env python3

import sys
import os
import subprocess
import shutil

# Configuration des chemins - à modifier selon vos besoins
COURS_SOURCE_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/Cours/"  # Répertoire contenant cours.tex
COURS_DEST_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/Site/Cours/"   # Répertoire de destination pour les chapitres

FICHES_SOURCE_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/Cours/"  # Répertoire contenant fiche_recap.tex
FICHES_DEST_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/Site/FichesRecap/"   # Répertoire de destination pour les fiches récapitulatives


SLIDES_SOURCE_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/Cours/"  # Répertoire contenant slides.tex
SLIDES_DEST_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/Site/Slides"   # Répertoire de destination pour les slides

EXERCICES_SOURCE_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/ExosFiches/"  # Répertoire contenant fiche_chapitre.tex
EXERCICES_DEST_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/Site/Exercices/"   # Répertoire de destination pour les exercices

INTERROGATIONS_SOURCE_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/Interrogations/"  # Répertoire contenant interro.tex
INTERROGATIONS_DEST_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/Site/Interrogations/"   # Répertoire de destination pour les interrogations

DS_SOURCE_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/DS/"  # Répertoire contenant ds.tex
DS_DEST_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/Site/DS/"   # Répertoire de destination pour les devoirs surveillés MPI

DSS_SOURCE_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/DS/"  # Répertoire contenant ds.tex
DSS_DEST_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/Site/DS*/"   # Répertoire de destination pour les devoirs surveillés MPI*

DM_SOURCE_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/DM/"  # Répertoire contenant dm.tex
DM_DEST_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/Site/DM/"   # Répertoire de destination pour les devoirs maison MPI

DMS_SOURCE_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/DM/"  # Répertoire contenant dm.tex
DMS_DEST_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/Site/DM*/"   # Répertoire de destination pour les devoirs maison MPI*

def compile_latex(source_dir, tex_file):
    """Compile un fichier LaTeX avec pdflatex"""
    # Changer vers le répertoire source
    original_dir = os.getcwd()
    os.chdir(source_dir)
    
    try:
        # Compilation avec pdflatex - utilisation de errors='replace' pour gérer les problèmes d'encodage
        result = subprocess.run(['pdflatex', tex_file], 
                              capture_output=True, text=True, errors='replace')
        if result.returncode != 0:
            print(f"Erreur lors de la compilation de {tex_file}")
            print(result.stderr)
            return False
    finally:
        os.chdir(original_dir)
    
    return True

def process_cours(chapter_num):
    """Traite la compilation pour le mot-clé 'cours'"""
    tex_file = "cours.tex"
    pdf_file = "cours.pdf"
    new_name = f"chapitre{chapter_num}.pdf"
    
    # Compilation
    if not compile_latex(COURS_SOURCE_DIR, tex_file):
        return False
    
    # Chemin du PDF généré
    source_pdf = os.path.join(COURS_SOURCE_DIR, pdf_file)
    dest_pdf = os.path.join(COURS_DEST_DIR, new_name)
    
    # Déplacement et renommage
    shutil.move(source_pdf, dest_pdf)
    print(f"Fichier créé : {dest_pdf}")
    return True


def process_fiche_recap(chapter_num):
    """Traite la compilation pour le mot-clé 'fiche'"""
    tex_file = "fiche_recap.tex"
    pdf_file = "fiche_recap.pdf"
    new_name = f"fiche{chapter_num}.pdf"
    
    # Compilation
    if not compile_latex(FICHES_SOURCE_DIR, tex_file):
        return False
    
    # Chemin du PDF généré
    source_pdf = os.path.join(FICHES_SOURCE_DIR, pdf_file)
    dest_pdf = os.path.join(FICHES_DEST_DIR, new_name)
    
    # Déplacement et renommage
    shutil.move(source_pdf, dest_pdf)
    print(f"Fichier créé : {dest_pdf}")
    return True


def process_slides(chapter_num):
    """Traite la compilation pour le mot-clé 'slides'"""
    tex_file = "slides.tex"
    pdf_file = "slides.pdf"
    new_name = f"chap{chapter_num}_slides.pdf"
    
    # Compilation
    if not compile_latex(SLIDES_SOURCE_DIR, tex_file):
        return False
    
    # Chemin du PDF généré
    source_pdf = os.path.join(SLIDES_SOURCE_DIR, pdf_file)
    dest_pdf = os.path.join(SLIDES_DEST_DIR, new_name)
    
    # Déplacement et renommage
    shutil.move(source_pdf, dest_pdf)
    print(f"Fichier créé : {dest_pdf}")
    return True

def process_exercices(chapter_num):
    """Traite la compilation pour le mot-clé 'exercices'"""
    tex_file = "fiche_chapitre.tex"
    pdf_file = "fiche_chapitre.pdf"
    new_name = f"chap{chapter_num}_exercices.pdf"
    
    # Compilation
    if not compile_latex(EXERCICES_SOURCE_DIR, tex_file):
        return False
    
    # Chemin du PDF généré
    source_pdf = os.path.join(EXERCICES_SOURCE_DIR, pdf_file)
    dest_pdf = os.path.join(EXERCICES_DEST_DIR, new_name)
    
    # Déplacement et renommage
    shutil.move(source_pdf, dest_pdf)
    print(f"Fichier créé : {dest_pdf}")
    return True

def process_interrogation(chapter_num):
    """Traite la compilation pour le mot-clé 'exercices'"""
    tex_file = "interro.tex"
    pdf_file = "interro.pdf"
    new_name = f"chap{chapter_num}_interrogation.pdf"
    
    # Compilation
    if not compile_latex(INTERROGATIONS_SOURCE_DIR, tex_file):
        return False
    
    # Chemin du PDF généré
    source_pdf = os.path.join(INTERROGATIONS_SOURCE_DIR, pdf_file)
    dest_pdf = os.path.join(INTERROGATIONS_DEST_DIR, new_name)
    
    # Déplacement et renommage
    shutil.move(source_pdf, dest_pdf)
    print(f"Fichier créé : {dest_pdf}")
    return True

def process_ds(num):
    """Traite la compilation pour le mot-clé 'ds'"""
    tex_file = "ds.tex"
    pdf_file = "ds.pdf"
    new_name = f"ds{num}.pdf"
    
    # Compilation
    if not compile_latex(DS_SOURCE_DIR, tex_file):
        return False
    
    # Chemin du PDF généré
    source_pdf = os.path.join(DS_SOURCE_DIR, pdf_file)
    dest_pdf = os.path.join(DS_DEST_DIR, new_name)
    
    # Déplacement et renommage
    shutil.move(source_pdf, dest_pdf)
    print(f"Fichier créé : {dest_pdf}")
    return True

def process_dss(num):
    """Traite la compilation pour le mot-clé 'dss'"""
    tex_file = "ds.tex"
    pdf_file = "ds.pdf"
    new_name = f"ds*{num}.pdf"
    
    # Compilation
    if not compile_latex(DSS_SOURCE_DIR, tex_file):
        return False
    
    # Chemin du PDF généré
    source_pdf = os.path.join(DSS_SOURCE_DIR, pdf_file)
    dest_pdf = os.path.join(DSS_DEST_DIR, new_name)
    
    # Déplacement et renommage
    shutil.move(source_pdf, dest_pdf)
    print(f"Fichier créé : {dest_pdf}")
    return True

def process_dm(num):
    """Traite la compilation pour le mot-clé 'dm'"""
    tex_file = "dm.tex"
    pdf_file = "dm.pdf"
    new_name = f"dm{num}.pdf"
    
    # Compilation
    if not compile_latex(DM_SOURCE_DIR, tex_file):
        return False
    
    # Chemin du PDF généré
    source_pdf = os.path.join(DM_SOURCE_DIR, pdf_file)
    dest_pdf = os.path.join(DM_DEST_DIR, new_name)
    
    # Déplacement et renommage
    shutil.move(source_pdf, dest_pdf)
    print(f"Fichier créé : {dest_pdf}")
    return True

def process_dms(num):
    """Traite la compilation pour le mot-clé 'dms'"""
    tex_file = "dm.tex"
    pdf_file = "dm.pdf"
    new_name = f"dm*{num}.pdf"
    
    # Compilation
    if not compile_latex(DMS_SOURCE_DIR, tex_file):
        return False
    
    # Chemin du PDF généré
    source_pdf = os.path.join(DMS_SOURCE_DIR, pdf_file)
    dest_pdf = os.path.join(DMS_DEST_DIR, new_name)
    
    # Déplacement et renommage
    shutil.move(source_pdf, dest_pdf)
    print(f"Fichier créé : {dest_pdf}")
    return True

def main():
    # Vérification des arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <mot_clef> <numero>")
        print("Mots-clés disponibles: cours, slides")
        sys.exit(1)
    
    keyword = sys.argv[1]
    try:
        num = int(sys.argv[2])
    except ValueError:
        print("Le second argument doit être un nombre entier")
        sys.exit(1)
    
    # Traitement selon le mot-clé
    if keyword == "cours":
        success = process_cours(num)
    elif keyword == "slides":
        success = process_slides(num)
    elif keyword == "exercices":
        success = process_exercices(num)
    elif keyword == "interro":
        success = process_interrogation(num)
    elif keyword == "ds":
        success = process_ds(num)
    elif keyword == "dss":
        success = process_dss(num)
    elif keyword == "dm":
        success = process_dm(num)
    elif keyword == "dms":
        success = process_dms(num)
    elif keyword == "fiche":
        success = process_fiche_recap(num) 
    else:
        print(f"Mot-clé '{keyword}' non reconnu")
        print("Mots-clés disponibles: cours, slides")
        sys.exit(1)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
