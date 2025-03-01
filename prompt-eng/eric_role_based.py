##
## ROLE-Based PROMPTING
##

from _pipeline import create_payload, model_req

# 1) Create a prompt for running this requirement analysis
# 2) The payload will be created
# 3) The prompt will be generated
# 4) Use the output prompt to call the model again (essentially, just copy/paste the same code). 
# Here, there is no human validation. The model validates the prompt in between (we are no longer the agent)
# Play around with changing the temperature and the context and generate alternatives. Pick a model.
# 0.5, 0.8, 1.0, 1.5, 1.8,
# 100, 500.

MESSAGE = "You are a cat behaviorist. Create a problem statement involving cats that requires step-by-step reasoning to solve. The problem should focus on understanding and addressing a specific behavioral issue. Include only the problem statement in the output."

PROMPT = MESSAGE

#### (3) Configure the Model request, simulating Workflow Orchestration
# Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md
payload = create_payload(target="ollama",
                         model="llama3.2:latest", 
                         prompt=PROMPT, 
                         temperature=1.0, 
                         num_ctx=100, 
                         num_predict=1000)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, response = model_req(payload=payload)
print(response)
if time: print(f'Time taken: {time}s')

# ### REFINE THE PROMPT ###
# PROMPT_2 = f"""You are an advanced AI prompt generator. Help me create a more detailed and effective prompt based on the text I provide. Your goal is to ehance clarity, specificity, and effectiveness of the prompt. Your goal is to refine the prompt, not answer it. The following is the prompt: 

# {response}
# """

# payload = create_payload(target="ollama",
#                          model="llama3.2:latest", 
#                          prompt=PROMPT_2, 
#                          temperature=1.0, 
#                          num_ctx=1000, 
#                          num_predict=1000)

# time, response = model_req(payload=payload)
# print(response)
# if time: print(f'Time taken: {time}s')

### USE REPONSE AS INPUT TO GENERATE SOLUTION ###
PROMPT_3 = f"""Generate a solution for this prompt:

### Prompt:
{response}

"""

payload = create_payload(target="ollama",
                         model="llama3.2:latest", 
                         prompt=PROMPT_3, 
                         temperature=1.0, 
                         num_ctx=1000, 
                         num_predict=1000)

time, response = model_req(payload=payload)
print(response)
if time: print(f'Time taken: {time}s')