input_path = "final_output_fixed.csv"
output_path = "final_output_clean.csv"

with open(input_path, "r", encoding="utf-8") as infile:
    lines = infile.readlines()

# Arreglar header manualmente
header = "post_id,author,created_utc,subreddit,score,num_comments,cleaned_text\n"

# Guardar con header limpio
with open(output_path, "w", encoding="utf-8") as outfile:
    outfile.write(header)
    for line in lines[1:]:
        outfile.write(line)

