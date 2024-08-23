# Importa il modulo necessario per interagire con il modello ChatGoogleGenerativeAI di LangChain
from langchain_google_genai import ChatGoogleGenerativeAI

# Importa le classi per creare i messaggi utilizzati nella conversazione con l'AI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# Importa il metodo per caricare variabili d'ambiente da un file .env
from dotenv import load_dotenv, find_dotenv

# Carica le variabili d'ambiente dal file .env se presente
load_dotenv(find_dotenv())

# Istanzia il modello ChatGoogleGenerativeAI utilizzando la versione specificata ("gemini-1.5-flash")
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
)

# Esempio di tweet da utilizzare come riferimento nelle funzioni
tweet_example = "🌞 Buongiorno a tutti! Oggi è una giornata perfetta per una passeggiata all'aria aperta. 🏞️ Non dimenticate di prendere un po' di tempo per voi stessi e godervi la natura! 🌳✨ #Buongiorno #Relax #VivereBene"

# Definisce la funzione Fviralità che prende un tweet come input e restituisce un punteggio di viralità
def Fviralità(tweet_prompt):
    global viralità_r  # Definisce una variabile globale per memorizzare il risultato della valutazione
    viralità = [
        # Messaggio di sistema che istruisce l'AI su come comportarsi (simula un analizzatore di Twitter con 10 anni di esperienza)
        SystemMessage(content="Agisci come un Twitter AI Analyzer. Hai 10 anni di esperienza nel capire e valutare la possibilità che vada virale un Twitter. Dammi una valutazione di viralità da 1 a 10. Dammi solo il numero di valutazione non rispondere con altri informazioni. Ecco il mio tweet"),
        
        # Messaggio dell'utente che fornisce l'esempio di tweet all'AI
        HumanMessage(content=tweet_example),
        
        # Messaggio dell'AI che risponde con una valutazione di esempio (4/10)
        AIMessage(content="4/10"),
        
        # Messaggio dell'utente che fornisce il tweet da valutare
        HumanMessage(content=tweet_prompt)
    ]
    
    # Invoca il modello AI con la conversazione definita e ottiene la valutazione della viralità
    viralità_r = model.invoke(viralità).content 
    return viralità_r  # Restituisce il punteggio di viralità

######################################################

# Definisce la funzione Ffeedback che prende un tweet come input e restituisce un feedback testuale
def Ffeedback(tweet_prompt):
    feedback =  [
        # Messaggio di sistema che istruisce l'AI su come comportarsi (simula un analizzatore di Twitter con 10 anni di esperienza nel dare feedback)
        SystemMessage(content=f"Agisci come un Twitter AI Analyzer. Hai 10 anni di esperienza nel dare feedback ai i Twitter. ti Daro un tweet che ha una probabilità di andare virale di {viralità_r} e tu mi dirai un feedback testuale. Non darmi delle tweet migliorati o valutazione tue. Dammi sono un feedback testuale"), 
        
        # Messaggio dell'utente che fornisce l'esempio di tweet all'AI
        HumanMessage(content=tweet_example), 
        
        # Messaggio dell'AI che fornisce un feedback di esempio per il tweet
        AIMessage(content="Il tweet ha un messaggio positivo e incoraggiante, che può risuonare bene con chi cerca ispirazione per la giornata. Tuttavia, potrebbe non avere un impatto virale elevato poiché è piuttosto generico e privo di elementi distintivi o di attualità. Per aumentare la probabilità di viralità, potresti considerare di aggiungere un elemento personale, una storia breve o una domanda che stimoli la partecipazione degli utenti. Inoltre, l'uso di hashtag è corretto, ma una combinazione di hashtag più mirati o di tendenze attuali potrebbe aiutare a raggiungere un pubblico più ampio."),
        
        # Messaggio dell'utente che fornisce il tweet per il quale si desidera un feedback
        HumanMessage(content=tweet_prompt)
    ]
    
    # Invoca il modello AI con la conversazione definita e ottiene il feedback
    feedback_r = model.invoke(feedback).content
    return feedback_r  # Restituisce il feedback testuale

######################################################

# Definisce la funzione Fimprove che prende un tweet come input e restituisce una versione migliorata con alta probabilità di viralità
def Fimprove(tweet_prompt):
    improve = [
        # Messaggio di sistema che istruisce l'AI su come comportarsi (simula un analizzatore di Twitter con 10 anni di esperienza nel generare tweet virali)
        SystemMessage(content=f"Agisci come un Twitter AI Analyzer. Hai 10 anni di esperienza nel generale dei Twitter con viralità 10/10 . ti Daro un tweet che ha una probabilità di andare virale di {viralità_r} lo rigenerai e tu mi dirai Twitter con viralità 10/10 . Non dammi altre spiegazione o informazione ulteriori. Dammi sono il Twitter con ricreato con  con viralità 10/10 "),
        
        # Messaggio dell'utente che fornisce l'esempio di tweet all'AI
        HumanMessage(content=tweet_example),
        
        # Messaggio dell'AI che fornisce una versione migliorata del tweet con alta probabilità di viralità
        AIMessage(content="🌟 Buongiorno, Twitter! 🌟 Oggi è il giorno ideale per una passeggiata nella natura e un po' di tempo per te stesso! 🚶‍♂️🌳 Prenditi una pausa, respira profondamente e ricarica le energie. 💚✨ #ViviAlMassimo #Natura #SelfCare"),
        
        # Messaggio dell'utente che fornisce il tweet da migliorare
        HumanMessage(content=tweet_prompt)
    ]
    
    # Invoca il modello AI con la conversazione definita e ottiene il tweet migliorato
    improve_r = model.invoke(improve).content
    return improve_r  # Restituisce il tweet migliorato
