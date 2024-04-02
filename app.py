from flask import Flask, render_template, request
from flask import jsonify
import os
from crewai import Agent, Task, Crew, Process
from langchain.agents import Tool
from langchain.utilities import GoogleSerperAPIWrapper
from langchain_groq import ChatGroq

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Capture the form inputs
        product = request.form['product']
        agentType = request.form['agentType']
        goally = request.form['goally']
        story = request.form['story']
        taskone = request.form['taskone']
        expectedone = request.form['expectedone']
        tasktwo = request.form['tasktwo']
        expectedtwo = request.form['expectedtwo']

        # Set up the environment variables (you should secure your API keys)
        os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"
        os.environ["OPENAI_API_BASE"] = "http://localhost:11434/v1"
        os.environ["OPENAI_MODEL_NAME"] = "Mixtral"
        os.environ["SERPER_API_KEY"] = "e4d0233da25a57465ed77b37b17eec2035d51738"

        llm = ChatGroq(
            temperature=0, 
            groq_api_key="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",
            model_name="mixtral-8x7b-32768"
        )

        search = GoogleSerperAPIWrapper()
        serper_tool = Tool(
            name="Intermediate Answer",
            func=search.run,
            description="Useful for search-based queries",
        )

        writer = Agent(
            role=agentType,
            goal=product + " " + goally,
            backstory=story,
            verbose=True,
            allow_delegation=True,
            tools=[serper_tool],
            llm=llm
        )

        task1 = Task(
            description=taskone,
            expected_output=expectedone,
            agent=writer
        )

        task2 = Task(
            description=tasktwo,
            expected_output=expectedtwo,
            agent=writer
        )

        crew = Crew(
            agents=[writer],
            tasks=[task1, task2],
            verbose=2
        )

        result = crew.kickoff()
        print()
        print(result)
        # Return the result as JSON
        return jsonify(result=result)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
