# Twitter AI Analyzer - API

Benvenuti nel progetto **Twitter AI Analyzer - API**. Questo progetto fornisce un'API che utilizza l'AI per analizzare e migliorare i tweet in base alla loro potenziale viralità. Utilizzando modelli avanzati di Google, l'API è progettata per offrire valutazioni di viralità, feedback dettagliati e suggerimenti per migliorare i tweet.

## Struttura del Progetto

Il progetto è organizzato come segue:
 ```bash
Twitter AI Analyzer - API/
│
├── server/
│   └── server.py
│
├── design/
│   ├── Sequence Diagram.png
│   └── System Diagram.png
│
├── requirements.txt
│
├── .env
│
├── .gitignore
│
└── README.md
```

### `server/`
- **`server.py`**: Il file principale del server Flask che espone l'API per l'analisi dei tweet. Contiene le definizioni delle rotte per valutare la viralità, fornire feedback e migliorare i tweet.

### `design/`
- **`Sequence Diagram.png`**: Diagramma di sequenza che illustra il flusso di dati e le interazioni tra i vari componenti del sistema.
- **`System Diagram.png`**: Diagramma di sistema che mostra l'architettura generale del progetto, inclusi i componenti principali e le loro interazioni.

### `requirements.txt`
File che elenca le dipendenze necessarie per il progetto. È utilizzato per installare tutte le librerie Python richieste.

### `.env`
File di configurazione che contiene variabili d'ambiente sensibili, come le credenziali per l'accesso ai modelli AI. Questo file deve essere configurato localmente e non deve essere incluso nel controllo di versione.

### `.gitignore`
File che specifica quali file e directory devono essere ignorati da Git. Include file temporanei, directory di compilazione, e file di configurazione sensibili.

### `README.md`
Questo file. Fornisce una panoramica del progetto, istruzioni per l'installazione e l'uso, e altre informazioni pertinenti.

## Installazione

1. **Clona il repository:**

   ```bash
   git clone https://github.com/tuo-utente/twitter-ai-analyzer-api.git
   cd twitter-ai-analyzer-api
2. **Installa le dipendenze:**
    Assicurati di avere pip installato. Poi, usa il comando seguente per installare le dipendenze necessarie:
   ```bash
    pip install -r requirements.txt
    ```
3. **Configura le variabili d'ambiente:**
  Crea un file .env nella root del progetto e aggiungi le variabili d'ambiente necessarie. Un esempio di configurazione potrebbe essere:
   ```bash
    GOOGLE_AI_API_KEY=tuo_api_key
    ```
4. **Avvia il server:**
  Per avviare il server Flask, esegui:


   ```bash
    python server/server.py
    ```
## Utilizzo dell'API

L'API **Twitter AI Analyzer** espone un endpoint che consente di inviare un tweet e ricevere una valutazione della viralità, feedback e suggerimenti per migliorare il tweet.

### Endpoint

- **`POST /TAIAPI`**

  Questo endpoint accetta un JSON contenente un tweet e restituisce una valutazione della viralità, feedback e un suggerimento per migliorare il tweet.

### Richiesta

La richiesta deve essere effettuata utilizzando il metodo POST e deve includere un corpo JSON con il campo `tweet_prompt` che contiene il testo del tweet da analizzare.

**Esempio di richiesta:**

```http
POST /TAIAPI
Host: localhost:5000
Content-Type: application/json

{
  "tweet_prompt": "Il tuo tweet qui"
}
```
### Risposta
La risposta dell'API sarà in formato JSON e conterrà tre campi: viralità, feedback, e improve.

**Esempio di risposta:**
```http
{
  "viralità": "4/10",
  "feedback": "Il tweet ha un messaggio positivo e incoraggiante, che può risuonare bene con chi cerca ispirazione per la giornata. Tuttavia, potrebbe non avere un impatto virale elevato poiché è piuttosto generico e privo di elementi distintivi o di attualità. Per aumentare la probabilità di viralità, potresti considerare di aggiungere un elemento personale, una storia breve o una domanda che stimoli la partecipazione degli utenti. Inoltre, l'uso di hashtag è corretto, ma una combinazione di hashtag più mirati o di tendenze attuali potrebbe aiutare a raggiungere un pubblico più ampio.",
  "improve": "🌟 Buongiorno, Twitter! 🌟 Oggi è il giorno ideale per una passeggiata nella natura e un po' di tempo per te stesso! 🚶‍♂️🌳 Prenditi una pausa, respira profondamente e ricarica le energie. 💚✨ #ViviAlMassimo #Natura #SelfCare"
}
```
**Campi della risposta:**
- `viralità`: (stringa) La valutazione della viralità del tweet su una scala da 1 a 10.
- `feedback`: (stringa) Commento dettagliato sul tweet, inclusi suggerimenti per migliorare la sua viralità.
- `improve`: (stringa) Un tweet migliorato con una maggiore probabilità di viralità.

## Diagrammi

### Diagramma di Sequenza

Il Diagramma di Sequenza illustra il flusso di dati e le interazioni tra i vari componenti del sistema durante il processo di analisi e miglioramento dei tweet. Questo diagramma mostra come i dati vengono trasferiti tra il client, il server e l'AI per ottenere una valutazione e un miglioramento del tweet.

![Diagramma di Sequenza](design/Sequence%20Diagram.png)

### Diagramma di Sistema

Il Diagramma di Sistema fornisce una visione d'insieme dell'architettura del progetto. Mostra i componenti principali del sistema e le loro interazioni. Questo diagramma aiuta a comprendere l'architettura generale e la struttura del progetto, inclusi i flussi di dati e le dipendenze tra i vari moduli.

![Diagramma di Sistema](design/System%20Diagram.png)

In questa sezione:
- **Diagramma di Sequenza:** Mostra come i dati vengono elaborati attraverso il sistema, evidenziando le interazioni tra i diversi componenti.
- **Diagramma di Sistema:** Illustra l'architettura complessiva, mostrando come i componenti del sistema interagiscono tra loro.
## Licenza

Questo progetto è distribuito sotto la Licenza MIT. La Licenza MIT è una licenza permissiva che consente a chiunque di utilizzare, copiare, modificare, fondere, pubblicare, distribuire, sublicenziare e vendere copie del Software, a condizione che siano inclusi nel software originale tutti i copyright e le dichiarazioni di permesso. Il software è fornito "così com'è", senza garanzie di alcun tipo, espresse o implicite, inclusi, ma non limitati a, le garanzie implicite di commerciabilità, idoneità per uno scopo particolare e non violazione.

### Testo della Licenza MIT

