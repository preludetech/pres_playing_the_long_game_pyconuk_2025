# The Hater's Guide To The AI Bubble
https://www.wheresyoured.at/the-haters-gui/ 

Magnificent 7 stocks — NVIDIA, Microsoft, Alphabet (Google), Apple, Meta, Tesla and Amazon — make up around 35% of the value of the US stock market, and of that, NVIDIA's market value makes up about 19% of the Magnificent 7.

May 2025:
Microsoft, Amazon, Meta, Alphabet, and Tesla alone make up 42.4% of NVIDIA's revenue. The breakdown makes things worse. 
Meta spends 25% — and Microsoft an alarming 47% — of its capital expenditures on NVIDIA chips
Microsoft rents servers from CoreWeave - accounted for $8 billion (more than 6%) of NVIDIA's revenue in 2024
companies like CoreWeave and Crusoe — that exist only to prove AI compute services — account for as much as 10% of NVIDIA's revenue.


The Magnificent 7's AI Story Is Flawed, With $560 Billion of Capex between 2024 and 2025 Leading to $35 billion of Revenue, And No Profit



# Model explosion
https://huggingface.co/models?sort=trending&search=prescription 
compare that to ChatGPT 5. Winner take all?




# Is there a wall? An Evidence-Based Analysis of Diminishing Returns in Large Language Model Scaling: Investigating Benchmark Plateaus, Data Scarcity, and Computational-Economic Constraints
https://medium.com/@adnanmasood/is-there-a-wall-34d02dfd85f3
throwing 50× more compute into training only yielded incremental improvements for GPT-4




# How to Upscale Neural Networks with Scaling Law? A Survey and Practical Guidelines
https://arxiv.org/html/2502.12051v1
Neural scaling laws have revolutionized the design and optimization of large-scale AI models by revealing predictable relationships between model size, dataset volume, and computational resources. Early research established power-law relationships in model performance, leading to compute-optimal scaling strategies. However, recent studies highlighted their limitations across architectures, modalities, and deployment contexts. Sparse models, mixture-of-experts, retrieval-augmented learning, and multimodal models often deviate from traditional scaling patterns. Moreover, scaling behaviors vary across domains such as vision, reinforcement learning, and fine-tuning, underscoring the need for more nuanced approaches. In this survey, we synthesize insights from over 50 studies, examining the theoretical foundations, empirical findings, and practical implications of scaling laws. We also explore key challenges, including data efficiency, inference scaling, and architecture-specific constraints, advocating for adaptive scaling strategies tailored to real-world applications. We suggest that while scaling laws provide a useful guide, they do not always generalize across all architectures and training strategies.

- The most common neural scaling laws take the form of power laws (Equation 1), where the model’s loss (L) or performance metric assumes to follow a predictable relationship with different scaling variables,
- Despite the growing importance of scaling laws, existing research remains fragmented, with limited synthesis of theoretical foundations, empirical findings, and practical implications. 
- However, recent studies Muennighoff et al. (2023); Caballero et al. (2023); Krajewski et al. (2024) have challenged the universality of these laws, highlighting cases where sparse models, mixture-of-experts architectures, and retrieval-augmented methods introduce deviations from traditional scaling patterns. These findings suggested that while scaling laws provide a useful guide, they do not always generalize across all architectures and training strategies.
- model performance can sometimes worsen before improving, depending on dataset thresholds and architectural bottlenecks (Caballero et al., 2023). Another exciting development came from small LMs, where optimized training strategies, such as a higher data-to-parameter ratio and adaptive learning schedules, enable models ranging from 1.2B to 2.4B parameters to rival significantly larger 7B-13B models (Hu et al., 2024). These findings reshape the fundamental assumptions of scaling laws,
- The best performance comes from balancing model size and data, rather than just increasing parameters.
- Performance does not always improve smoothly; there are inflection points where scaling stops working.
- Smaller models with better training can rival much larger models.

