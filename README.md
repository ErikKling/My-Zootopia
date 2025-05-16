# 🦊 Zootopia – Animal Explorer

This project generates a styled HTML website to display animal facts.

The data is fetched from the [API Ninja Animals API](https://api-ninjas.com/api/animals) using a user-provided animal name.  
The site displays each animal’s name, diet, type, and habitat in card format.

## 🛠 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourname/my-zootopia.git
   cd my-zootopia
   ```

2. Create and activate a virtual environment:

   ```bash
   uv venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   uv pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your API key:

   ```
   API_KEY=your-api-key-here
   ```

## 🚀 Usage

Run the generator script and enter an animal name when prompted:

```bash
python animals_web_generator.py
```

This will generate a new `animals_page.html` file with the animal cards.

## 🤝 Contributing

Pull requests are welcome!  
Feel free to suggest improvements or add more features.
