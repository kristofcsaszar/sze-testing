# Pipeline

Miután az alkalmazás helyesen működik és minden teszt sikeres, automatizáljuk a tesztelési folyamatot. Hoz létre egy GitHub Actions pipeline-t, amely minden push és pull_request eseménykor a main ágra automatikusan lefuttatja az összes tesztet.

1. Definiáld a függőségeket

Hozd létre a projekt gyökérkönyvtárában a `requirements.txt` fájlt a következő tartalommal. Ez a fájl mondja meg a GitHub Actions-nek, hogy milyen Python csomagokat kell telepítenie.

```bash
flask
pytest
pytest-bdd
```

2. A workflow fájl létrehozása

A projekt gyökérkönyvtárában hozd létre a .github/workflows/ mappaszerkezetet. Ezen belül hozz létre egy ci.yml nevű fájlt.

3. A pipeline kódjának megírása

`.github/workflows/ci.yml`

- Add hozzá a triggert: `on`

- Hozd létre a `job`-ot

1. lépés hozzáadása ami letölti a repository kódját

2. lépés hozzáadása ami beállítja a python-t (`actions/setup-python@v4`)

3. lépés a függőségek telepítése (`pip install -r requirements.txt`)

4. lépés a tesztek futtatása

4. Státusz-jelvény (Status Badge) hozzáadása

Hogy a projekt főoldalán is látható legyen a tesztek aktuális állapota, adj hozzá egy státusz-jelvényt.

- Nyisd meg a repository-t a böngészőben, és kattints az Actions fülre.

- Válaszd ki a bal oldali listából az elkészített workflow-t.

- Kattints a "..." menüre a jobb felső sarokban, majd a Create status badge opcióra.

- Másold ki a felugró ablakból a Markdown kódot.

- Illeszd be a kimásolt kódot a README.md fájlod legelejére.
