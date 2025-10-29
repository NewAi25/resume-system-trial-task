from transformers import pipeline

# Load model only once for efficiency
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(resume_data):
    """Generate a summary from structured resume JSON."""
    text = " ".join([str(v) for v in resume_data.values()])
    summary = summarizer(text, max_length=120, min_length=30, do_sample=False)
    return summary[0]['summary_text']
