from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama

def create_response(prompt, input_array):
    title, page, snippet = input_array
    model = Ollama(model="llama3")

    shia_scholar = Agent(
        role='Shia Islamic Scholar',
        goal='Provide detailed answers based on Shia Islamic teachings for the given input',
        verbose=True,
        memory=True,
        backstory=(
            "As a knowledgeable Shia Islamic scholar, you aim to provide"
            "insightful and accurate answers based on the teachings and"
            "traditions of Shia Islam."
        ),
        llm=model,
        allow_delegation=False
    )

    scholar_task = Task(
        description=(
            f"Given the prompt '{prompt}', the title '{title}', and the snippet '{snippet}',"
            " provide a detailed answer based on Shia Islamic teachings."
        ),
        expected_output='A scholarly response elaborating on the provided snippet.',
        llm=model,
        agent=shia_scholar,
    )

    crew = Crew(
        agents=[shia_scholar],
        tasks=[scholar_task],
        process=Process.sequential
    )

    result = crew.kickoff(inputs={})
    return result
