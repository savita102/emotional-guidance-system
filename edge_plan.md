Edge Case Planning – Emotional Guidance System

This document describes how the system is designed to handle unusual, unclear, or difficult user inputs (edge cases).

1. Very Short Inputs

Examples:

"ok"

"fine"

"nothing"

"idk"

Handling:
The model may not have enough context, so the system:

Shows a low confidence warning

Suggests neutral guidance instead of strong actions

2. Mixed Emotional Inputs

Examples:

"I feel calm but also tired"

"I'm not stressed but my mind is racing"

"I feel fine but something still feels off"

Handling:
The model predicts the dominant emotional signal and:

Keeps intensity moderate

Uses safer recommendations like pause_and_breathe or light_planning

3. Conflicting Behaviour Signals

Example:

Sleep: 8 hours

Stress: 9

Energy: 8

Input: "I'm okay"

Handling:
The model prioritizes text input first, then uses behavioral signals to adjust intensity.

4. Unclear Emotional Language

Examples:

"I don't know what I'm feeling"

"Something feels strange today"

"My thoughts feel weird"

Handling:
The model may show low confidence and suggest grounding or calming actions.

5. Extremely Negative Inputs

Examples:

"Everything feels too much"

"I feel mentally exhausted"

"My thoughts won't stop"

Handling:
The model prioritizes safe emotional actions like:

grounding

box breathing

pause and breathe

6. Neutral / Calm Inputs

Examples:

"I feel quiet today"

"Nothing feels heavy"

"My mind is calm today"

Handling:
The model recommends:

light planning

deep work

focus-based actions

This system was designed to avoid risky predictions and provide safe emotional guidance even when the input is unclear.