# Is there a wall? An Evidence-Based Analysis of Diminishing Returns in Large Language Model Scaling: Investigating Benchmark Plateaus, Data Scarcity, and Computational-Economic Constraints
https://medium.com/@adnanmasood/is-there-a-wall-34d02dfd85f3
- Gains that were once leaps (e.g. GPT-3 to GPT-4) have become incremental. Figure 1 illustrates how MMLU accuracy nearly doubled from 2020 to 2023 but has since begun to plateau, approaching an apparent ceiling around human-level performance.
- Impending Data Shortage: Modern LLMs are voracious, trained on trillions of tokens. Developers have “quickly exhausted available data online” [3]. Epoch AI estimates the stock of high-quality English text (~300 trillion tokens) could be fully utilized by 2026–2032 [4], [2]. In fact, median projections suggest 2028 as the tipping point when fresh human-generated text is effectively tapped out [3]. Figure 2 shows how dataset sizes (blue trajectory) used in LLM training are racing toward the total public text available (green band), indicating an approaching data cap. To compensate, companies are turning to synthetic data (AI-generated text) and aggressive filtering of low-quality content — but these approaches bring concerns about factuality and diversity [3]. As Databricks’ Ion Stoica observes, “for general-knowledge questions, we are seeing a plateau…‘factual data’ [is] more useful than synthetic” 
- Rising Compute & Energy Costs: Achieving even modest performance gains now demands astronomical compute. OpenAI’s GPT-4 required an estimated 200,000 petaFLOP-days to train — roughly 55× the compute used for GPT-3 [5] — yet yielded diminishing marginal returns on many benchmarks. Each new model generation strains hardware and budgets: Altman noted GPT-4 cost >$100 million to develop [3], and future frontier trainings are projected in the billions. Anthropic’s CEO Dario Amodei predicts coming runs could cost “$100 billion” [3] (an order of magnitude jump that only a handful of tech giants could finance). Power requirements are surging as well — Mark Zuckerberg highlighted that data centers’ electricity use (460 TWh in 2021) may nearly double to 848 TWh by 2030, largely due to AI [6]. 
-  The era of easy wins by throwing more GPUs at the problem is ending
- Expert Opinions Diverge: Leading voices in AI are split on whether we’re at a fundamental plateau or just a temporary slowdown. Pessimists argue we’re hitting scaling limits: NYU professor Gary Marcus contends that LLM improvements are “destined to hit a wall”, noting the latest models show “convergence, rather than continued exponential growth” 
- A middle view envisions an S-curve: early rapid gains tapering to slower progress, yet not flatlining entirely. Researchers in scaling laws note that performance still improves with scale but following a sub-exponential law (diminishing returns) [10]. Ilya Sutskever — once a chief scaling proponent — observed that “the 2010s were the age of scaling” but now “results from scaling up pre-training have plateaued”, signaling we must “scale the right thing” and hunt for algorithmic breakthroughs


# Does RLHF Scale? Exploring the Impacts from Data, Model, and Method

https://arxiv.org/html/2412.06000v1
this approach has been successfully applied to leading models like ChatGPT (Achiam et al., 2023), Llama (Touvron et al., 2023; Dubey et al., 2024), and Claude (Bai et al., 2022b), yielding notable improvements. RLHF improves the model’s behavior by integrating external feedback, such as human preferences

Our findings show that increasing data diversity and volume improves reward model performance, helping process-supervision models scale better. For policy training, more response samples per prompt boost performance initially but quickly plateau. And larger reward models offer modest gains in policy training. In addition, larger policy models benefit less from RLHF with a fixed reward model. Overall, RLHF scales less efficiently than pretraining, with diminishing returns from additional computational resources. Based on these observations, we propose strategies to optimize RLHF performance within computational limits.

# 
https://www.bbc.com/news/live/cjr85l2e4l4t
Nvidia dropped 17% in one day
 - suffered the biggest single-day loss in US market history on Monday



# Daria Kulikova 
 https://www.youtube.com/watch?v=OYlQyPo-L4g

Economics of vibey apps:

Traditional SAAS
- B2B SAAS 70-90% margins
- Best ones are 80% or higher
Low marginal cost per customer

AI SAAS
- 30-60% margin at best
Big marginal cost per customer


Where are we in the hype cycle? 


ChatGPT has probably 700-800 m users
10million ChatGPT + plan
less than 2% conversion. Some sources say 6-7%
This is a major disrupter, they invented the category

