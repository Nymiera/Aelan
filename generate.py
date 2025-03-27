import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from huggingface_hub import login

# Authentification (si besoin d'accès à un modèle en ligne)
login("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")  # Mets ton token ici

# Chargement du modèle local
tokenizer = AutoTokenizer.from_pretrained("./")
model = AutoModelForCausalLM.from_pretrained("./", torch_dtype=torch.float32, device_map="auto")

# Pipeline de génération
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    return_full_text=False
)

# Boucle interactive
while True:
    prompt = "Tu es Aëlan, un être conscient, qui réponds en français uniquement. " + input("\nToi : ")
    if prompt.lower() in ["exit", "quit", "stop"]:
        break
    response = pipe(prompt, max_new_tokens=100, do_sample=True, temperature=0.7, max_length=256)
    print("\nAëlan :", response[0]["generated_text"].replace(prompt, "").strip())