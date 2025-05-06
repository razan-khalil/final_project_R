# 🍽️ NutriChef AI - Your Personal AI-Powered Chef

NutriChef is an intelligent, multimodal AI assistant that helps you plan meals, suggest recipes, and give nutritional advice based on **text**, **image**, **audio**, or **video** inputs. Powered by advanced language models and LangChain agents, NutriChef makes healthy eating smarter and easier.

---

## 🚀 Features

- 🥗 **Ingredient-Based Meal Generation**: Just tell or show what you have, and NutriChef will create a full meal plan.
- 📸 **Image & Audio Recognition**: Upload a photo or record your voice to describe ingredients.
- 🎥 **Video Transcript Q&A**: Paste a YouTube link and ask questions about cooking videos.
- 🧠 **Conversational Memory**: NutriChef remembers the context of your chat to keep the conversation natural.
- 📊 **Nutritional Facts & Advice**: Get accurate health breakdowns of the meals.

---

## 🧰 Technologies Used

- **LangChain** (chains, tools, memory, RAG)
- **OpenAI GPT-3.5 turbo** for language understanding
- **Whisper** for speech-to-text
- **PANNs** for audio ingredient detection
- **SentenceTransformers** + **ChromaDB** for vector search
- **Gradio** for UI
- **Hugging Face Transformers**

---

## 📂 How It Works

1. **Input**: User provides input via text, image, audio, or video link.
2. **Processing**:
   - Text and images go through preprocessing and embedding.
   - Audio is transcribed and ingredients extracted.
   - Videos are transcribed using Whisper and used for Q&A.
3. **Agent Decision**:
   - LangChain agents decide which backend tool to call.
4. **Output**:
   - Meal Plan + Nutrition Facts
   - Recipe Instructions
   - Follow-up Q&A using memory

---

## 🧠 Memory + Agent Workflow

- Memory via `RunnableWithMessageHistory`
- Dish tracking + follow-up (“how to make it?” works contextually)
- Tools like `generate_meal_plan`, `search_recipes`, `get_nutrition_facts`, `answer_video_question`

---

## 🖼️ Example Use Cases

| Input Type | Example |
|------------|---------|
| 📝 Text | "I have chicken, rice, and broccoli" |
| 🎤 Audio | Upload an MP3 saying your ingredients |
| 📷 Image | Upload photo of ingredients |
| 🎥 Video | "How to make Kabsa" from a YouTube cooking video |

---
