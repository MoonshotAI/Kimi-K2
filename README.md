<div align="center">
  <picture>
      <img src="figures/kimi-logo.png" width="30%" alt="Kimi K2: Open Agentic Intelligence">
  </picture>
</div>

<hr>

<div align="center" style="line-height:1">
  <a href="https://www.kimi.com" target="_blank"><img alt="Chat" src="https://img.shields.io/badge/🤖%20Chat-Kimi%20K2-ff6b6b?color=1783ff&logoColor=white"/></a>
  <a href="https://www.moonshot.ai" target="_blank"><img alt="Homepage" src="https://img.shields.io/badge/Homepage-Moonshot%20AI-white?logo=Kimi&logoColor=white"/></a>
</div>

<div align="center" style="line-height: 1;">
  <a href="https://huggingface.co/moonshotai" target="_blank"><img alt="Hugging Face" src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Moonshot%20AI-ffc107?color=ffc107&logoColor=white"/></a>
  <a href="https://twitter.com/kimi_moonshot" target="_blank"><img alt="Twitter Follow" src="https://img.shields.io/badge/Twitter-Kimi.ai-white?logo=x&logoColor=white"/></a>
    <a href="https://discord.gg/TYU2fdJykW" target="_blank"><img alt="Discord" src="https://img.shields.io/badge/Discord-Kimi.ai-white?logo=discord&logoColor=white"/></a>
</div>

<div align="center" style="line-height: 1;">
  <a href="https://github.com/moonshotai/Kimi-K2/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/badge/License-Modified_MIT-f5de53?&color=f5de53"/></a>
</div>

<p align="center">
<b>📰&nbsp;&nbsp;<a href="https://moonshotai.github.io/Kimi-K2/">Tech Blog</a></b> &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp; <b>📄&nbsp;&nbsp;Paper Link (coming soon)</b>
</p>

## 1. Model Introduction

Kimi K2 is a state-of-the-art mixture-of-experts (MoE) language model with 32 billion activated parameters and 1 trillion total parameters. Trained with the Muon optimizer, Kimi K2 achieves exceptional performance across frontier knowledge, reasoning, and coding tasks while being meticulously optimized for agentic capabilities.

### Key Features
- Large-Scale Training: Pre-trained a 1T parameter MoE model on 15.5T tokens with zero training instability.
- MuonClip Optimizer: We apply the Muon optimizer to an unprecedented scale, and develop novel optimization techniques to resolve instabilities while scaling up.
- Agentic Intelligence: Specifically designed for tool use, reasoning, and autonomous problem-solving.

### Model Variants
- **Kimi-K2-Base**: The foundation model, a strong start for researchers and builders who want full control for fine-tuning and custom solutions.
- **Kimi-K2-Instruct**: The post-trained model best for drop-in, general-purpose chat and agentic experiences. It is a reflex-grade model without long thinking.

<div align="center">
  <picture>
      <img src="figures/banner.png" width="80%" alt="Evaluation Results">
  </picture>
</div>

## 2. Model Summary

<div align="center">


| | |
|:---:|:---:|
| **Architecture** | Mixture-of-Experts (MoE) |
| **Total Parameters** | 1T |
| **Activated Parameters** | 32B |
| **Number of Layers** (Dense layer included) | 61 |
| **Number of Dense Layers** | 1 |
| **Attention Hidden Dimension** | 7168 |
| **MoE Hidden Dimension** (per Expert) | 2048 |
| **Number of Attention Heads** | 64 |
| **Number of Experts** | 384 |
| **Selected Experts per Token** | 8 |
| **Number of Shared Experts** | 1 |
| **Vocabulary Size** | 160K |
| **Context Length** | 128K |
| **Attention Mechanism** | MLA |
| **Activation Function** | SwiGLU |
</div>

## 3. Evaluation Results

#### Instruction model evaluation results

