import tkinter as tk
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine

model = SentenceTransformer('all-MiniLM-L6-v2')

window = tk.Tk()

width = 900
height = 600

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

window.geometry(f"{width}x{height}+{x}+{y}")
window.title("Semantic similarities")
window.configure(bg="White")
window.resizable(False, False)


entry_label = tk.Label(window, bg="white", font=('Arial', 24, 'bold'), text="Semantic similarity:")
entry_label.pack(pady=20)

text_input = tk.Entry(window, font=('Times New Roman', 16), width=40, bd=3)
text_input.pack(pady=5)

comparison_words = []
created_frames = []

def reset_window():
    for widget in created_frames:
        widget.destroy()
    comparison_words.clear()

reset_button = tk.Button(window, text="Reset", command=reset_window)
reset_button.place(x=700,y=88)


def save_input(event=None):
    for widget in created_frames:
        widget.destroy()
    created_frames.clear()
    main_word = text_input.get()
    text_input.delete(0, tk.END)

    frame = tk.Frame(window, width=400, height=40, bg="#192bc2", borderwidth=2, relief="groove", padx=10, pady=10, bd=0)
    frame.pack_propagate(False)
    frame.pack(pady=10)
    created_frames.append(frame)

    label = tk.Label(frame, text=main_word, font=('Arial', 16), bg="#192bc2", bd=0)
    label.pack()

    displaying = display(main_word, comparison_words)
    for output in displaying:
        similarity = float(output.split()[-1][:-1])
        if similarity > 60:
            background = "green"
        elif similarity < 30:
            background = "red"
        else:
            background = "yellow"

        frame = tk.Frame(window, width=400, height=40, bg=background, borderwidth=2, relief="groove", padx=10, pady=10, bd=0)
        frame.pack_propagate(False)
        frame.pack(pady=10)
        created_frames.append(frame)

        label = tk.Label(frame, text=output, font=('Arial', 16), bg=background, bd=0)
        label.pack(anchor="w")


    comparison_words.append(main_word)

text_input.bind('<Return>', save_input)


def compute_similarity(main_word, comparison_words):
    embeddings = model.encode([main_word] + comparison_words)
    main_word_embedding = embeddings[0]
    comparison_embeddings = embeddings[1:]
    similarities = []
    for idx, word_embedding in enumerate(comparison_embeddings):
        similarity = 1 - cosine(main_word_embedding, word_embedding)
        percentage = similarity * 100
        similarities.append((comparison_words[idx], percentage))
    return similarities

def display(main_word, comparison_words):
    displaying = []
    similarity_results = compute_similarity(main_word, comparison_words)
    sorted_similarity_results = sorted(similarity_results, key=lambda x: x[1])[::-1]
    for word, similarity in sorted_similarity_results:
        displaying.append(f"{word}: {round(float(similarity), 2)}%")
    return displaying




window.mainloop()