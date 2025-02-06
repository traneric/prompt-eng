![GenI-Banner](./images/geni-banner.png)

# Configure your Lab Enviroment

## Model Server

The simplest way to experiment with this Prompt Engineering Lab is to have [OLLAMA](http://www.ollama.com) installed on localhost or some accessible network point.

The alternative way for FAU students is to [Config Chat@FAU](./CONFIG-FAU.md)

### Ollama Server

Then you adjust your `prompt-eng/_config` file as

```bash

URL_GENERATE=http://OLLAMA_SERVER_IP:11434/api/generate

```

Note: if you install OLLAMA server on anoher computer, remeber to make it listen to all network devices to be able to access remotely:

```bash
export OLLAMA_HOST=0.0.0.0
ollama server
```

## Lab Enviroment

Our exercises can be executed from Jupyter Notebooks that you can setup in different ways:
* **use your computer**, e.g. using [Visual Studio Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) or [installing Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)
* **use [MyBinder.org](http://mybinder.org)**: we provide links to Binder Notebooks in every exercise


To install on your computer, you first have to clone the code from Github:

```bash
git clone https://github.com/GenILab-FAU/prompt-eng.git prompt-eng
```

If installing locally, remember to make sure you have the dependencies installed:

```bash

python -m pip install --break-system-packages -r requirements.txt

```

In any case you need to **adjust the CONFIGURATION file**:

[prompt-eng/_config](./prompt-eng/_config.example)

Once executing, you will be able to duplicate the exemples being provided by modifying the configuration in three easy points:

* **(1) Change the Simulated inbounding message**

```python

MESSAGE = "What is 2 * log(10)?"

```

* **(2) Adjust the Prompt Engineering Technique to be applied**

```python

TEMPLATE_BEFORE = "Act like you are a math teacher\nYour student is asking:"
TEMPLATE_AFTER = "Give only the answer; refrain from any more information"
PROMPT = TEMPLATE_BEFORE + '\n' + MESSAGE + '\n' + TEMPLATE_AFTER

```

* **(3) Configure your payload (optional)**

Documentation about [available parameters](https://github.com/ollama/ollama/blob/main/docs/api.md).

```python

payload = create_payload(model="llama3.2", 
                         prompt=PROMPT, 
                         temperature=1.0, 
                         num_ctx=100, 
                         num_predict=100)
```

