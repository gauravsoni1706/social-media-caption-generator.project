import random

def generate_caption(keywords, platform, tone):
    emojis = ["🔥", "💡", "✨", "🚀", "🎯", "😎", "📸"]
    hashtags = [f"#{word.strip().replace(' ', '')}" for word in keywords.split(",")]

    base_captions = {
        "fun": [
            "Let the good vibes roll with {keywords} {emoji}",
            "Just vibin' with {keywords} today! {emoji}",
        ],
        "professional": [
            "Exploring the value of {keywords} in today’s world. {emoji}",
            "Sharing insights on {keywords}. Stay tuned! {emoji}",
        ],
        "inspirational": [
            "Believe in the magic of {keywords} {emoji}",
            "Let {keywords} guide your path forward. {emoji}",
        ]
    }

    tone = tone.lower()
    selected_caption = random.choice(base_captions.get(tone, base_captions["fun"]))
    emoji = random.choice(emojis)
    caption = selected_caption.format(keywords=keywords, emoji=emoji)

    return {
        "caption": caption,
        "hashtags": " ".join(hashtags)
    }