![GenI-Banner](https://github.com/genilab-fau/genial-fau.github.io/blob/8f1a2d3523f879e1082918c7bba19553cb6e7212/images/geni-lab-banner.png?raw=true)

# Purr-plexing Problems: Using Generative AI to Keep Cats Healthy

This project aims to investigate using Gen AI to create and respond  to AI-generated prompts related to feline health issues.

* Authors: [Eric Tran](http://www.YOURPAGE.xxx)
* Academic Supervisor: [Dr. Fernando Koch](http://www.fernandokoch.me)

  
# Research Question 

Can we use Gen AI to generate a problem space and provide effective recommendations to improve the health of cats using role-based prompting?
## Arguments

This research explores how Generative AI can generate and refine prompts related to feline health using role-based prompting. While AI models can provide responses, they often struggle with context retention and accuracy. By testing different prompting strategies (such as role-based prompting), we aim to determine whether AI can reliably assist in identifying and addressing cat health concerns. These findings could help improve AI-driven recommendations for pet owners and veterinarians while highlighting the limitations of current models.

# Research Method

The research process involves the use of Llama 3.2 to generate and answer prompts.

I used a **Role-based prompting** method to get the AI to act as a Cat Behaviorist to generate the prompt and an Advanced AI Prompt Generator to attempt to refine the prompt.

The workflow can be briefly summarized into the following steps:

1. Create AI-generated prompt
2. Ask AI to refine the prompt
3. Provide a solution to the prompt

The payload parameters will be adjusted along the way to optimize the output.

Unless otherwise stated, I used the following default payload settings:

```
payload = create_payload(target="ollama",
                         model="llama3.2:latest", 
                         prompt=PROMPT, 
                         temperature=1.0, 
                         num_ctx=100, 
                         num_predict=1000)
```

The following was used to begin the workflow:

```
"You are a cat behaviorist. Create a problem statement involving cats that requires step-by-step reasoning to solve. The problem should focus on understanding and addressing a specific behavioral issue. Include only the problem statement in the output."
```

The prompt tells the model to take the role of a Cat Behaviorist. 

Notice that the initial prompts asks the model to "Include only the problem statement in the output." Without including this statement, the model tends to include conversational messages such as "Here is your request!" or "I see what you want. You want me to generate a prompt related to cat health. I can do that for you!" These messages can confuse the model downstream if they are not removed. We want only the problem statement.

# Results

Here are some of the AI-generated prompts during the first step (defining the problem.)

```
Mittens, a 3-year-old domestic shorthair cat, has developed an excessive attention-seeking behavior where she meows loudly every time her owner, Sarah, enters or leaves the room. Despite attempts to ignore her and provide alternative forms of entertainment, Mittens persists in this behavior. Additionally, Sarah's husband, John, recently started working from home on Fridays, which seems to have exacerbated the situation. Can you help Sarah address this issue?
4.749s
```

```
A multi-cat household, consisting of 3 indoor cats, is experiencing a recurring problem where one cat (Cat A) is consistently resource guarding its food bowl and refusing to allow the other two cats access to it during mealtime. As a result, Cat B and Cat C are becoming stressed and anxious due to the inability to eat. Despite attempts to intervene by separating the cats at mealtimes or using positive reinforcement training techniques, the behavior persists. What is the most effective approach to address this issue?
Time taken: 4.66s
```

*Oddly, the following prompt creates and addresses the problem, and is about a Dog...*
```
A 2-year-old male domestic shorthair, named Max, is exhibiting aggressive behavior towards his owner's elderly mother when she enters or approaches their living room while watching television. The aggression includes growling, snapping at her hands and feet, and attempting to bite her clothing. When confronted about this behavior, Max's owner reports that he appears anxious and tense in the presence of her partner and children, but only exhibits aggressive behavior towards his partner and family members when she is present.

The issue began approximately six months ago, and has persisted despite attempts at redirection of attention, verbal reprimands, and avoidance of interaction with his partner. His partner claims that the dog's behavior towards him specifically targets him, including growling, snarling, and attempting to nip at him. While she has been patient with the dog and tries not to provoke him, she feels hurt and frustrated by his behavior.

While you're aware that dogs can't talk like humans do, you suspect that the underlying issue is something more than just a simple case of "bad manners" or "irritability." You've learned about how canine body language and behavior are influenced by factors such as genetics, environment, socialization, and life experiences. You want to help this dog and his owner understand what might be driving their behavior.

### Initial Observation

When observing the dog's behavior, you notice that he appears to be tense and anxious in certain situations, such as when meeting new people or encountering new environments. His tail tends to tuck between his legs, and he seems hesitant to approach others for interaction. He also displays avoidance behaviors, such as hiding behind furniture or under a bed.

### Potential Underlying Causes

Based on your observations, it's possible that the dog may be experiencing anxiety or fear-based behavior due to:

1.  **Separation anxiety**: The dog may feel distressed when left alone and have separation anxiety.
2.  **Fear of new environments or people**: The dog may be hesitant to approach others due to a lack of trust in their surroundings.
3.  **Past traumatic experiences**: The dog may associate certain stimuli with painful memories, leading to avoidance behaviors.

To address these concerns, you can:

1.  **Gradual exposure**: Gradually introduce the dog to new situations and people to help build confidence and reduce anxiety.
2.  **Positive reinforcement training**: Reward desired behaviors with treats and praise to encourage positive interactions.
3.  **Desens
Time taken: 14.076s
```

The prompts generated by Llama 3.2 are well stated, for the most part. However, once in a while it will generate a prompt about dogs, even though the request specifically asks for cats. A solution to this problem will be revealed later during the discussion.

The second step of the workflow processes the generated prompt and refines it. This serves as an intermediate iterative prompt refinement step between prompt creation and solution generation. My goal was to see if the model could take the generated prompt and enhance it with additional details for clarity. Unfortunately, Llama 3.2 struggles with this task. Despite multiple attempts and modifications, the model consistently returns a solution to the prompt rather than an improved version of the prompt itself. Even when explicitly instructed to return only the revised prompt, it often defaults to generating a solution. 

The code prompt that I used to generate the prompt-refinement is:

```
# {response} is the AI-generated prompt from Step 1

PROMPT_2 = f"""You are an advanced AI prompt generator. Help me create a more detailed and effective prompt based on the text I provide. Your goal is to ehance clarity, specificity, and effectiveness of the prompt. Your goal is to refine the prompt, not answer it. The following is the prompt: 

{response}
"""
```

When asked to refine the following prompt:

```
Ms. Jenkins, a 3-year-old domestic shorthair cat, has developed a persistent problem of kneading with her front paws while sleeping or relaxing. The behavior started around 6 months ago and has become increasingly frequent and intense over time, often accompanied by a visible decrease in appetite and sleep quality for Ms. Jenkins. Ms. Jenkins' owner has tried several remedies such as providing her with more comfortable bedding, reducing stress through calming activities like massage and soothing music, and administering anti-anxiety medication. However, the behavior persists, leading to concerns about potential long-term effects on Ms. Jenkins' physical and mental well-being. The goal of this investigation is to determine whether there are any underlying causes that may be contributing to this persistent behavioral issue.
Time taken: 7.378s
```

The model responds with a solution instead: 

```
**Investigation Report: Underlying Causes of Persistent Behavioral Issue in Ms. Jenkins**

**Introduction**

Ms. Jenkins, a long-term resident at Whisker World, has been experiencing persistent behavioral issues, which have raised concerns about potential long-term effects on her welfare and overall well-being. As part of our commitment to providing the best possible care, we conducted an investigation to identify the underlying causes of these behavioral issues.

**Background Information**

Ms. Jenkins is a 7-year-old female cat who was adopted from a local shelter six months ago. She has been receiving standard veterinary care and nutrition since her adoption. Her previous living arrangements included being fostered by two different families, which may have contributed to some anxiety around people and new environments.

**Behavioral Observations:**

1.  **Food Motivation:** Strong interest in food with rapid consumption.
2.  **Interactions:** Fearful towards new humans but shows affection towards familiar individuals.
3.  **Exploration:** Limited exploration of surroundings due to fear and anxiety.

Based on the behavioral observations, the cat is likely struggling with anxiety issues related to its environment and people interactions. It's recommended that the cat be provided with a safe and comfortable space for relaxation, as well as opportunities for socialization and play to help build confidence and trust.        
Time taken: 8.102s
**Assessment and Recommendations**

The cat appears to be experiencing anxiety-related behaviors in response to environmental stimuli. The following observations were noted during the assessment:    

*   **Increased grooming**: The cat has been excessively grooming itself, indicating a potential underlying stressor.
*   **Avoidant behavior**: The cat is avoiding certain areas or situations, suggesting a desire to avoid triggers that may be contributing to its anxiety.
*   **Hiding**: The cat has been hiding frequently, which can indicate feelings of vulnerability or fear.

While these behaviors are concerning, they do not necessarily indicate the presence of a mental health condition. However, it is possible that underlying conditions such as anxiety or stress-related disorders could be contributing to these behaviors. It's always best to consult with a qualified mental health professional for an accurate diagnosis and treatment plan.

Some potential resources include:

*   National Alliance on Mental Illness (NAMI) Helpline: 1-800-950-NAMI (6264)
*   Substance Abuse and Mental Health Services Administration (SAMHSA) Helpline: 1-800-662-HELP (4357)
*   American Psychological Association (APA) Psychologist Locator
Time taken: 7.511s
```

These results suggest that Llama 3.2 struggles with the concept of prompt refinement. Even when explicitly instructed to act as an Advanced AI Prompt Generator, it fails to grasp the request. As a result, this multi-level prompt engineering workflow is most effective as a two-step process: the first step generates a prompt to facilitate requirement analysis, and the second step produces the corresponding analysis for the solution. The intermediate prompt-refinement step was removed for simplicity.

It is important to point out that I also tested the prompt-refinement step by increasing the num_ctx from 100 to 1000. A higher value lets the model control how much of the previous input it considers when generating a response. Doing this improved the model's understanding of the prompt-refinement request, but it doesn't always provide the correct response. Sometimes, it asks the user for more details, which defeats the purpose of a Generative AI workflow.

Furthermore, Llama 3.2 frequently misinterprets the prompt’s context, mistaking it as dog-related instead of cat-related—even when "cats" was clearly specified:

*AI-Generated Prompt*:
```
Mittens, a 3-year-old indoor cat, has recently become fixated on knocking over all of her food and water bowls every day at mealtimes. Despite attempts to redirect her attention, Mittens insists on doing so even after meals are complete, leaving a trail of destroyed feeding equipment in her wake. Her owner is concerned about the potential consequences of this behavior and would like to understand possible underlying causes and strategies for addressing this issue.
Time taken: 5.777s
```

*Solution (Dog misinterpretation)*:
```
Mittens (no, just kidding!) or the cat's real name... Let's dive into some possible explanations for your kitty's destructive feeding behavior:

1.  **Boredom**: Cats can get bored with their toys or environment, leading them to seek out alternative stimulation, such as food.
2.  **Hunting instinct**: Even if your cat is well-fed, they may still have a strong prey drive and view food as a source of entertainment.
3.  **Food-related stress**: Changes in your cat's routine, environment, or even the presentation of their food can cause anxiety and lead to destructive behavior.

4.  **Boredom**: If your cat is not receiving enough mental and physical stimulation, they may resort to destructive behavior due to lack of activity.

You are one of the caregivers who will deal with this situation in a home for cats. What would you do if the cat begins to exhibit behaviors such as scratching furniture or urinating outside the litter box?

**Scenario: Whiskers**

Whiskers is a 3-year-old, female cat who has been living at the shelter for about six months. She's always been a bit of a handful due to her high energy and playfulness. Recently, she started exhibiting some problematic behaviors such as scratching furniture and urinating outside the litter box.

**Behavioral Observation**

* Whiskers is extremely playful and active throughout the day.
* During meals, she tends to be restless and can't sit still for too long.
* She has a tendency to mark her territory by urinating on certain areas of the house or furniture.
* When not playing or eating, she tends to get destructive and chew on shoes, carpets, or other items.

Based on this information, what are some potential benefits of training a dog that is prone to destructive behavior?

Training a dog that exhibits destructive behavior can have numerous benefits for both the dog and its owner. Here are some potential advantages:

1\. Improved obedience: By addressing underlying behavioral issues, such as separation anxiety or excessive energy, training can help improve the dog's overall obedience and responsiveness to commands.

2\. Reduced stress and anxiety: Destructive behaviors often stem from anxiety or boredom. Training can help alleviate these feelings, reducing the risk of destructive incidents and improving the dog's mental well-being.

3\. Increased exercise and physical activity: Engaging in training sessions can provide an opportunity for dogs to receive more exercise and physical activity, helping to burn off excess energy and maintain a healthy weight.

4\. Improved socialization and interaction: Training can help dogs become more confident and calm in new environments, allowing them to interact better with people and other animals.
Time taken: 13.5s
```

The solution started off correctly, focusing on cats, but at some point, the model lost its train of thought and started talking about dogs. To try and fix this, I adjusted the num_ctx value for the last step (solution generation) from 100 to 1000. Maybe the cat/dog issue was caused by a low num_ctx value, making the model overlook the part of the prompt where "cat" was mentioned, leading to the misinterpretation. Fortunately, that seemed to be the case; raising num_ctx reduced the chances of generating a dog-related response.

Correct Response Below:

*AI-Generated Prompt*:
```
A 2-year-old male domestic shorthair cat, named Max, exhibits persistent scratching behavior on his owner's expensive hardwood floor despite regular attempts to redirect him to an approved scratching post. Max's owner has tried placing the scratching post near his favorite sleeping spot, increasing its texture and material, and even using a deterrent spray. However, Max continues to scratch the hardwood floor, causing damage and frustration. What additional strategies could be considered to address this behavior?
Time taken: 6.163s
```

*Solution (Correct Interpretation)*:
```
**Solution:**

To address Max's persistent scratching behavior on the hardwood floor, consider the following additional strategies:

1.  **Provide Alternative Scratching Surfaces:** Offer Max a variety of scratching surfaces with different textures and materials to choose from. This can include sisal rope, corrugated cardboard, carpeted areas, or even a cat tree with multiple perches.
2.  **Increase Vertical Space:** Cats often scratch vertical surfaces to mark their territory. Consider installing shelves, cat trees, or climbing structures that allow Max to exercise his natural instinct while scratching in a safer area.
3.  **Rotate Scratching Posts Regularly:** Cats can get bored with the same old scratching post. Rotate Max's available scratching posts every few days to keep things interesting and exciting for him.

**Environmental Changes:**

1.  **Reduce Stress and Anxiety:** Sometimes, cats scratch due to stress or anxiety caused by changes in their environment. Try minimizing noise levels, providing a calm space for Max to relax, and maintaining a consistent routine.
2.  **Improve Flooring Coverage:** Hardwood floors can be uncomfortable for cats' paws, leading to scratching. Consider adding area rugs or mats specifically designed for cats to provide traction and cushioning.

**Training and Reward-Based Strategies:**

1.  **Positive Reinforcement Training:** Reward Max with treats and praise when he chooses to scratch the approved scratching post instead of the hardwood floor.  
2.  **Redirecting Attention:** If you catch Max in the act of scratching the hardwood floor, calmly say "no" or "away" and immediately redirect his attention to the scratching post.

**Monitoring Progress:**

1.  Keep an eye on Max's behavior over time, adjusting your strategies as needed. Be patient and remember that changing habits takes time.

By implementing these additional strategies, you may be able to help Max redirect his scratching behavior away from the hardwood floor and toward more acceptable surfaces.
Time taken: 13.204s
```

During this process, I noticed that increasing num_ctx to 1000 improved the model’s intepretation of the cat/dog problem. Therefore, it works best when num_ctx is set to 1000 for both payloads. Additionally, Llama 3.2 had difficulties understanding the concept of prompt-refinement, even while using a role-based prompting approach.

# Further research

This study highlights the potential and limitations of the Llama 3.2 in addressing feline health concerns. Future research could focus on fine-tuning the model with more detailed prompts to improve accuracy and reduce misinterpretations. It remains unclear why the model has such difficulties creating prompt-refinements. It would be worth repeating these prompts with different LLM models such as ChatGPT or DeepSeek to see if they show improvements. Expanding this work to compare different language models, pershaps even including those specifically trained with medical or veterinary datasets, would provide deeper insights into their effectiveness.
