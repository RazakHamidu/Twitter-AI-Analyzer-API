# Importa le classi necessarie dalla libreria langchain per l'integrazione con l'AI di Google
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, jsonify

# Carica le variabili d'ambiente dal file .env
load_dotenv(find_dotenv())

# Crea un'istanza di Flask per il web server
app = Flask(__name__)

# Crea un'istanza del modello AI di Google Generative AI con un modello specifico
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Esempio di tweet per testare le funzioni
tweet_example = "🌞 Buongiorno a tutti! Oggi è una giornata perfetta per una passeggiata all'aria aperta. 🏞️ Non dimenticate di prendere un po' di tempo per voi stessi e godervi la natura! 🌳✨ #Buongiorno #Relax #VivereBene"

# Funzione per valutare la viralità di un tweet basata su un prompt
def evaluate_virality(tweet_prompt):
    viralità = [
        # Messaggio di sistema che specifica il ruolo dell'AI nell'analisi della viralità del tweet
        SystemMessage(content="Agisci come un Twitter AI Analyzer. Hai 10 anni di esperienza nel capire e valutare la possibilità che vada virale un Twitter. Dammi una valutazione di viralità da 1 a 10. Dammi solo il numero di valutazione non rispondere con altri informazioni. Ecco il mio tweet"),
        # Messaggio umano con l'esempio di tweet da analizzare
        HumanMessage(content=tweet_example),
        # Risposta dell'AI (esempio) sulla viralità del tweet
        AIMessage(content="4/10"),  # Questo è un valore di esempio. Considera di rimuovere o modificare se necessario.
        # Messaggio umano con il tweet da valutare
        HumanMessage(content=tweet_prompt)
    ]
    # Invoca il modello AI con i messaggi e restituisce il contenuto della risposta dell'AI
    return model.invoke(viralità).content

# Funzione per fornire feedback su un tweet in base alla sua valutazione di viralità
def provide_feedback(tweet_prompt, viralità_r):
    feedback = [
        # Messaggio di sistema che specifica il ruolo dell'AI nel fornire feedback testuale sul tweet
        SystemMessage(content=f"Agisci come un Twitter AI Analyzer. Hai 10 anni di esperienza nel dare feedback ai Twitter. Ti darò un tweet che ha una probabilità di andare virale di {viralità_r} e tu mi dirai un feedback testuale. Non darmi dei tweet migliorati o valutazioni tue. Dammi solo un feedback testuale."),
        # Messaggio umano con l'esempio di tweet da cui trarre feedback
        HumanMessage(content=tweet_example),
        # Risposta dell'AI (esempio) con il feedback sul tweet
        AIMessage(content="Il tweet ha un messaggio positivo e incoraggiante, che può risuonare bene con chi cerca ispirazione per la giornata. Tuttavia, potrebbe non avere un impatto virale elevato poiché è piuttosto generico e privo di elementi distintivi o di attualità. Per aumentare la probabilità di viralità, potresti considerare di aggiungere un elemento personale, una storia breve o una domanda che stimoli la partecipazione degli utenti. Inoltre, l'uso di hashtag è corretto, ma una combinazione di hashtag più mirati o di tendenze attuali potrebbe aiutare a raggiungere un pubblico più ampio."),
        # Messaggio umano con il tweet da cui fornire feedback
        HumanMessage(content=tweet_prompt)
    ]
    # Invoca il modello AI con i messaggi e restituisce il contenuto della risposta dell'AI
    return model.invoke(feedback).content

# Funzione per migliorare un tweet per raggiungere una viralità massima
def improve_tweet(tweet_prompt, viralità_r):
    improve = [
        # Messaggio di sistema che specifica il ruolo dell'AI nel migliorare il tweet per ottenere una viralità massima
        SystemMessage(content=f"Agisci come un Twitter AI Analyzer. Hai 10 anni di esperienza nel generare dei tweet con viralità 10/10. Ti darò un tweet che ha una probabilità di andare virale di {viralità_r} e lo rigenererai per ottenere un tweet con viralità 10/10. Non fornirmi altre spiegazioni o informazioni ulteriori. Dammi solo il tweet migliorato con viralità 10/10."),
        # Messaggio umano con l'esempio di tweet da migliorare
        HumanMessage(content=tweet_example),
        # Risposta dell'AI (esempio) con il tweet migliorato per massimizzare la viralità
        AIMessage(content="🌟 Buongiorno, Twitter! 🌟 Oggi è il giorno ideale per una passeggiata nella natura e un po' di tempo per te stesso! 🚶‍♂️🌳 Prenditi una pausa, respira profondamente e ricarica le energie. 💚✨ #ViviAlMassimo #Natura #SelfCare"),
        # Messaggio umano con il tweet da migliorare
        HumanMessage(content=tweet_prompt)
    ]
    # Invoca il modello AI con i messaggi e restituisce il contenuto della risposta dell'AI
    return model.invoke(improve).content

# Definisce una route per l'API Flask che gestisce le richieste POST per "/TAIAPI"
@app.route("/TAIAPI", methods=['POST'])
def main():
    # Estrae il tweet dal corpo della richiesta JSON
    tweet_prompt = request.json.get("tweet_prompt")
    # Controlla se il tweet è presente nella richiesta
    if not tweet_prompt:
        return jsonify({"error": "Tweet is required"}), 400

    try:
        # Valuta la viralità del tweet, fornisce feedback e migliora il tweet
        viralità_r = evaluate_virality(tweet_prompt)
        feedback_r = provide_feedback(tweet_prompt, viralità_r)
        improve_r = improve_tweet(tweet_prompt, viralità_r)
        
        # Restituisce le valutazioni e il feedback in formato JSON
        return jsonify({
            "viralità": viralità_r,
            "feedback": feedback_r,
            "improve": improve_r
        }), 201

    except Exception as e:
        # Gestisce gli errori e restituisce un messaggio di errore
        return jsonify({"error": str(e)}), 500

# Avvia il server Flask se il file viene eseguito direttamente
if __name__ == "__main__":
    app.run(debug=False)