<div align="center">
<table>
<thead>
<tr>
<th align="center">Benchmark</th>
<th align="center">Metric</th>
<th align="center"><sup>Kimi K2 Instruct</sup></th>
<th align="center"><sup>DeepSeek-V3-0324</sup></th>
<th align="center"><sup>Qwen3-235B-A22B <br><sup>(non-thinking)</sup></sup></th>
<th align="center"><sup>Claude Sonnet 4 <br><sup>(w/o extended thinking)</sup></sup></th>
<th align="center"><sup>Claude Opus 4 <br><sup>(w/o extended thinking)</sup></sup></th>
<th align="center"><sup>GPT-4.1</sup></th>
<th align="center"><sup>Gemini 2.5 Flash <br> Preview (05-20)</sup></th>
</tr>
</thead>
<tbody>
<tr>
<td align="center" colspan=9><strong>Coding Tasks</strong></td>
</tr>
<tr>
<td align="center">LiveCodeBench v6<br><sup>(Aug 24 - May 25)</sup></td>
<td align="center">Pass@1</td>
<td align="center"><strong>53.7</strong></td>
<td align="center">46.9</td>
<td align="center">37.0</td>
<td align="center">48.5</td>
<td align="center">47.4</td>
<td align="center">44.7</td>
<td align="center">44.7</td>
</tr>
<tr>
<td align="center">OJBench</td>
<td align="center">Pass@1</td>
<td align="center"><strong>27.1</strong></td>
<td align="center">24.0</td>
<td align="center">11.3</td>
<td align="center">15.3</td>
<td align="center">19.6</td>
<td align="center">19.5</td>
<td align="center">19.5</td>
</tr>

<tr>
<td align="center">MultiPL-E</td>
<td align="center">Pass@1</td>
<td align="center"><ins><strong>85.7</strong></ins></td>
<td align="center">83.1</td>
<td align="center">78.2</td>
<td align="center">88.6</td>
<td align="center"><strong>89.6</strong></td>
<td align="center">86.7</td>
<td align="center">85.6</td>
</tr>

<tr>
<td align="center">SWE-bench Verified <br/><sup>(Agentless Coding)</sup></td>
<td align="center">Single Patch w/o Test (Acc)</td>
<td align="center"><ins><strong>51.8</strong></ins></td>
<td align="center">36.6</td>
<td align="center">39.4</td>
<td align="center">50.2</td>
<td align="center"><strong>53.0</strong></td>
<td align="center">40.8</td>
<td align="center">32.6</td>
</tr>

<tr>
<td align="center" rowspan="2">SWE-bench Verified <br/> <sup>(Agentic Coding)</sup></td>
<td align="center">Single Attempt (Acc)</td>
<td align="center"><ins><strong>65.8</strong></ins></td>
<td align="center">38.8</td>
<td align="center">34.4</td>
<td align="center"><strong>72.7</strong><sup>*</sup></td>
<td align="center">72.5<sup>*</sup></td>
<td align="center">54.6</td>
<td align="center">—</td>
</tr>

<tr>
<!--<td align="center">(Agentic Coding)</td>-->
<td align="center">Multiple Attempts (Acc)</td>
<td align="center"><ins><strong>71.6</strong></ins></td>
<td align="center">—</td>
<td align="center">—</td>
<td align="center"><strong>80.2</strong></td>
<td align="center">79.4<sup>*</sup></td>
<td align="center">—</td>
<td align="center">—</td>
</tr>

<tr>
<td align="center">SWE-bench Multilingual<br /> <sup>(Agentic Coding)</sup></td>
<td align="center">Single Attempt (Acc)</td>
<td align="center"><ins><strong>47.3</strong> </ins></td>
<td align="center">25.8</td>
<td align="center">20.9</td>
<td align="center"><strong>51.0</strong></td>
<td align="center">—</td>
<td align="center">31.5</td>
<td align="center">—</td>
</tr>

<tr>
<td align="center" rowspan="2">TerminalBench</td>
<td align="center">Inhouse Framework (Acc)</td>
<td align="center"><ins><strong>30.0</strong></ins></td>
<td align="center">—</td>
<td align="center">—</td>
<td align="center">35.5</td>
<td align="center"><strong>43.2</strong></td>
<td align="center">8.3</td>
<td align="center">—</td>
</tr>

