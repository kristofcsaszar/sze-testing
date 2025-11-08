## A projekt beállítás

- Nyisd meg a Visual Studio Code alkalmazást
- Nyiss egy új terminált és válaszd ki a git bash opciót
- Forkold ezt a GitHub repository-t, majd klónozhatod a helyi gépedre: [Github projekt](https://github.com/CsDenes/sze-test-lab/tree/main)

```bash
git clone https://github.com/<felhasznalo>/sze-testing/tree/main
```

### Telepítés

Nyiss meg egy terminált és futtasd a következő parancsokat, amivel létrehozunk egy python virtuális környezetet és telepítjuk a szükséges csomagokat.

```bash
# Hozz létre és aktiválj egy virtuális környezetet
python -m venv venv
source venv/Scripts/activate

# Telepítsd a szükséges könyvtárakat
pip install flask pytest pytest-bdd locust gunicorn flask-cors

```

A TDD-ben mindig egy hibát produkáló (failing) teszt megírásával kezdünk. Ez a teszt határozza meg, hogy mit várunk el a kódunktól

A teszt a `test_app.py` fileban található

Az Flask web alkalmazás a következővel paranccsal futtatható:

```bash
flask run
```

Majd az alkalmazás böngészőben itt megnyitható: `http://127.0.0.1:5000`


Feladatok

- [1. TDD](tdd/README.md)
- [2. BDD](bdd/README.md)
- [3. Pipeline fejlesztés](pipeline/README.md)
- [4. API tesztelés](api/README.md)
- [5. Load tesztelés](load/README.md)
- [6. UI tesztelés](ui/README.md)