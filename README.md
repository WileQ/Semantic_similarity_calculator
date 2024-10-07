# Semantic Similarities with a GUI using Sentence Transformers
This Python application provides a GUI to calculate semantic similarity between words or phrases using the Sentence Transformers library. The interface uses Tkinter and the similarity is computed by comparing embeddings using cosine similarity from the scipy library.

# Features
- Graphical User Interface
- Sentence Transformer Embeddings: Computes semantic similarity using pre-trained sentence embeddings (all-MiniLM-L6-v2 model)
- Color-coded Results: Shows the similarity results in a color-coded fashion:
  * Green: High similarity (Above 60 similarity)
  * Yellow: Moderate similarity (Between 30 and 60 similarity)
  * Red: Low similarity (Below 30 similarity)
    
- Reset Option: Users can reset the input to start over

# How It Works
1. The user enters a word or phrase in the input field.
2. Upon pressing Enter, the application compares this input to previously entered words/phrases.
3. The similarity results are displayed as a percentage, with color coding to indicate the similarity level.
4. The Reset button clears the screen, allowing the user to start fresh.


# Usage
Clone the repository:
```bash
git clone https://github.com/WileQ/Semantic_similarity_calculator
cd Semantic_similarity_calculator
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run it:
```bash
python main.py
```