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

5. Very Short / Vague Inputs

Observed issue:
The model struggles with very short or vague text like “ok”, “fine”, “nothing”.

Example input:
“ok”

Model output:
Happy, intensity 3

Reason:
Insufficient context in the text; model relies mostly on metadata, leading to potentially incorrect emotional state.

Improvement:
Use metadata (sleep, stress, energy) more heavily when text is too short and mark uncertain_flag=1.

6. Conflicting Signals from Text & Metadata

Observed issue:
Text suggests calm, but metadata indicates high stress.

Example input:
Text: “I’m fine”
Sleep: 4
Stress: 9

Model output:
Calm, intensity 3

Reason:
Model prioritizes text over metadata, leading to overestimation of calmness.

Improvement:
Combine text and metadata signals with weighted scoring; lower confidence for contradictory inputs.

7. Mixed Emotions

Observed issue:
Text shows mixed emotions (“I feel calm but tired”) leading to moderate predictions.

Example input:
“I feel calm but my body is exhausted”

Model output:
Calm, intensity 2

Reason:
Model cannot separate simultaneous emotional signals.

Improvement:
Consider multiple output signals or intensity ranges to capture mixed states.

8. Overgeneralization

Observed issue:
Short journal entries like “nothing much happened today” are sometimes classified as neutral.

Example input:
“Nothing much happened today”

Model output:
Neutral, intensity 3

Reason:
Model tends to default to the majority class when text has no strong emotional cues.

Improvement:
Include historical mood or previous_day_mood as features to provide context.

9. Extreme Negative Inputs Misinterpreted

Observed issue:
Text indicating high stress or exhaustion is sometimes predicted as overwhelmed but with low intensity.

Example input:
“Everything feels too much, I can’t handle it”

Model output:
Overwhelmed, intensity 2

Reason:
Model fails to capture severity due to lack of strong negative keywords in training data.

Improvement:
Augment training data with extreme negative examples; adjust intensity scoring for certain keywords.

10. Ambiguous Language

Observed issue:
Text is vague or metaphorical: “My thoughts won’t stop, but I feel okay”

Example input:
“My thoughts won’t stop, but I feel okay”

Model output:
Calm, intensity 3

Reason:
Model is confused by contradictory emotional signals within the same text.

Improvement:
Lower confidence in ambiguous cases and suggest conservative actions like pause_and_breathe.




These mistakes were analyzed to improve the reliability and real-world usability of the system.