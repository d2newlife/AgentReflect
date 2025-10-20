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


def generation_node(state: GraphState) -> List[BaseMessage]:
    gen_response = generate_chain.invoke({"messages": state["messages"]})
    return {"messages": [gen_response]}

def reflect_node(state: GraphState) -> List[BaseMessage]:
    ref_response = reflect_chain.invoke({"messages": state["messages"]})
    return {"messages": [HumanMessage(content=ref_response.content)]}

def should_continue(state: GraphState) -> str:
   if len(state["messages"]) >= 4:
       return END
   return REFLECT


execGraph = StateGraph(GraphState)
execGraph.add_node(GENERATE, generation_node)
execGraph.add_node(REFLECT, reflect_node)
execGraph.set_entry_point(GENERATE)
execGraph.add_conditional_edges(GENERATE, should_continue, {END:END, REFLECT:REFLECT})
execGraph.add_edge(REFLECT, GENERATE)

app = execGraph.compile()
print(app.get_graph().draw_mermaid())

if __name__ == "__main__":
    # Example usage:
    input = HumanMessage(content="Write a tweet about the benefits of learning Python.")
    final_state = app.invoke({"messages": [input]})
    print(final_state["messages"][-1].content)