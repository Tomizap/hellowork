from hellowork import HelloWork

# Andie Matondo nivesmatondo@gmail.com Bowhokodia45?
# Sainte fleur koudiata koudiatasaintefleur@gmail.com Koudiata_14
# Mirna mirnaelhosary932@gmail.com MirnaMirna93270%

config = {
#   "_id": "",
  "name": "Auto Apply Indeed Test",
  # "description": "",
  # "website": "indeed.com",
  # "message": "",
  "urls": [
    f"https://www.hellowork.com/fr-fr/emploi/recherche.html?k=vente&k_autocomplete=vente&l=%C3%8Ele-de-France&l_autocomplete=http%3A%2F%2Fwww.rj.com%2Fcommun%2Flocalite%2Fregion%2F11&ray=20&c=Alternance&msa=&cod=all&d=all&c_idesegal=",
    f"https://www.hellowork.com/fr-fr/emploi/recherche.html?k=commerce&k_autocomplete=commerce&l=%C3%8Ele-de-France&l_autocomplete=http%3A%2F%2Fwww.rj.com%2Fcommun%2Flocalite%2Fregion%2F11&ray=20&c=Alternance&msa=&cod=all&d=all&c_idesegal="
  ],
  "user": {
    "email": "mirnaelhosary932@gmail.com",
    "password": "MirnaMirna93270%",
    "phone": "0621596610",
    "cv": f"D:\\CODE\\python\\packages\\hellowork\\CV\\CV Mirna El Hosary.pdf"
  },
  "setting": {
    "excluded_keywords": [
      'formation',
      'bts',
      "diplome",
      "bachelor"
    ],
    "excluded_companies": [
      "iscod",
      "aston",
      "ascencia",
      "iffp",
      "ifcv",
      "efht",
      "euridis",
      "talia.fr",
      "institut de management",
      "formation",
      "ima business",
      "iag",
      "enaco",
      "institut des langues",
      "studi cfa",
      "talentis",
      "propulsup",
      "france métiers",
      "institut des compétences",
      "f2i",
      "groupe alternance",
      "school",
      "college",
      "école",
      "education",
      "ecole",
      "cfa",
      "campus",
      "recrutement"
    ],
    "infinite": True,
    "scrap": False,
    "presets": {
      "phone": "0621596610",
      "name": "Mirna",
      "nom": "Mirna",
      "pays": "fr",
      "postal": "93270",
      "ville": "Sevran",
      "adresse": "Sevran 93270",
      "mail": "koudiatasaintefleur@gmail.com",
      # "linkedin": "https://www.linkedin.com/in/tom-zapico/"
    }
  },
  # "usersAccess": [
  #   "student@alter-recrut.fr"
  # ],
  # "status": "inactif",
  # "active": False,
  # "result": {
  #   "success": 0,
  #   "error": 0,
  #   "attempt": 0
  # },
  "data": []
}
HelloWork(config).application_loop()
