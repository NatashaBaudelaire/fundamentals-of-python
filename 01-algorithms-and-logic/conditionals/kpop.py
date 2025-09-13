kpops_bands = {
    "BTS": "Pop, EDM, Hip-hop",
    "BLACKPINK": "Electronic, Hip-hop, Trap",
    "NewJeans": "R&B/Soul, Future Bass, Pop, Dance",
    "Stray Kids": "Hip-hop, Pop, Rock, Pop Rock",
    "Twice": "Hip-hop, EDM",
    "Kiss of Life": "Dance, Pop, Hip-Hop, Rock and R&B",
    "Le Sserafim": "Pop, Disco-Funk, R&B",
    "Fifty Fitfy": "Dance, EDM, R&B, Dance, Pop",
    "Red Velvet": "R&B, Pop, Dance",
}
print("Available bands:")
for band in kpops_bands:
    print("-", band)

choice = input("\nEnter the name of a K-pop band from the list above: ")

if choice in kpops_bands:
    print(f"The main musical style of {choice} is: {kpops_bands[choice]}")
else:
    print(f"K-pop band not found in the list.")