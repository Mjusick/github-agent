from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_astradb import AstraDBVectorStore
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor
from langchain.tools.retriever import create_retriever_tool
from langchain import hub
from github import fetch_github_issues
from note import note_tool

load_dotenv()

def connect_to_vstore():
    embeddings = OpenAIEmbeddings()
    ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
    desired_namespace = os.getenv("ASTRA_DB_KEYSPACE")
    ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
    
    if desired_namespace:
        ASTRA_DB_KEYSPACE = desired_namespace
    else:
        ASTRA_DB_KEYSPACE = None


    vstore = AstraDBVectorStore(
        embedding=embeddings,
        collection_name="github",
        api_endpoint=ASTRA_DB_API_ENDPOINT,
        token=ASTRA_DB_APPLICATION_TOKEN,
        namespace=ASTRA_DB_KEYSPACE,
    )
    return vstore

vstore = connect_to_vstore()
add_to_vectorstore = input("Add to vectorstore? (y/n): ").lower() in ["y", "yes"]
if add_to_vectorstore:
    owner = "SeleniumHQ"
    repo = "selenium"
    issues = fetch_github_issues(owner=owner, repo=repo)

    try:
        vstore.delete_collection()
    except:
        pass

    vstore = connect_to_vstore()
    
    # Add documents with error handling for large documents
    successful_docs = 0
    skipped_docs = 0
    for issue in issues:
        try:
            vstore.add_documents([issue])
            successful_docs += 1
        except Exception as e:
            print(f"Error adding document: {e}")
            skipped_docs += 1
    
    print(f"Added {successful_docs} documents, skipped {skipped_docs} documents")

retriever = vstore.as_retriever(search_kwargs={"k": 3})
retriever_tool = create_retriever_tool(retriever, name="github", description="Search Github issues")

prompt = hub.pull("hwchase17/openai-functions-agent")
llm = ChatOpenAI()

tools = [retriever_tool, note_tool]
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

while(question := input("Ask about github issues (q to quit): ")) != "q":
    result = agent_executor.invoke({"input": question})
    print(result["output"])