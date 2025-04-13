# 📚 Hindi Literature-Based Personalized Book Recommendation System

### 🚀 [Live Demo on Streamlit](https://sunnyrecommendshindibooks.streamlit.app/)

## 🌟 Overview
Welcome to the **Hindi Literature-Based Personalized Book Recommendation System** — a unique project tailored for enthusiasts of **Hindi literature** and **creative writing**. This system provides personalized book recommendations, inspired by the way a knowledgeable librarian would help you explore your next favorite book based on your reading history and preferences.

Whether you're a fan of **Premchand’s social realism**, **Mahadevi Verma’s emotional poetry**, or **contemporary Hindi fiction**, this system adapts to your evolving tastes, offering books that resonate with your literary interests.

## 🧭 How It Works
1. **📖 Cold Start**: The system begins by recommending books based on their content (genre, themes, tags) and overall popularity. It's perfect for new users or those exploring various literary genres.
2. **🖱️ User Interaction**: Users can simulate interest by selecting books they like, helping the system understand their preferences.
3. **🧠 Profile Update**: Based on the books you select, your personal reading preferences — like favorite genres and thematic interests — are captured and stored.
4. **🎯 Personalized Recommendations**: In subsequent rounds, the system refines its recommendations, offering more relevant book suggestions based on your profile and preferences.
5. **🤝 Hybrid Suggestions**: The final round combines your personal preferences with insights gathered from similar readers' choices, offering diverse yet tailored suggestions.

## 💡 Recommendation Logic

### **1. Content-Based Filtering**
- Books are recommended based on matching tags, genres, and thematic elements (e.g., books with themes of love, social issues, or historical fiction).
- The system considers features like genre, author, publication year, and plot themes to match books that are conceptually similar to the ones you’ve liked.

### **2. Collaborative Filtering (Simulated)**
- Collaborative filtering is simulated by considering **popularity scores**. While real collaborative filtering relies on user interactions (ratings, reviews), here we simulate it by suggesting books that are popular among users with overlapping interests.
- The system tracks books frequently selected by other users with similar interests and recommends those books to the current user.

### **3. User Profile Update**
- **User profile** is maintained as a Python dictionary that stores key preferences, such as:
  - `preferred_tags`: Thematic tags such as "love," "history," "society," etc.
  - `preferred_categories`: Book genres such as "fiction," "poetry," "drama," etc.
- As users interact by selecting books, the profile is updated dynamically, with new preferences added or adjusted based on the user’s interactions.
