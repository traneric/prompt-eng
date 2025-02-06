# Configure your Lab Enviroment with CHAT@FAU

**This is for Florida Atlantic University students only.**


## Model Server

At FAU, we have our [OLLAMA](http://www.ollama.com)  configure through a Open-WebUI interface at:

[http://fau.hpc.fau.edu](http://fau.hpc.fau.edu)

To use this Ollama Server, you must generate and configure the API_KEY into `prompt-eng/_config` file as

```bash
# this is file: prompt-eng/config
URL=http://localhost:11434/api/generate
```

Note: if you install OLLAMA server on anoher computer, remeber to make it listen to all network devices to be able to access remotely:

```bash
# this is file: prompt-eng/config
# Point to the target Ollama or Open-WebUI Server

URL_GENERATE=https://chat.hpc.fau.edu/api/chat/completions
API_KEY=YOUR_API_KEY_HERE
```

## Finding **YOUR_API_KEY_HERE** 

1. Go to [http://fau.hpc.fau.edu](http://fau.hpc.fau.edu)
2. After login with your @fau account, go to `Your Account` (top-left)

![Your Account](./images/chatfau-login.png)

3. Next, go to `Accounts` tab on the right

![Account Tab](./images/chatfau-account.png)

4. Then , click on `Show` API Keys and copy the `JWST Key` 

![API Key](./images/chatfau-key.png)
