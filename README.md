

# 🌱 Voice Carbon Footprint Tracker

A web application that lets you upload or record a voice note describing your daily activities, transcribes your speech, extracts activities, and estimates your carbon footprint.

## 🚀 Features

- **Voice note upload**: Speak your activities, the app does the rest!
- **Automatic transcription**: Uses OpenAI Whisper for accurate speech-to-text.
- **Activity extraction**: NLP with spaCy to identify daily actions.
- **Carbon footprint estimation**: Calculates CO₂ emissions for your activities.
- **Modern React frontend**: Simple, clean, and responsive interface.

## 📦 Folder Structure

```
your-repo/
├── backend/     # FastAPI + Whisper backend
│   ├── main.py
│   ├── requirements.txt
│   └── ...
├── frontend/    # React frontend
│   ├── src/
│   ├── package.json
│   └── ...
└── README.md
```

## ⚡ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### 2. Backend Setup (FastAPI + Whisper)

#### A. **System Requirements**

- **Python 3.12**
- **ffmpeg** installed and in your system PATH  
  (Install from [ffmpeg.org](https://ffmpeg.org/download.html) or via `brew install ffmpeg` on macOS)

#### B. **Create and Activate Virtual Environment**

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### C. **Install Python Dependencies**

```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install git+https://github.com/openai/whisper.git
python -m spacy download en_core_web_sm
```

> **If you see numpy or torch errors, run:**  
> `pip install "numpy<2.0"`

#### D. **Run the Backend Server**

```bash
uvicorn main:app --reload
```

- The backend will be available at [http://localhost:8000](http://localhost:8000)
- Test endpoints at [http://localhost:8000/docs](http://localhost:8000/docs)

### 3. Frontend Setup (React)

```bash
cd ../frontend
npm install
npm start
```

- The frontend will be available at [http://localhost:3000](http://localhost:3000)

### 4. Using the App

- Open [http://localhost:3000](http://localhost:3000) in your browser.
- Upload or record a voice note describing your activities (e.g., "I drove 2 kilometers on petrol").
- The app will transcribe your speech, extract activities, and estimate your carbon footprint.

## 🛠️ Troubleshooting & FAQ

- **ffmpeg not found:**  
  Install ffmpeg and restart your terminal.

- **Module not found:**  
  Ensure you activated your virtual environment and installed all requirements.

- **NumPy version error:**  
  Run `pip install "numpy<2.0"`

- **CORS errors:**  
  Make sure the backend is running and CORS is enabled in `main.py`.

- **Large files or slow processing:**  
  Try with a smaller audio file first.

- **Submodule or folder errors in Git:**  
  Ensure you do not commit `venv/` or `node_modules/` folders.  
  If you see arrows on folders in GitHub, remove any nested `.git` folders and re-add as normal folders.

## 📝 .gitignore Recommendations

- In `backend/.gitignore`:
  ```
  venv/
  __pycache__/
  *.pyc
  ```

- In `frontend/.gitignore`:
  ```
  node_modules/
  build/
  ```

## 🌍 Deploying Online

- Deploy the backend (FastAPI) to a cloud VM or service (see deployment instructions).
- Deploy the frontend (React) to Vercel, Netlify, or similar.
- Update the API URL in your frontend code to point to your deployed backend.

## 🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss what you would like to change.

## 📄 License

[MIT](LICENSE)

## 🙏 Credits

- [OpenAI Whisper](https://github.com/openai/whisper)
- [spaCy](https://spacy.io/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [React](https://react.dev/)
- [FFmpeg](https://ffmpeg.org/)

**Enjoy tracking your carbon footprint by voice!**

You can copy this README, fill in your actual GitHub repo URL, and adjust any sections as needed for your project specifics.  
This will make it much easier for others to clone, set up, and use your project successfully![1][2]

[1] programming.version_control
[2] programming.natural_language_processing
