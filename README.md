# Fiskus — nedokončený experiment s AI

Malý experimentální projekt obsahující implementaci průběžných odpovědí generativního modelu a seznam závislostí pro Python.

**Stav:** Starší/nedokončený projekt; uložené soubory netvoří spustitelnou aplikaci v Pythonu.

## Skutečný obsah

- `app.py` navzdory příponě obsahuje importy TypeScriptu a export `streamTherapyResponse` využívající `@google/genai`.
- `requirements.txt` uvádí Streamlit a knihovnu Google pro generativní AI v Pythonu.
- `.devcontainer/devcontainer.json` obsahuje konfiguraci vývojového kontejneru.

## Omezení spuštění

Příkaz `streamlit run app.py` nelze považovat za funkční: soubor není napsaný v Pythonu. Před instalací či nasazením je nutné obnovit zamýšlenou strukturu a zvolit běhové prostředí. Příbuzný experiment s konverzační AI je v `psycholog`; tato kopie není prezentována jako samostatný dokončený produkt.

## Další postup

Zvolit jeden jazyk a běhové prostředí, doplnit chybějící strukturu a ověřit základní průchod odpovědi na fiktivních datech. Přihlašovací údaje poskytovatele patří mimo Git a soukromé klíče nesmějí být v klientském balíčku. Nejde o klinický ani diagnostický nástroj.
