from typing import List, Sequence, Union, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import StateGraph, END, START
from chains import generate_chain, reflect_chain
from dotenv import load_dotenv
from typing_extensions import Annotated
import operator

load_dotenv()


REFLECT="reflect"
GENERATE="generate"


class GraphState(TypedDict):
    messages: Annotated[List[BaseMessage], operator.add]


def generation_node(state: List[BaseMessage]) -> List[BaseMessage]:
    gen_response = generate_chain.invoke(messages=state["messages"])
    return {"messages": [gen_response]}

def reflect_node(state: List[BaseMessage]) -> List[BaseMessage]:
    ref_response = reflect_chain.invoke(messages=state["messages"])
    return {"messages": [HumanMessage(content=ref_response.content)]}


execGraph = StateGraph(GraphState)
execGraph.add_node(GENERATE, generation_node)
execGraph.add_node(REFLECT, reflect_node)
execGraph.set_entry_point(GENERATE)
execGraph.add_edge(GENERATE, REFLECT)
execGraph.add_edge(REFLECT, GENERATE)

app = execGraph.compile()

if __name__ == "__main__":
    print("This script is being run directly.")
    # Example usage:
    # final_state = app.invoke({"messages": [HumanMessage(content="Write a tweet about the benefits of learning Python.")]})
    # print(final_state["messages"][-1].content)