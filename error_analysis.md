Error Analysis – Emotional Guidance System

This document explains the mistakes made by the model and how they were analyzed.

1. Calm vs Neutral Confusion

Observed issue:
The model sometimes predicts neutral instead of calm.

Example input:

"I finally feel quiet inside today. Nothing feels heavy and my thoughts are slow and steady."

Model output:
Neutral (instead of Calm)

Reason:
The training data contains fewer strong calm examples compared to neutral ones.

2. Low Confidence Predictions

Observed issue:
Some predictions show confidence below 0.40.

Example input:

"ended up like everything piled up. then my mind wandered again. then it faded again."

Model output:
Calm (low confidence)

Reason:
The sentence contains unclear emotional signals and no strong keywords.

3. Restless vs Overwhelmed Confusion

Observed issue:
The model sometimes confuses:

Restless

Overwhelmed

Example input:

"I tried to relax but my thoughts kept racing and I couldn't stay still."

Model output:
Restless (correct but sometimes predicted as overwhelmed)

Reason:
Both emotions share similar keywords like:

racing thoughts

can't focus

mental overload

4. Behaviour Signals Not Strong Enough

Observed issue:
Sometimes the model does not change prediction even when stress level is high.

Example:
Stress Level: 9
Sleep: 4.5
Energy: 3

Reason:
The text input has more weight than numerical inputs in the model.


These mistakes were analyzed to improve the reliability and real-world usability of the system.