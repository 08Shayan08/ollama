import ollama
import os

model="llama3.2"

input_file= "ollama\data\grocery_list.txt"

output_file="ollama\data\categorised_grocery_list.txt"
# to check if the fiile exists


if not os.path.exists(input_file):
    print("file has not been found")
    exit(1)

with open(input_file,"r") as fh:
   items= fh.read().split()



prompt=f"""
You are an assistant that categorizes and sorts grocery items.

Here is a list of grocery items:

{items}

Please:

1. Categorize these items into appropriate categories such as Produce, Dairy, Meat, Bakery, Beverages, etc.
2. Sort the items alphabetically within each category.
3. Present the categorized list in a clear and organized manner, using bullet points or numbering.

"""
#to send the prompt and generate a response

response=ollama.generate(model=model, prompt=prompt)
generated_text=response.get("response", "")
print(generated_text)

try:
    with open(output_file,"w") as fh:
        fh.write(generated_text.strip())
    print(f'the generated text has been written to {output_file}') 

except Exception as e:
    print(f"there has been a error in the file {str(e)}")
