# Leer el archivo original con tabs y escribir uno nuevo con comas
with open("final_output.csv", "r", encoding="utf-8") as infile, \
     open("final_output_fixed.csv", "w", encoding="utf-8") as outfile:

    for line in infile:
        fields = line.strip().split("\t")  # Divide por tabulaciones
        cleaned_fields = [field.replace(",", " ") for field in fields]  # Evita conflictos con comas internas
        outfile.write(",".join(cleaned_fields) + "\n")  # Une por comas