Open AI REvenue estimate by Futuresearch June 2024 = $3.4 Billion ARR

https://www.youtube.com/watch?v=OBX1YmJL0dw
Layoff hype
There are big layoffs, but it's often just Big Tech adjusting to economic conditions. Eg overhiring earlier
Customer support layoffs are a thing, but often that leads to bad customer support
IBM fired lots of HR people and used AI to automate, then hired a lot of people back again

AI + offshore staff can help overcome language barriers
lowers barrier to entry

Adopting AI:
- operationally challenging
- culturally challenging


# AI Bubble? Why the Doom Narrative is Wrong
AI News and Strat
https://natesnewsletter.substack.com/p/ai-bubble-why-the-doom-narrative?r=1z4sm5&utm_campaign=post&utm_medium=web&triedRedirect=true

Chat GPT 5 botched rollout

- Chatbot usecase is saturated. Wont get much better
- progress is moving towards agentic orchistrated workflows 
- There is a gold rush, lots of "to too" products. Definately hype 
- there is real value, step change gains 
- rational to over-invest when the stakes are this high 

 95% of enterprise AI projects are failing. But think about what that means: 95% of companies are trying so hard to implement AI that they're running pilots. The demand signal is deafening.

More importantly, look at what the 5% who succeed are achieving. The study mentions startups jumping from zero to $20 million in revenue within a year.

https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
There are still exponential laws that are holding: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
timed humans with relevant domain expertise


# Zuckerberg's STUNNING Statement: “AI Will Write MOST Software Soon"
https://www.youtube.com/watch?v=USBW0ESLEK0
2025 we'll have an ai that acts as a mid level engineer

# DAve Farley
https://www.youtube.com/watch?v=1A6uPztchXk
It's a myth that writing code is the hard part
A good programmer can learn enough about a new language to get by in a few days, maybe weeks
usually when a product brain tried to "vibe" and get a programmer to convert their words into code, mistakes happen
human languages are imprecise, not the law is not easy to understand 
we dont define a plumber by their use of a wrench. They do a lot
Code:
    - organise our thinking
    - express outselves clearly
    - tell a machine what to do
Engineering includes:
    - modular
    - cohesive
    - separation of concerns
    - abstraction
    - managed coupling

Good programs have good taste
LLMSs often trained on nasty code



# Does AI Actually Boost Developer Productivity? (100k Devs Study) - Yegor Denisov-Blanch, Stanford
https://www.youtube.com/watch?v=tbDDYKRFjhk
https://arxiv.org/html/2409.15152v1

After Zuk's prediction, lots of CEOs started expecting magic from their CTOs

600 companies
Git history since pre 2023
i00k+ engineers
Billions of commits and LOC
80% private repos
    - work repo. not a fun weekend thing 

9.5% of engineers in dataset do no code work

Made a model to measure productivity. 85% agreement with a panel of experts
Productivity is functionality delivered over time (NOT LOC)

With AI:
- lots more rework + refactoring. rework is always wasteful
- 15-20% productivity boost total

More gains for simple, greenfield tasks. Very wide distribution. Sometimes it sucks 
less from complicated brownfield 
can actually decrease productivity
decreases productivity for high complexity greenfield, in unpopular languages 
lower performance the bigger the code base size (context matters)
domain-specific knowledge
big context window does not mean good performance with big contexts



<!-- https://chatgpt.com/c/68bbfcdf-2a80-8321-be60-b670d814901c HYpe quotes-->
						 <!-- https://claude.ai/chat/4dbff1f4-4481-4e00-b3fa-6d52498086a0 -->

# Stargate energy
https://apcoworldwide.com/blog/the-stargate-initiative-a-catalyst-for-the-next-energy-revolution/

https://www.certrec.com/blog/energy-demands-for-openai-stargate-project/

# data center water usage
https://www.theguardian.com/environment/2025/apr/09/big-tech-datacentres-water

https://www.tpr.org/environment/2025-08-15/big-techs-big-thirst-ais-demand-for-texas-water 

# Medical Prescriptions 
https://escconf.com/speakers/jochen-kirstaetter/