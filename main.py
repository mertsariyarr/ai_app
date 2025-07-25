import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_files_content
from functions.write_file import schema_write_file
from functions.run_python import schema_run_python_file
from prompts import system_prompt
from functions.call_function import call_function, available_functions



def main():
    load_dotenv()
    args = sys.argv[1:]
    verbose = "--verbose" in sys.argv
    if not args:
        print("Give us something to respond!")
        sys.exit(1)
        

    user_prompt = " ".join(args)


    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    ###

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]) ##We store user's prompts for tracking conversation history and answer the question in convension.
    ]




    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_files_content,
            schema_write_file,
            schema_run_python_file
        ]
    )


    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt
            ) 
        
    )
    

    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(response._get_text())

    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])
    
    if not function_responses:
        raise Exception("no function responses generated, exiting.")


    # if "--verbose" in args:
    #     print(f"User prompt: {user_prompt}")
    #     print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    #     print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
  


if __name__ == "__main__":
    main()