<tr>
<!--<td align="center">TerminalBench</td>-->
<td align="center">Terminus (Acc)</td>
<td align="center"><ins><strong>25.0</strong> </ins></td>
<td align="center">16.3</td>
<td align="center">6.6</td>
<td align="center">—</td>
<td align="center">—</td>
<td align="center"><strong>30.3</strong></td>
<td align="center">16.8</td>
</tr>
<tr>
<td align="center">Aider-Polyglot</td>
<td align="center">Acc</td>
<td align="center">60.0</td>
<td align="center">55.1</td>
<td align="center"><ins><strong>61.8</strong></ins></td>
<td align="center">56.4</td>
<td align="center"><strong>70.7</strong></td>
<td align="center">52.4</td>
<td align="center">44.0</td>
</tr>
<tr>
<td align="center" colspan=9><strong>Tool Use Tasks</strong></td>
</tr>
<tr>
<td align="center">Tau2 retail</td>
<td align="center">Avg@4</td>
<td align="center"><ins><strong>70.6</strong></ins></td>
<td align="center">69.1</td>
<td align="center">57.0</td>
<td align="center">75.0</td>
<td align="center"><strong>81.8</strong></td>
<td align="center">74.8</td>
<td align="center">64.3</td>
</tr>
<tr>
<td align="center">Tau2 airline</td>
<td align="center">Avg@4</td>
<td align="center"><ins><strong>56.5</strong></ins></td>
<td align="center">39.0</td>
<td align="center">26.5</td>
<td align="center">55.5</td>
<td align="center"><strong>60.0</strong></td>
<td align="center">54.5</td>
<td align="center">42.5</td>
</tr>
<tr>
<td align="center">Tau2 telecom</td>
<td align="center">Avg@4</td>
<td align="center"><strong>65.8</strong></td>
<td align="center">32.5</td>
<td align="center">22.1</td>
<td align="center">45.2</td>
<td align="center">57.0</td>
<td align="center">38.6</td>
<td align="center">16.9</td>
</tr>
<tr>
<td align="center">AceBench</td>
<td align="center">Acc</td>
<td align="center"><ins><strong>76.5</strong></ins></td>
<td align="center">72.7</td>
<td align="center">70.5</td>
<td align="center">76.2</td>
<td align="center">75.6</td>
<td align="center"><strong>80.1</strong></td>
<td align="center">74.5</td>
</tr>
<tr>
<td align="center" colspan=9><strong>Math &amp; STEM Tasks</strong></td>
</tr>
<tr>
<td align="center">AIME 2024</td>
<td align="center">Avg@64</td>
<td align="center"><strong>69.6</strong></td>
<td align="center">59.4<sup>*</sup></td>
<td align="center">40.1<sup>*</sup></td>
<td align="center">43.4</td>
<td align="center">48.2</td>
<td align="center">46.5</td>
<td align="center">61.3</td>
</tr>
<tr>
<td align="center">AIME 2025</td>
<td align="center">Avg@64</td>
<td align="center"><strong>49.5</strong></td>
<td align="center">46.7</td>
<td align="center">24.7<sup>*</sup></td>
<td align="center">33.1<sup>*</sup></td>
<td align="center">33.9<sup>*</sup></td>
<td align="center">37.0</td>
<td align="center">46.6</td>
</tr>
<tr>
<td align="center">MATH-500</td>
<td align="center">Acc</td>
<td align="center"><strong>97.4</strong></td>
<td align="center">94.0<sup>*</sup></td>
<td align="center">91.2<sup>*</sup></td>
<td align="center">94.0</td>
<td align="center">94.4</td>
<td align="center">92.4</td>
<td align="center">95.4</td>
</tr>
<tr>
<td align="center">HMMT 2025</td>
<td align="center">Avg@32</td>
<td align="center"><strong>38.8</strong></td>
<td align="center">27.5</td>
<td align="center">11.9</td>
<td align="center">15.9</td>
<td align="center">15.9</td>
<td align="center">19.4</td>
<td align="center">34.7</td>
</tr>
<tr>
<td align="center">CNMO 2024</td>
<td align="center">Avg@16</td>
<td align="center">74.3</td>
<td align="center"><ins><strong>74.7</strong></ins></td>
<td align="center">48.6</td>
<td align="center">60.4</td>
<td align="center">57.6</td>
<td align="center">56.6</td>
<td align="center"><strong>75.0</strong></td>
</tr>
<tr>
<td align="center">PolyMath-en</td>
<td align="center">Avg@4</td>
<td align="center"><strong>65.1</strong></td>
<td align="center">59.5</td>
<td align="center">51.9</td>
<td align="center">52.8</td>
<td align="center">49.8</td>
<td align="center">54.0</td>
<td align="center">49.9</td>
</tr>

<tr>
<td align="center">ZebraLogic</td>
<td align="center">Acc</td>
<td align="center"><strong>89.0</strong></td>
<td align="center">84.0</td>
<td align="center">37.7<sup>*</sup></td>
<td align="center">73.7</td>
<td align="center">59.3</td>
<td align="center">58.5</td>
<td align="center">57.9</td>
</tr>

<tr>
<td align="center">AutoLogi</td>
<td align="center">Acc</td>
<td align="center"><ins><strong>89.5</strong></ins></td>
<td align="center">88.9</td>
<td align="center">83.3</td>
<td align="center"><strong>89.8</strong></td>
<td align="center">86.1</td>
<td align="center">88.2</td>
<td align="center">84.1</td>
</tr>

