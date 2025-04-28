---

# SJPU System Definition

## 1. Definition

SJPU stands for Sensor-Judgment-Propagation-Understanding.  
It refers to a system architecture that:  
1. Detects sensor-based input signals,  
2. Propagates the input signals into "meaningful flows,"  
3. Makes judgments only when conditions are satisfied, and  
4. Outputs the judged results via speech.  

Unlike traditional deep learning models, which compute all inputs unconditionally,  
SJPU adopts a fundamentally different approach:  
"It only computes when necessary."

---

## 2. Purpose

- **Reduce unnecessary computations**  
  → Reduces computational costs for meaningless data.  

- **Generate meaning based on sensing**  
  → Not just a simple input processing system,  
  but one that detects and decides "meaning" within input flows.  

- **Autonomous computation control**  
  → Sensor nodes can autonomously choose or reject computations.  

- **Low-power, high-intelligence structure**  
  → Maintains judgment capability while reducing GPU dependency.  

- **Simultaneous scalability and controllability**  
  → Allows infinite scalability with a node-based distributed structure,  
  while enabling overall flow control by modifying specific nodes.  

---

## 3. Background and Motivation

Existing systems like LLMs, Transformers, and GPT models  
process "all inputs at all times."  

This approach works well with large-scale data and parameters,  
but in real-world applications, most computations are unnecessary.  

SJPU was designed to solve this problem.  

---

## 4. Core Summary

> SJPU does not "compute" data.  
> Instead, it "transfers data into meaning."  
> This structure provides a natural foundation for AI to not just mimic thought,  
> but actually decide "when to think."

---

