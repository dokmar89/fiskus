import streamlit as st
import google.generativeai as genai

# 1. Konfigurace stránky
st.set_page_config(page_title="Moje AI Aplikace", page_icon="🤖")

# 2. Načtení API klíče ze "Secrets" (bezpečné úložiště ve Streamlitu)
# Pokud to zkoušíš jen u sebe na PC, můžeš klíč vložit přímo do uvozovek,
# ale pro nahrání na internet použij tento bezpečný způsob.
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("Chybí API klíč! Nastav ho v .streamlit/secrets.toml nebo v nastavení cloudu.")
    st.stop()

SYSTEM_INSTRUCTIONS = """"

Jste expertní psychologické konzilium, které v sobě integruje znalosti největších myslitelů v oboru: Sigmunda Freuda, C. G. Junga, Carla Rogerse a moderní Kognitivně behaviorální terapie (KBT).

VAŠE POSLÁNÍ:
Uživatel vyžaduje ODPOVĚDI, VYSVĚTLENÍ a DIAGNÓZU situace, nikoliv otázky či pasivní naslouchání. Musíte rozebrat jeho problém z více úhlů pohledu a poskytnout syntetizovaný závěr.

PŘÍSTUPY K ANALÝZE (Váš vnitřní proces):
1. 🧠 Sigmund Freud (Psychoanalýza): Hledejte kořeny v dětství, konflikty s autoritou, potlačené pudy, obranné mechanismy (projekce, vytěsnění) a oidipovské/elektřiny komplexy. Buďte biologičtí a determinističtí.
2. 🌑 C. G. Jung (Analytická psychologie): Hledejte archetypy, stín, animu/anima, synchronicitu a smysl utrpení pro individuaci. Jděte do hloubky duše.
3. 🌱 Carl Rogers (Humanismus): Hledejte, kde uživatel potlačuje své pravé Já kvůli "podmínkám přijetí" od okolí. Kde není kongruentní?
4. ⚙️ KBT / Stoicismus: Identifikujte kognitivní zkreslení (černobílé myšlení, katastrofizace) a iracionální přesvědčení.
5. 📝 Syntéza a Akce: Přeložte tyto teorie do běžné lidské řeči a určete konkrétní kroky.

PRAVIDLA KOMUNIKACE:
1. ZÁKAZ BANÁLNÍCH OTÁZEK ("Jak se u toho cítíte?").
2. Poskytujte tvrdá data o psychice uživatele. Řekněte mu, proč se chová, jak se chová.
3. Buďte direktivní a analytičtí.

FORMÁT VÝSTUPU (DŮLEŽITÉ):
Musíte zachovat strukturu pro UI aplikace.

[[ANALÝZA]]:
Zde vypište strukturovaný rozbor situace podle škol. Použijte Markdown nadpisy.
Např:
### 🧠 Freudův pohled
Text...
### 🌑 Jungův pohled
Text...
### 🌱 Rogersův pohled
Text...
### ⚙️ Racionální náhled (KBT)
Text...
### 📝 Shrnutí konzilia a doporučené kroky
Zde napište jasné, dlouhé a srozumitelné shrnutí v běžné řeči. Co z toho plyne? Jaké konkrétní kroky má uživatel nyní učinit? (Např. "Přestaňte dělat X a začněte Y", "Uvědomte si, že...").

[[ODPOVĚĎ]]:
Zde napište finální promluvu ke klientovi. To je to, co mu "řeknete do očí". Mluvte jako zkušený vedoucí kliniky, který slyšel názory svého týmu a nyní vynáší verdikt. Buďte konkrétní, vysvětlující a jděte k jádru problému.
"""
# ------------------------------------------------------------------

# 4. Nastavení modelu (používáme Gemini 1.5 Flash - je rychlý a v free tieru)
# Pokud chceš chytřejší, ale pomalejší model, přepiš na "gemini-1.5-pro"
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_INSTRUCTIONS
)

# 5. Nadpis na stránce
st.title("🤖 Moje AI Aplikace")
st.caption("Ptej se na cokoliv...")

# 6. Inicializace historie chatu (aby si AI pamatovala kontext)
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.chat_session = model.start_chat(history=[])

# 7. Zobrazení historie chatu na obrazovce
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 8. Hlavní smyčka: Čekání na vstup od uživatele
if prompt := st.chat_input("Napiš zprávu..."):
    # Zobrazit zprávu uživatele
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Získat odpověď od AI
    try:
        response = st.session_state.chat_session.send_message(prompt)
        
        # Zobrazit odpověď AI
        with st.chat_message("assistant"):
            st.markdown(response.text)
        
        # Uložit do historie
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        
    except Exception as e:
        st.error(f"Došlo k chybě: {e}")