<tr>
<td align="center">GPQA-Diamond</td>
<td align="center">Avg@8</td>
<td align="center"><strong>75.1</strong></td>
<td align="center">68.4<sup>*</sup></td>
<td align="center">62.9<sup>*</sup></td>
<td align="center">70.0<sup>*</sup></td>
<td align="center">74.9<sup>*</sup></td>
<td align="center">66.3</td>
<td align="center">68.2</td>
</tr>

<tr>
<td align="center">SuperGPQA</td>
<td align="center">Acc</td>
<td align="center"><strong>57.2</strong></td>
<td align="center">53.7</td>
<td align="center">50.2</td>
<td align="center">55.7</td>
<td align="center">56.5</td>
<td align="center">50.8</td>
<td align="center">49.6</td>
</tr>

<tr>
<td align="center">Humanity's Last Exam<br><sup>(Text Only)</sup></td>
<td align="center">-</td>
<td align="center">4.7</td>
<td align="center">5.2</td>
<td align="center"><ins><strong>5.7</strong></ins></td>
<td align="center">5.8</td>
<td align="center"><strong>7.1</strong></td>
<td align="center">3.7</td>
<td align="center">5.6</td>
</tr>

<tr>
<td align="center" colspan=9><strong>General Tasks</strong></td>
</tr>

<tr>
<td align="center">MMLU</td>
<td align="center">EM</td>
<td align="center"><ins><strong>89.5</strong></ins></td>
<td align="center">89.4</td>
<td align="center">87.0</td>
<td align="center">91.5</td>
<td align="center"><strong>92.9</strong></td>
<td align="center">90.4</td>
<td align="center">90.1</td>
</tr>

<tr>
<td align="center">MMLU-Redux</td>
<td align="center">EM</td>
<td align="center"><ins><strong>92.7</strong></ins></td>
<td align="center">90.5</td>
<td align="center">89.2</td>
<td align="center">93.6</td>
<td align="center"><strong>94.2</strong></td>
<td align="center">92.4</td>
<td align="center">90.6</td>
</tr>

<tr>
<td align="center">MMLU-Pro</td>
<td align="center">EM</td>
<td align="center">81.1</td>
<td align="center"><ins><strong>81.2</strong></ins><sup>*</sup></td>
<td align="center">77.3</td>
<td align="center">83.7</td>
<td align="center"><strong>86.6</strong></td>
<td align="center">81.8</td>
<td align="center">79.4</td>
</tr>

<tr>
<td align="center">IFEval</td>
<td align="center">Prompt Strict</td>
<td align="center"><strong>89.8</strong></td>
<td align="center">81.1</td>
<td align="center">83.2<sup>*</sup></td>
<td align="center">87.6</td>
<td align="center">87.4</td>
<td align="center">88.0</td>
<td align="center">84.3</td>
</tr>

<tr>
<td align="center">Multi-Challenge</td>
<td align="center">Acc</td>
<td align="center"><strong>54.1</strong></td>
<td align="center">31.4</td>
<td align="center">34.0</td>
<td align="center">46.8</td>
<td align="center">49.0</td>
<td align="center">36.4</td>
<td align="center">39.5</td>
</tr>

<tr>
<td align="center">SimpleQA</td>
<td align="center">Correct</td>
<td align="center"><ins><strong>31.0</strong></ins></td>
<td align="center">27.7</td>
<td align="center">13.2</td>
<td align="center">15.9</td>
<td align="center">22.8</td>
<td align="center"><strong>42.3</strong></td>
<td align="center">23.3</td>
</tr>

<tr>
<td align="center">Livebench</td>
<td align="center">Pass@1</td>
<td align="center"><strong>76.4</strong></td>
<td align="center">72.4</td>
<td align="center">67.6</td>
<td align="center">74.8</td>
<td align="center">74.6</td>
<td align="center">69.8</td>
<td align="center">67.8</td>
</tr>
</tbody>
</table>
</div>
<sup>
• Bold denotes global SOTA, and underlined denotes open-source SOTA.
</sup><br/><sup>
• Data points marked with * are directly from the model's tech report or blog.
</sup><br/><sup>
• All metrics, except for SWE-bench Verified (Agentless), are evaluated with an 8k output token length. SWE-bench Verified (Agentless) is limited to a 16k output token length.
</sup><br/><sup>
• Kimi K2 achieves 65.8% pass@1 on the SWE-bench Verified tests with bash/editor tools (single-attempt patches, no test-time compute). It also achieves a 47.3% pass@1 on the SWE-bench Multilingual tests under the same conditions. Additionally, we report results on SWE-bench Verified tests (71.6%) that leverage parallel test-time compute by sampling multiple sequences and selecting the single best via an internal scoring model.
</sup><br/><sup>
• To ensure the stability of the evaluation, we employed avg@k on the AIME, HMMT, CNMO, PolyMath-en, GPQA-Diamond, EvalPlus, Tau2.
</sup><br/><sup>
• Some data points have been omitted due to prohibitively expensive evaluation costs.
    </sup>

