# One Man Crew

One Man Crew is a Flask application that uses the `crewai` and `langchain` libraries to create a creative content generation system. It allows users to input tasks and expected outputs, and uses an AI model to generate the content.

## Features

- **Task Input**: Users can input tasks and expected outputs through a web form.
- **AI Content Generation**: The application uses an AI model to generate content based on the tasks and expected outputs provided by the user.
- **Result Display**: The generated content is returned as a JSON response.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/onemancrew.git
    cd onemancrew
    ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up the environment variables:
    ```bash
    export OPENAI_API_BASE=http://localhost:11434/v1
    export OPENAI_MODEL_NAME=Mixtral
    export SERPER_API_KEY=your_serper_api_key
    ```
4. Run the application:
    ```bash
    python app.py
    ```

## Usage

1. Open your web browser and navigate to `http://localhost:5000`.
2. Fill out the form with your task and expected output.
3. Click the 'Submit' button to generate the content.
4. The generated content will be displayed in the 'Output' section.

## Contributing

Contributions are welcome! Please read the contributing guidelines before getting started.

## License

This project is licensed under the terms of the MIT license. See the LICENSE file for details.
