import ollama

response = ollama.chat(
    model='llama3.2',
    messages=[{'role': 'user', 'content': 'Reply in one short sentence: Are you online?'}]
)

# Print the actual text response
print("Response:", response['message']['content'])

# Extract and format the metrics
time_in_seconds = response['eval_duration'] / 1_000_000_000
tokens_generated = response['eval_count']
prompt_tokens = response['prompt_eval_count']

# Print the metrics
print("\n--- METRICS ---")
print(f"Time Taken: {time_in_seconds:.2f} seconds")
print(f"Tokens Generated (Output): {tokens_generated}")
print(f"Tokens Evaluated (Input): {prompt_tokens}")