---

#### Base model evaluation results

<div align="center">

<table>
<thead>
<tr>
<th align="center">Benchmark</th>
<th align="center">Metric</th>
<th align="center">Shot</th>
<th align="center">Kimi K2 Base</th>
<th align="center">Deepseek-V3-Base</th>
<th align="center">Qwen2.5-72B</th>
<th align="center">Llama 4 Maverick</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center" colspan="7"><strong>General Tasks</strong></td>
</tr>
<tr>
<td align="center">MMLU</td>
<td align="center">EM</td>
<td align="center">5-shot</td>
<td align="center"><strong>87.8</strong></td>
<td align="center">87.1</td>
<td align="center">86.1</td>
<td align="center">84.9</td>
</tr>
<tr>
<td align="center">MMLU-pro</td>
<td align="center">EM</td>
<td align="center">5-shot</td>
<td align="center"><strong>69.2</strong></td>
<td align="center">60.6</td>
<td align="center">62.8</td>
<td align="center">63.5</td>
</tr>
<tr>
<td align="center">MMLU-redux-2.0</td>
<td align="center">EM</td>
<td align="center">5-shot</td>
<td align="center"><strong>90.2</strong></td>
<td align="center">89.5</td>
<td align="center">87.8</td>
<td align="center">88.2</td>
</tr>
<tr>
<td align="center">SimpleQA</td>
<td align="center">Correct</td>
<td align="center">5-shot</td>
<td align="center"><strong>35.3</strong></td>
<td align="center">26.5</td>
<td align="center">10.3</td>
<td align="center">23.7</td>
</tr>
<tr>
<td align="center">TriviaQA</td>
<td align="center">EM</td>
<td align="center">5-shot</td>
<td align="center"><strong>85.1</strong></td>
<td align="center">84.1</td>
<td align="center">76.0</td>
<td align="center">79.3</td>
</tr>
<tr>
<td align="center">GPQA-Diamond</td>
<td align="center">Avg@8</td>
<td align="center">5-shot</td>
<td align="center">48.1</td>
<td align="center"><strong>50.5</strong></td>
<td align="center">40.8</td>
<td align="center">49.4</td>
</tr>
<tr>
<td align="center">SuperGPQA</td>
<td align="center">EM</td>
<td align="center">5-shot</td>
<td align="center"><strong>44.7</strong></td>
<td align="center">39.2</td>
<td align="center">34.2</td>
<td align="center">38.8</td>
</tr>
<tr>
<td align="center" colspan="7"><strong>Coding Tasks</strong></td>
</tr>
<tr>
<td align="center">LiveCodeBench v6</td>
<td align="center">Pass@1</td>
<td align="center">1-shot</td>
<td align="center"><strong>26.3</strong></td>
<td align="center">22.9</td>
<td align="center">21.1</td>
<td align="center">25.1</td>
</tr>
<tr>
<td align="center">EvalPlus</td>
<td align="center">Pass@1</td>
<td align="center">-</td>
<td align="center"><strong>80.3</strong></td>
<td align="center">65.6</td>
<td align="center">66.0</td>
<td align="center">65.5</td>
</tr>
<tr>
<td align="center" colspan="7"><strong>Mathematics Tasks</strong></td>
</tr>
<tr>
<td align="center">MATH</td>
<td align="center">EM</td>
<td align="center">4-shot</td>
<td align="center"><strong>70.2</strong></td>
<td align="center">60.1</td>
<td align="center">61.0</td>
<td align="center">63.0</td>
</tr>
<tr>
<td align="center">GSM8k</td>
<td align="center">EM</td>
<td align="center">8-shot</td>
<td align="center"><strong>92.1</strong></td>
<td align="center">91.7</td>
<td align="center">90.4</td>
<td align="center">86.3</td>
</tr>
<tr>
<td align="center" colspan="7"><strong>Chinese Tasks</strong></td>
</tr>
<tr>
<td align="center">C-Eval</td>
<td align="center">EM</td>
<td align="center">5-shot</td>
<td align="center"><strong>92.5</strong></td>
<td align="center">90.0</td>
<td align="center">90.9</td>
<td align="center">80.9</td>
</tr>
<tr>
<td align="center">CSimpleQA</td>
<td align="center">Correct</td>
<td align="center">5-shot</td>
<td align="center"><strong>77.6</strong></td>
<td align="center">72.1</td>
<td align="center">50.5</td>
<td align="center">53.5</td>
</tr>
</tbody>
</table>
</div>
<sup>
• We only evaluate open-source pretrained models in this work. We report results for Qwen2.5-72B because the base checkpoint for Qwen3-235B-A22B was not open-sourced at the time of our study.
</sup><br/><sup>
• All models are evaluated using the same evaluation protocol.

