![GenI-Banner](https://github.com/genilab-fau/genial-fau.github.io/blob/8f1a2d3523f879e1082918c7bba19553cb6e7212/images/geni-lab-banner.png?raw=true)


# Configuring the Prompt Engineering Lab for FAU students

> If you ARE NOT a FAU student, go to 
> [Configure Lab Enviroment for General Audience](https://github.com/genilab-fau/prompt-eng/CONFIG.md)
> 


The configuration requires:
* the **Prompt Engineeting Lab**, which provides the simulated GenAI pipeline, and;
* a **Model Server**, whcih for FAU studetns can be either a locally installed **Ollama Server** OR use [chat.fau.hpc.edu](chat.fau.hpc.edu).

You have a more options (than the general public) for this configuration:

* (Option 1): Install both **Prompt Engineeting Lab** and **OLLAMA Server** on the same computer (RECOMMENDED)
* (Option 2): Install **Prompt Engineeting Lab** on one computer and use the **OLLAMA Server** installed on other computer in the same network (or accessible through the Internet, if feasible)
* (Option 3): Install **Prompt Engineeting Lab** on your computer and integrate to [chat.fau.hpc.edu](chat.fau.hpc.edu).(SECOND BEST)
* (Option 4): Execute the **Prompt Engineeting Lab** through [MyBinder.org](http://mybinder.org)**, using the links to Binder Notebooks in every exercise and integrate to [chat.fau.hpc.edu](chat.fau.hpc.edu).(SECOND BEST)

We recommend using [Visual Code Studio](https://code.visualstudio.com) and installing everything on your computer.

For (Option 1) and (Option 2) follow the same instructions as in [Configure Lab Enviroment for General Audience](https://github.com/genilab-fau/prompt-eng/CONFIG.md)



For (Option 3) and (Option 4), the installing steps include:
* (Step 1) Downloading **Prompt Engineeting Lab** on your computer
* (Step 2) Connecting the **Prompt Engineeting Lab** to [chat.fau.hpc.edu](chat.fau.hpc.edu).
* (Step 3) Test the enviroment



# (Step 1) Downloading **Prompt Engineeting Lab** on your computer

This is the same as (Step 2) in [Configure Lab Enviroment for General Audience](https://github.com/genilab-fau/prompt-eng/CONFIG.md).

Please follow those instructions!

# (Step 2) Connecting the **Prompt Engineeting Lab** to chat.fau.hpc.edu

You need to configure the enviroment so that the **Prompt Engineeting Lab** connected to your Model Server at [chat.fau.hpc.edu](chat.fau.hpc.edu).

For that, you will need to:
* (Step 2.a) Collect the API_KEY from [chat.fau.hpc.edu](chat.fau.hpc.edu)
* (Step 2.b) Setup the `prompt_eng/_config` file


## (Step 2.a) Collect the API_KEY from chat.fau.hpc.edu

At FAU, we have our shared OLLAMA Server that can be accessed through an Open-WebUI interface at:

[http://fau.hpc.fau.edu](http://fau.hpc.fau.edu)

To use this service for our setup, you must generate and configure the API_KEY.

#### Finding **YOUR_API_KEY_HERE** 

1. Go to [http://fau.hpc.fau.edu](http://fau.hpc.fau.edu)
2. After login with your @fau account, go to `Your Account` (top-left)

![Your Account](./images/chatfau-login.png)

3. Next, go to `Accounts` tab on the right

![Account Tab](./images/chatfau-account.png)

4. Then , click on `Show` API Keys and copy the `JWST Key` 

![API Key](./images/chatfau-key.png)



## (Step 2.b) Setup the `prompt_eng/_config` file


Once you have collected the API_KEY, create `prompt_eng/_config` as:

```bash

# this is file: prompt-eng/config
# Point to the target open-webui

URL_GENERATE=https://chat.hpc.fau.edu/api/chat/completions
API_KEY=YOUR_API_KEY_HERE

```

# (Step 3) Test the Enviroment


To test the connection, you need to adjust the debug code in `prompt_eng/_pipeline` for the right TARGET and MODEL:

```python
###
### DEBUG
###

if __name__ == "__main__":
    from _pipeline import create_payload, model_req
    MESSAGE = "1 + 1"
    PROMPT = MESSAGE 
    payload = create_payload(
                         target="open-webui",  ## instead of "ollama"   
                         model="phi4:latest",  ## instead of "llama3.2:latest", 
                         prompt=PROMPT, 
                         temperature=1.0, 
                         num_ctx=100, 
                         num_predict=100)


```

Then you can execute the test code as:

```bash

python prompt-eng/_pipeline.py

```


If all goes well:


```bash

$ python3 prompt-eng/_pipeline.py
1 + 1 = 2
Time taken: 3.111s

```

If you are having problems, check [Troubleshooting ](https://github.com/genilab-fau/prompt-eng/TROUBLESHOOTING.md)

