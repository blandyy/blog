from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class Crewai():
    """Crewai crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def product_manager(self) -> Agent:
        return Agent(
            config=self.agents_config["product_manager"], # type: ignore[index]
            verbose=True
        )

    @agent
    def software_architect(self) -> Agent:
        return Agent(
            config=self.agents_config["software_architect"], # type: ignore[index]
            verbose=True
        )

    @task
    def requirement_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["requirement_analysis_task"], # type: ignore[index]
            output_file="requirement_analysis.md"
        )

    @task
    def architecture_design_task(self) -> Task:
        return Task(
            config=self.tasks_config["architecture_design_task"], # type: ignore[index]
            output_file="architecture_design.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Crewai crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
