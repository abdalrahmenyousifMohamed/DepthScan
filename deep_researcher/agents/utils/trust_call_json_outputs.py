from langchain_openai import ChatOpenAI
from trustcall import create_extractor
from pydantic import BaseModel, Field
from typing import List


llm=ChatOpenAI(model="AMead10/SuperNova-Medius-AWQ", verbose=True,api_key="tst" , openai_api_base="https://z9v53bple9owlo-8000.proxy.runpod.net/v1")

def get_json_output(type:BaseModel,message):
    print(f"--- processing type:{type} for message : {message} ")
    try:
       bound = create_extractor(
            llm,
            tools=[type.model_json_schema()],
            # tool_choice=f"{type}",
        )
       result = bound.invoke(
            f"""
    Extract the  Output from the following result:
    {str(message)}
    The output should be in the following format:
    {type.model_json_schema()}
        """ )
       tool_call_text = result["messages"][0].content
       import re,json
       match = re.search(r"<tool_call>\s*(\{.*\})\s*</tool_call>", tool_call_text, re.DOTALL)
       if match:
            tool_call_data = json.loads(match.group(1))
            res = tool_call_data["arguments"]
            print(f"parsed output : {res}")
       else:
            print("No tool_call content found.")
       return res

    except Exception as e:
        print(f"Error occurred: {e}")
        return ["error"]  # Return an empty list as a fallback