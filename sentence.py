from llama_cpp import Llama

def summarize_to_one_sentence(text):
    # Initialize the model with your local GGUF file
    llm = Llama(
        model_path="./Llama-3.2-3B-Instruct-Q4_K_M.gguf",
        n_ctx=120000,
        n_threads=4
    )

    # Create a more explicit prompt
    prompt = f"""<|start_header_id|>system<|end_header_id|>
You are a helpful AI assistant that summarizes text into exactly one sentence from json file with the parsed articles. 

<|start_header_id|>user<|end_header_id|>
You will be given a json file with the parsed articles. Return only valuable and important information from content. Summarize these articles
and return a few important texts in 20 or fewer words:
{text}

<|start_header_id|>assistant<|end_header_id|>"""

    # Generate response with debug prints
    print("Generating response...")
    response = llm(
        prompt,
        max_tokens=256,
        temperature=0.7,
        stop=["<|end_header_id|>", "<|eot_id|>"],
        echo=False
    )
    
    # Print raw response for debugging
    print("Raw response:", response)
    
    if response and 'choices' in response and len(response['choices']) > 0:
        return response['choices'][0]['text'].strip()
    else:
        return "Error: No response generated"

if __name__ == "__main__":
    import json
    
    # Read the JSON file
    with open('parsed_articles_with_ocr.json', 'r', encoding='utf-8') as file:
        json_content = json.load(file)
    
    print("Starting summarization...")
    summary = summarize_to_one_sentence(json_content)
    print("\nFinal Summary:", summary)