from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline 

model_id = "meta-llama/Llama-2-7b-chat-hf"

model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True).to("cuda")
tokenizer = AutoTokenizer.from_pretrained(model_id)

pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=200, device=0)

prompt = """You are a helpful assistant that helps students with their problems:

Question: {question}

Give a correct and straight answer, if you don't know the answer just say I don't know the answer.
Return the answer and nothing else
Helpful answer:
"""
result = pipe(prompt)
print(result[0]['generated_text'])
