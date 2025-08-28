#!/usr/bin/env python3

import sys
import os
import subprocess
import shutil

# Configuration des chemins - à modifier selon vos besoins
COURS_SOURCE_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/Cours/"  # Répertoire contenant cours.tex
COURS_DEST_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/Site/Cours/"   # Répertoire de destination pour les chapitres


SLIDES_SOURCE_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/Cours/"  # Répertoire contenant slides.tex
SLIDES_DEST_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/Site/Slides"   # Répertoire de destination pour les slides

EXERCICES_SOURCE_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/ExosFiches/"  # Répertoire contenant fiche_chapitre.tex
EXERCICES_DEST_DIR = "/Users/olivier/Dropbox/Work/Prepa/MPI/Maths/Site/Exercices/"   # Répertoire de destination pour les exercices

def compile_latex(source_dir, tex_file):
    """Compile un fichier LaTeX avec pdflatex"""
    # Changer vers le répertoire source
    original_dir = os.getcwd()
    os.chdir(source_dir)
    
    try:
        # Compilation avec pdflatex
        result = subprocess.run(['pdflatex', tex_file], 
                              capture_output=True, text=True)
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

def main():
    # Vérification des arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <mot_clef> <numero>")
        print("Mots-clés disponibles: cours, slides")
        sys.exit(1)
    
    keyword = sys.argv[1]
    try:
        chapter_num = int(sys.argv[2])
    except ValueError:
        print("Le second argument doit être un nombre entier")
        sys.exit(1)
    
    # Traitement selon le mot-clé
    if keyword == "cours":
        success = process_cours(chapter_num)
    elif keyword == "slides":
        success = process_slides(chapter_num)
    elif keyword == "exercices":
        success = process_exercices(chapter_num)
    else:
        print(f"Mot-clé '{keyword}' non reconnu")
        print("Mots-clés disponibles: cours, slides")
        sys.exit(1)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
