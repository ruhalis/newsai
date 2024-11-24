from llama_cpp import Llama

def summarize_to_one_sentence(text):
    # Initialize the model with your local GGUF file
    llm = Llama(
        model_path="./Llama-3.2-3B-Instruct-Q4_K_M.gguf",
        n_ctx=2048,
        n_threads=4
    )

    # Create a more explicit prompt
    prompt = f"""<|start_header_id|>system<|end_header_id|>
You are a helpful AI assistant that summarizes text into exactly one sentence.

<|start_header_id|>user<|end_header_id|>
Summarize this text in 20 or fewer words:
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
    text = """
    The Industrial Revolution was a major turning point in human history. 
    It began in Britain in the late 18th century. The introduction of steam 
    power and mechanized manufacturing processes led to dramatic increases 
    in production capacity. This period saw significant social and economic changes.
    """
    
    print("Starting summarization...")
    summary = summarize_to_one_sentence(text)
    print("\nFinal Summary:", summary)