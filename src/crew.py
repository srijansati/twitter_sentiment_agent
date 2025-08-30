from crewai import Agent, Crew, Process
from crewai.project import CrewBase, crew, agent
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class TwitterCrew():
    """
    Agents for analyzing sentiment of twitter users.
    """
    
    agents : List[BaseAgent]



    agents_config = "config/agent.yaml"

    @agent
    def data_scraper(self, tools) -> Agent:
        return Agent(
            config= self.agents_config['data_scraper'],
            verbose= True,
            tools= tools,
        )

    @agent
    def sentiment_analyzer(self) -> Agent:
        return Agent(
            config= self.agents_config['sentiment_analyzer'],
            verbose= True,
        )

    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config= self.agents_config['report_generator'],
            verbose = True
        )

        
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents= self.agents,
            process= Process.sequential,
            verbose= True
        )