</sup>


## 4. Deployment
> [!Note]
> You can access Kimi K2's API on https://platform.moonshot.ai , we provide OpenAI/Anthropic-compatible API for you.
>
> The Anthropic-compatible API maps temperature by `real_temperature = request_temperature * 0.6` for better compatiblity with existing applications.

Our model checkpoints are stored in block-fp8 format, you can find it on [Huggingface](https://huggingface.co/moonshotai/Kimi-K2-Instruct).

Currently, it is recommended to run Kimi-K2 on the following inference engines:

* vLLM
* SGLang
* KTransformers
* TensorRT-LLM

Deployment examples for vLLM and SGLang can be found in the [Model Deployment Guide](docs/deploy_guidance.md).

---

## 5. Model Usage

### Chat Completion

Once the local inference service is set up, you can interact with it through the chat endpoint:

```python
def simple_chat(client: OpenAI, model_name: str):
    messages = [
        {"role": "system", "content": "You are Kimi, an AI assistant created by Moonshot AI."},
        {"role": "user", "content": [{"type": "text", "text": "Please give a brief self-introduction."}]},
    ]
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        stream=False,
        temperature=0.6,
        max_tokens=256
    )
    print(response.choices[0].message.content)
```

> [!NOTE]
> The recommended temperature for Kimi-K2-Instruct is `temperature = 0.6`.
> If no special instructions are required, the system prompt above is a good default.

---

### Tool Calling

Kimi-K2-Instruct has strong tool-calling capabilities.
To enable them, you need to pass the list of available tools in each request, then the model will autonomously decide when and how to invoke them.

The following example demonstrates calling a weather tool end-to-end:

```python
# Your tool implementation
def get_weather(city: str) -> dict:
    return {"weather": "Sunny"}

# Tool schema definition
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Retrieve current weather information. Call this when the user asks about the weather.",
        "parameters": {
            "type": "object",
            "required": ["city"],
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Name of the city"
                }
            }
        }
    }
}]

# Map tool names to their implementations
tool_map = {
    "get_weather": get_weather
}

def tool_call_with_client(client: OpenAI, model_name: str):
    messages = [
        {"role": "system", "content": "You are Kimi, an AI assistant created by Moonshot AI."},
        {"role": "user", "content": "What's the weather like in Beijing today? Use the tool to check."}
    ]
    finish_reason = None
    while finish_reason is None or finish_reason == "tool_calls":
        completion = client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=0.6,
            tools=tools,          # tool list defined above
            tool_choice="auto"
        )
        choice = completion.choices[0]
        finish_reason = choice.finish_reason
        if finish_reason == "tool_calls":
            messages.append(choice.message)
            for tool_call in choice.message.tool_calls:
                tool_call_name = tool_call.function.name
                tool_call_arguments = json.loads(tool_call.function.arguments)
                tool_function = tool_map[tool_call_name]
                tool_result = tool_function(**tool_call_arguments)
                print("tool_result:", tool_result)

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_call_name,
                    "content": json.dumps(tool_result)
                })
    print("-" * 100)
    print(choice.message.content)
```

The `tool_call_with_client` function implements the pipeline from user query to tool execution.
This pipeline requires the inference engine to support Kimi-K2’s native tool-parsing logic.
For streaming output and manual tool-parsing, see the [Tool Calling Guide](docs/tool_call_guidance.md).

---

## 6. License

Both the code and the model weights are released under the [Modified MIT License](LICENSE).

---

## 7. Contact Us

If you have any questions or concerns, please reach out to us at [support@moonshot.cn](mailto:support@moonshot.cn).
