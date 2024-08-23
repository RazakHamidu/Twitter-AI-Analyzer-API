from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, jsonify


load_dotenv(find_dotenv())

app = Flask(__name__)

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")


tweet_example = "🌞 Buongiorno a tutti! Oggi è una giornata perfetta per una passeggiata all'aria aperta. 🏞️ Non dimenticate di prendere un po' di tempo per voi stessi e godervi la natura! 🌳✨ #Buongiorno #Relax #VivereBene"

def evaluate_virality(tweet_prompt):
    viralità = [
        SystemMessage(content="Agisci come un Twitter AI Analyzer. Hai 10 anni di esperienza nel capire e valutare la possibilità che vada virale un Twitter. Dammi una valutazione di viralità da 1 a 10. Dammi solo il numero di valutazione non rispondere con altri informazioni. Ecco il mio tweet"),
        HumanMessage(content=tweet_example),
        AIMessage(content="4/10"),  # Questo è un valore di esempio. Considera di rimuovere o modificare se necessario.
        HumanMessage(content=tweet_prompt)
    ]
    return model.invoke(viralità).content

def provide_feedback(tweet_prompt, viralità_r):
    feedback = [
        SystemMessage(content=f"Agisci come un Twitter AI Analyzer. Hai 10 anni di esperienza nel dare feedback ai Twitter. Ti darò un tweet che ha una probabilità di andare virale di {viralità_r} e tu mi dirai un feedback testuale. Non darmi dei tweet migliorati o valutazioni tue. Dammi solo un feedback testuale."),
        HumanMessage(content=tweet_example),
        AIMessage(content="Il tweet ha un messaggio positivo e incoraggiante, che può risuonare bene con chi cerca ispirazione per la giornata. Tuttavia, potrebbe non avere un impatto virale elevato poiché è piuttosto generico e privo di elementi distintivi o di attualità. Per aumentare la probabilità di viralità, potresti considerare di aggiungere un elemento personale, una storia breve o una domanda che stimoli la partecipazione degli utenti. Inoltre, l'uso di hashtag è corretto, ma una combinazione di hashtag più mirati o di tendenze attuali potrebbe aiutare a raggiungere un pubblico più ampio."),
        HumanMessage(content=tweet_prompt)
    ]
    return model.invoke(feedback).content

def improve_tweet(tweet_prompt, viralità_r):
    improve = [
        SystemMessage(content=f"Agisci come un Twitter AI Analyzer. Hai 10 anni di esperienza nel generare dei tweet con viralità 10/10. Ti darò un tweet che ha una probabilità di andare virale di {viralità_r} e lo rigenererai per ottenere un tweet con viralità 10/10. Non fornirmi altre spiegazioni o informazioni ulteriori. Dammi solo il tweet migliorato con viralità 10/10."),
        HumanMessage(content=tweet_example),
        AIMessage(content="🌟 Buongiorno, Twitter! 🌟 Oggi è il giorno ideale per una passeggiata nella natura e un po' di tempo per te stesso! 🚶‍♂️🌳 Prenditi una pausa, respira profondamente e ricarica le energie. 💚✨ #ViviAlMassimo #Natura #SelfCare"),
        HumanMessage(content=tweet_prompt)
    ]
    return model.invoke(improve).content

@app.route("/TAIAPI", methods=['POST'])
def main():
    tweet_prompt = request.json.get("tweet_prompt")
    if not tweet_prompt:
        return jsonify({"error": "Tweet is required"}), 400

    try:
        viralità_r = evaluate_virality(tweet_prompt)
        feedback_r = provide_feedback(tweet_prompt, viralità_r)
        improve_r = improve_tweet(tweet_prompt, viralità_r)
        
        return jsonify({
            "viralità": viralità_r,
            "feedback": feedback_r,
            "improve": improve_r
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False)
