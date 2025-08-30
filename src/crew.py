from crewai import Agent, Crew, Process
from crewai.project import CrewBase, crew, agent
import yaml

import crewai

@CrewBase
class TwitterCrew():
    """
    Agents for analyzing sentiment of twitter users.
    """
    agents_config = "config/agent.yaml"

    @agent
    def data_scraper(self, tools):
        return Agent(
            config= self.agents_config['data_scraper'],
            verbose= True,
            tools= tools,
        )

    @agent
    def sentiment_analyzer(self):
        return Agent(
            config= self.agents_config['sentiment_analyzer'],
            verbose= True,
        )

    @agent
    def report_generator(self):
        return Agent(
            config= self.agents_config['report_generator'],
            verbose = True
        )

        