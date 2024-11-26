# Joke API
Welcome to the Joke API repository! 🎭 This project provides a simple, fun, and interactive way to access and share jokes programmatically. 
Whether you're building a comedy bot, spicing up your app with humor, or simply looking to add a touch of laughter to your day, the Joke API has you covered.

## Features
- Fetch a random joke 🎲
- Categorized jokes (e.g., puns, dad jokes, tech jokes, etc.)
- Search for jokes by keyword 🔍
- Developer-friendly API endpoints
##Demo
- Random Joke Endpoint
GET /api/jokes/random  
- Response:
json

{
  "id": 1,
  "category": "Tech",
  "joke": "Why do programmers prefer dark mode? Because light attracts bugs!"
}
- Category Jokes Endpoint
GET /api/jokes/{category}  
Replace {category} with the desired category, such as tech, dad, or puns.

## Installation
- Clone the repository:
git clone https://github.com/Cyab1/joke.git  
- Navigate to the project directory:
cd joke  
- Install dependencies:
npm install  
_ Run the application:
npm start  
- Usage
Visit http://localhost:3000/api/jokes/random or any specific endpoint using tools like Postman, cURL, or your browser to explore the available jokes.

## Contributing
Contributions are welcome! 🎉 If you have jokes or features you'd like to add:

# Fork the repository.
- Create a new branch:
git checkout -b feature/your-feature-name  
- Commit your changes:
git commit -m "Added new feature/joke"  
- Push the branch:
git push origin feature/your-feature-name  
Open a Pull Request.

### License
This project is licensed under the MIT License.

### Author
Developed by Siyabonga Ndlovu. Check out more of my projects on GitHub https://github.com/Cyab1.

### Contact
Feel free to reach out with questions, feedback, or just to share a joke!

Email: ndlovusiyabonga181@gmail.com
LinkedIn: https://www.linkedin.com/in/siyabonga-ndlovu/
