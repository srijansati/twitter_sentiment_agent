from crewai_tools import MCPServerAdapter
from crew import TwitterCrew

server_params = {
    "url" : "http://localhost:3000/sse",
    "transport" : "sse"
}

def main():
    with MCPServerAdapter(serverparams= server_params, connect_timeout= 60) as mcp_tools:
        print(f"Available tools: {[tool.name for tool in mcp_tools]}")

        
        agent = TwitterCrew().data_scraper(tools= mcp_tools)

        result = agent.kickoff(messages= 'Scrape data form twitter profile of any random user.')

        print(result.raw)



if __name__ == "__main__":
    main()