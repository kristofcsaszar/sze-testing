## TDD

A TDD egy olyan szoftverfejlesztési folyamat, amely egy nagyon rövid fejlesztési ciklus ismétlésén alapul:

- Piros: Írj egy olyan tesztet az új funkcióhoz, ami hibát ad.
- Zöld: Írd meg a teszt átmenetéhez szükséges minimális kódot.
- Refaktor: Tisztítsd meg a kódot, miközben gondoskodsz róla, hogy minden teszt továbbra is átmenjen.

Ez az iteratív folyamat biztosítja, hogy minden kódot teszt támogasson, ami robusztusabb és könnyebben karbantartható alkalmazásokhoz vezet.

## Feladatok

1. Futtasd a teszteket `pytest` segítségével

```
pytest
```

2. Hozd működésbe a tesztet (a "ZÖLD" fázis), írd meg a lehető legkevesebb kódot, ami ahhoz szükséges, hogy a teszt sikeres legyen

3. Fejleszd tovább az alkalmazást hogy képes legyen új TODO elem hozzáadására

- Készítsd el először a tesztet a `test_app.py` fájlban
- Implementáld a POST hívást a `/todos` végponton is is az `app.py` fájlban
- Futtasd az alkalmazást és küldj POST hívást a `todos` végpontra  
  
  `curl -X POST -H "Content-Type: application/json" -d '{"task": "Finish the project"}' http://127.0.0.1:5000/todos`
